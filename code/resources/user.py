from flask_restful import Resource, reqparse

from models.user import UserModel


class UserRegister(Resource):
    """
    Authentication class.
    """

    parser = reqparse.RequestParser()

    parser.add_argument('username',
                        type=str,
                        required=True,
                        help='This field cannot be blank!')

    parser.add_argument('password',
                        type=str,
                        required=True,
                        help='This field cannot be blank!')

    def post(self):
        """
        It creates a user object or retrieves an error.

        :return: a message plus a 400 or 201 return code.
        :rtype: tuple
        """
        data = UserRegister.parser.parse_args()
        if UserModel.find_by_username(data['username']):
            return {"message": "User with that username already exists."}, 400

        user = UserModel(**data)
        user.save_to_db()

        return {"message": "User created succesfully."}, 201
