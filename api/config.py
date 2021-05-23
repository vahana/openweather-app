from starlette.config import Config
from slovar import slovar

config = Config('.env')

settings = slovar({
    'HOST': config('HOST', default='0.0.0.0'),
    'PORT': config('PORT', default=6543),
    'OPEN_WEATHER_API_URL': config('OPEN_WEATHER_API_URL', default='https://api.openweathermap.org/data/2.5/weather'),
    'OPEN_WEATHER_API_KEY': config('OPEN_WEATHER_API_KEY'),
    'TEMP_UNITS': config('TEMP_UNITS', default='metric'),
    'cors.allow_origins': config('CORS_ALLOW_ORIGINS', default='http://0.0.0.0:3000'),
    'cors.allow_credentials': 'false',
})