from random import sample

from db import db


class GameModel(db.Model):
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
        code = sample(self.COLOURS, 4)
        self.first, self.second, self.third, self.fourth = code

    def json(self):
        return {'id': self.id, 'code': [self.first, self.second, self.third,
                                        self.fourth]}

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    def get_result(self, guess_code):
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
        return [self.first, self.second, self.third, self.fourth]

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()