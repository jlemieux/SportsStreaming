import json
import traceback
import logging
from werkzeug.exceptions import HTTPException
from flask import jsonify


LOGGER = logging.getLogger('main-app')


class NoStreamersFound(Exception):
  def __init__(self, *args, **kwargs):
    super().__init__(*args)
    self.game_id = kwargs.get('game_id')

class NoWeakSpellFound(Exception):
  def __init__(self, *args, **kwargs):
    super().__init__(*args)
    self.game_id = kwargs.get('game_id')

class NoGamesFound(Exception):
  def __init__(self, *args, **kwargs):
    super().__init__(*args)
    self.sport = kwargs.get('sport')


def _log_stacktrace():
  stacktrace = [line for line in traceback.format_exc().split('\n') if line]
  for line in stacktrace:
    LOGGER.error(line)


def handle_exception(e):
  if isinstance(e, HTTPException):
    serializable = {
      'code': e.code,
      'name': e.name,
      'description': e.description,
    }
    _log_stacktrace()
  elif isinstance(e, NoStreamersFound):
    serializable = {
      'code': 404,
      'name': NoStreamersFound.__name__,
      'description': f'No streamers were found for game_id={e.game_id}.',
    }
  elif isinstance(e, NoWeakSpellFound):
    serializable = {
      'code': 404,
      'name': NoWeakSpellFound.__name__,
      'description': f'Weak_Spell stream was not found for game_id={e.game_id}.',
    }
  elif isinstance(e, NoGamesFound):
    serializable = {
      'code': 404,
      'name': NoGamesFound.__name__,
      'description': f'No games were found for sport={e.sport}.',
    }
  else:
    serializable = {
      'code': 500,
      'name': 'Server Error',
      'description': 'Some error occurred on the server.'
    }
    _log_stacktrace()
  
  LOGGER.error(serializable)
  
  return jsonify(serializable), serializable['code']
