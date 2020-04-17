import logging, sqlite3
from datetime import datetime

try:
    logging.basicConfig(filename="databaseDebug.log", filemode='w', level=logging.DEBUG)
    logging.info("getting database connection")
    conn = sqlite3.connect("MyDB.db")
    cursor = conn.cursor()
    cursor.execute("select * from employee where id = 2235")
    varList = cursor.fetchall()
    if len(varList) != 0:
        logging.info("data is retrieved")
        for row in varList:
            print(row)
    else:
        logging.debug("No records found %s" % datetime.now().strftime("%D %M - %H:%M:%S"))

    cursor.close()
    conn.close()
except Exception as e:
    logging.error("Some exception in the database operation")
    print(e.__str__())