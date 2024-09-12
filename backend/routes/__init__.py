from flask import Blueprint

user_bp = Blueprint('users', __name__, url_prefix='/users')
task_bp = Blueprint('tasks', __name__, url_prefix='/tasks')
auth_bp = Blueprint('auths', __name__, url_prefix='/auths')

# Import the routes
from .users import *
from .tasks import *
from .auths import *