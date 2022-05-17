

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
    for mx in range(len(my_list)-1, -1, -1):
        for i in range(mx):
            if my_list[i][1] == my_list[i+1][1]:
                if my_list[i][0] >my_list[i+1][0]:
                    my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]


    return  my_list

if __name__ == '__main__':
        print(q1())