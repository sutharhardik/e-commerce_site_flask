from project.com.dao import con_db

class ProductDAO:
    def insertProduct(self, productVO):

        connection = con_db()
        cursor1 = connection.cursor()
        cursor1.execute("INSERT INTO productmaster (productName,productPrize,productDescription,productQuantity,productActiveStatus,product_categoryId,product_subcategoryId,product_registerId,productImageName,productpath) VALUES ('"+productVO.productName+"','"+productVO.productPrize+"','"+productVO.productDescription+"','"+productVO.productQuantity+"','"+productVO.productActiveStatus+"','"+productVO.product_categoryId+"','"+productVO.product_subcategoryId+"','"+str(productVO.product_registerId)+"','"+productVO.productImageName+"','"+productVO.productpath+"')")

        connection.commit()
        cursor1.close()
        connection.close()

    def search_Product(self):
        connection = con_db()
        cursor1 = connection.cursor()
        #cursor2 = connection.cursor()

        cursor1.execute("SELECT * FROM productmaster")
        #cursor2.execute("SELECT * FROM productmaster")

        #cursor1.execute ("SELECT * FROM productmaster AS p INNER JOIN categorymaster AS c  ON p.`product_categoryId` = c.`categoryId`")

        #cursor1.execute("SELECT product_subcategoryId FROM productmaster INNER JOIN subcategorymaster ON productmaster.product_subcategoryId = subcategorymaster.subcategoryId")
        cursor1.execute ("SELECT * FROM  subcategorymaster  INNER JOIN productmaster ON product_subcategoryId = subcategoryId INNER JOIN categorymaster ON categoryId=subcategory_categoryId")
        #cursor1.execute("SELECT * FROM productmaster INNER JOIN subcategorymaster ON productmaster.'product_subcategoryId' = subcatrgorymaster.'subcategoryId'")

        data1 = cursor1.fetchall()
        #data = cursor2.fetchall()
        print(data1)
        #print(data)

        connection.commit()
        connection.close()
        cursor1.close()
        #cursor2.close()
        return data1
        #return data


    def deleteProduct(self, productVO):
        connection = con_db()
        cursor1 = connection.cursor()

        cursor1.execute("UPDATE  productmaster SET productActiveStatus='deactive' WHERE  productId='" + productVO.productId + "'")

        connection.commit()
        connection.close()
        cursor1.close()

    # def ajaxSubcategoryProduct(self,subcategoryVO):
    #     connection = con_db()
    #     cursor1 =connection.cursor()
    #
    #     cursor1.execute("SELECT * FROM categorymaster WHERE categoryId='"+subcategoryVO.product_categoryId+"' ")
    #
    #     connection.commit()
    #     connection.close()
    #     cursor1.close()
    #
