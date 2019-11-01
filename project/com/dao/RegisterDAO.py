from project.com.dao import con_db


class RegisterDAO:

    def insertRegister(self, registerVO):
        connection = con_db()
        cursor1 = connection.cursor()

        cursor1.execute("INSERT INTO sellerregistermaster(registerName,registerAddress,registerGender,registerArea,registerCity,registerPincode,registerMobileno,registerEmail,registerActivestatus,register_loginId) VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(registerVO.registerName, registerVO.registerAddress, registerVO.registerGender, registerVO.registerArea,registerVO.registerCity, registerVO.registerPincode, registerVO.registerMobileno,registerVO.registerEmail, registerVO.registerActivestatus, str(registerVO.register_loginId)))


        connection.commit()

        registerDict = cursor1.fetchall()


        cursor1.close()

        connection.close()

        return registerDict

    def deleteseller(self,registerVO):
        connection = con_db()
        cursor1 = connection.cursor()

        cursor1.execute("UPDATE  sellerregistermaster SET registerActivestatus='deactive' WHERE  registerId='" + registerVO.registerId + "'")

        connection.commit()
        cursor1.close()
        connection.close()


