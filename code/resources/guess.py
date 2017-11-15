from flask_restful import Resource, reqparse

from models.guess import GuessModel
from models.game import GameModel


class Guess(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('code',
                        action='append',
                        required=True,
                        help='Every guess needs a code.')

    def post(self, game_id):
        data = Guess.parser.parse_args()
        game = GameModel.find_by_id(game_id)
        result = game.get_result(data['code'])
        guess = GuessModel(game_id, result, **data)

        try:
            guess.save_to_db()
        except:
            return {'message': 'An error ocurred when creating a guess.'}, 500

        return guess.json(), 201

class GuessList(Resource):

    def get(self, game_id):
        return {'guesses': [guess.json() for guess in
                            GuessModel.find_by_game_id(game_id)]}