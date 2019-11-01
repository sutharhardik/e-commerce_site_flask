from wtforms import *

class FeedbackVO:
    feedbackId = IntegerField
    feedbackSubject = StringField
    feedbackDescription = StringField
    feedbackRating = StringField
    feedbackDate = StringField
    feedbackTime = StringField
    feedbackActiveStatus = StringField
    #feedback_loginId = IntegerField
    feedbackFrom_loginId = IntegerField