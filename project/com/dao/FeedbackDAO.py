from project.com.dao import con_db

class FeedbackDAO:
    def insertFeedback(self,feedbackVO):
        connection=con_db()
        cursor1=connection.cursor()

        cursor1.execute("INSERT INTO feedbackmaster (feedbackSubject,feedbackDescription,feedbackRating,feedbackDate,feedbackTime,feedbackActiveStatus, feedbackFrom_loginId)VALUES ('"+feedbackVO.feedbackSubject+"','"+feedbackVO.feedbackDescription+"','"+feedbackVO.feedbackRating+"','"+feedbackVO.feedbackDate+"','"+feedbackVO.feedbackTime+"','"+feedbackVO.feedbackActivestatus+"','"+str(feedbackVO.feedbackFrom_loginId)+"')")
        connection.commit()
        cursor1.close()
        connection.close()

    def searchFeedback(self, feedbackVO):
        connection = con_db ()
        cursor1 = connection.cursor ()

        cursor1.execute (
            "SELECT * FROM feedbackmaster JOIN loginmaster ON feedbackmaster.feedbackFrom_loginId=loginmaster.loginId WHERE feedbackActiveStatus='active' ")
        data = cursor1.fetchall ()
        connection.commit ()
        cursor1.close ()
        connection.close ()
        return data