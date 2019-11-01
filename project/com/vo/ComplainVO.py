from wtforms import *

class ComplainVO:

    complainId = IntegerField
    complainSubject = StringField
    complainDescription = StringField
    complainImageName = StringField
    # complainImagepath = StringField
    complainDate = StringField
    complainTime = StringField
    complainStatus = StringField
    complainReply = StringField
    complainActiveStatus = StringField
    complainTo_loginId = IntegerField
    complainFrom_loginId = IntegerField
