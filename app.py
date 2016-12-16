from flask import Flask,render_template,url_for,request
import mongoengine
from mongoengine import *

app = Flask(__name__)
host="ds133428.mlab.com"
port=33428
db_name="minhle"
user_name="sport_minh"
password="ckiuckiu2511"
mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)
class User(Document):
    email=StringField()
    password=StringField()
class Sport(Document):
    name=StringField()
    sport=StringField()
    link=StringField()
@app.route('/')
def hello_world():
    return 'Hello World!'
sport_list=[
    {
        "Name":"Badminton",
        "Desc":"Badminton World Federation",
        "link":"http://bwfbadminton.com/",
        "img":"http://www.chinadaily.com.cn/sports/images/attachement/jpg/site1/20150514/f8bc1269fd8316be3f5b01.jpg"
    },
    {
        "Name":"Football",
        "Desc":"FIFA",
        "link":"http://www.fifa.com/",
        "img":"http://www.chronicle.co.zw/wp-content/uploads/2016/11/soccer1.jpg"
    },
    {
        "Name":"Tennis",
        "Desc":"International Tennis Federation",
        "link":"http://www.atpworldtour.com/en",
        "img":"https://www.queenoftickets.com/media/wysiwyg/ausopen/maria-sharapova.jpg"
    },
    {
        "Name":"Swimming",
        "Desc":"International Swimming Federation",
        "link":"https://www.fina.org/",
        "img":"http://www.iphotoscrap.com/Image/837/1222047723-m.jpg"
    },
    {
        "Name":"Motorcycle racing",
        "Desc":"Federation of International Motorcycling",
        "link":"http://www.fim-live.com/",
        "img":"https://s-media-cache-ak0.pinimg.com/736x/7d/8e/38/7d8e38e61e77c67d556ea11cef5cf9a2.jpg"
    },
    {
        "Name":"Boxing",
        "Desc":" International Boxing Federation",
        "link":"http://www.worldboxingfederation.net/",
        "img":"https://s-media-cache-ak0.pinimg.com/736x/d1/10/71/d110715ac88f2caaf3c09a3cd5befa01.jpg"
    },
    {
        "Name":"Japanese Anti-Virus",
        "Desc":"JAV ^^",
        "link":"https://www.facebook.com/javfanclub02/",
        "img":"http://www.japantrends.com/japan-trends/wp-content/uploads/2014/08/akb48-idol-group-decline-popularity-tv-commercials.jpg"
    }
]
@app.route("/sport",methods=["GET","POST"])
def sport():
    if request.method =="GET":
        return render_template("Sport.html",sport_list=sport_list)
    elif request.method=="POST":
        name=request.form["name"]
        sport=request.form["sport"]
        link=request.form["link"]

        idea=Sport(name=name,sport=sport,link=link)
        idea.save()
        return "Thank for your ideas"

@app.route("/myself")
def myself():
    return render_template("my_self.html")

@app.route("/register",methods=["GET","POST"])
def register():
    if request.method=="GET":
        return render_template("register_form.html")
    elif request.method=="POST":
        email=request.form["email"]
        password=request.form["password"]

        user = User(email=email,password=password) #Contructor
        user.save()
        # kiem tra tai khoan
        return "Thank you for registering"



if __name__ == '__main__':
    app.run()
