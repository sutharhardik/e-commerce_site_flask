from wtforms import *

class ProductVO:
    productId=IntegerField
    productName=StringField
    productPrize=StringField
    productDescription=StringField
    productQuantity=StringField
    datasetname = StringField
    productImageName=StringField
    productActiveStatus=StringField
    product_categoryId=IntegerField
    product_subcategoryId=IntegerField
    product_registerId=IntegerField
    productpath=StringField