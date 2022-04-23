import json
import os
from flask import Flask, jsonify, request
api = Flask(__name__)

#route 1
@api.route('/plus', methods=['POST'])
def plus():
    result = 0
    jsonData = request.get_json()
    x = jsonData.get('x')
    y = jsonData.get('y')
    result = x + y
    resultAsJson = {"result":result}

    return resultAsJson

#route 2
@api.route('/minus', methods=['POST'])
def minus():
    result = 0
    jsonData = request.get_json()
    x = jsonData.get('x')
    y = jsonData.get('y')
    result = x - y
    resultAsJson = {"result":result}
    return resultAsJson

#route 3
@api.route('/multiplePlus', methods=['POST'])
def multiplePlus():
    jsonArray = []
    jsonData = request.get_json()
    index = 1
    for json in jsonData:
        indexText = str(index)
        #result = 0
        result = json['x'] + json['y']
        jsonArray.append({"result"+indexText:result})
        index+=1
    return jsonify(jsonArray)

if __name__ == '__main__':
    api.run()