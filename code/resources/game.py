from flask_restful import Resource

from models.game import GameModel


class Game(Resource):

    def get(self, id):
        game = GameModel.find_by_id(id)
        if game:
            return game.json()

        return {'message': 'Game not found!'}, 404

    def post(self):
        game = GameModel()
        try:
            game.save_to_db()
        except:
            return {'message': 'An error occurred when creating the game.'}, 500

        return game.json(), 201

    def delete(self, id):
        game = GameModel.find_by_id(id)

        if game:
            game.delete_from_db()

        return {'message': 'Game deleted.'}

class GameList(Resource):

    def get(self):
        return {'games': [game.json() for game in GameModel.query.all()]}
