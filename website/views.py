from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        #note = request.form.get('note')

        #if len(note) < 1:
        #    flash('Note is too short!', category='error')
        #else:
        #    new_note = Note(data=note, user_id=current_user.id)
        #    db.session.add(new_note)
        #    db.session.commit()
        #    flash('Note added!', category='success')
        lockerid = request.form.get('lockerid')

        if lockerid == True:
            flash('You have a locker checked out', category='error')
        else:
            new_locker = LockerId(lockernum=lockerid, user_id=current_user.id)
            db.session.add(new_locker)
            db.session.commit()
            flash('Locker checked out.', category='success')

    return render_template("home.html", user=current_user)

@views.route('/mylocker')
@login_required
def mylocker():
    return render_template("mylocker.html", user=current_user)

@views.route('/locker1')
def locker1():
    return render_template("locker1.html", user=current_user)

@views.route('/locker2')
def locker2():
    flash('Locker is occupied.', category='error')
    return render_template("home.html", user=current_user)

    #return render_template("locker2.html", user=current_user)

@views.route('/locker3')
def locker3():
    flash('Locker is out of order.', category='error')
    return render_template("home.html", user=current_user)

    #return render_template("locker3.html", user=current_user)

@views.route('/locker4')
def locker4():
    flash('Locker is in maintenance.', category='error')
    return render_template("home.html", user=current_user)

    #return render_template("locker4.html", user=current_user)

@views.route('/AboutUs')
def AboutUs():
    return render_template("AboutUs.html", user=current_user)

@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})