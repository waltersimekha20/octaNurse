from flask import Flask,request,make_response,jsonify
from flask_cors import CORS
# from flask_bcrypt import BCrypt
from flask_migrate import Migrate
from model import db
from config import ApplicationConfig
from flask_restful import Api,Resource # type: ignore


def create_app():
    app=Flask(__name__)
    return app

app=create_app()

app.config.from_object(ApplicationConfig)

Migrate(app,db)
# bcrypt = BCrypt(app)
api=Api(app)



class Index(Resource):
    def index(self):
        
        return {"message":"Welcome to Onto Nurse API"}

api.add_resource(Index,'/')

    
if(__name__=="__main__"):
   app.run(debug=True,port=5000)