from tkinter import *
import pymysql


def input_checkin():
    input_checkin = Tk()
    bottomframe = Frame(input_checkin)
    bottomframe.pack( side = BOTTOM )
    
    L1 = Label(input_checkin, text = "Enter CID")
    L1.pack( side = LEFT)
    E1 = Entry(input_checkin, bd = 5)
    E1.pack(side = RIGHT)
    

    enter_button=Button(bottomframe,text='Enter',command=lambda:checkin_details(E1))
    enter_button.pack(side=BOTTOM)

    input_checkin.mainloop()

def checkin_details(entry):
    checkin_details_window=Tk()
    text=Text(checkin_details_window)
    entered_value=entry.get()
    
    result=checkin_results(entered_value)
    if result==():
        text.insert('current linestart','No such CID exists\n')
        text.insert('current linestart','please enter again')
        ok_button=Button(input_checkin,text='OK',command=input_checkin)
    else:
        for row in result:
            line=' '.join([str(i) for i in row])+'\n'
            text.insert(INSERT,line)

    text.pack()

    checkin_details_window.mainloop()
        


def checkin_results(value):
    db = pymysql.connect("localhost","arpan","hiarpanshah","hotel_management")
    cursor = db.cursor()    
    sql = """
          """

    cursor.execute(sql)
    results=cursor.fetchall()
    
    return results

    
    
    
    
    
