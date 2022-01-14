from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError
from flaskblog.models import User

class entryName(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(max=30)])
    submit = SubmitField("Enter Username")

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()

class questions(FlaskForm):
    question_1 = StringField("Question_1", validators=[DataRequired(), Length(max=20)])
    question_2 = StringField("Question_2", validators=[DataRequired(), Length(max=20)])
    question_3 = StringField("Question_3", validators=[DataRequired(), Length(max=20)])
    question_4 = StringField("Question_4", validators=[DataRequired(), Length(max=20)])
    question_5 = StringField("Question_5", validators=[DataRequired(), Length(max=20)])
    
    submit = SubmitField('Enter')

class score_page(FlaskForm):
    submit = SubmitField('Continue')
    