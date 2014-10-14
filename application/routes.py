import logging
from flask import render_template


def create_routes(app):
    ## Error handlers
    # Handle 404 errors
    @app.errorhandler(404)
    def page_not_found(e=Exception):
        logging.debug(e)
        # return 'Sorry, Nothing at this URL.', 404
        return render_template('404.html', e=e), 404

    # Handle 500 errors
    @app.errorhandler(500)
    def server_error(e=Exception):
        # return 'Sorry, unexpected error: {}'.format(e), 500
        return render_template('500.html', e=e), 500

    def build_routes(app):  # pragma: no cover
        """
        build routes for Flask
        :param app:
        """
        # App Engine warm up handler
        # this code is what App Engine calls when starting up a new instance; we could set this up to email us whenever
        #  a new instance is started, if we cared about that sort of thing.
        # See http://code.google.com/appengine/docs/python/config/appconfig.html#Warming_Requests
        app.add_url_rule('/_ah/warmup', endpoint='warmup',
                         view_func=warmup,
                         methods=['GET'])

        app.add_url_rule('/404', endpoint='404',
                         view_func=page_not_found,
                         methods=['GET', 'POST'])

        app.add_url_rule('/', endpoint='home',
                         view_func=home,
                         methods=['GET'])

    build_routes(app)  # pragma: no cover


def warmup():
    # http://code.google.com/appengine/docs/python/config/appconfig.html#Warming_Requests
    return ''


def home():
    return render_template('home.html')
