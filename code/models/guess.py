from db import db


class GuessModel(db.Model):
    """
    It represents the guess model.
    """
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
        """
        Class constructor.

        :param game_id: id of the game related with the guess.
        :type game_id: str
        :param result: result of the guess against the game code.
        :type result: tuple
        :param code: incoming code.
        :type code: list
        """
        self.game_id = game_id
        self.black_pegs, self.white_pegs = result
        self.first, self.second, self.third, self.fourth = code

    def json(self):
        """
        It builds the response into a dictonary to send it back through the
        service.

        :return: class response.
        :rtype: dict
        """
        return {'id': self.id, 'result': [self.black_pegs, self.white_pegs]}

    @classmethod
    def find_by_game_id(cls, game_id):
        """
        Class method which returns guesses by a game id.

        :param game_id: id of a game.
        :type game_id: str
        :return: list of guesses filtered by its game id.
        :rtype: list
        """
        return cls.query.filter_by(game_id=game_id).all()

    def save_to_db(self):
        """
        It stores the object in the database.
        """
        db.session.add(self)
        db.session.commit()
