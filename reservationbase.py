import pymysql

def reservationdata(db):
    cursor = db.cursor()    
    sql = """
          """

    cursor.execute(sql)
    results=cursor.fetchall()    
    return results

def update_database(*arg):
    cursor = db.cursor()
    sql = """
          """

    cursor.execute(sql)
    try:
       # Execute the SQL command
       cursor.execute(sql)
       # Commit your changes in the database
       db.commit()
    except:
       # Rollback in case there is any error
       db.rollback()
