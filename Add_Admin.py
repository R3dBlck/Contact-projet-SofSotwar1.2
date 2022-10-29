def El_nombre_del_nuevo_usario():
    nombre = input("Quien es el nuevo usuario ?")
    return nombre


def Verificacion_de_la_escritura(nombre):
    if nombre.isalpha():
        return True


def re_escritura_del_nombre_del_usuario(nom):
    nom_new = nom.lower()  # I correctly rewrite the name to be able to compare it to the database afterwards
    return nom_new


def entraga_los_derechos():
    print("Administrado ?   -- 1 ")
    print("Gestor ?         -- 2 ")
    print("Asistente ?      -- 3 ")
    De_num = input("Que typo de derechas tienne ? ")
    return De_num


def verrif_la_entraga_de_los_derechos(num_dere):
    if num_dere.isdigit():
        if int(num_dere) in (1, 2, 3):
            return True
        else:
            return False
    else:
        return False


def escritura_en_la_base(num_der, nombre):
    fichier_admin = open("Bdatos_Admin.txt", "a")
    if int(num_der) == 1:
        a = (nombre + ";T;T;T;T;T;")
        fichier_admin.write("\n")
        fichier_admin.write(a)
        fichier_admin.close()
    if int(num_der) == 2:
        a = (nombre + ";T;T;F;T;F;")
        fichier_admin.write("\n")
        fichier_admin.write(a)
        fichier_admin.close()
    if int(num_der) == 3:
        a = (nombre + ";F;F;F;T;F;")
        fichier_admin.write("\n")
        fichier_admin.write(a)
        fichier_admin.close()
