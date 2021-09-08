from flask import Flask
from flask_restful import Resource, Api, reqparse
import json

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('data')


class ChatRobot(Resource):
    list_word = ['您好，您吃了吗？', '回见了您内', '天气不错']
    def post(self):
        args = parser.parse_args()
        date = json.loads(args['data'])
        if '您好' in date['msg']:
            result = self.list_word[0]
            if '再见' in date['msg']:
                result = self.list_word[2]
        else:
            if '再见' in date['msg']:
                result = self.list_word[1]
        return {"result": result}


api.add_resource(ChatRobot, '/chat')

# 指定flask_restful取消ensure_ascii输出中文
app.config.update(RESTFUL_JSON=dict(ensure_ascii=False))

app.run()
