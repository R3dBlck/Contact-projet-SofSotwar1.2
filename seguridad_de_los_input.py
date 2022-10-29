def el_nombre_es_un_nombre(nom):  # the enter name is letters ?
    if nom.isalpha():  # Yes ok !
        return True
    else:
        return False  # No ...


def el_enter_is_num(entre):
    if entre.isdigit():
        return True


def el_num_del_menu_es_correcto(num_entree):
    if el_enter_is_num(num_entree):
        if int(num_entree) in (1, 2, 3, 4, 5, 0):
            return True
        else:
            return False
    else:
        return False
