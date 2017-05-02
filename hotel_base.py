import pymysql



def hotel_database(db):
    cursor = db.cursor()    
    sql = """SELECT *
             FROM HOTEL"""

    cursor.execute(sql)
    results=cursor.fetchall()
    return results

def room_database(db):
    cursor = db.cursor()    
    sql = """
          """

    cursor.execute(sql)
    results=cursor.fetchall()
    return results
    
    
    



