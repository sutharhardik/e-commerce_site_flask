import os

from project import app

from flask import render_template, session, request, redirect , url_for,flash

from werkzeug.utils import secure_filename

from project.com.dao.ComplainDAO import ComplainDAO

from project.com.vo.ComplainVO import ComplainVO

from datetime import datetime


@app.route('/loadcomplain')
def loadcomplain():

    if session['loginDictrole'] == 'seller':
        return render_template('seller/complain.html')

    else:
        return render_template("admin/login.html")


@app.route('/insertcomplain', methods=['POST'])
def insertcomplain():

    if session['loginDictrole'] =='seller':

        # app.config['UPLOAD_FILE'] = 'C:/Users/RetailAdmin/PycharmProjects/hardik/project/static/adminResources/complaindataset/'
        #
        # file = request.files['complainImageName']

        complainDAO = ComplainDAO()

        complainVO = ComplainVO()

        complainVO.complainSubject = request.form['complainSubject']

        complainVO.complainDescription = request.form['complainDescription']

        complainVO.complainImageName = request.form['complainImageName']

        complainVO.complainFrom_loginId = str(session['loginDictId'])

        complainVO.complainDate = str(datetime.today().strftime("%d-%m-%y"))

        complainVO.complainTime =str(datetime.today().hour) + ":" + str(datetime.now().minute)

        complainVO.complainStatus = 'Pending'

        complainVO.complainActiveStatus = 'Activate'


        # filename = secure_filename(file.filename)
        # file.save(app.config['UPLOAD_FILE'] + filename)
        #
        # filepath = os.path.join(app.config['UPLOAD_FILE'])
        #
        # complainVO.complainPath = filepath
        # complainVO.complainImageName = filename

        complainDAO.insertcomplain(complainVO)


        return render_template("seller/complain.html")

    else:

        return render_template("admin/login.html")


@app.route("/viewcomplain", methods=['GET'])
def viewcomplain():


        complainDAO = ComplainDAO()

        complainVO = ComplainVO()

        complainVO.complainId = request.args.get('complainId')

        complainDict = complainDAO.searchcomplain(complainVO)

        try:
            if session['loginDictrole'] == 'admin':
                return render_template('admin/viewcomplain.html', complainDict=complainDict)
            elif session['loginDictrole'] == 'seller':
                return render_template('seller/viewcomplain.html', complainDict=complainDict)
        except:
            flash('Plese Login First !', 'danger')
            return redirect(url_for('Login'))



@app.route("/loadReplyComplain", methods=["GET"])
def loadReplyComplain():

    if session['loginDictrole'] == 'admin':

        complainDAO = ComplainDAO()

        complainVO  = ComplainVO()

        complainVO.complainId = str(request.args.get('complainId'))

        complainDict = complainDAO.searchreplycomplain(complainVO)

        return render_template("admin/reply.html", complainDict1 = complainDict)

@app.route("/insertReplycomplain", methods=["POST"])
def insertReplycomplain():

    if session['loginDictrole'] == "admin":

        complainDAO = ComplainDAO()

        complainVO = ComplainVO()

        complainVO.complainId = request.form['complainId']

        complainVO.complainReply = request.form['complainReply'].replace("'", "")

        complainVO.complainStatus = 'replyed'

        complainVO.complainTo_loginId = str(session['loginDictId'])

        complainDAO.insertreplycomplain(complainVO)

        return redirect(url_for("viewcomplain"))


@app.route("/deletecomplain" ,methods=['POST'])
def deleteComplain():

    if session['loginDictrole'] == "seller":

        complainDAO = ComplainDAO()

        complainVO = ComplainVO()

        complainVO.complainId=request.form['complainId']

        complainDAO.deleteComplain(complainVO)

        return redirect('/viewcomplain')
