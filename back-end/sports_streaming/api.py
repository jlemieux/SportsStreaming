from flask import jsonify, Blueprint
import games
import streamers
import streams


api = Blueprint('api', __name__)


@api.route('/baseball', methods=['GET'])
def hello():
  serialized = [
    {
      'team1': game.team1,
      'team2': game.team2,
      'score': game.score,
      'time': game.time,
      'link': game.link,
      'id': game.id
    }
    for game in games.mlb.get_games()
  ]
  return jsonify(serialized)

@api.route('/baseball/<game_id>', methods=['GET'])
def there(game_id):
  g = games.models.MLBGame(None, None, None, None, f'some/{game_id}')
  s = streamers.mlb.get_streamers(g)
  weak = s[0]
  ss = streams.mlb.fetch_stream(weak)
  return jsonify({'link': ss})
