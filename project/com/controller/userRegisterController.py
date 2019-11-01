import smtplib

import string

from email.mime.multipart import MIMEMultipart

from email.mime.text import MIMEText

from random import choice

from project import app

from flask import render_template, request, session, flash, redirect, url_for

from project.com.dao.LoginDAO import LoginDAO

from project.com.dao.UserregisterDAO import UserregisterDAO

from project.com.vo.LoginVO import LoginVO


from project.com.vo.UserregisterVO import UserregisterVO

@app.route("/loaduserregister")

def userregister():

    return render_template("user/userregister.html")


@app.route('/userinsertregister', methods=['POST'])

def userinsertRegister():
    registerVO = UserregisterVO()
    registerDAO = UserregisterDAO()
    loginVO = LoginVO()
    loginDAO = LoginDAO()

    alphabet = string.ascii_letters + string.digits
    password = ''.join(choice(alphabet) for i in range(8))

    registerVO.userregisterName = request.form['userregisterName']

    registerVO.userregisterAddress = request.form['userregisterAddress']

    registerVO.userregisterGender = request.form['userregisterGender']

    registerVO.userregisterArea = request.form['userregisterArea']

    registerVO.userregisterCity = request.form['userregisterCity']

    registerVO.userregisterPincode = request.form['userregisterPincode']

    registerVO.userregisterMobileno = request.form['userregisterMobileno']

    registerVO.userregisterEmail = request.form['userregisterEmail']

    registerVO.userregisterActivestatus = 'active'

    print ("Hello i am user")

    loginVO.loginEmail = request.form['userregisterEmail']
    loginVO.loginPassword = password
    loginVO.loginRole = 'user'
    loginVO.loginActivestatus='active'

    print('EMAIL',loginVO.loginEmail)
    print("password",loginVO.loginPassword)
    print("role",loginVO.loginRole)
    print("status",loginVO.loginActivestatus)

    loginDict = loginDAO.loadlogin(loginVO)

    print(loginDict)

    fromaddr = "ecommercepython@gmail.com"    #email

    msg = MIMEMultipart()

    msg['From'] = fromaddr

    msg['To'] = loginVO.loginEmail

    msg['Subject'] = "PASSWORD FOR YOUR LOGIN"

    msg.attach(MIMEText(loginVO.loginPassword, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)

    server.starttls()

    passw = "hardik@4693"           #password
    server.login(fromaddr, passw)

    text = msg.as_string()

    server.sendmail(fromaddr, loginVO.loginEmail, text)

    server.quit()

    loginDict = loginDAO.searchloginId()
    print(loginDict)

    registerVO.userregister_loginId = str(loginDict)

    registerDAO.userinsertRegister(registerVO)

    return render_template('admin/login.html')



@app.route("/viewbuyer")


def viewbuyer():

    registerDAO = UserregisterDAO()

    data1 = registerDAO.viewbuyer()

    try:
        if session['loginDictrole'] == 'admin':
            return render_template('admin/viewbuyer.html',data2=data1)

    except:
            flash('Plese Login First !', 'danger')
            return redirect(url_for('Login'))


@app.route("/deletebuyer" ,methods=['POST'])
def deletebuyer():

    if session['loginDictrole'] == "admin":

        registerDAO = UserregisterDAO()
        loginVO = LoginVO()


        #registerVO.userregisterId=request.form['userregisterId']
        loginVO.loginId=request.form['loginId']

        registerDAO.deletebuyer(loginVO)


        return redirect("/viewbuyer")

