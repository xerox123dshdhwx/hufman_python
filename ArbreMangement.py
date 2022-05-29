import ArbreBinaire as abr
def createTree(my_list):
    nodeList = []
    for k in range(len(my_list)):
        node = abr.ArbreBinaire(my_list[k])
        nodeList.append(node)

    for k in range(len(nodeList)):
        print(nodeList[k].valeur, end=" ")

    while len(nodeList) != 1:
        node1 = nodeList[0]
        node2 = nodeList[1]
        new_node = abr.ArbreBinaire(('', node2.valeur[1] + node1.valeur[1]))
        new_node.insert_gauche(node1)
        new_node.insert_droit(node2)
        # nodeList.append(new_node)
        x = True
        for k in range(len(nodeList)):
            if (new_node.valeur[1] <= nodeList[k].valeur[1]):
                nodeList.insert(k, new_node)
                x = False
                break
        if (x):
            nodeList.append(new_node)
        nodeList.remove(node1)
        nodeList.remove(node2)
    return nodeList

def affichageJson(T: abr.ArbreBinaire):
    """
    Permet l'affichage d'un arbre binaire sous format JSON
    :param T:
    :return: void
    """
    if (T != None):
        print("{\"label\" : \"" + T.get_valeur()[0] + "\", \"frequence\" : " + str(T.get_valeur()[1]) + ", \"left\":")
        affichageJson(T.get_gauche())
        print(", \"right\":");
        affichageJson(T.get_droit())
        print("}")
    else:
        print("null")


global_list = []
dict = {}

def get_codage(T: abr.ArbreBinaire, constructor=""):
    """
    Fonction qui parcours l'arbre binaire et cree une chaine de caractére de bit pour chaque feuille atteint aisin que sont caractére associer la feuille
    et renvoie un dictionnaire d'association caractére -> chaine binaire ainsi qu'une liste de tout les codage binaire
    :param T:
    :param constructor:
    :return: global_list dict
    """
    if T.get_droit() == None and T.get_gauche() == None:
        print(T.get_valeur()[0], " : ", constructor)
        l = []
        dict.update({T.get_valeur()[0]: constructor})
        l.append(constructor)
        global_list.append(l)
    else:
        c = constructor + "0"
        get_codage(T.get_gauche(), c)
        c = constructor + "1"
        get_codage(T.get_droit(), c)
    return (dict,global_list)

