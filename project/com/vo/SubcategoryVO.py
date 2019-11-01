from wtforms import *

class SubcategoryVO:
    subcategoryId=IntegerField
    subcategoryName=StringField
    subcategoryDescription=StringField
    subcategoryActiveStatus=StringField
    subcategory_categoryId=IntegerField