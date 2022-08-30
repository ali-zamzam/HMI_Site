import json
import random

class user():

    def __init__(self):
        self.pseudo=""
        self.password=""
        self.id=0
        self.theme=""
        self.surface = ""
        self.habitants = ""
        self.commerce = ""
        self.voyageurs = ""
        self.arrets = ""

    def savejson(self,list):
        f = open("data-json/users.json","r")
        d = json.load(f)
        f.close()
        d[list['pseudo']]=list
        f = open("data-json/users.json", "w")
        json.dump(d,f)
        f.close()
        return "Un nouvel compte est crée avec succès"

    def uservalidation(self,user,pas):
        f = open("data-json/users.json", "r")
        d = json.load(f)
        f.close()
        if user in d.keys():
            if d[user]["password"] == pas:
                return (True,d[user]["key"])
            else:
                return (False,False)
        else:
            return (False,False)




    def zonejson(self, list):
        f = open("data-json/zone.json", "r")
        d = json.load(f)
        f.close()
        d[list['surface']] = list
        f = open("data-json/zone.json", "w")
        json.dump(d, f)
        f.close()
        return "Les paramètres sont sauvgardés avec succès"

