from flask import Blueprint
from app import db
from models import Student

student_bp = Blueprint('student', __name__)


@student_bp.route('/student', methods=['POST', 'GET'])
def get(self, id):
    student = Student.find_by_id(id)
