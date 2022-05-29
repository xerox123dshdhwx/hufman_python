import os


def read_file(file):
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
    init = os.path.getsize(fileName)
    final = os.path.getsize("res.bin")
    print((1-int(final)/init)*100, "%")

def getTextToBin(fileName,dict):
    text_to_bin = ""
    with open(fileName, "r") as f:
        for x in f:
            for y in x:
                text_to_bin+=dict.get(y)
    return text_to_bin

def writteFileBin(text_to_bin):
    with open("res.bin", "wb") as f_bin:
        f_bin.write(int(text_to_bin, base=2).to_bytes((len(text_to_bin) + 7) // 8, byteorder='big'))