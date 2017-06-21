from flask import Flask, Response, request, url_for, redirect, jsonify, render_template
from flask_restful import Resource, Api

app = Flask(__name__)

app = Flask(__name__)
api = Api(app)

todos = {}

class TodoSimple(Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}

api.add_resource(TodoSimple, '/<string:todo_id>')

@app.route('/test')
def test():
    return 'OMG'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
