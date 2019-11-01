from flask import *
from flask import render_template, request, session, redirect, url_for, flash

from project import app
from project.com.dao.LoginDAO import LoginDAO
from project.com.dao.SubcategoryDAO import SubcategoryDAO
from project.com.vo.LoginVO import LoginVO
from project.com.vo.SubcategoryVO import SubcategoryVO
from project.com.dao.CategoryDAO import CategoryDAO


@app.route("/", methods=["GET"])
def Login():
    return render_template("user/home.html")

@app.route('/loadlogin')

def loadlogin():

    return render_template('admin/login.html')


@app.route("/checkLogin", methods=["POST"])

def checklogin():

    loginVO = LoginVO()

    loginDAO = LoginDAO()

    loginEmail = request.form["loginEmail"]

    loginPassword = request.form["loginPassword"]

    loginVO.loginEmail = loginEmail

    loginVO.loginPassword = loginPassword

    print(loginVO.loginPassword)

    loginDict = loginDAO.searchEmaillogin(loginVO)

    print(loginDict)

    if len(loginDict) == 0:
        print("34567")
        return render_template("admin/login.html", msg = "Invalid Email")

    elif loginDict[0]['loginPassword'] != loginVO.loginPassword:
        print("123")
        return render_template("admin/login.html", msg="Invalid Password")

    else:

        session['loginDictrole'] = loginDict[0]["loginRole"]
        session['loginDictId'] = loginDict[0]["loginId"]
        session['loginActivestatus'] = 'active'

        return redirect(url_for("index"))


@app.route("/index")
def index():
    try:

        if session["loginDictrole"] == "admin":

            return render_template("admin/index.html")

        elif session["loginDictrole"] == "seller" and session['loginActivestatus']== 'active':

            return render_template("seller/index.html")

        elif session["loginDictrole"] == "user":

            subcategoryDAO = SubcategoryDAO()
            data1 = subcategoryDAO.forheadersubcategorymen()
            data2 = subcategoryDAO.forheadersubcategorywomen()

            return render_template('user/index.html',men= data1,women= data2)

    except Exception:

            return render_template("admin/login.html", msg = "Please Login First")


@app.route("/ajaxLoadheadersubcategory")
def ajaxLoadheadersubcategory():

    subcategoryVO = SubcategoryVO()
    subcategoryDAO = SubcategoryDAO()

    subcategory_categoryId=request.args.get('product_categoryId')
    print(subcategory_categoryId)

    subcategoryVO.subcategory_categoryId = subcategory_categoryId

    ajaxLoadheadersubcategoryDict = subcategoryDAO.ajaxLoadheadersubcategory(subcategoryVO)

    print(ajaxLoadheadersubcategoryDict)

    jsn=json.dumps(ajaxLoadheadersubcategoryDict)

    return jsn




@app.route("/logout")
def logout():

    session.clear()
    return Login()

##########################################################################



@app.route("/viewseller")

def viewseller():

    loginDAO = LoginDAO()

    data1 = loginDAO.viewseller()

    try:
        if session['loginDictrole'] == 'admin':
            return render_template('admin/viewseller.html',data2=data1)

    except:
            flash('Plese Login First !', 'danger')
            return redirect(url_for('Login'))


@app.route("/aboutus")

def aboutus():

    return render_template("user/about-us.html")

@app.route("/contactus")

def contactus():

    return render_template("user/contact-us.html")

@app.route('/viewalldatabyadmin')

def viewalldatabyadmin():

    loginDAO = LoginDAO()

    data = loginDAO.viewalldata()

    try:
        if session['loginDictrole'] == 'admin':
            return render_template('admin/viewdata.html',data2=data)

    except:
            flash('Plese Login First !', 'danger')
            return redirect(url_for('Login'))

@app.route('/deletedata', methods=['POST'])

def deletedata():

    if session['loginDictrole'] == "admin":

        loginDAO = LoginDAO()

        loginVO = LoginVO()

        loginVO.loginId=request.form['loginId']

        loginDAO.deletedatabyadmin(loginVO)

        return redirect("/viewalldatabyadmin")
