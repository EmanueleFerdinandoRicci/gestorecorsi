from database.DB_connect import DBConnect
from model.corso import Corso
from model.studente import Studente


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

    @staticmethod
    def getCorsiPD(pd):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """select *
                    from corso c
                    where c.pd = %s"""

        cursor.execute(query, (pd,))

        res = []
        for row in cursor:
            res.append(Corso(**row))  #se il nome delle colonne del databse è uguale agli attributi

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getCorsiPDwIscritti(pd):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """select c.codins , c.crediti ,c.nome ,c.pd , count(*) as n
                    from corso c, iscrizione i
                    where c.codins = i.codins 
                    and c.pd = %s
                    group by c.codins , c.crediti ,c.nome ,c.pd"""

        cursor.execute(query, (pd,))

        res = []
        for row in cursor:
            res.append((Corso(
                codins = row["codins"],
                crediti = row["crediti"],
                nome = row["nome"],
                pd = row["pd"]),
                row["n"]))
        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getStudentiCorso(codins):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """select s.*, i.codins 
                    from studente s, iscrizione i
                    where s.matricola = i.matricola 
                    and i.codins = %s"""

        cursor.execute(query, (codins,))

        res = []
        for row in cursor:
            res.append(Studente(matricola=row["matricola"],
                cognome=row["cognome"],
                nome=row["nome"],
                CDS=row["CDS"]))
        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getCDSofCorso(codins):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """select s.CDS, count(*) as n
                    from studente s, iscrizione i
                    where s.matricola = i.matricola 
                    and i.codins = %s
                    and s.CDS != ""
                    group by s.CDS"""

        cursor.execute(query, (codins,))

        res = []
        for row in cursor:
            res.append((row["CDS"], row["n"]))
        cursor.close()
        cnx.close()
        return res

