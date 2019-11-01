import smtplib
import string
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from random import choice

from flask import *
from project import app
from flask import render_template, request

from project.com.dao.LoginDAO import LoginDAO
from project.com.dao.RegisterDAO import RegisterDAO
from project.com.vo.LoginVO import LoginVO
from project.com.vo.RegisterVO import RegisterVO


@app.route("/loadregister")
def viewRegister():
    return render_template('admin/register.html')


@app.route('/insertregister', methods=['POST'])
def insertRegister():
    registerVO = RegisterVO()
    registerDAO = RegisterDAO()
    loginVO = LoginVO()
    loginDAO = LoginDAO()

    alphabet = string.ascii_letters + string.digits
    password = ''.join(choice(alphabet) for i in range(8))

    registerVO.registerName = request.form['registerName']
    registerVO.registerAddress = request.form['registerAddress']
    registerVO.registerGender = request.form['registerGender']
    registerVO.registerArea = request.form['registerArea']
    registerVO.registerCity = request.form['registerCity']
    registerVO.registerPincode = request.form['registerPincode']
    registerVO.registerMobileno = request.form['registerMobileno']
    registerVO.registerEmail = request.form['registerEmail']
    registerVO.registerActivestatus = 'active'

    print ("Hello i am Seller")

    loginVO.loginEmail = request.form['registerEmail']
    loginVO.loginPassword = password
    loginVO.loginRole = 'seller'
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

    registerVO.register_loginId = str(loginDict)

    registerDAO.insertRegister(registerVO)

    return render_template('admin/login.html')


@app.route('/')
def loadtheRegister():
    return render_template('admin/login.html')


@app.route("/deleteseller" ,methods=['POST'])
def deleteseller():

    if session['loginDictrole'] == "admin":

        registerDAO = RegisterDAO()

        registerVO = RegisterVO()

        registerVO.registerId=request.form['registerId']

        registerDAO.deleteseller(registerVO)

        return redirect("/viewseller")

