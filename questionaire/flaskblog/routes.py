import os
from flaskblog.forms import entryName, questions, score_page
from flaskblog.models import User, Questions
from flask import render_template, redirect, url_for, request, flash
from flaskblog import app, db

@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                 endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)

@app.route("/", methods=['GET', 'POST'])
def home():
    form = entryName()
    if form.validate_on_submit():
        user = User(username=form.username.data)
        db.session.add(user)
        db.session.commit()
        flash(f"Welcome Plase answer the following question to get the results", 'success')
        return redirect(url_for('game'))
    return render_template('home.html', form=form)


@app.route("/game", methods=["GET", "POST"])
def game():
    form = questions()
    score = 0
    if request.method == "POST" and form.validate_on_submit():
        Questions = {
            "When did malaysia gain independence" : form.question_1.data == "31/8/57",
            "What is the name of Malaysia before the unification" : form.question_2.data == "melaya",
            "What is the capital city of Malaysia" : form.question_3.data == "kl",
            "Who is ur current prime minister of Malaysia" : form.question_4.data ==  "muyiddin yassin",
            "How many PM do we have so far" : form.question_5.data == "8"             
        }
        #this will itterate the values in the dictionary
        for answer in Questions.values():
            #if the value = true then the score will be incremented
            if answer == True:
                score += 1
        return render_template('result_page.html', Questions=Questions, score=score)
    user = User.query.all()
    return render_template('game_page.html', user=user, form=form)

@app.route("/result_page", methods=["GET", "POST"])
def result_page():
        User.query.delete()
        db.session.commit()
        return redirect(url_for('home'))   
    #elif score_page.answer == Questions:
    #    score = score + 1
    #return render_template('result_page.html', form=form, score=score)
