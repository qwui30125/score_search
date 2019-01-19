# coding:utf-8

from isearch import db


class Student(db.Model):
    """学生"""
    __tablename__ = "student"
    id = db.Column(db.Integer, primary_key=True) # 
    stu_id = db.Column(db.String(20), unique=True, nullable=False)
    stu_name = db.Column(db.String(32), unique=True, nullable=False)
    stu_class = db.Column(db.String(20))


class Exam(db.Model):
    """考试"""
    __tablename__ = "exam"
    id = db.Column(db.Integer, primary_key=True) # 
    name = db.Column(db.String(60), unique=True, nullable=False)


class Score(db.Model):
    """成绩表"""
    id = db.Column(db.Integer, primary_key=True)
    stu_id = db.Column(db.String(20), db.ForeignKey("student.stu_id"), nullable=False)
    exam_id = db.Column(db.Integer, db.ForeignKey("exam.id"), nullable=False)
    score = db.Column(db.Integer, default=0)
    

class MathScore(Score):
    """数学成绩表"""
    __tablename__ = "mathscore"


class ChineseScore(Score):
    """语文成绩表"""
    __tablename__ = "chinesescore"


class EnglishScore(Score):
    """英语成绩表"""
    __tablename__ = "englishscore"


class WrittenScore(Score):
    """数学成绩表"""
    __tablename__ = "writtenscore"


class SpeakingScore(Score):
    """数学成绩表"""
    __tablename__ = "speakingscore"


class PoliticalScore(Score):
    """数学成绩表"""
    __tablename__ = "politicalscore"


class HistoryScore(Score):
    """数学成绩表"""
    __tablename__ = "historyscore"


class GeographyScore(Score):
    """数学成绩表"""
    __tablename__ = "geographyscore"


class BiologicalScore(Score):
    """生物成绩表"""
    __tablename__ = "biologicalscore"


class AntidrugScore(Score):
    """禁毒成绩表"""
    __tablename__ = "antidrugscore"


class TotalScore(Score):
    """总成绩表"""
    __tablename__ = "totalscore"
