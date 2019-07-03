from flask import Flask, request
from flask_restful import Resource, Api
import json

app = Flask(__name__)
api = Api(app)

class Get_Json(Resource):
    def get(self, value):
        
        if (value % 7 == 0) and (value % 9 == 0):
            result = {"result":"CN"}			
        elif (value % 7 == 0):
            result = {"result":"C"}
        elif (value % 9 == 0):
            result = {"result":"N"}
        else:
            result = {"result":value}
        return json.dumps(result)

api.add_resource(Get_Json, '/GET/<value>')


if __name__ == '__main__':
     app.run(port='80')
     
