from flask import Flask,render_template,redirect,url_for,request
import uuid
app=Flask(__name__,
          template_folder="templates",
          static_folder="statics"
          )

notes=[{"id":"5716bf0d-9c59-4602-978c-9d3ec5d2550e","title":"note 1","content":"this is a test not"}]

@app.route('/')
def index():
    return render_template("index.html",notes=notes)


@app.post('/create')
def create_note():
    content=request.form.get("content")
    title=request.form.get("title")
    # id=request.form.get("id")
    notes.append({"id":str(uuid.uuid4),"title":title,"content":content})
    return redirect(url_for("index"))


@app.post('/edit/<note_id>')
def edit_note(note_id):
    content=request.form.get("content")
    title=request.form.get("title")
    app.logger.debug(content)
    for note in notes:
        if note["id"]==note_id:
            note["title"]=title
            note["content"]=content
        else:
            print("not not found")
    return redirect(url_for("index"))



@app.post('/delete/<note_id>')
def delete_note(note_id):
    for note in notes:
        if note["id"]==note_id:
            notes.remove(note)
            return redirect(url_for("index"))