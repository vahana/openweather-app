from waitress import serve
from pyramid.config import Configurator

from config import settings
import views

if __name__ == '__main__':

    with Configurator(settings=settings) as config:
        config.include('prf')  # pyramid way of adding external packages.
        config.add_tween('prf.tweens.GET_tunneling')
        config.add_tween('prf.tweens.cors')

        config.add_error_view(KeyError, error='Missing param: %s', error_attr='args')
        config.add_error_view(ValueError, error='Missing values: %s', error_attr='args')

        root = config.get_root_resource()  # acquire root resource.
        root.add_singular('zip', view=views.ZipView)
        root.add_singular('search', view=views.SearchView)
        root.add_singular('geo', view=views.GeoView)

        app = config.make_wsgi_app()

    print('Serving on http://%s:%s' % (settings.HOST, settings.PORT))
    serve(app, host=settings.HOST, port=settings.PORT)