from project.com.dao import  *

class ComplainDAO:

    def insertcomplain(self, complainVO):

        connection = con_db()

        cursour1 = connection.cursor()

        cursour1.execute("INSERT INTO complainmaster (complainSubject, complainDescription , complainImageName, complainDate, complainTime, complainStatus ,complainActiveStatus, complainFrom_loginId )VALUES ('"+complainVO.complainSubject+"','"+complainVO.complainDescription+"', '"+ complainVO.complainImageName+"','"+complainVO.complainDate+"','"+complainVO.complainTime+"','"+complainVO.complainStatus+"', '"+complainVO.complainActiveStatus+"','"+str(complainVO.complainFrom_loginId)+"')")


        connection.commit()

        cursour1.close()

        connection.close()

    def searchcomplain(self, complainVO):

        connection  = con_db()

        cursour1 = connection.cursor()

        cursour1.execute("SELECT * FROM complainmaster INNER JOIN loginmaster ON complainmaster.complainFrom_loginId = loginmaster.loginId WHERE complainStatus = 'pending'")

        complainDict = cursour1.fetchall()

        cursour1.close()

        connection.close()

        return complainDict

    def searchreplycomplain(self,complainVO):

        connection = con_db()

        cursour1 = connection.cursor()

        cursour1.execute("SELECT * FROM complainmaster WHERE complainId = '"+complainVO.complainId+"'")

        complainDict1 = cursour1.fetchall()
        print(complainDict1)

        connection.commit()

        cursour1.close()

        connection.close()

        return complainDict1

    def insertreplycomplain(self, complainVO):

        connection = con_db()

        cursour1 = connection.cursor()

        cursour1.execute("UPDATE complainmaster SET complainReply='"+complainVO.complainReply+"',complainStatus ='"+complainVO.complainStatus+"',complainTo_loginId= '"+complainVO.complainTo_loginId+"' WHERE complainId = '"+complainVO.complainId+"'")

        complainDict = cursour1.fetchall()

        cursour1.close()

        connection.commit()

        connection.close()

        return complainDict


    def deleteComplain(self, complainVO):
        connection = con_db()
        cursor1 = connection.cursor()

        cursor1.execute("UPDATE  complainmaster SET complainActiveStatus='deactive' WHERE  complainId='" + str(complainVO.complainId) + "'")

        connection.commit()
        connection.close()
        cursor1.close()

