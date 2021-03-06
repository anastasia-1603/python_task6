class FDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def getEvents(self, day, month, year):
        sql = f"SELECT * FROM events WHERE day={day} AND month={month} AND year={year}"
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res:
                return res
        except:
            print("Error read from database")
        return []

    def addEvent(self, day, month, year, event):
        sql = f"insert into events (event, day, month, year, time) values " \
              f"('{event}', '{day}', '{month}', '{year}','20:00')"
        try:
            self.__cur.execute(sql)
            self.__db.commit()
        except:
            print("Error write to database")
