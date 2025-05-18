# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.default_api_base import BaseDefaultApi
import openapi_server.impl

from fastapi import (  # noqa: F401
    APIRouter,
    Body,
    Cookie,
    Depends,
    Form,
    Header,
    HTTPException,
    Path,
    Query,
    Response,
    Security,
    status,
)

from openapi_server.models.extra_models import TokenModel  # noqa: F401
from pydantic import Field, StrictStr
from typing import Optional
from typing_extensions import Annotated
from openapi_server.models.air_temperature_get200_response import AirTemperatureGet200Response
from openapi_server.models.four_day_outlook_get200_response import FourDayOutlookGet200Response
from openapi_server.models.twenty_four_hr_forecast_get200_response import TwentyFourHrForecastGet200Response
from openapi_server.models.twenty_four_hr_forecast_get400_response import TwentyFourHrForecastGet400Response
from openapi_server.models.twenty_four_hr_forecast_get404_response import TwentyFourHrForecastGet404Response
from openapi_server.models.two_hr_forecast_get200_response import TwoHrForecastGet200Response
from openapi_server.models.weather_get200_response import WeatherGet200Response
from openapi_server.models.weather_get400_response import WeatherGet400Response
from openapi_server.models.wind_direction_get200_response import WindDirectionGet200Response


router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/air-temperature",
    responses={
        200: {"model": AirTemperatureGet200Response, "description": "Air Temperature Information"},
        400: {"model": TwentyFourHrForecastGet400Response, "description": "Invalid HTTP request body"},
        404: {"model": TwentyFourHrForecastGet404Response, "description": "Weather data not found"},
    },
    tags=["default"],
    summary="Get air temperature readings across Singapore",
    response_model_by_alias=True,
)
async def air_temperature_get(
    var_date: Annotated[Optional[StrictStr], Field(description="Format: YYYY-MM-DD or YYYY-MM-DDTHH:MM:SS (SGT). Example: 2024-07-16 or 2024-07-16T23:59:00")] = Query(None, description="Format: YYYY-MM-DD or YYYY-MM-DDTHH:MM:SS (SGT). Example: 2024-07-16 or 2024-07-16T23:59:00", alias="date"),
    pagination_token: Optional[StrictStr] = Query(None, description="Pagination token for retrieving subsequent data pages", alias="paginationToken"),
) -> AirTemperatureGet200Response:
    """**[https://api-open.data.gov.sg/v2/real-time/api/air-temperature](https://api-open.data.gov.sg/v2/real-time/api/air-temperature)**  &lt;br/&gt;  - Has per-minute readings from NEA  &lt;br/&gt;  - Filter for specific date or date-time by providing &#x60;date&#x60; in query parameter.   - use YYYY-MM-DD format to retrieve all of the readings for that day   - use YYYY-MM-DDTHH:mm:ss to retrieve the latest readings at that moment in time   - example: &#x60;?date&#x3D;2024-07-16&#x60; or &#x60;?date&#x3D;2024-07-16T23:59:00&#x60;   - Unit of measure for readings is &#x60;°C&#x60;  """
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().air_temperature_get(var_date, pagination_token)


@router.get(
    "/four-day-outlook",
    responses={
        200: {"model": FourDayOutlookGet200Response, "description": "4 Day Weather Forecast"},
        400: {"model": TwentyFourHrForecastGet400Response, "description": "Invalid HTTP request body"},
        404: {"model": TwentyFourHrForecastGet404Response, "description": "Weather data not found"},
    },
    tags=["default"],
    summary="Retrieve the latest 4 day weather forecast",
    response_model_by_alias=True,
)
async def four_day_outlook_get(
    var_date: Annotated[Optional[StrictStr], Field(description="SGT date for which to retrieve data (YYYY-MM-DD or YYYY-MM-DDTHH:MM:SS)")] = Query(None, description="SGT date for which to retrieve data (YYYY-MM-DD or YYYY-MM-DDTHH:MM:SS)", alias="date"),
    pagination_token: Optional[StrictStr] = Query(None, description="Pagination token for retrieving subsequent data pages", alias="paginationToken"),
) -> FourDayOutlookGet200Response:
    """**[https://api-open.data.gov.sg/v2/real-time/api/four-day-outlook](https://api-open.data.gov.sg/v2/real-time/api/four-day-outlook)**  &lt;br/&gt;  - Updated twice a day from NEA - The forecast is for the next 4 days.  &lt;br/&gt;  - Filter for specific date or date-time by providing &#x60;date&#x60; in query parameter.   - use YYYY-MM-DD format to retrieve all of the readings for that day   - use YYYY-MM-DDTHH:mm:ss to retrieve the latest readings at that moment in time   - example: &#x60;?date&#x3D;2024-07-16&#x60; or &#x60;?date&#x3D;2024-07-16T23:59:00&#x60; """
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().four_day_outlook_get(var_date, pagination_token)


