from flask import render_template, redirect, request, session, url_for
from project import app
from project.com.dao.FeedbackDAO import FeedbackDAO
from project.com.vo.FeedbackVO import FeedbackVO
from project.com.dao.LoginDAO import LoginDAO
from  project.com.vo.LoginVO import LoginVO
import time

@app.route("/loadfeedback")
def loadFeddback():
    try:
        if session['loginDictrole'] == 'admin':
            return render_template('admin/addfeedback.html')
        elif session['loginDictrole'] == 'seller':
            return render_template('seller/addfeedback.html')

    except:
            flash=('Plese Login First !', 'danger')
            return redirect(url_for('Login'))

@app.route("/insertfeedback" , methods=["POST"])
def insertfeedback():
    if session['loginDictrole']=='seller':


        feedbackDAO=FeedbackDAO()
        feedbackVO=FeedbackVO()

        feedbackVO.feedbackSubject=str(request.form["feedbackSubject"])

        feedbackVO.feedbackDescription = str(request.form["feedbackDescription"])


        feedbackVO.feedbackRating = str(request.form["feedbackRating"])

        datetime = time.ctime ().split (" ")
        feedbackVO.feedbackTime = datetime[-2]
        feedbackVO.feedbackDate = " ".join([datetime[1], datetime[2], datetime[4]])

        feedbackVO.feedbackActivestatus = "active"

        feedbackVO.feedbackFrom_loginId = str(session['loginDictId'])

        #feedbackVO.feedback_loginId = str(session['loginDictId'])
        #print feedbackVO.feedback_loginId

        feedbackDAO.insertFeedback(feedbackVO)

        return "vffd"

@app.route('/viewfeedback')
def viewFeedback():
    if session['loginDictrole'] == 'admin':
        feedbackDAO = FeedbackDAO()
        feedbackVO = FeedbackVO()

        feedbackVO.feedbackActiveStatus = 'activate'
        feedbackDict = feedbackDAO.searchFeedback(feedbackVO)

        return render_template('admin/viewfeedback.html', data2=feedbackDict)
    return render_template('admin/signin.html')

@app.route('/deleteFeedback')
def deleteFeedback():
    if session['loginDictrole'] == 'seller':
        feedbackDAO = FeedbackDAO()
        feedbackVO = FeedbackVO()

        feedbackVO.feedbackActiveStatus = 'deactivate'

        feedbackVO.feedbackId = request.args.get('feedbackId')

        feedbackDAO.deleteFeedback(feedbackVO)

        return redirect('/viewuserFeedback')
    else:
        return render_template('admin/login.html', loginerrorDict='Please login first')