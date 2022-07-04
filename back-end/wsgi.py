from sports_streaming import create_app

app = create_app()

# # import menus
# import games
# import streamers
# import streams
# from flask import jsonify

# # def run():
# #   menus.sports.show_menu()

# # def run():
# #   pass


# # if __name__ == '__main__':
# #   run()

# from flask import Flask
# from flask_cors import CORS

# app = Flask(__name__)
# CORS(app)


# @app.route('/baseball')
# def hello():
#   serialized = [
#     {
#       'team1': game.team1,
#       'team2': game.team2,
#       'score': game.score,
#       'time': game.time,
#       'link': game.link,
#       'id': game.id
#     }
#     for game in games.mlb.get_games()
#   ]
#   return jsonify(serialized)

# @app.route('/baseball/<game_id>')
# def there(game_id):
#   g = games.models.MLBGame(None, None, None, None, f'some/{game_id}')
#   s = streamers.mlb.get_streamers(g)
#   weak = s[0]
#   ss = streams.mlb.fetch_stream(weak)
#   return jsonify({'link': ss})