@router.get(
    "/twenty-four-hr-forecast",
    responses={
        200: {"model": TwentyFourHrForecastGet200Response, "description": "24 Hour Weather Forecast"},
        400: {"model": TwentyFourHrForecastGet400Response, "description": "Invalid HTTP request body"},
        404: {"model": TwentyFourHrForecastGet404Response, "description": "Weather data not found"},
    },
    tags=["default"],
    summary="Retrieve the latest 24 hour weather forecast",
    response_model_by_alias=True,
)
async def twenty_four_hr_forecast_get(
    var_date: Annotated[Optional[StrictStr], Field(description="SGT date (YYYY-MM-DD or YYYY-MM-DDTHH:MM:SS). Example: 2024-07-16 or 2024-07-16T23:59:00")] = Query(None, description="SGT date (YYYY-MM-DD or YYYY-MM-DDTHH:MM:SS). Example: 2024-07-16 or 2024-07-16T23:59:00", alias="date"),
    pagination_token: Optional[StrictStr] = Query(None, description="Pagination token for retrieving subsequent data pages", alias="paginationToken"),
) -> TwentyFourHrForecastGet200Response:
    """**[https://api-open.data.gov.sg/v2/real-time/api/twenty-four-hr-forecast](https://api-open.data.gov.sg/v2/real-time/api/twenty-four-hr-forecast)**  &lt;br/&gt;  - Updated multiple times throughout the day  &lt;br/&gt;  - Filter for specific date or date-time by providing &#x60;date&#x60; in query parameter.   - use YYYY-MM-DD format to retrieve all of the readings for that day   - use YYYY-MM-DDTHH:mm:ss to retrieve the latest readings at that moment in time   - example: &#x60;?date&#x3D;2024-07-16&#x60; or &#x60;?date&#x3D;2024-07-16T23:59:00&#x60;  &lt;br/&gt;  - Possible values for forecast include:   - Fair   - Fair (Day)   - Fair (Night)   - Fair and Warm   - Partly Cloudy   - Partly Cloudy (Day)   - Partly Cloudy (Night)   - Cloudy   - Hazy   - Slightly Hazy   - Windy   - Mist   - Fog   - Light Rain   - Moderate Rain   - Heavy Rain   - Passing Showers   - Light Showers   - Showers   - Heavy Showers   - Thundery Showers   - Heavy Thundery Showers   - Heavy Thundery Showers with Gusty Winds """
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().twenty_four_hr_forecast_get(var_date, pagination_token)


@router.get(
    "/two-hr-forecast",
    responses={
        200: {"model": TwoHrForecastGet200Response, "description": "2 Hour Weather Forecast"},
        400: {"model": TwentyFourHrForecastGet400Response, "description": "Invalid HTTP request body"},
        404: {"model": TwentyFourHrForecastGet404Response, "description": "Weather data not found"},
    },
    tags=["default"],
    summary="Retrieve the latest two hour weather forecast",
    response_model_by_alias=True,
)
async def two_hr_forecast_get(
    var_date: Annotated[Optional[StrictStr], Field(description="SGT date for which to retrieve data (YYYY-MM-DD or YYYY-MM-DDTHH:MM:SS)")] = Query(None, description="SGT date for which to retrieve data (YYYY-MM-DD or YYYY-MM-DDTHH:MM:SS)", alias="date"),
    pagination_token: Optional[StrictStr] = Query(None, description="Pagination token for retrieving subsequent data pages", alias="paginationToken"),
) -> TwoHrForecastGet200Response:
    """**[https://api-open.data.gov.sg/v2/real-time/api/two-hr-forecast](https://api-open.data.gov.sg/v2/real-time/api/two-hr-forecast)**  &lt;br/&gt;  - Updated half-hourly from NEA - Forecasts are given for multiple areas in Singapore  &lt;br/&gt;  - Filter for specific date or date-time by providing &#x60;date&#x60; in query parameter.   - use YYYY-MM-DD format to retrieve all of the readings for that day   - use YYYY-MM-DDTHH:mm:ss to retrieve the latest readings at that moment in time   - example: &#x60;?date&#x3D;2024-07-16&#x60; or &#x60;?date&#x3D;2024-07-16T23:59:00&#x60;  &lt;br/&gt;  - Possible values for forecast include:   - Fair   - Fair (Day)   - Fair (Night)   - Fair and Warm   - Partly Cloudy   - Partly Cloudy (Day)   - Partly Cloudy (Night)   - Cloudy   - Hazy   - Slightly Hazy   - Windy   - Mist   - Fog   - Light Rain   - Moderate Rain   - Heavy Rain   - Passing Showers   - Light Showers   - Showers   - Heavy Showers   - Thundery Showers   - Heavy Thundery Showers   - Heavy Thundery Showers with Gusty Winds  &lt;br/&gt;  - Area metadata   - The &#x60;area_metadata&#x60; field in the response provides longitude/latitude information for the areas. You can use that to place the forecasts on a map. """
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().two_hr_forecast_get(var_date, pagination_token)


