# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictStr  # noqa: F401
from typing import Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.air_temperature_get200_response import AirTemperatureGet200Response  # noqa: F401
from openapi_server.models.four_day_outlook_get200_response import FourDayOutlookGet200Response  # noqa: F401
from openapi_server.models.twenty_four_hr_forecast_get200_response import TwentyFourHrForecastGet200Response  # noqa: F401
from openapi_server.models.twenty_four_hr_forecast_get400_response import TwentyFourHrForecastGet400Response  # noqa: F401
from openapi_server.models.twenty_four_hr_forecast_get404_response import TwentyFourHrForecastGet404Response  # noqa: F401
from openapi_server.models.two_hr_forecast_get200_response import TwoHrForecastGet200Response  # noqa: F401
from openapi_server.models.weather_get200_response import WeatherGet200Response  # noqa: F401
from openapi_server.models.weather_get400_response import WeatherGet400Response  # noqa: F401
from openapi_server.models.wind_direction_get200_response import WindDirectionGet200Response  # noqa: F401


def test_air_temperature_get(client: TestClient):
    """Test case for air_temperature_get

    Get air temperature readings across Singapore
    """
    params = [("var_date", 'var_date_example'),     ("pagination_token", 'pagination_token_example')]
    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/air-temperature",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_four_day_outlook_get(client: TestClient):
    """Test case for four_day_outlook_get

    Retrieve the latest 4 day weather forecast
    """
    params = [("var_date", 'var_date_example'),     ("pagination_token", 'pagination_token_example')]
    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/four-day-outlook",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_twenty_four_hr_forecast_get(client: TestClient):
    """Test case for twenty_four_hr_forecast_get

    Retrieve the latest 24 hour weather forecast
    """
    params = [("var_date", 'var_date_example'),     ("pagination_token", 'pagination_token_example')]
    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/twenty-four-hr-forecast",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_two_hr_forecast_get(client: TestClient):
    """Test case for two_hr_forecast_get

    Retrieve the latest two hour weather forecast
    """
    params = [("var_date", 'var_date_example'),     ("pagination_token", 'pagination_token_example')]
    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/two-hr-forecast",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_weather_get(client: TestClient):
    """Test case for weather_get

    Retrieve the latest WBGT data for accurate heat stress assessment
    """
    params = [("api", 'wbgt'),     ("var_date", '2025-01-16T23:59:00.000Z'),     ("pagination_token", 'pagination_token_example')]
    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/weather",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_wind_direction_get(client: TestClient):
    """Test case for wind_direction_get

    Get wind direction readings across Singapore
    """
    params = [("var_date", 'var_date_example'),     ("pagination_token", 'pagination_token_example')]
    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/wind-direction",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

