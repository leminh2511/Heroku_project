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
# OOP: Object Oriented Programming
class Ninja:
    def __init__(self,name,atk,def_,hp):  #Contructor
        self.name = name
        self.atk = atk
        self.def_ = def_
        self.hp = hp
    def print(self):    #Context
        print("'{0}',{1},{2},{3}".format(self.name,self.atk,self.def_,self.hp))
    def attack(self, other):
        print("{0} attack {1}".format(self.name, other.name))
        if self.atk>other.def_:
            other.hp=other.hp-(self.atk-other.def_)
            print(self,other)
        else:
            self.hp=self.hp-(other.def_-self.atk)
            print(self, other)

ninja1 = Ninja(name="Naruto",atk=10,def_=9,hp=8)  #Ninja() -> la ham init, ninja1,2 la bien (self)
ninja2 = Ninja(name="Sasuke",atk=9,def_=6,hp=7)

ninja1.attack(ninja2)

print(ninja1.atk)
ninja1.atk= 10 #-> dau . la of ninja 1
print(ninja1.atk)
# ninja1.print() la xai ham print cho ninja1
ninja1.print()
ninja2.print()

class User(Document):
    email=StringField()
    password=StringField()

class Sport(Document):
    name=StringField()
    desc=StringField()
    img=StringField()
    link=StringField()

@app.route('/')
def hello_world():
    return 'Hello World!'
sport_list=[
    {
        "name":"Badminton",
        "desc":"Badminton World Federation",
        "link":"http://bwfbadminton.com/",
        "img":"http://www.chinadaily.com.cn/sports/images/attachement/jpg/site1/20150514/f8bc1269fd8316be3f5b01.jpg"
    },
    {
        "name":"Football",
        "desc":"FIFA",
        "link":"http://www.fifa.com/",
        "img":"http://www.chronicle.co.zw/wp-content/uploads/2016/11/soccer1.jpg"
    },
    {
        "name":"Tennis",
        "desc":"International Tennis Federation",
        "link":"http://www.atpworldtour.com/en",
        "img":"https://www.queenoftickets.com/media/wysiwyg/ausopen/maria-sharapova.jpg"
    },
    {
        "name":"Swimming",
        "desc":"International Swimming Federation",
        "link":"https://www.fina.org/",
        "img":"http://www.iphotoscrap.com/Image/837/1222047723-m.jpg"
    },
    {
        "name":"Motorcycle racing",
        "desc":"Federation of International Motorcycling",
        "link":"http://www.fim-live.com/",
        "img":"https://s-media-cache-ak0.pinimg.com/736x/7d/8e/38/7d8e38e61e77c67d556ea11cef5cf9a2.jpg"
    },
    {
        "name":"Boxing",
        "desc":" International Boxing Federation",
        "link":"http://www.worldboxingfederation.net/",
        "img":"https://s-media-cache-ak0.pinimg.com/736x/d1/10/71/d110715ac88f2caaf3c09a3cd5befa01.jpg"
    },
    {
        "name":"Japanese Anti-Virus",
        "desc":"JAV ^^",
        "link":"https://www.facebook.com/javfanclub02/",
        "img":"http://www.japantrends.com/japan-trends/wp-content/uploads/2014/08/akb48-idol-group-decline-popularity-tv-commercials.jpg"
    }
]
# Up sport_list len Mlab
# for sport_local in sport_list:
#     name = sport_local["name"]
#     desc = sport_local["desc"]
#     link = sport_local["link"]
#     img = sport_local["img"]
#     idea=Sport(name=name,desc=desc,link=link,img=img)
#     idea.save()

@app.route("/sport",methods=["GET","POST"])
def sport():
    if request.method =="GET":
        # keo du lieu tren Mlab
        return render_template("Sport.html",sport_list=Sport.objects)
    elif request.method=="POST":
        name=request.form["name"]
        desc=request.form["desc"]
        link=request.form["link"]
        img=request.form["img"]

        idea=Sport(name=name,desc=desc,link=link,img=img)
        idea.save()
        return 'ok'

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

        user = User(email=email,password=password)
        user.save()
        # kiem tra tai khoan
        return "Thank you for registering"



if __name__ == '__main__':
    app.run()
