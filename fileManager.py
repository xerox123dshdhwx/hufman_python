import os


def read_file(file):
    """
    Fonction qui permet de lire un fichier et d'associer une fréquence d'apparition à chaque caractère lu
    :param file:
    :return: dict de fréquence
    """
    dict = {}
    with open(file, "r") as f:
        for x in f:
            for y in x:
                if y not in dict:
                    dict.update({y: 1})
                else:
                    val = dict[y] + 1
                    dict.update({y: val})
    return dict


def tauxCompression(fileName):
    """
    Fonction qui fait le rapport du poids en octet de 2 fichiers
    :param fileName:
    :return:
    """
    init = os.path.getsize(fileName)
    final = os.path.getsize("res.bin")
    print((1 - int(final) / init) * 100, "%")


def getTextToBin(fileName, dict):
    """
    Fonction qui permet de convertir tout un fichier en chaine de caractère binaire lui correspondant
    :param fileName:
    :param dict: d'association caractère -> chaine binaire
    :return:
    """
    text_to_bin = ""
    with open(fileName, "r") as f:
        for x in f:
            for y in x:
                text_to_bin += dict.get(y)
    return text_to_bin


def writteFileBin(text_to_bin):
    """
    Fonction qui convertie une chaine de caractère binaire en un entier base 2 puis la convertie en bit pour l'écrire dans un fchier binaire
    :param text_to_bin:
    :return:
    """
    with open("res.bin", "wb") as f_bin:
        f_bin.write(int(text_to_bin, base=2).to_bytes((len(text_to_bin) + 7) // 8, byteorder='big'))

def moyenneBit(my_list,list):
    sum = 0
    for bit in list:
        sum += len(bit[0])

    print(sum/len(my_list))