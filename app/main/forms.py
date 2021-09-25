from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required, Email, Length, EqualTo
from ..models import Post, Comment, Subscriber
from wtforms import ValidationError


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you:',validators = [Required()])
    submit = SubmitField('Submit')


class CategoryForm(FlaskForm):
    name = StringField('Category', validators=[Required()])
    submit = SubmitField('Submit')


class CommentForm(FlaskForm):
    body = StringField('Comment', validators=[Required()])
    submit = SubmitField('Submit')



class SubscriberForm(FlaskForm):
    email = StringField('Email', validators=[
                        Required(), Length(1, 80), Email()])
    submit = SubmitField('Subscribe')



