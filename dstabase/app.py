from flask import Flask
from pymongo import MongoClient
from bson.json_util import dumps
import names

app = Flask(__name__)
client = MongoClient("mongodb+srv://Solexgreat:solexgreat1$@cluster0.wekq3.mongodb.net/task-manager-project")
db = client.flask_example_db


@app.route('/')
def index():
	return "Hello, Flask with mongodb"

@app.route("/create")
def add_user():
  result = db.users.insert_one({"name": names.get_full_name()})
  return str(result.inserted_id)

@app.route("/list")
def get_user():
  users = list(db.users.find({}))
  return dumps(users)

# @app.route('/users', methods=['POST'])
# def create_user():
#     data = request.get_json()
#     user = User(
#         username=data['username'],
#         email=data['email'],
#         password_hash=data['password_hash']
#     )
#     user.save()
#     return jsonify({"_id": str(user.id)}), 201

# @app.route('/tasks', methods=['POST'])
# def create_task():
# 	data = request.get_json()
# 	user = User.Objects(id=data[user.id])
# 	if user is None:
# 		return jsonify({'Error': 'user not found'}), 404

# 	task = Task(
# 		title = data['title'],
# 		description = data.get('description', ''),
# 		status = data.get('status', 'pending'),
# 		user_id = user,
# 	)
# 	return jsonify({'_id': str(task.id)}), 201



if __name__ == '__main__':
	app.run(debug=True)