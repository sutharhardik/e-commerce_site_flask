from project.com.dao import con_db


class UserregisterDAO:

    def userinsertRegister(self, registerVO):
        connection = con_db()
        cursor1 = connection.cursor()

        cursor1.execute("INSERT INTO userregistermaster(userregisterName,userregisterAddress,userregisterGender,userregisterArea,userregisterCity,userregisterPincode,userregisterMobileno,userregisterEmail,userregisterActivestatus,userregister_loginId) VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(registerVO.userregisterName, registerVO.userregisterAddress, registerVO.userregisterGender, registerVO.userregisterArea,registerVO.userregisterCity, registerVO.userregisterPincode, registerVO.userregisterMobileno,registerVO.userregisterEmail, registerVO.userregisterActivestatus, str(registerVO.userregister_loginId)))


        connection.commit()

        registerDict = cursor1.fetchall()


        cursor1.close()

        connection.close()

        return registerDict


    def viewbuyer(self):


        connection = con_db()

        cursor1 = connection.cursor()

        cursor1.execute("SELECT * FROM userregistermaster")

        data1 = cursor1.fetchall()

        connection.commit()

        connection.close()

        return data1

    def deletebuyer(self,loginVO):
        connection = con_db()
        cursor1 = connection.cursor()

        #cursor1.execute("UPDATE  userregistermaster SET userregisterActivestatus='deactive' WHERE  userregisterId='" + registerVO.userregisterId + "' ")
        cursor1.execute("UPDATE  loginmaster SET loginActivestatus='deactive' WHERE  loginId='" + loginVO.loginId + "'")
        connection.commit()
        connection.close()
        cursor1.close()