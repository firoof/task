from flask import Flask
from flask_restful import Resource, Api
import datetime

app = Flask(__name__)
api = Api(app)

class GetDate(Resource):
    def get(self):
        tody = str(datetime.date.today())
        date = {"date": tody}
        return date

api.add_resource(GetDate, '/get_date')
app.run()