from flask_restful import Resource, reqparse
from app.models import db, Auth

parser = reqparse.RequestParser()
parser.add_argument(
    'username', help="This field cannot be blank", required=True)
parser.add_argument(
    'password', help="This field cannot be blank", required=True)


class UserRegistration (Resource):
    print(Resource)
    def post(self):
        data = parser.parse_args()
        new_user = Auth(
            username=data['username'],
            password=data['password']
        )
        try:
            new_user.save_to_db()
            return{
                'message': "User {} was created".format(data['username'])
            }
        except:
            return{'message':"Somthing went worng " },500


class UserLogin (Resource):
    def post(self):
        data = parser.parse_args()
        current_user=Auth.find_username(data['username'])
        return current_user


class UserLogoutAccess (Resource):
    def post(self):
        return {'message': 'User logout'}


class UserLogoutRefresh (Resource):
    def post(self):
        return {'message': 'User logout'}


class TokenRefresh (Resource):
    def post(self):
        return {'message': 'Token refresh'}


class AllUsers (Resource):
    def get(self):
        return {'message': 'List of users'}

    def delete(self):
        return {'message': 'Delete all users'}


class SecretResource (Resource):
    def get(self):
        return {
            'answer': 42
        }
