def sortascci(my_list):
    for mx in range(len(my_list) - 1, -1, -1):
        for i in range(mx):
            if my_list[i][1] == my_list[i + 1][1]:
                if my_list[i][0] > my_list[i + 1][0]:
                    my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
    return my_list
def q1():
    def read_file(file):
        dict = {}
        with open(file, "r") as f:
           for x in f:
               for y in x:
                   if y not in dict:
                        dict.update({y: 1})
                   else:
                    val = dict[y]+1
                    dict.update({y:val})
        return dict

    dictList = read_file("textesimple.txt")

    var = {k: v for k, v in sorted(dictList.items(), key=lambda item: item[1])}

    my_list = list(var.items())

    return sortascci(my_list)
def q2(my_list):
    class ArbreBinaire:
        def __init__(self, valeur):
            self.valeur = valeur
            self.bit = 0
            self.enfant_gauche = None
            self.enfant_droit = None

        def insert_gauche(self, valeur):
            if self.enfant_gauche == None:
                self.enfant_gauche = (valeur)

        def insert_droit(self, valeur):
            if self.enfant_droit == None:
                self.enfant_droit = (valeur)

        def get_valeur(self):
            return self.valeur

        def get_gauche(self):
            return self.enfant_gauche

        def get_droit(self):
            return self.enfant_droit

        def get_bit(self):
           return self.bit

    nodeList = []
    for k in range(len(my_list)):
        node = ArbreBinaire(my_list[k])
        nodeList.append(node)

    for k in range(len(nodeList)):
        print(nodeList[k].valeur, end=" ")
    node1 = nodeList[5]
    node2 = nodeList[6]

    print()
    new_node = ArbreBinaire(('',node2.valeur[1] + node1.valeur[1]))
    #new_node.insert_gauche(node1)
    #new_node.insert_droit(node2)
    #nodeList.insert(0,new_node)
    #print(new_node.valeur[1])

    while len(nodeList) != 1:
        node1 = nodeList[0]
        node2 = nodeList[1]
        new_node = ArbreBinaire(('', node2.valeur[1] + node1.valeur[1]))
        new_node.insert_gauche(node1)
        new_node.insert_droit(node2)
        #nodeList.append(new_node)
        x = True
        for k in range(len(nodeList)):
            if (new_node.valeur[1] <= nodeList[k].valeur[1]):
                nodeList.insert(k, new_node)
                x = False
                break
        if(x):
            nodeList.append(new_node)
        nodeList.remove(node1)
        nodeList.remove(node2)

    def remplissage(T:ArbreBinaire):
        if(T!=None):
            #print(T.get_valeur()[1])
            #print("Bit :", T.bit)
            if(T.get_gauche() != None):
                T.get_gauche().bit = 0
                remplissage(T.get_gauche())
            if(T.get_droit() != None):
                T.get_droit().bit = 1
                remplissage(T.get_droit())

    def affichageMaisonMaison(T:ArbreBinaire):
        if(T!=None):
            print("{\"label\" : \""+T.get_valeur()[0]+"\", \"frequence\" : "+str(T.get_valeur()[1])+", \"left\":" )
            affichageMaisonMaison(T.get_gauche())
            print(", \"right\":");
            affichageMaisonMaison(T.get_droit())
            print("}")
        else :
            print("null")

    def affiche(T):
        if T != None:
            return (T.get_valeur(),T.bit, affiche(T.get_gauche()), affiche(T.get_droit()))

    global_dict = []

    def get_codage(T: ArbreBinaire, constructor=""):
        if T.get_droit() == None and T.get_gauche() == None:
            print("constructor : ", constructor)
            l = []
            l.append(constructor)
            global_dict.append(l)
        else :
            #if (T.get_gauche() != None):
            c = constructor +  "0"
            #print("0", end="")
            get_codage(T.get_gauche(), c)
            #if (T.get_droit() != None):
            c = constructor + "1"
            #print("1",end="")
            get_codage(T.get_droit(), c)

    #print(nodeList[0].valeur)
    remplissage(nodeList[0])
    affichageMaisonMaison(nodeList[0])
    #print(affiche(nodeList[0]))
    #affichageMaisonMaison(nodeList[0])
    #print
    get_codage(nodeList[0])
    print(global_dict)
if __name__ == '__main__':
        #print((q1()))
        print(q2(q1()))