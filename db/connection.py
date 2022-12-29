import pymysql

def connection():
    # Connect to the database
    conn = pymysql.connect(host='localhost',
                           user='root',
                           password='',
                           db='userdb',
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)
    return conn.cursor()
