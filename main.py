import ArbreMangement as am
import fileManager
import listManagement

def q1(fileName):
    dictList = fileManager.read_file(fileName)
    var = {k: v for k, v in sorted(dictList.items(), key=lambda item: item[1])}
    my_list = list(var.items())
    q2(listManagement.sortascci(my_list))

def q2(my_list):
    nodeList = am.createTree(my_list)

    dict, list = am.get_codage(nodeList[0])
    am.affichageJson(nodeList[0])
    #am.get_codage(nodeList[0])
    text_to_bin = fileManager.getTextToBin(filePath, dict)
    fileManager.writteFileBin(text_to_bin)
    fileManager.tauxCompression(filePath)
    fileManager.moyenneBit(my_list,list)

if __name__ == '__main__':
    filePath = "FileToCompress/textesimple.txt"
    print(q1(filePath))
