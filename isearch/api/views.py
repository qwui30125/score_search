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


def insert():
    with open("2018grade7.csv") as f:
        lines = f.readlines()
        title = lines[0].strip().split(",")
        exam = Exam(name="2018年秋季")
        try:
            db.session.add(exam)
        except:
            db.session.rollback()
            raise
        else:
            db.session.commit()
            exam_id = exam.id
        for line in lines[1:]:
            stu_info = line.strip().split(",")
            # 班级,考号,姓名,总分,语文,数学,英语,笔试,口语,政治,历史,地理,生物,禁毒,总分
            # 701,2018012529,朱可欣,531,108,113,114,100,14,47,41,48,50,10,531
            stu_class = stu_info[0]
            stu_id = stu_info[1]
            stu_name = stu_info[2]
            student = Student(stu_id=stu_id, stu_name=stu_name, stu_class=stu_class)
            try:
                db.session.add(student)
            except:
                db.session.rollback()
                raise
            else:
                db.session.commit()
                stu_id = student.id
            chinesescore = ChineseScore(stu_id=stu_id, exam_id=exam_id, score=stu_info[4])
            mathscore = MathScore(stu_id=stu_id, exam_id=exam_id, score=stu_info[5])
            englishscore = EnglishScore(stu_id=stu_id, exam_id=exam_id, score=stu_info[6])
            writtenscore = MathScore(stu_id=stu_id, exam_id=exam_id, score=stu_info[7])
            speakingscore = SpeakingScore(stu_id=stu_id, exam_id=exam_id, score=stu_info[8])
            politicalscore = PoliticalScore(stu_id=stu_id, exam_id=exam_id, score=stu_info[9])
            historyscore = HistoryScore(stu_id=stu_id, exam_id=exam_id, score=stu_info[10])
            geographyscore = GeographyScore(stu_id=stu_id, exam_id=exam_id, score=stu_info[11])
            biologicalscore = BiologicalScore(stu_id=stu_id, exam_id=exam_id, score=stu_info[12])
            antidrugscore = AntidrugScore(stu_id=stu_id, exam_id=exam_id, score=stu_info[13])
            totalscore = TotalScore(stu_id=stu_id, exam_id=exam_id, score=stu_info[14])
        
        try:
            db.session.add_all(chinesescore, mathscore, englishscore, writtenscore, speakingscore, 
                            politicalscore, historyscore, geographyscore, antidrugscore, totalscore)
        except:
            db.session.rollback()
            raise
        else:
            db.session.commit()


if __name__ == "__main__":
    insert()
