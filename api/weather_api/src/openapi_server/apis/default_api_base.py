# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

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


class BaseDefaultApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseDefaultApi.subclasses = BaseDefaultApi.subclasses + (cls,)
    async def air_temperature_get(
        self,
        var_date: Annotated[Optional[StrictStr], Field(description="Format: YYYY-MM-DD or YYYY-MM-DDTHH:MM:SS (SGT). Example: 2024-07-16 or 2024-07-16T23:59:00")],
        pagination_token: Annotated[Optional[StrictStr], Field(description="Pagination token for retrieving subsequent data pages")],
    ) -> AirTemperatureGet200Response:
        """**[https://api-open.data.gov.sg/v2/real-time/api/air-temperature](https://api-open.data.gov.sg/v2/real-time/api/air-temperature)**  &lt;br/&gt;  - Has per-minute readings from NEA  &lt;br/&gt;  - Filter for specific date or date-time by providing &#x60;date&#x60; in query parameter.   - use YYYY-MM-DD format to retrieve all of the readings for that day   - use YYYY-MM-DDTHH:mm:ss to retrieve the latest readings at that moment in time   - example: &#x60;?date&#x3D;2024-07-16&#x60; or &#x60;?date&#x3D;2024-07-16T23:59:00&#x60;   - Unit of measure for readings is &#x60;°C&#x60;  """
        ...


    async def four_day_outlook_get(
        self,
        var_date: Annotated[Optional[StrictStr], Field(description="SGT date for which to retrieve data (YYYY-MM-DD or YYYY-MM-DDTHH:MM:SS)")],
        pagination_token: Annotated[Optional[StrictStr], Field(description="Pagination token for retrieving subsequent data pages")],
    ) -> FourDayOutlookGet200Response:
        """**[https://api-open.data.gov.sg/v2/real-time/api/four-day-outlook](https://api-open.data.gov.sg/v2/real-time/api/four-day-outlook)**  &lt;br/&gt;  - Updated twice a day from NEA - The forecast is for the next 4 days.  &lt;br/&gt;  - Filter for specific date or date-time by providing &#x60;date&#x60; in query parameter.   - use YYYY-MM-DD format to retrieve all of the readings for that day   - use YYYY-MM-DDTHH:mm:ss to retrieve the latest readings at that moment in time   - example: &#x60;?date&#x3D;2024-07-16&#x60; or &#x60;?date&#x3D;2024-07-16T23:59:00&#x60; """
        ...


    async def twenty_four_hr_forecast_get(
        self,
        var_date: Annotated[Optional[StrictStr], Field(description="SGT date (YYYY-MM-DD or YYYY-MM-DDTHH:MM:SS). Example: 2024-07-16 or 2024-07-16T23:59:00")],
        pagination_token: Annotated[Optional[StrictStr], Field(description="Pagination token for retrieving subsequent data pages")],
    ) -> TwentyFourHrForecastGet200Response:
        """**[https://api-open.data.gov.sg/v2/real-time/api/twenty-four-hr-forecast](https://api-open.data.gov.sg/v2/real-time/api/twenty-four-hr-forecast)**  &lt;br/&gt;  - Updated multiple times throughout the day  &lt;br/&gt;  - Filter for specific date or date-time by providing &#x60;date&#x60; in query parameter.   - use YYYY-MM-DD format to retrieve all of the readings for that day   - use YYYY-MM-DDTHH:mm:ss to retrieve the latest readings at that moment in time   - example: &#x60;?date&#x3D;2024-07-16&#x60; or &#x60;?date&#x3D;2024-07-16T23:59:00&#x60;  &lt;br/&gt;  - Possible values for forecast include:   - Fair   - Fair (Day)   - Fair (Night)   - Fair and Warm   - Partly Cloudy   - Partly Cloudy (Day)   - Partly Cloudy (Night)   - Cloudy   - Hazy   - Slightly Hazy   - Windy   - Mist   - Fog   - Light Rain   - Moderate Rain   - Heavy Rain   - Passing Showers   - Light Showers   - Showers   - Heavy Showers   - Thundery Showers   - Heavy Thundery Showers   - Heavy Thundery Showers with Gusty Winds """
        ...


    async def two_hr_forecast_get(
        self,
        var_date: Annotated[Optional[StrictStr], Field(description="SGT date for which to retrieve data (YYYY-MM-DD or YYYY-MM-DDTHH:MM:SS)")],
        pagination_token: Annotated[Optional[StrictStr], Field(description="Pagination token for retrieving subsequent data pages")],
    ) -> TwoHrForecastGet200Response:
        """**[https://api-open.data.gov.sg/v2/real-time/api/two-hr-forecast](https://api-open.data.gov.sg/v2/real-time/api/two-hr-forecast)**  &lt;br/&gt;  - Updated half-hourly from NEA - Forecasts are given for multiple areas in Singapore  &lt;br/&gt;  - Filter for specific date or date-time by providing &#x60;date&#x60; in query parameter.   - use YYYY-MM-DD format to retrieve all of the readings for that day   - use YYYY-MM-DDTHH:mm:ss to retrieve the latest readings at that moment in time   - example: &#x60;?date&#x3D;2024-07-16&#x60; or &#x60;?date&#x3D;2024-07-16T23:59:00&#x60;  &lt;br/&gt;  - Possible values for forecast include:   - Fair   - Fair (Day)   - Fair (Night)   - Fair and Warm   - Partly Cloudy   - Partly Cloudy (Day)   - Partly Cloudy (Night)   - Cloudy   - Hazy   - Slightly Hazy   - Windy   - Mist   - Fog   - Light Rain   - Moderate Rain   - Heavy Rain   - Passing Showers   - Light Showers   - Showers   - Heavy Showers   - Thundery Showers   - Heavy Thundery Showers   - Heavy Thundery Showers with Gusty Winds  &lt;br/&gt;  - Area metadata   - The &#x60;area_metadata&#x60; field in the response provides longitude/latitude information for the areas. You can use that to place the forecasts on a map. """
        ...


    async def weather_get(
        self,
        api: Annotated[Optional[StrictStr], Field(description="Set the value to `wbgt` to fetch WBGT records")],
        var_date: Annotated[Optional[StrictStr], Field(description="SGT date (YYYY-MM-DD or YYYY-MM-DDTHH:MM:SS). Example: 2025-01-16 or 2025-01-16T23:59:00")],
        pagination_token: Annotated[Optional[StrictStr], Field(description="Pagination token for retrieving subsequent data pages")],
    ) -> WeatherGet200Response:
        """**[https://api-open.data.gov.sg/v2/real-time/api/weather?api&#x3D;wbgt](https://api-open.data.gov.sg/v2/real-time/api/weather?api&#x3D;wbgt)**  &lt;br/&gt;  - Updated multiple times throughout the day &lt;br/&gt; - Filter for specific date or date-time by providing &#x60;date&#x60; in query parameter.   - use YYYY-MM-DD format to retrieve all of the readings for that day   - use YYYY-MM-DDTHH:mm:ss to retrieve the latest readings at that moment in time   - example: &#x60;?date&#x3D;2025-01-16&#x60; or &#x60;?date&#x3D;2025-01-16T23:59:00&#x60;   - Unit of measure for readings is &#x60;°C&#x60;  """
        ...


    async def wind_direction_get(
        self,
        var_date: Annotated[Optional[StrictStr], Field(description="SGT date for which to retrieve data (YYYY-MM-DD or YYYY-MM-DDTHH:MM:SS)")],
        pagination_token: Annotated[Optional[StrictStr], Field(description="Pagination token for retrieving subsequent data pages")],
    ) -> WindDirectionGet200Response:
        """**[https://api-open.data.gov.sg/v2/real-time/api/wind-direction](https://api-open.data.gov.sg/v2/real-time/api/wind-direction)**  &lt;br/&gt;  - Has per-minute readings from NEA  &lt;br/&gt;  - Filter for specific date or date-time by providing &#x60;date&#x60; in query parameter.   - use YYYY-MM-DD format to retrieve all of the readings for that day   - use YYYY-MM-DDTHH:mm:ss to retrieve the latest readings at that moment in time   - example: &#x60;?date&#x3D;2024-07-16&#x60; or &#x60;?date&#x3D;2024-07-16T23:59:00&#x60;   - Unit of measure for readings is &#x60;°&#x60;  """
        ...
