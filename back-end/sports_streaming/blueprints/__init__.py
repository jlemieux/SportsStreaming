import threading
import subprocess
import pathlib
from flask import jsonify, Blueprint
from sports_streaming.games.baseball.controller import api as baseball_api


api = Blueprint('sports_streaming', __name__) # app level blueprint


@api.route('/shutdown', methods=['GET'])
def shutdown():
  thread = threading.Timer(2.0, _shutdown)
  thread.start()
  return jsonify({'shutdown': True})

def _shutdown():
  print('Running shutdown...')
  script = pathlib.Path(__file__).parents[3] / 'scripts/shutdown.sh'
  subprocess.Popen([script])


# blueprint modules
api.register_blueprint(baseball_api)
