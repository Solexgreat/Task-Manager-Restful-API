from flask import Flask, request, jsonify

from column.app.v1.custom_base_schemas import PyObjectId
import json
import datetime


from routes import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)


app = Flask(__name__)




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