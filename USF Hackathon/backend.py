# Authors: Shyon Ghahghahi, Esha Dupuguntla, Amaya Ling, Carlo Duque

import random as rand
from PIL import Image
import base64
import io
from flask import Flask, request, render_template

score = 10 # Global score tracker
turn = 0

sentData = []

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    img = Image.open("templates/learn2.png")
    imgData = io.BytesIO()
    img.save(imgData, "PNG")
    encoded_img_data = base64.b64encode(imgData.getvalue())


    return render_template("home.html", img=encoded_img_data.decode("utf-8"))

@app.route("/play", methods=["POST"])
def play():
    global turn

    data = [
        ["cat1.jpg", "cat"],
        ["cat2.jpg", "cat"],
        ["germanshepherd.jpeg", "dog"],
        ["goldenretriever.jpeg", "dog"],
        ["dolphin.jpeg", "dolphin"],
        ["shark.jpeg", "shark"],
        ["toucan.jpeg", "bird"],
        ["zebra.jpeg", "zebra"],
        ["penguin.jpeg", "penguin"],
        ["donkey.jpg", "donkey"],
        ["fox.jpg", "fox"],
        ["mouse.jpg", "mouse"],
        ["pig.jpg", "pig"],
        ["squirrel.jpg", "squirrel"],
        ["wolf.jpg", "wolf"]
    ]

    path = "Pictures/"
    options = []
    index = []

    # Loop until we have 4 choices of animals
    while len(options) != 4:

        # Choose random element (animal) from "data" list
        ran = rand.randint(0, len(data) - 1)
        animal = data[ran][1]

        # Add as an option if animal not in list
        if animal not in options:
            options.append(animal)
            index.append(data[ran])

    # Choose which option should be correct one
    correct =  rand.choice(index)
    picture = correct[0]

    answer = correct[1]

    finalAns = []
    finalAns.append(answer)

    for option in options:
        if option != answer:
            finalAns.append(option)
    
    rand.shuffle(finalAns)

    
    # Pass them to the HTML
    img = Image.open(path + picture)
    imgData = io.BytesIO()
    img.save(imgData, "JPEG")
    encoded_img_data = base64.b64encode(imgData.getvalue())
    
    turn += 1

    # return render_template("hackathon.html", img=encoded_img_data.decode("utf-8"), ans1=finalAns[0], ans2=finalAns[1], ans3=finalAns[2], ans4=finalAns[3])

    
    if turn != 10:
        return render_template("hackathon.html", img=encoded_img_data.decode("utf-8"), action="/play", ans1=finalAns[0], ans2=finalAns[1], ans3=finalAns[2], ans4=finalAns[3])
    else:
        return render_template("hackathon.html", img=encoded_img_data.decode("utf-8"), action="/results", ans1=finalAns[0], ans2=finalAns[1], ans3=finalAns[2], ans4=finalAns[3])


@app.route("/results", methods=["GET", "POST"])
def results():
    global score

    score = "Excellent Work!"

    return render_template("results.html", result=score)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)


# http://127.0.0.1:3000/play