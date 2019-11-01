from project.com.dao import *

class LoginDAO:

    def loadlogin(self,loginVO):
        connection = con_db()

        cursor1 = connection.cursor()

        cursor1.execute("INSERT INTO loginmaster(loginEmail,loginPassword,loginRole,loginActivestatus) VALUES('{}','{}','{}','{}')".format(loginVO.loginEmail,loginVO.loginPassword,loginVO.loginRole,loginVO.loginActivestatus))

        connection.commit()

        cursor1.close()

        connection.close()

    def searchloginId(self):

        connection = con_db()

        cursor1 = connection.cursor()

        cursor1.execute("SELECT MAX(loginId) FROM loginmaster")

        loginDict = cursor1.fetchall()

        loginDict = loginDict[0]

        loginDict = loginDict['MAX(loginId)']

        cursor1.close()

        connection.close()

        return loginDict


    def searchEmaillogin(self,loginVO):

        connection = con_db()

        cursor1 = connection.cursor()

        cursor1.execute("SELECT * FROM loginmaster WHERE loginEmail = '"+loginVO.loginEmail+"' AND loginActivestatus='active'")

        connection.commit()

        loginDict = cursor1.fetchall()

        cursor1.close()

        connection.close()

        return loginDict

    def viewseller(self):

        connection = con_db()

        cursor1 = connection.cursor()

        cursor1.execute("SELECT * FROM sellerregistermaster")

        data1 = cursor1.fetchall()

        connection.commit()

        connection.close()

        cursor1.close()

        return data1



    def viewalldata(self):

        connection = con_db()

        cursor1 = connection.cursor()

        cursor1.execute("SELECT * FROM loginmaster")

        data1 = cursor1.fetchall()

        connection.commit()

        connection.close()

        cursor1.close()

        return data1

    def deletedatabyadmin(self,loginVO):

        connection = con_db()
        cursor1 = connection.cursor()

        cursor1.execute("UPDATE  loginmaster SET loginActivestatus='deactive' WHERE  loginId='" + loginVO.loginId + "'")

        connection.commit()
        cursor1.close()
        connection.close()