@router.get(
    "/weather",
    responses={
        200: {"model": WeatherGet200Response, "description": "WBGT Weather Observations"},
        400: {"model": WeatherGet400Response, "description": "Invalid HTTP request body"},
        404: {"model": TwentyFourHrForecastGet404Response, "description": "Weather data not found"},
    },
    tags=["default"],
    summary="Retrieve the latest WBGT data for accurate heat stress assessment",
    response_model_by_alias=True,
)
async def weather_get(
    api: Optional[StrictStr] = Query(None, description="Set the value to &#x60;wbgt&#x60; to fetch WBGT records", alias="api"),
    var_date: Annotated[Optional[StrictStr], Field(description="SGT date (YYYY-MM-DD or YYYY-MM-DDTHH:MM:SS). Example: 2025-01-16 or 2025-01-16T23:59:00")] = Query(None, description="SGT date (YYYY-MM-DD or YYYY-MM-DDTHH:MM:SS). Example: 2025-01-16 or 2025-01-16T23:59:00", alias="date"),
    pagination_token: Optional[StrictStr] = Query(None, description="Pagination token for retrieving subsequent data pages", alias="paginationToken"),
) -> WeatherGet200Response:
    """**[https://api-open.data.gov.sg/v2/real-time/api/weather?api&#x3D;wbgt](https://api-open.data.gov.sg/v2/real-time/api/weather?api&#x3D;wbgt)**  &lt;br/&gt;  - Updated multiple times throughout the day &lt;br/&gt; - Filter for specific date or date-time by providing &#x60;date&#x60; in query parameter.   - use YYYY-MM-DD format to retrieve all of the readings for that day   - use YYYY-MM-DDTHH:mm:ss to retrieve the latest readings at that moment in time   - example: &#x60;?date&#x3D;2025-01-16&#x60; or &#x60;?date&#x3D;2025-01-16T23:59:00&#x60;   - Unit of measure for readings is &#x60;°C&#x60;  """
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().weather_get(api, var_date, pagination_token)


@router.get(
    "/wind-direction",
    responses={
        200: {"model": WindDirectionGet200Response, "description": "Wind Direction Information"},
        400: {"model": TwentyFourHrForecastGet400Response, "description": "Invalid HTTP request body"},
        404: {"model": TwentyFourHrForecastGet404Response, "description": "Weather data not found"},
    },
    tags=["default"],
    summary="Get wind direction readings across Singapore",
    response_model_by_alias=True,
)
async def wind_direction_get(
    var_date: Annotated[Optional[StrictStr], Field(description="SGT date for which to retrieve data (YYYY-MM-DD or YYYY-MM-DDTHH:MM:SS)")] = Query(None, description="SGT date for which to retrieve data (YYYY-MM-DD or YYYY-MM-DDTHH:MM:SS)", alias="date"),
    pagination_token: Optional[StrictStr] = Query(None, description="Pagination token for retrieving subsequent data pages", alias="paginationToken"),
) -> WindDirectionGet200Response:
    """**[https://api-open.data.gov.sg/v2/real-time/api/wind-direction](https://api-open.data.gov.sg/v2/real-time/api/wind-direction)**  &lt;br/&gt;  - Has per-minute readings from NEA  &lt;br/&gt;  - Filter for specific date or date-time by providing &#x60;date&#x60; in query parameter.   - use YYYY-MM-DD format to retrieve all of the readings for that day   - use YYYY-MM-DDTHH:mm:ss to retrieve the latest readings at that moment in time   - example: &#x60;?date&#x3D;2024-07-16&#x60; or &#x60;?date&#x3D;2024-07-16T23:59:00&#x60;   - Unit of measure for readings is &#x60;°&#x60;  """
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().wind_direction_get(var_date, pagination_token)
