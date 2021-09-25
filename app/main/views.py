from app.requests import get_quote
from flask import render_template, request, redirect, url_for, abort
from flask.helpers import flash
from . import main
from .forms import UpdateProfile
from ..models import User
# from flask_login import login_required
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
    quotes = get_quote()
    title="Welcome to my blog"
    
    return render_template('index.html',title=title,quotes=quotes,current_user=current_user)


@main.route('/posts')
@login_required
def posts():
    posts = Post.query.all()
    likes = Upvote.query.all()
    user = current_user
    return render_template('blog.html', posts=posts, likes=likes, user=user)


@main.route("/user/<uname>")
@login_required
def profile(uname):
    user = User.query.filter_by(username=uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user=user)


@main.route("/user/<uname>/update", methods=["GET", "POST"])
def update_profile(uname):
    user = User.query.filter_by(username=uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for(".profile", uname=user.username))

    return render_template("profile/update.html", form=form)



@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))


@main.route('/user')
@login_required
def user():
    username = current_user.username
    user = User.query.filter_by(username=username).first()
    if user is None:
        return ('not found')
    return render_template('profile.html', user=user)

