def listar_contacto():
    fichier_contact = open("Bdatos.txt", "r")
    contact = fichier_contact.readlines()
    fichier_contact.close()
    print("                     ##############################################")
    print("                     #--------------------------------------------#")
    for i in range(0, len(contact)):
        c = contact[i].split(";")
        print("                     Contacto n° : ", i)
        for j in range(0, len(c)):
            print("                     ", c[j])
        print("                     #--------------------------------------------#")
    print("                     ##############################################")
def nombre_de_contacto():
    fichier_contact = open("Bdatos.txt", "r")
    contact = fichier_contact.readlines()
    fichier_contact.close()
    return len(contact)

def Quien_kill():
    listar_contacto()
    num_del_proximo_muerte = input("Quien tu quierres kill ??? (enter el num)")
    return num_del_proximo_muerte

def el_num_del_proximo_muerto_es_correcto(num_del_proximo_muerte):
    if num_del_proximo_muerte.isdigit():
        if int(num_del_proximo_muerte) <= nombre_de_contacto() and int(num_del_proximo_muerte) >= 0 :
            return True
        else:
            return False
    else:
        return False

def function_de_la_muerte_de_los_contactos(nom_kill_prox):
    fichier_contact = open("Bdatos.txt", "r")
    contact = fichier_contact.readlines()
    fichier_contact.close()
    a = ""
    for i in range(0, len(contact)):
        if i != int(nom_kill_prox):
            c = contact[i].split(";")
            for j in range(0, 3):
                a = a + c[j]
                if j == 1 or j == 0:
                    a = a + ";"
    fichier_contact = open("Bdatos.txt", "w")
    fichier_contact.truncate()
    fichier_contact.write(a)

def agregar_nombre():
    nombre=input("¿Cómo se llama el afortunado que vas a añadir (nombre)?")
    return nombre

def agregar_appellido():
    appellido=input("¿Cómo se llama el afortunado que vas a añadir (appellido)?")
    return appellido

def agregar_numero():
    numero=input("¿Cómo se llama el afortunado que vas a añadir (numero)?")
    return numero

def entraga_num_corect(enter):
    if enter.isdigit():
        if len(enter)==10:
            return True
        else:
            return False
    else:
        return False
def entraga_letter_corect(enter):
    if enter.isalpha():
        return True
    else:
        return False

def entraga_min(enter):
    enter_new = enter.lower()  # I correctly rewrite the name to be able to compare it to the database afterwards
    return enter_new

def entraga_en_grange(enter):
    entrer_new = enter.upper()
    return entrer_new


def agregar_contacto():
    num=agregar_numero()
    nom=agregar_nombre()
    ape=agregar_appellido()
    if entraga_letter_corect(nom):
        nom=entraga_min(nom)
        if entraga_letter_corect(ape):
            ape=entraga_en_grange(ape)
            if entraga_num_corect(num):
                fichier_contact = open("Bdatos.txt", "a")
                a = (nom + ";" + ape + ";" + num)
                fichier_contact.write("\n")
                fichier_contact.write(a)
                fichier_contact.close()
            else:
                agregar_contacto()
        else:
            agregar_contacto()
    else:
        agregar_contacto()

def quien_tu_quiere_modif():
    quien_modif = input("Quien tu quierres modif ?? (El numero !!!)")
    return quien_modif


def modif_contacto(num_ct):
    fichier_contact = open("Bdatos.txt", "r")
    contact = fichier_contact.readlines()
    fichier_contact.close()
    a = ""
    for i in range(0, len(contact)):
        if i != int(num_ct):
            c = contact[i].split(";")
            for j in range(0, 3):
                a = a + c[j]
                if j == 1 or j == 0:
                    a = a + ";"
    fichier_contact = open("Bdatos.txt", "w")
    fichier_contact.truncate()
    fichier_contact.write(a)

    num = agregar_numero()
    nom = agregar_nombre()
    ape = agregar_appellido()
    if entraga_letter_corect(nom):
        nom = entraga_min(nom)
        if entraga_letter_corect(ape):
            ape = entraga_en_grange(ape)
            if entraga_num_corect(num):
                fichier_contact = open("Bdatos.txt", "a")
                a = (nom + ";" + ape + ";" + num)
                fichier_contact.write("\n")
                fichier_contact.write(a)
                fichier_contact.close()
            else:
                agregar_contacto()
        else:
            agregar_contacto()
    else:
        agregar_contacto()





