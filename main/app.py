from flask import Flask
from flask_restful import Api
from main.db import initialize_db
from main.service.routes import initialize_routes

app = Flask(__name__)
api = Api(app)

app.config['MONGODB_SETTINGS'] = {
    'db': 'pokedev',
    'host': '127.0.0.1',
    'port':27017,
    'connect': False
}

initialize_db(app)
initialize_routes(api)

if __name__ == '__main__':
    app.run(debug=True)
