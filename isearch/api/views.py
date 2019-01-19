# coding:utf-8

from flask import render_template, request
from . import api
from isearch.models import *

@api.route("/")
@api.route("/index")
def index():
    return render_template("index.html")

@api.route("/search", methods=["POST"])
def search():
    form = request.form
    stu_name = form.get("stu_name")
    stu_id = form.get("stu_id")

    student = Student.query.filter_by(stu_id=stu_id).first()

    mathscore = MathScore.query.filter_by(stu_id=stu_id).first()
    chinesescore = ChineseScore.query.filter_by(stu_id=stu_id).first()
    englishscore = EnglishScore.query.filter_by(stu_id=stu_id).first()
    writtenscore = MathScore.query.filter_by(stu_id=stu_id).first()
    speakingscore = SpeakingScore.query.filter_by(stu_id=stu_id).first()
    politicalscore = PoliticalScore.query.filter_by(stu_id=stu_id).first()
    historyscore = HistoryScore.query.filter_by(stu_id=stu_id).first()
    geographyscore = GeographyScore.query.filter_by(stu_id=stu_id).first()
    biologicalscore = BiologicalScore.query.filter_by(stu_id=stu_id).first()
    antidrugscore = AntidrugScore.query.filter_by(stu_id=stu_id).first()
    totalscore = TotalScore.query.filter_by(stu_id=stu_id).first()

    titles = ["数学", "语文", "英语", "笔试", "口语", "政治", "历史", "地理", "生物", "禁毒", "总分"]
    scores = [mathscore, chinesescore, englishscore, writtenscore, speakingscore, politicalscore,
             historyscore, geographyscore, biologicalscore, antidrugscore, totalscore]

    return render_template("search.html", 
                           student=student,
                           titles=titles,
                           scores=scores)
