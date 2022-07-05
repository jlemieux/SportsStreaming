from flask import jsonify, Blueprint
from sports_streaming import games, streamers, streams


api = Blueprint('baseball_api', __name__, url_prefix='/baseball')


@api.route('/', methods=['GET'])
def get_games():
  serializable = [
    {
      'team1': game.team1,
      'team2': game.team2,
      'score': game.score,
      'time': game.time,
      'link': game.link,
      'id': game.id
    }
    for game in games.baseball.service.get_games()
  ]
  return jsonify(serializable)


@api.route('/<game_id>', methods=['GET'])
def get_stream(game_id):
  serializable = {
    'link': streams.baseball.service.get_stream(
      streamers.baseball.service.get_best_streamer(game_id)
    )
  }
  return jsonify(serializable)
