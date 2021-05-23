from unittest import TestCase
import pytest
from pyramid.exceptions import HTTPForbidden

from api.openweather import API
from api.config import settings

openweather_response = {
    "coord": {
        "lon": -122.088,
        "lat": 37.3855
    },
    "weather": [
    {
        "id": 801,
        "main": "Clouds",
        "description": "few clouds",
        "icon": "02d"
    }
    ],
    "main": {
        "temp": 286.23,
        "feels_like": 285.42,
        "temp_min": 283.41,
        "temp_max": 288.68,
        "pressure": 1020,
        "humidity": 70
    },
    "dt": 1621784091,
    "sys": {
        "type": 2,
        "id": 2003994,
        "country": "US",
        "sunrise": 1621774413,
        "sunset": 1621826223
    },
    "name": "Mountain View",
}

class MockedResponse:
    def __init__(self, ok, status_code, data):
        self.ok = ok
        self.status_code = status_code
        self.json_data = data

    def json(self):
        return self.json_data

class OpenWeatherAPITests(TestCase):
    def setUp(self):
        self.api = API(settings)
        return super().setUp

    def test_api_init(self):
        # raises if no settings
        with pytest.raises(KeyError):
            API({})

        api = API(settings)
        assert api.url == settings.OPEN_WEATHER_API_URL
        assert api.default_params.units == settings.TEMP_UNITS
        assert api.default_params.appid == settings.OPEN_WEATHER_API_KEY

    def test_process_response(self):
        api = API(settings)

        with pytest.raises(ValueError):
            api.process_response(MockedResponse(False, 400, dict(error='some error')))

        try:
            api.process_response(MockedResponse(False, 401, dict(error='some error')))
        except HTTPForbidden:
            pass

        data = api.process_response(MockedResponse(True, 200, openweather_response))

        assert data.temp == 286.23
        assert data.feels_like == 285.42
        assert data.humidity == 70
