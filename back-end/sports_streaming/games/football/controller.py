import base64
from flask import jsonify, Blueprint
from sports_streaming import games, streamers, streams


api = Blueprint('football_api', __name__, url_prefix='/football')


@api.route('/', methods=['GET'])
def get_games():
  serializable = [
    {
      'team1': game.team1,
      'team2': game.team2,
      'score': game.score,
      'time': game.time,
      'link': game.link,
      'league': game.league
    }
    for game in games.football.service.get_games()
  ]
  return jsonify(serializable)


@api.route('/<streams_link>', methods=['GET'])
def get_stream(streams_link):
  base64_bytes = streams_link.encode('ascii')
  message_bytes = base64.b64decode(base64_bytes)
  streams_link = message_bytes.decode('ascii')
  serializable = {
    'link': streams.football.service.get_stream(
      streamers.football.service.get_best_streamer(streams_link)
    )
  }
  return jsonify(serializable)
