class student_infor(db.Model):
    __tablename__ = 'student_infor'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(10))
    english_score = db.Column(db.Integer)
    python_score = db.Column(db.Integer)
    C_score = db.Column(db.Integer)
    score_sum = db.Column(db.Integer)
