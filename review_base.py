import pymysql

def room_reviews(db):
    cursor = db.cursor()    
    sql = """
          """

    cursor.execute(sql)
    results=cursor.fetchall()    
    return results

def service_reviews(db):
    cursor = db.cursor()    
    sql = """
          """

    cursor.execute(sql)
    results=cursor.fetchall()    
    return results

def breakfast_reviews(db):
    cursor = db.cursor()    
    sql = """
          """

    cursor.execute(sql)
    results=cursor.fetchall()
    return results

def update_database(db,E1,E2,E3,E4):
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

    
    
