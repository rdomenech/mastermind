from flask_jwt import jwt_required
from flask_restful import Resource, reqparse

from models.guess import GuessModel
from models.game import GameModel


class Guess(Resource):
    """
    Class which represents a guess REST webservice resource.
    """

    parser = reqparse.RequestParser()
    parser.add_argument('code',
                        action='append',
                        required=True,
                        help='Every guess needs a code.')

    @jwt_required()
    def post(self, game_id):
        """
        It creates a guess object or retrieves an error.

        :param game_id: id of the guess game.
        :type game_id: str
        :return: the representation of a guess object plus the 201 return code
        or an error message plus the 500 return code.
        :rtype: tuple
        """
        data = Guess.parser.parse_args()
        game = GameModel.find_by_id(game_id)

        try:
            result = game.get_result(data['code'])
            guess = GuessModel(game_id, result, **data)
            guess.save_to_db()
        except:
            return {'message': 'An error ocurred when creating a guess.'}, 500

        return guess.json(), 201


class GuessList(Resource):
    """
    Class which represents a guesses REST webservice resource.
    """

    @jwt_required()
    def get(self, game_id):
        """
        It retrieves a list of guesses.

        :return: a list of guess representations.
        :rtype: dict
        """
        return {'guesses': [guess.json() for guess in
                            GuessModel.find_by_game_id(game_id)]}
