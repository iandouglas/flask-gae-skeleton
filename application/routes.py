# coding=utf-8
import logging
from flask import render_template
from controllers.static import home, privacy, robots_txt


def create_routes(app):

    # Handle 404 errors
    @app.errorhandler(404)
    def page_not_found(e=Exception):  # pragma: no cover
        logging.debug(e)
        # return 'Sorry, Nothing at this URL.', 404
        return render_template('404.html', e=e), 404

    # Handle 500 errors
    @app.errorhandler(500)
    def server_error(e=Exception):  # pragma: no cover
        # return 'Sorry, unexpected error: {}'.format(e), 500
        logging.debug(e)
        return render_template('500.html', e=e), 500

    def build_routes(app):
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

        app.add_url_rule('/privacy', endpoint='privacy',
                         view_func=privacy,
                         methods=['GET'])

        app.add_url_rule('/robots.txt', endpoint='robots_txt',
                         view_func=robots_txt,
                         methods=['GET'])

    build_routes(app)  # pragma: no cover


def warmup():  # pragma: no cover
    # http://code.google.com/appengine/docs/python/config/appconfig.html#Warming_Requests
    return ''
