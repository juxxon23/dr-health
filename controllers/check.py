from flask import jsonify, request
from flask.views import MethodView
from config.config import KEY_TOKEN_AUTH
import jwt

class Check(MethodView):

    def get(self):
        header = request.headers.get('Authorization')
        if header:
            token = header.split(" ")
            try:
                token_auth = jwt.decode(token[1], KEY_TOKEN_AUTH, algorithms=['HS256'])
                return jsonify({'state':'welcome'}), 200
            except:
                return jsonify({'state':'token'}), 403
        return jsonify({'state':'not found'}), 404
