from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column,Integer,String


app = Flask(__name__)

HOSTNAME = "127.0.0.1"
POST = 3306
USERNAME = "root"
PASSWORD = "522526"
DATABASE = "world"

db_url = "mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8mb4".format(USERNAME,PASSWORD,HOSTNAME,POST,DATABASE)
app.config['SQLALCHEMY_DATABASE_URI']=db_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class student_infor(db.Model):
    __tablename__ = 'student_infor'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(10))
    english_score = db.Column(db.Integer)
    python_score = db.Column(db.Integer)
    C_score = db.Column(db.Integer)
    score_sum = db.Column(db.Integer)


db.create_all()
@app.route("/",endpoint="index")
def index():
    a = db.session.query(student_infor).all()
    b = len(a)
    return render_template("index.html",b=b)

@app.route("/append/",methods=['POST','GET'],endpoint="add")
def add_stu_infor():
    if request.method.lower() == "post":
        id_get = request.form.get("id")
        name_get = request.form.get("name")
        english_get = request.form.get("e_score")
        python_get = request.form.get("p_score")
        c_get = request.form.get("c_score")
        if id_get and name_get and english_get and python_get and c_get:
            score_num = int(english_get)+int(python_get)+int(c_get)
            stu_infor = student_infor(id=id_get,name=name_get,english_score=english_get,python_score=python_get,C_score=c_get,score_sum=score_num)
            db.session.add(stu_infor)
            db.session.commit()
            return render_template("add_stu.html",ok="添加成功")
        else:
            return render_template("add_stu.html",err="请检查是否有漏填")

    else:
        return render_template("add_stu.html")

@app.route("/find/",methods=["POST",'GET'],endpoint="find")
def find_stu_infor():
    if request.method.lower() == "post":
        get_cond = request.form.get("condation")
        get_cont = request.form.get("tiaojian")
        if get_cond == "学号":
            a = db.session.query(student_infor).filter(student_infor.id == int(get_cont)).all()
            return render_template("find_stu.html",stu_list = a)
        if get_cond == "姓名":
            a = db.session.query(student_infor).filter(student_infor.name == get_cont).all()
            return render_template("find_stu.html",stu_list = a)
        if get_cond == "english分数":
            a = db.session.query(student_infor).filter(student_infor.english_score == int(get_cont)).all()
            return render_template("find_stu.html",stu_list = a)
        if get_cond == "python分数":
            a = db.session.query(student_infor).filter(student_infor.python_score == int(get_cont)).all()
            return render_template("find_stu.html",stu_list = a)
        if get_cond == "C语言分数":
            a = db.session.query(student_infor).filter(student_infor.C_score == int(get_cont)).all()
            return render_template("find_stu.html",stu_list = a)
    return render_template("find_stu.html")

@app.route("/del/",methods=["POST","GET"],endpoint="del")
def dele_stu_infor():
    if request.method.lower() == "post":
        stu_num = request.form.get("stu_id")
        db.session.query(student_infor).filter(student_infor.id == int(stu_num)).delete()
        db.session.commit()
        return render_template("del_stu.html",of="学生信息删除成功")
    else:
        return render_template("del_stu.html")
