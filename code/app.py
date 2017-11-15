from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from resources.game import Game, GameList
from resources.guess import Guess, GuessList
from resources.user import UserRegister
from security import authenticate, identity

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'roger'
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


jwt = JWT(app, authenticate, identity)

api.add_resource(Game, '/game', '/game/<string:id>')
api.add_resource(GameList, '/games')
api.add_resource(Guess, '/guess/<string:game_id>')
api.add_resource(GuessList, '/guesses/<string:game_id>')
api.add_resource(UserRegister, '/register')


if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
