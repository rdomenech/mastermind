from db import db


class GuessModel(db.Model):
    __tablename__ = 'guesses'

    COLOURS = ['aqua', 'black', 'blue', 'fuchsia', 'grey', 'green', 'lime',
               'maroon', 'navy', 'olive', 'purple', 'red', 'silver', 'teal',
               'white', 'yellow', 'orange']

    id = db.Column(db.Integer, primary_key=True)

    game_id = db.Column(db.Integer, db.ForeignKey('games.id'))
    game = db.relationship('GameModel')

    first = db.Column(db.String(10))
    second = db.Column(db.String(10))
    third = db.Column(db.String(10))
    fourth = db.Column(db.String(10))

    black_pegs = db.Column(db.Integer)
    white_pegs = db.Column(db.Integer)

    def __init__(self, game_id, result, code):
        self.game_id = game_id
        self.black_pegs, self.white_pegs = result
        self.first, self.second, self.third, self.fourth = code

    def json(self):
        return {'id': self.id, 'result': [self.black_pegs, self.white_pegs]}

    @classmethod
    def find_by_game_id(cls, game_id):
        return cls.query.filter_by(game_id=game_id).all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
