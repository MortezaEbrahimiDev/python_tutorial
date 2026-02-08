from flask import Flask,render_template,request,redirect,url_for

app=Flask(__name__
          ,template_folder="templates"
          ,static_folder="statics")




@app.get('/')
def index():
    context={
        "message":request.args.get("message","")
    }
    return render_template('index2.html',context=context)


# @app.get('/contact')
# def contact():
#     return 'contact page'



@app.post('/contact')
def contact():
    app.logger.debug(request.form)
    return redirect(url_for('index',message="your message send successfully"))

