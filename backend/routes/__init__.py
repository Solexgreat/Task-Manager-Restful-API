from flask import Blueprint

user_bp = Blueprint('users', __name__, url_prefix='/users')
task_bp = Blueprint('tasks', __name__, url_prefix='/tasks')

# Import the routes
from .users import *
from .tasks import *