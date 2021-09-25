from flask import Blueprint

main = Blueprint('main', __name__)
# try:
from app.main import views
# except:
