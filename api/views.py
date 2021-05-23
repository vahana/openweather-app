from prf.view import BaseView as _BaseView
from openweather import API as OAPI

class Base(_BaseView):
    def __init__(self, ctx, req):
        super().__init__(ctx, req)
        self.wapi = OAPI(req.registry.settings)


class ZipView(Base):
    def __init__(self, ctx, req):
        super().__init__(ctx, req)

    def show(self):
        return dict(data = self.wapi.get_by_zip(zip=self._params.zip, country=self._params.get('country')))

class SearchView(Base):
    def __init__(self, ctx, req):
        super().__init__(ctx, req)

    def show(self):
        return dict(data = self.wapi.search(self._params.q))

class GeoView(Base):
    def __init__(self, ctx, req):
        super().__init__(ctx, req)

    def show(self):
        return dict(data = self.wapi.get_by_geo(self._params.lat, self._params.lon))