def recuperer_nombre_que_conozco(user_enter):  # Check if I know the user in the database
    fichier_admin = open("Bdatos_Admin.txt", "r")
    Admin = fichier_admin.readlines()
    fichier_admin.close()
    for i in range(0, len(Admin)):
        User = Admin[i].split(";")
        if User[0] == user_enter:
            return True


def Droit_gene(user_enter):
    fichier_admin = open("Bdatos_Admin.txt", "r")
    Admin = fichier_admin.readlines()
    fichier_admin.close()
    for i in range(0, len(Admin)):
        User = Admin[i].split(";")
        if User[0] == user_enter:
            return User


def derechas_por_eso_menu(user, val_menu):
    list_droit = Droit_gene(user)
    if list_droit[int(val_menu)] == "T":
        print("Ok tu tiennes el DERECHA de hacer lo ! ")
        return True
    else:
        print("NO !! tu NO tiennes el derecha de haver lo ! ")
        return False
