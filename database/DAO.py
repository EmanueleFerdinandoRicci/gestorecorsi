from database.DB_connect import DBConnect
from model.corso import Corso


class DAO():

    @staticmethod
    def getcodIns():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query= "select codIns from corso"
        cursor.execute(query)

        res=[]
        for row in cursor:
            res.append(row["codIns"])

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getAllCorsi():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = "select * from corso"
        cursor.execute(query)

        res = []
        for row in cursor:
            res.append(Corso(
                codins = row["codins"],
                crediti = row["crediti"],
                nome = row["nome"],
                pd = row["pd"]
            ))

        cursor.close()
        cnx.close()
        return res

