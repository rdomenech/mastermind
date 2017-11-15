from flask_jwt import jwt_required
from flask_restful import Resource

from models.game import GameModel


class Game(Resource):
    """
    Class which represents a game REST webservice resource.
    """

    @jwt_required()
    def get(self, id):
        """
        It retrieves a game object.

        :param id: id of the game.
        :type id: str
        :return: the representation of a game object or an error message plus
        the 404 return code.
        :rtype: dict or tuple
        """
        game = GameModel.find_by_id(id)
        if game:
            return game.json()

        return {'message': 'Game not found.'}, 404

    @jwt_required()
    def post(self):
        """
        It creates a game object or retrieves a message.

        :return: the representation of a game object plus the 201 or 500 return
        code.
        :rtype: tuple
        """
        game = GameModel()
        try:
            game.save_to_db()
        except:
            return {'message': 'An error occurred when creating the game.'}, \
                   500

        return game.json(), 201

    @jwt_required()
    def delete(self, id):
        """
        It deletes a game object or returns a message.

        :param id: id of the game.
        :type id: str
        :return: a message or a message plus the 404 return code.
        """
        game = GameModel.find_by_id(id)

        if game:
            game.delete_from_db()
            return {'message': 'Game deleted.'}

        return {'message': 'Game not found.'}, 404


class GameList(Resource):
    """
    Class which represents a games REST webservice resource.
    """

    @jwt_required()
    def get(self):
        """
        It retrieves a list of games.

        :return: a list of game representations.
        :rtype: dict
        """
        return {'games': [game.json() for game in GameModel.query.all()]}
