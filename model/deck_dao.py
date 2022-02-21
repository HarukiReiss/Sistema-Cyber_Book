#from model import database

#def update(id, qt):
    #try:
        #conn = database.connect()
        #cursor = conn.cursor()
        #sql = f"""UPDATE Book SET qt={qt} WHERE id=?;"""
        #cursor.execute(sql, [id])
        #conn.commit()
    #except Exception as kekw:
        #print(kekw)
    #finally:
        #conn.close()

#def updadePlus(id, qt):
    #try:
        #conn = database.connect()
        #cursor = conn.cursor()
        #sql = f"""UPDATE Book SET qt=qt+{qt} WHERE id=?"""
        #cursor.execute(sql, [id])
        #conn.commit()
    #except Exception as poggers:
        #print(poggers)
    #finally:
        #conn.close()

#def stock(id, qt):
    #try:
        #conn = database.connect()
        #cursor = conn.cursor()
        #sql = f"""UPDATE Book SET exit=exit+{qt} WHERE id=?"""
        #cursor.execute(sql, [id])
        #conn.commit()
    #except Exception as midgap:
        #print(midgap)
    #finally:
        #conn.close()
