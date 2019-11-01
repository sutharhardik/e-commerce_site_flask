from project.com.dao import con_db

class CategoryDAO:
    def insertCategory(self,categoryVO):
        connection=con_db()
        cursor1=connection.cursor()
        cursor1.execute("INSERT INTO categorymaster (categoryName,categoryDescription,categoryActiveStatus) VALUES ('"+categoryVO.categoryName+"','"+categoryVO.categoryDescription+"','"+categoryVO.categoryActiveStatus+"')")
        connection.commit()
        cursor1.close()
        connection.close()

    def searchCategory(self):
        connection = con_db()
        cursor1 = connection.cursor()

        cursor1.execute("SELECT * FROM categorymaster WHERE categoryActiveStatus='active'")
        data = cursor1.fetchall()

        connection.commit()
        connection.close()
        cursor1.close()
        return data

    def searchCategoryId(self,categoryVO):
        connection = con_db()
        cursor1 = connection.cursor()

        cursor1.execute("SELECT * FROM categorymaster WHERE categoryName LIKE '"+categoryVO.categoryName+"%'")
        data = cursor1.fetchall()

        connection.commit()
        connection.close()
        cursor1.close()
        return data

    def deleteCategory(self, categoryVO):
        connection = con_db()
        cursor1 = connection.cursor()

        cursor1.execute("UPDATE  categorymaster SET   WHERE  categoryId='" + categoryVO.categoryId + "'")

        connection.commit()
        connection.close()
        cursor1.close()