@app.route("/alter/",methods=["POST","GET"],endpoint="alter")
def alter_stu_infor():
    if request.method.lower() == "post":
        id_get = request.form.get("id")
        get_cond = request.form.get("condation")
        get_cont = request.form.get("tiaojian")
        if get_cond == "姓名":
            db.session.query(student_infor).filter(student_infor.id == int(id_get)).update({"name":get_cont})
            db.session.commit()
            return render_template("alter_stu.html",ok="修改成功")
        if get_cond == "english分数":
            db.session.query(student_infor).filter(student_infor.id == int(id_get)).update({"english_score":int(get_cont)})
            db.session.commit()
            a = db.session.query(student_infor).filter(student_infor.id == int(id_get))
            for i in a:
                a1 = i.english_score
                a2 = i.python_score
                a3 = i.C_score
                a4 = a1+a2+a3
                db.session.query(student_infor).filter(student_infor.id == int(id_get)).update({"score_sum":a4})
                db.session.commit()
            return render_template("alter_stu.html",ok="修改成功")
        if get_cond == "python分数":
            db.session.query(student_infor).filter(student_infor.id == int(id_get)).update({"python_score":int(get_cont)})
            db.session.commit()
            a = db.session.query(student_infor).filter(student_infor.id == int(id_get))
            for i in a:
                a1 = i.english_score
                a2 = i.python_score
                a3 = i.C_score
                a4 = a1+a2+a3
                db.session.query(student_infor).filter(student_infor.id == int(id_get)).update({"score_sum":a4})
                db.session.commit()
            return render_template("alter_stu.html",ok="修改成功")
        if get_cond == "C语言分数":
            db.session.query(student_infor).filter(student_infor.id == int(id_get)).update({"C_score":int(get_cont)})
            db.session.commit()
            a = db.session.query(student_infor).filter(student_infor.id == int(id_get))
            for i in a:
                a1 = i.english_score
                a2 = i.python_score
                a3 = i.C_score
                a4 = a1+a2+a3
                db.session.query(student_infor).filter(student_infor.id == int(id_get)).update({"score_sum":a4})
                db.session.commit()
            return render_template("alter_stu.html",ok="修改成功")
    return render_template("alter_stu.html")

@app.route("/sort_stu/",methods=['POST','GET'],endpoint="sort_stu")
def stu_infor_sort():
    if request.method.lower() == "post":
        get_cond = request.form.get("condation")
        get_cont = request.form.get("condation1")
        b = student_infor.query.order_by(student_infor.english_score).all()
        for i in b:
            print(i.python_score)
        if get_cond == "english分数":
            if get_cont == "升序":
                a = student_infor.query.order_by(student_infor.english_score).all()
                # a = db.session.query(student_infor).order_by(student_infor.english_score).all()
                return render_template("sort_stu.html",stu_list1=a)
            if get_cont == "降序":
                a = student_infor.query.order_by(student_infor.english_score.desc()).all()
                # a = db.session.query(student_infor).order_by(student_infor.english_score.desc()).all()
                return render_template("sort_stu.html",stu_list1=a)
        if get_cond == "python分数":
            if get_cont == "升序":
                a = db.session.query(student_infor).order_by(student_infor.python_score).all()
                return render_template("sort_stu.html",stu_list1=a)
            if get_cont == "降序":
                a = db.session.query(student_infor).order_by(student_infor.python_score.desc()).all()
                return render_template("sort_stu.html",stu_list1=a)
        if get_cond == "C语言分数":
            if get_cont == "升序":
                a = db.session.query(student_infor).order_by(student_infor.C_score).all()
                return render_template("sort_stu.html",stu_list1=a)
            if get_cont == "降序":
                a = db.session.query(student_infor).order_by(student_infor.C_score.desc()).all()
                return render_template("sort_stu.html",stu_list1=a)
        if get_cond == "总分":
            if get_cont == "升序":
                a = db.session.query(student_infor).order_by(student_infor.score_sum).all()
                return render_template("sort_stu.html",stu_list1=a)
            if get_cont == "降序":
                a = db.session.query(student_infor).order_by(student_infor.score_sum.desc()).all()
                return render_template("sort_stu.html",stu_list1=a)
    return render_template("sort_stu.html")
@app.route("/show_stu/",methods=['POST','GET'],endpoint="show_stu")
def show_all_stu():
    a = db.session.query(student_infor).all()
    return render_template("show_stu.html",stu_list1=a)
if __name__ == "__main__":
    API_HOST = "127.1.1.1"
    API_PORT = 5555
    app.run(API_HOST,API_PORT,debug=True)