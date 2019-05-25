from flask_restplus import Namespace, Resource
from flask import jsonify, request

from myapp.models.APIModel import UsersModels as apimodel

from myapp import db
from myapp.models.dbModel import UserInfo


main = Namespace('api')


@main.route('/')
class MainRestAPIs(Resource):
    @main.expect(apimodel.user)
    def post(self):

        username = request.json.get('username')
        adduser = UserInfo(username=username)
        try:
            db.session.add(adduser)
            db.session.commit()
        except Exception as e:
            return jsonify({'dbmsg': str(e)})

        return jsonify({'msg': username, 'status': 'add completed'})


@main.route('/getuser')
class Getuser(Resource):
    def get(self):

        getuser = db.session.query(UserInfo).all()

        data = []
        for i in getuser:
            temp = {}
            temp['id'] = i.id
            temp['username'] = i.username
            temp['created'] = i.created
            data.append(temp)

        print(getuser)

        return jsonify(data)
