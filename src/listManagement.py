def sortascci(my_list):
    """
    Fonction qui trie un dictionnaire en fonction des valeurs de leur clef
    :param my_list:
    :return:
    """
    for mx in range(len(my_list) - 1, -1, -1):
        for i in range(mx):
            if my_list[i][1] == my_list[i + 1][1]:
                if my_list[i][0] > my_list[i + 1][0]:
                    my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
    return my_list
