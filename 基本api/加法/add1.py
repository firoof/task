from flask import Flask
from flask_restful import Resource, Api, reqparse
import json

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('data')

class AddCount(Resource):
    num = 0
    def post(self):
        args = parser.parse_args()
        data = json.loads(args['data'])
        for val in data["value_array"]:
            self.num += int(val["value"])
        result = {"result": self.num}
        return result


api.add_resource(AddCount, '/add')

app.run()
