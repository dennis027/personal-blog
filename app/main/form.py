from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, SubmitField,DateField
from wtforms.validators import Required

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Write a brief bio about you.',validators = [Required()])
    submit = SubmitField('Save')

class PitchForm(FlaskForm):
    title = StringField('Title', validators=[Required()])
    category = SelectField('Category', choices=[('Events','Events'),('Job','Job'),('Advertisement','Advertisement')],validators=[Required()])
    # date_of_birth = DateField('Date of Birth', validators=[Required()])
    hobbies= TextAreaField('Hobbies', validators=[Required()])
    about=TextAreaField('About', validators=[Required()])
    contact=TextAreaField('Contact', validators=[Required()])
    twitter=TextAreaField('Twitter')
    facebook=TextAreaField('Facebook')
    instagram=TextAreaField('Instagram')
    email=TextAreaField('Email')

    post = TextAreaField('About Me', validators=[Required()])
    submit = SubmitField('Your Post')

class CommentForm(FlaskForm):
    comment = TextAreaField('Leave a comment',validators=[Required()])
    submit = SubmitField('Comment')

