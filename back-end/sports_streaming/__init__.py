import logging
from pathlib import Path


logging.basicConfig(
  level=logging.ERROR,
  format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
  datefmt='%m-%d-%Y %H:%M:%S',
  filename=str(Path(__file__).parent / 'logs/server.log'),
  filemode='a'
)


def filter_loggers():
  debug_loggers = ['werkzeug', 'urllib3.connectionpool', 'main-app']
  logging.getLogger('main-app').info(logging.root.manager.loggerDict)
  for logger in debug_loggers:
    if logger in logging.root.manager.loggerDict:
      logging.getLogger(logger).setLevel(logging.DEBUG)


def create_app():
  from flask import Flask
  from flask_cors import CORS
  import config
  from sports_streaming import util, blueprints

  app = Flask(__name__)
  app.config.from_object(config)
  CORS(app)

  app.register_blueprint(blueprints.api) # register app level

  # api = Blueprint('sports_streaming', __name__) # app level blueprint

  # # blueprint modules
  # from sports_streaming.games.baseball.controller import api as baseball_api
  # api.register_blueprint(baseball_api) # register to 'api', not 'app'

  # app.register_blueprint(api) # register app level

  app.register_error_handler(Exception, util.errors.handle_exception)

  filter_loggers() # do this at the end so all the modules are imported & shown in loggerDict

  return app
