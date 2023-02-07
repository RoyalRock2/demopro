from flask import Flask,render_template,request,url_for

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template(template_name_or_list="index.html")


@app.route('/display')
def display():
    msg = "This is your beautiful pic"
    name = request.args["name"].strip().replace(" ","")
    image = "yours.png"
    if "bharath" in name.lower():
        image = "mine.png"
        name = ""
        msg = "Get lost"



    return render_template("display.html",name=name,image=image,msg=msg)


if __name__ == '__main__':
    app.run()