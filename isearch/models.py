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


class MathScore(Score):
    """数学成绩表"""
    __tablename__ = "mathscore"
        id = db.Column(db.Integer, primary_key=True)
    stu_id = db.Column(db.String(20), db.ForeignKey("student.stu_id"), nullable=False)
    exam_id = db.Column(db.Integer, db.ForeignKey("exam.id"), nullable=False)
    score = db.Column(db.Integer, default=0)


class ChineseScore(Score):
    """语文成绩表"""
    __tablename__ = "chinesescore"
    id = db.Column(db.Integer, primary_key=True)
    stu_id = db.Column(db.String(20), db.ForeignKey("student.stu_id"), nullable=False)
    exam_id = db.Column(db.Integer, db.ForeignKey("exam.id"), nullable=False)
    score = db.Column(db.Integer, default=0)


class EnglishScore(Score):
    """英语成绩表"""
    __tablename__ = "englishscore"
    id = db.Column(db.Integer, primary_key=True)
    stu_id = db.Column(db.String(20), db.ForeignKey("student.stu_id"), nullable=False)
    exam_id = db.Column(db.Integer, db.ForeignKey("exam.id"), nullable=False)
    score = db.Column(db.Integer, default=0)


class WrittenScore(Score):
    """数学成绩表"""
    __tablename__ = "writtenscore"
    id = db.Column(db.Integer, primary_key=True)
    stu_id = db.Column(db.String(20), db.ForeignKey("student.stu_id"), nullable=False)
    exam_id = db.Column(db.Integer, db.ForeignKey("exam.id"), nullable=False)
    score = db.Column(db.Integer, default=0)


class SpeakingScore(Score):
    """数学成绩表"""
    __tablename__ = "speakingscore"
    id = db.Column(db.Integer, primary_key=True)
    stu_id = db.Column(db.String(20), db.ForeignKey("student.stu_id"), nullable=False)
    exam_id = db.Column(db.Integer, db.ForeignKey("exam.id"), nullable=False)
    score = db.Column(db.Integer, default=0)


class PoliticalScore(Score):
    """数学成绩表"""
    __tablename__ = "politicalscore"
    id = db.Column(db.Integer, primary_key=True)
    stu_id = db.Column(db.String(20), db.ForeignKey("student.stu_id"), nullable=False)
    exam_id = db.Column(db.Integer, db.ForeignKey("exam.id"), nullable=False)
    score = db.Column(db.Integer, default=0)


class HistoryScore(Score):
    """数学成绩表"""
    __tablename__ = "historyscore"
    id = db.Column(db.Integer, primary_key=True)
    stu_id = db.Column(db.String(20), db.ForeignKey("student.stu_id"), nullable=False)
    exam_id = db.Column(db.Integer, db.ForeignKey("exam.id"), nullable=False)
    score = db.Column(db.Integer, default=0)


class GeographyScore(Score):
    """数学成绩表"""
    __tablename__ = "geographyscore"
    id = db.Column(db.Integer, primary_key=True)
    stu_id = db.Column(db.String(20), db.ForeignKey("student.stu_id"), nullable=False)
    exam_id = db.Column(db.Integer, db.ForeignKey("exam.id"), nullable=False)
    score = db.Column(db.Integer, default=0)


class BiologicalScore(Score):
    """生物成绩表"""
    __tablename__ = "biologicalscore"
    id = db.Column(db.Integer, primary_key=True)
    stu_id = db.Column(db.String(20), db.ForeignKey("student.stu_id"), nullable=False)
    exam_id = db.Column(db.Integer, db.ForeignKey("exam.id"), nullable=False)
    score = db.Column(db.Integer, default=0)


class AntidrugScore(Score):
    """禁毒成绩表"""
    __tablename__ = "antidrugscore"
    id = db.Column(db.Integer, primary_key=True)
    stu_id = db.Column(db.String(20), db.ForeignKey("student.stu_id"), nullable=False)
    exam_id = db.Column(db.Integer, db.ForeignKey("exam.id"), nullable=False)
    score = db.Column(db.Integer, default=0)


class TotalScore(Score):
    """总成绩表"""
    __tablename__ = "totalscore"
    id = db.Column(db.Integer, primary_key=True)
    stu_id = db.Column(db.String(20), db.ForeignKey("student.stu_id"), nullable=False)
    exam_id = db.Column(db.Integer, db.ForeignKey("exam.id"), nullable=False)
    score = db.Column(db.Integer, default=0)
