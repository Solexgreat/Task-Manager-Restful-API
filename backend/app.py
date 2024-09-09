from flask import Flask, request, jsonify

from column.app.v1.custom_base_schemas import PyObjectId
import json
import datetime


from routes import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)


app = Flask(__name__)





@app.route("/reset_tokens/<user_email>", methods=['GET'], strict_slashes=False)
def reset_token(user_email):
	try:
		reset_token = get_reset_password_token(user_email)
		return jsonify({"reset_token": reset_token}), 200
	except BadRequest as e:
			return jsonify({"error": str(e)}), 400
	except Exception as e:
			return jsonify({"error": "An error occurred"}), 500

@app.route("/reset_password", methods=['POST'], strict_slashes=False)
def reset_password():
	data = request.json
	try:
		updated_password= update_password(data['reset_token'], data['password'])
		if updated_password is None:
			return jsonify({"success": "password changed successfully"}), 200
	except BadRequest as e:
		return jsonify({'error': str(e)}), 400
	except Exception as e:
		return jsonify({"error": str(e)}), 500


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