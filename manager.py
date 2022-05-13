from math import fabs

#Déclaration couleurs
class bcolors:
    OK = '\033[92m' #GREEN
    LIGHT_RED = "\033[1;31m"
    YELLOW = '\033[93m' 
    RED = '\033[91m' 
    BLUE = "\033[0;34m"
    LIGHT_BLUE = "\033[1;34m"
    LIGHT_GRAY = "\033[0;37m"
    DARK_GRAY = "\033[1;30m"
    RESET = '\033[0m' #RESET COLOR

#chiffrage des données
def encrypt (data, shift):
    encrypted = ""
    for i in range (len(data)):
        char = data[i]
        if (char.isupper()):
            encrypted += chr((ord(char) + shift -65) % 26 +65)
        elif (char.islower()):
            encrypted += chr((ord(char) + shift -97) % 26 +97)
        elif (char.isdigit()):
            number = (int(char) + shift) % 10
            encrypted += str(number)
        else:
            encrypted += char
    return encrypted 

#déchiffrage
def decrypt (data, shift):
    decrypted = ""
    for i in range (len(data)):
        char = data[i]
        if (char.isupper()):
            decrypted += chr((ord(char) - shift -65) % 26 +65)
        elif (char.islower()):
            decrypted += chr((ord(char) - shift -97) % 26 +97)
        elif (char.isdigit()):
            number = (int(char) + shift) % 10
            decrypted += str(number)
        else:
            decrypted += char
    return decrypted 

menu = ""
while menu != '1' or menu != '2':
    menu = input("\nQue souhaitez vous faire ?" 
                 "\n1. Nouveau mot de passe"
                 "\n2. Voir les mots de passe"
                 "\n3. Générateur de mot de passe (à venir)"
                 "\n4. Quitter"
                 "\nVotre choix : ")
    if menu=='1':
        softwareName = input("\nNom du site: ")
        username = input("Nom utilisateur: ")
        password = input("Mot de passe: ")
        shift = 5
        file = open("passwordsData.txt", "a")
        file.write(encrypt(softwareName,shift)+";|"+encrypt(username,shift)+";|"+encrypt(password,shift)+"\n")
        file.close()
        print (bcolors.OK + "\n" "Votre nouveau mot de passe a bien été ajouté !" "\n" + bcolors.RESET)
    if menu=='2':
       file = open("passwordsData.txt", "r")
       print(bcolors.BLUE + "\n" "Software\tUsername\tPassword" "\n" + bcolors.RESET)
       for i in file:
           shift = 5
           data = i.split(";|")
           print(bcolors.DARK_GRAY + decrypt(data[0],shift)+"\t\t"+decrypt(data[1],shift)+"\t\t"+decrypt(data[2],shift) + bcolors.RESET)
    if menu =='4':
        exit()
        