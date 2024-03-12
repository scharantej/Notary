
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    folder_id = db.Column(db.Integer, db.ForeignKey('folder.id'))

class Folder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    notes = db.relationship('Note', backref='folder')

@app.route('/notes/new', methods=['GET', 'POST'])
def new_note():
    if request.method == 'POST':
        note = Note(content=request.form['content'], folder_id=request.form['folder_id'])
        db.session.add(note)
        db.session.commit()
        return redirect(url_for('notes'))
    else:
        folders = Folder.query.all()
        return render_template('notes_form.html', folders=folders)

@app.route('/notes/')
def notes():
    notes = Note.query.all()
    return render_template('notes_list.html', notes=notes)

@app.route('/notes/<int:note_id>')
def note(note_id):
    note = Note.query.get(note_id)
    return render_template('notes_form.html', note=note)

@app.route('/folders/')
def folders():
    folders = Folder.query.all()
    return render_template('folders_list.html', folders=folders)

@app.route('/folders/<int:folder_id>')
def folder(folder_id):
    folder = Folder.query.get(folder_id)
    notes = Note.query.filter_by(folder_id=folder_id)
    return render_template('notes_list.html', notes=notes)

if __name__ == '__main__':
    app.run()
