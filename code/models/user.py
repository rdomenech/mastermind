from db import db


class UserModel(db.Model):
    """
    It represents the user model.
    """
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, username, password):
        """
        Class cosntructor.

        :param username: authentication name.
        :type username: str
        :param password: authentication key.
        :type password: str
        """
        self.username = username
        self.password = password

    def save_to_db(self):
        """
        It stores the object in the database.
        """
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        """
        Class method which retrieves a user object by its username.

        :param username: authentication name.
        :type username: str
        :return: a user object.
        :rtype: models.user.UserModel
        """
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        """
        Class method which retrieves a user object by its id.

        :param password: authentication key.
        :type password: str
        :return: a user object.
        :rtype: models.user.UserModel
        """
        return cls.query.filter_by(id=_id).first()
