from random import sample

from db import db


class GameModel(db.Model):
    """
    It represents the game model
    """
    __tablename__ = 'games'

    COLOURS = ['aqua', 'black', 'blue', 'fuchsia', 'grey', 'green', 'lime',
               'maroon', 'navy', 'olive', 'purple', 'red', 'silver', 'teal',
               'white', 'yellow', 'orange']

    id = db.Column(db.Integer, primary_key=True)

    first = db.Column(db.String(10))
    second = db.Column(db.String(10))
    third = db.Column(db.String(10))
    fourth = db.Column(db.String(10))

    def __init__(self):
        """
        Class constructor
        """
        code = sample(self.COLOURS, 4)
        self.first, self.second, self.third, self.fourth = code

    def json(self):
        """
        It builds the response into a dictonary to send it back through the
        service.

        :return: class response.
        :rtype: dict
        """
        return {'id': self.id, 'code': [self.first, self.second, self.third,
                                        self.fourth]}

    @classmethod
    def find_by_id(cls, _id):
        """
        Class method to find a game by his id.

        :param _id: game id.
        :type _id: str
        :return: game object.
        :rtype: models.game.GameModel
        """
        return cls.query.filter_by(id=_id).first()

    def get_result(self, guess_code):
        """
        Method which calculates the response of the guess given the game code.

        :param guess_code: code send by the guess service.
        :type guess_code: list
        :return: result of the calculation.
        :rtype: tuple
        """
        code = self.get_code()

        black_pegs = 0
        white_pegs = 0
        for element in guess_code:
            if element in code:
                white_pegs += 1
                if guess_code.index(element) == code.index(element):
                    black_pegs += 1
                    white_pegs -= 1

        return (black_pegs, white_pegs)

    def get_code(self):
        """
        It returns the code of the game as a list.

        :return: the game code as a list.
        :rtype: list
        """
        return [self.first, self.second, self.third, self.fourth]

    def save_to_db(self):
        """
        It saves the object in the database.
        """
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        """
        It deletes the objects from the database.
        """
        db.session.delete(self)
        db.session.commit()
