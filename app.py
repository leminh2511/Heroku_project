from flask import Flask,render_template

app = Flask(__name__)


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
    }
]
@app.route("/sport")
def sport():
    return render_template("Sport.html",sport_list=sport_list)

@app.route("/myself")
def myself():
    return render_template("my_self.html")

if __name__ == '__main__':
    app.run()
