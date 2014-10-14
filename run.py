# coding=utf-8
import os
import sys
# from werkzeug.debug import DebuggedApplication

sys.path.insert(1, os.path.join(os.path.abspath('.'), 'lib'))

COV = None
if os.environ.get('FLASK_COVERAGE'):
    import coverage
    COV = coverage.coverage(branch=True, include='application/*')
    COV.start()

from application import create_app
app = create_app(os.getenv('FLASK_CONFIG') or 'default')

from application.routes import create_routes
create_routes(app)

# if app.debug:
#     app.wsgi_app = DebuggedApplication(app.wsgi_app, evalex=True)
