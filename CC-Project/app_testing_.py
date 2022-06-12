from flask import Flask, jsonify
from flask_cors import CORS

#print("Hello World.. Moga bisa cepat lulus dari bangkit ini. T-T")
#print("Yang ngikut Bangkit di angkatan selanjutnya.. Semangat Kuyyy!!")
#   return (Lulus!)


app = Flask(__name__)
CORS(app)

ujicoba = [
    {
        "id": 1,
        "title": u"Genre Game",
        "description": u"RPG, Open World, FPS, MOBA",
        "done": False,
    },
    {
        "id": 2,
        "title": u"Hobi kesukaan",
        "description": u"I am an adventure rider, I like to riding and go to the destination that has great view landscape",
        "done": False,
    },
    {
        "id": 3,
        "title": u"Still Waiting",
        "description": u"Adalah sebuah kata untuk menunggu sesuatu yang belum pasti, namun berharap agar terwujud.",
        "done": False,
    },
]

@app.route("/")
def home():
    return "Hello Bangkit!!"


@app.route("/json", methods=["GET"])
def get_tasks():
    return jsonify({"ujicoba": ujicoba})