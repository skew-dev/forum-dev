from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_URI'] = "mongodb://localhost/forum-dev"

mongo = PyMongo(app)

from src.endpoints.discussion import discussion_endpoints
app.register_blueprint(discussion_endpoints, url_prefix='/api')

