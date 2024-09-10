from flask import Flask
from . import create_app

app = create_app()

if __name__ == '__main__':
  app.run(debug=True)





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
