import sqlite3

try:
    conn = sqlite3.connect("MyDB.db")
    cursor = conn.cursor()
    #cursor.execute("Create table employee (id number, name text,"
    #               "job text, department text)")
    #cursor.execute('insert into employee values'
    #               '(1, "Python", "Development", "R&D")')
    #conn.commit()
    var = 1
    cursor.execute("select * from employee where id = %s" % var)
    varList = cursor.fetchall()
    if len(varList) != 0:
        for row in varList:
            for value in row:
                print(value)
    cursor.close()
    conn.close()
except Exception as e:
    print(e.__str__())

#Lunch break, meet at 1.40 PM