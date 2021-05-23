import logging
import requests
from slovar import slovar
import prf.exc as prf_exc

log = logging.getLogger(__name__)


class API():
    def __init__(self, settings):
        self.settings = slovar(settings)

        self.url = self.settings.OPEN_WEATHER_API_URL
        self.default_params = slovar({
            'units': self.settings.TEMP_UNITS,
            'appid': self.settings.OPEN_WEATHER_API_KEY,
        })

    def process_response(self, resp):
        if not resp.ok:
            if resp.status_code == 401:
                raise prf_exc.HTTPForbidden('Bad API key')
            raise ValueError(resp.json())
        else:
            data = slovar(resp.json()).extract(
                ['main.*',
                'dt__as__date:ts2dt',
                'coord.*',
                'unit:=%s' % self.settings.TEMP_UNITS,
                'weather.0.description__as__',
                'weather.0.icon__as__',
                'sys.country__as__',
                'name',
                ])
            return data


    def get_by_zip(self, zip, country='us'):
        params = self.default_params.update({'zip':zip,'country':country})
        return self.process_response(requests.get(self.url, params=params))

    def get_by_geo(self, lat, lon):
        params = self.default_params.update({'lat':lat,'lon':lon})
        return self.process_response(requests.get(self.url, params=params))

    def search(self, q):
        params = self.default_params.update({'q': q})
        return self.process_response(requests.get(self.url, params=params))
