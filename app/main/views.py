from app.requests import get_quote
from flask import render_template, request, redirect, url_for, abort
from flask.helpers import flash
from . import main
# from .forms import UpdateProfile
from ..models import User
from flask_login import login_required
from .. import db,photos
from flask_login import login_required, current_user
# import markdown2  
# from .forms import PostForm, CommentForm
from ..models import Post, Comment, User, Upvote, Category,Quote,Subscriber


@main.route('/')
@main.route('/home')
def index():
    
    """
    View root page function that returns the index page and its data
    """
    # quotes = get_quote()
    title="Welcome to my blog"
    
    return render_template('index.html', title=title)