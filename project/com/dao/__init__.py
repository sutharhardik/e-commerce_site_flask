import pymysql

def con_db():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='root',
        db='project',
        cursorclass = pymysql.cursors.DictCursor
    )
