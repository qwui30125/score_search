from flask import Flask
from flask import render_template
import sys

app = Flask(__name__)

@app.route("/01/")
def index01():
    return render_template("01_onclick.html")

@app.route("/02/")
def index02():
    return render_template("02_script_import.html")

@app.route("/03/")
def index03():
    return render_template("03_practice.html")


@app.route("/04/")
def index04():
    return render_template("04_var.html")

@app.route("/PI/")
def PI():
    return render_template("pi.html")

@app.route("/hello/")
def hello():
    return render_template("hello.html")

@app.route("/index/")
def index():
    titles, prices, users, images, icons = getItemInfo()
    return render_template("customers.html", 
                           titles = titles, 
                           prices = prices, 
                           users = users,
                           images = images,
                           icons = icons)

# @app.route("/02/01.js")
# def index03():
#     return render_template("01.js")
# 
def getItemInfo():
    import re
    import urllib.request
    url = "https://2.taobao.com"
    res = urllib.request.urlopen(url)
    data = res.read().decode('gbk')
    data = f.read()
    title_pattern = "class=\"item-title\">([\s\S]+?)</p>" 
    titles = re.findall(title_pattern, data)
    price_pattern = "class=\"price-value\">(\d+)</p>"
    prices = re.findall(price_pattern, data)
    user_pattern = "class=\"user-name\">([\s\S]+?)</p>"
    users = re.findall(user_pattern, data)
    img_pattern = "class=\"item-img\"[\s\S]+?url\(&quot;([\s\S]+?)&quot;\)"
    images = re.findall(img_pattern, data)
    icon_pattern = "class=\"user-info\"><img data-v-4c853d07=\"\" src=\"([\s\S]+?)\" class=\"usericon\""
    # icon_pattern = "src=\"([\s\S]+?)\" class=\"usericon\""
    icons = re.findall(icon_pattern, data)
    print(len(icons))
    print(icons[2])
    with open("image_url", "w") as f:
                  

    return titles, prices, users, images, icons
        

if __name__ == "__main__":
    app.run(debug=True)

