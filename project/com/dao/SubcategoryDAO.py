from project.com.dao import con_db

class SubcategoryDAO:
    def insertSubcategory(self,subcategoryVO):
        connection=con_db()
        cursor1=connection.cursor()
        cursor1.execute("INSERT INTO subcategorymaster (subcategoryName,subcategoryDescription,subcategoryActiveStatus,subcategory_categoryId) VALUES ('"+subcategoryVO.subcategoryName+"','"+subcategoryVO.subcategoryDescription+"','"+subcategoryVO.subcategoryActiveStatus+"','"+str(subcategoryVO.subcategory_categoryId)+"')")

        connection.commit()
        print (subcategoryVO.subcategoryName, subcategoryVO.subcategoryDescription,
               subcategoryVO.subcategoryActiveStatus, subcategoryVO.subcategory_categoryId)
        cursor1.close()
        connection.close()

    def searchSubcategory(self):
        connection = con_db()
        cursor1 = connection.cursor()

        cursor1.execute("SELECT * FROM subcategorymaster")
        cursor1.execute("SELECT * FROM subcategorymaster AS s INNER JOIN categorymaster AS c ON s.`subcategory_categoryId` = c.`categoryId`")

        data = cursor1.fetchall()

        connection.commit()
        connection.close()
        cursor1.close()
        return data

    def searchSubcategoryId(self,subcategoryVO):
        connection = con_db()
        cursor1 = connection.cursor()

        cursor1.execute("SELECT * FROM subcategorymaster WHERE subcategoryName LIKE '"+subcategoryVO.subcategoryName+"%'")
        data = cursor1.fetchall()

        connection.commit()
        connection.close()
        cursor1.close()
        return data

    def deleteSubcategory(self, subcategoryVO):
        connection = con_db()
        cursor1 = connection.cursor()

        cursor1.execute("UPDATE  subcategorymaster SET subcategoryActiveStatus='deactive' WHERE  subcategoryId='" + subcategoryVO.subcategoryId + "'")

        connection.commit()
        connection.close()
        cursor1.close()

    def ajaxSubcategoryProduct(self,subcategoryVO):
        connection = con_db()
        cursor1 =connection.cursor()

        cursor1.execute("SELECT * FROM subcategorymaster WHERE subcategory_categoryId='"+str(subcategoryVO.subcategory_categoryId)+"' ")

        subcategoryJsonDict=cursor1.fetchall()
        connection.close()
        cursor1.close()
        return subcategoryJsonDict

    def ajaxLoadheadersubcategory(self,subcategoryVO):


        connection = con_db()

        cursor1 = connection.cursor()

        cursor1.execute("SELECT * FROM subcategorymaster WHERE subcategory_categoryId= '"+str(subcategoryVO.subcategory_categoryId)+"'")

        ajaxheadersubcategoryDict = cursor1.fetchall()

        connection.close()
        cursor1.close()

        return ajaxheadersubcategoryDict



    def forheadersubcategorymen(self):
        connection = con_db()
        cursor1 = connection.cursor()

        cursor1.execute("SELECT * FROM subcategorymaster AS s INNER JOIN categorymaster AS c ON s.`subcategory_categoryId` = c.`categoryId` WHERE s.subcategoryActiveStatus='active' and c.categoryName='men'")

        data = cursor1.fetchall()
        print("data=",data)
        connection.commit()
        connection.close()
        cursor1.close()
        return data

    def forheadersubcategorywomen(self):
        connection = con_db()
        cursor2 = connection.cursor()

        cursor2.execute("SELECT * FROM subcategorymaster AS s INNER JOIN categorymaster AS c ON s.`subcategory_categoryId` = c.`categoryId` WHERE s.subcategoryActiveStatus='active' and c.categoryName='women'")

        data = cursor2.fetchall()
        print("data=",data)
        connection.commit()
        connection.close()
        cursor2.close()
        return data