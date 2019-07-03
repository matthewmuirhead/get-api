#import necessary libraries
from flask import Flask, request
from flask_restful import Resource, Api
import json

#create instance of flask framework
app = Flask(__name__)
api = Api(app)

#create function to process data
class Get_Json(Resource):
    def get(self, value):

        #check the value to return corresponding answer
        if (value % 7 == 0) and (value % 9 == 0):
            result = {"result":"CN"}			
        elif (value % 7 == 0):
            result = {"result":"C"}
        elif (value % 9 == 0):
            result = {"result":"N"}
        else:
            result = {"result":value}

        #return answer in json format
        return json.dumps(result)

#add path to call function
api.add_resource(Get_Json, '/GET/<value>')

#run api if it is main
if __name__ == '__main__':
    app.run(port='80')
     
