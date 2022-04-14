from flask import Blueprint, request, Response
from bson import json_util

from src.app import mongo


discussion_endpoints = Blueprint('discussion_endpoints', __name__)


@discussion_endpoints.route('/discussion', methods=['GET'])
def list_discussions():
    discussions = mongo.db.discussions.find()
    response = json_util.dumps(discussions)
    return Response(response, status=200)


@discussion_endpoints.route('/discussion', methods=['POST'])
def create_discussion():
    author = request.json.get('author')
    content = request.json.get('content')

    if author and content:
        mongo.db.discussions.insert_one(request.json)
        return Response(request.json, status=200) 

    return Response({"msg":"Bad request"}, status=400)





