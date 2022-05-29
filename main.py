import os.path
from cgitb import text

import ArbreBinaire as abr
import ArbreMangement as am
import fileManager
import listManagement

fileName = "FileToCompress/alice.txt"


def q1():
    dictList = fileManager.read_file(fileName)
    var = {k: v for k, v in sorted(dictList.items(), key=lambda item: item[1])}
    my_list = list(var.items())
    return listManagement.sortascci(my_list)

def q2(my_list):
    nodeList = am.createTree(my_list)
    dict,list = am.get_codage(nodeList[0])
    #am.affichageMaisonMaison(nodeList[0])
    am.get_codage(nodeList[0])
    #print(list)
    #print(dict)
    text_to_bin = fileManager.getTextToBin(fileName,dict)
    fileManager.writteFileBin(text_to_bin)
    fileManager.tauxCompression(fileName)

if __name__ == '__main__':
        #print((q1()))
        print(q2(q1()))