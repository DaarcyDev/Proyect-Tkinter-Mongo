from tkinter import PROJECTING
from pymongo import MongoClient


def conect():

    client = MongoClient("localhost")
    db = client["Escolar"]
    collections = db["profesores"]
    # print(collections)
    return collections


# for x in conect().find():

#     if('Tesis' in x):
#         print(x['Tesis'])
#     else:
#         print(x['Tesistas']['Tesis'])
# #     print(if(not str(x['Telefonos']).find("casa")==-1): print (x['Telefonos'].pop('casa')))
# #     # if('celular' in x['Telefonos']):print ("si");print("no")
# #     # print(str(x['Telefonos']).find("casa"):str(x['Telefonos']).find('"'))
#     # if (x.find('Tesis')):
#     #     print((x['Tesis']))
#     # else:
#     #     print("")
     
    