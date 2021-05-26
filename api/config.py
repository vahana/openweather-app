from starlette.config import Config
from slovar import slovar

config = Config('.env')

settings = slovar({
    'HOST': config('HOST', default='localhost'),
    'PORT': config('PORT', default=6543),
    'OPEN_WEATHER_API_URL': config('OPEN_WEATHER_API_URL', default='https://api.openweathermap.org/data/2.5/weather'),
    'OPEN_WEATHER_API_KEY': config('OPEN_WEATHER_API_KEY', default='INVALID KEY'),
    'TEMP_UNITS': config('TEMP_UNITS', default='metric'),
    'REDIS_EXP': config('REDIS_EXP', default=10),
    'cors.allow_origins': config('CORS_ALLOW_ORIGINS', default='http://localhost:3000'),

})
