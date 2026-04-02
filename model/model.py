from pickle import TRUE

from database.DAO import DAO


class Model:
    def __init__(self):
        pass

    def getCodIns(self):
        return DAO.getcodIns()

    def getAllCorsi(self):
        return DAO.getAllCorsi()

    def getCorsiPD(self,pd):
        return DAO.getCorsiPD(pd)

    def getCorsiPDwIscritti(self,pd):
        result = DAO.getCorsiPDwIscritti(pd)
        result.sort(key = lambda s : s[1], reverse = True) #primo elemento di s è corso il secondo è il numero di iscitti
        return result

    def getStudentiCorso(self, codins):
        studenti = DAO.getStudentiCorso(codins)
        studenti.sort(key = lambda s : s.cognome)
        return studenti

    def getCDSofCorso(self, codins):
        cds = DAO.getCDSofCorso(codins)
        cds.sort(key = lambda c : c[1], reverse = True)
        return cds