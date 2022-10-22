import random
import LinkedList_Wordle
from time import sleep
from termcolor import colored
from colorama import Cursor,Fore,Back,init
init(autoreset=True)
 
         
def en_verde(L1_node, L2_node):     #Para poner valor en color verde       
    Pinte = L2_node.value
    while(L1_node is not None):
        if(L2_node.value == L1_node.value and L2_node.pos == L1_node.pos):
            L1_node.used = True
            Pinte = colored(L2_node.value, "green")
            break
        L1_node = L1_node.next
    return Pinte

def en_amarillo(L1_node, L2_node): #Para poner valor en color amarillo        
    Pinte = L2_node.value
    while(L1_node is not None):
     if(L2_node.value == L1_node.value and L1_node.used == False):
        if(L2_node.pos > L1_node.pos):
            L1_node.used = True
        Pinte = colored(L2_node.value, "yellow")
     L1_node = L1_node.next
    return Pinte


print(Fore.BLACK + Back.RED + """
▀█████████▄   ▄█     ▄████████ ███▄▄▄▄    ▄█    █▄     ▄████████ ███▄▄▄▄    ▄█  ████████▄   ▄██████▄          ▄████████       ▄█     █▄   ▄██████▄     ▄████████ ████████▄   ▄█          ▄████████ 
  ███    ███ ███    ███    ███ ███▀▀▀██▄ ███    ███   ███    ███ ███▀▀▀██▄ ███  ███   ▀███ ███    ███        ███    ███      ███     ███ ███    ███   ███    ███ ███   ▀███ ███         ███    ███ 
  ███    ███ ███▌   ███    █▀  ███   ███ ███    ███   ███    █▀  ███   ███ ███▌ ███    ███ ███    ███        ███    ███      ███     ███ ███    ███   ███    ███ ███    ███ ███         ███    █▀  
 ▄███▄▄▄██▀  ███▌  ▄███▄▄▄     ███   ███ ███    ███  ▄███▄▄▄     ███   ███ ███▌ ███    ███ ███    ███        ███    ███      ███     ███ ███    ███  ▄███▄▄▄▄██▀ ███    ███ ███        ▄███▄▄▄     
▀▀███▀▀▀██▄  ███▌ ▀▀███▀▀▀     ███   ███ ███    ███ ▀▀███▀▀▀     ███   ███ ███▌ ███    ███ ███    ███      ▀███████████      ███     ███ ███    ███ ▀▀███▀▀▀▀▀   ███    ███ ███       ▀▀███▀▀▀     
  ███    ██▄ ███    ███    █▄  ███   ███ ███    ███   ███    █▄  ███   ███ ███  ███    ███ ███    ███        ███    ███      ███     ███ ███    ███ ▀███████████ ███    ███ ███         ███    █▄  
  ███    ███ ███    ███    ███ ███   ███ ███    ███   ███    ███ ███   ███ ███  ███   ▄███ ███    ███        ███    ███      ███ ▄█▄ ███ ███    ███   ███    ███ ███   ▄███ ███▌    ▄   ███    ███ 
▄█████████▀  █▀     ██████████  ▀█   █▀   ▀██████▀    ██████████  ▀█   █▀  █▀   ████████▀   ▀██████▀         ███    █▀        ▀███▀███▀   ▀██████▀    ███    ███ ████████▀  █████▄▄██   ██████████ 
                                                                                                                                                      ███    ███            ▀                      
  \n""")

       
s=str(input("Por favor ingrese la letra s: "))
if s!= "s":
    print("Has ingresado un caracter erroneo")  
else:
    print("\n¡Has ingresado a Wordle!\n")
  
L1=LinkedList_Wordle.LinkedList() # Lista para almacenar la palabra a adivinar 
L2=LinkedList_Wordle.LinkedList() # Lista para guardar caracteres que estan en la posicion correcta
L3=LinkedList_Wordle.LinkedList() # Lista para guardar caracteres que estan en la posicion incorrecta
L4=LinkedList_Wordle.LinkedList() # Lista que retorna la palabra despues de haber pasado los filtros

Palabras=str(input("Por favor palabra a adivinar: "))
Palabras=Palabras.lower()
print("Cargando palabra...\n")
            
print("""[■□□□□□□□□□] 10%""")
sleep(0.1)
print(Cursor.BACK(16) + Cursor.UP(1) + """[■■□□□□□□□□] 20%""")
sleep(0.1)
print(Cursor.BACK(16) + Cursor.UP(1) + """[■■■□□□□□□□] 30%""")
sleep(0.1)
print(Cursor.BACK(16) + Cursor.UP(1) + """[■■■■□□□□□□] 40%""")
sleep(0.1)
print(Cursor.BACK(16) + Cursor.UP(1) + """[■■■■■□□□□□] 50%""")
sleep(0.1)
print(Cursor.BACK(16) + Cursor.UP(1) + """[■■■■■■□□□□] 60%""")
sleep(0.1)
print(Cursor.BACK(16) + Cursor.UP(1) + """[■■■■■■■□□□] 70%""")
sleep(0.1)
print(Cursor.BACK(16) + Cursor.UP(1) + """[■■■■■■■■□□] 80%""")
sleep(0.1)
print(Cursor.BACK(16) + Cursor.UP(1) + """[■■■■■■■■■□] 90%""")
sleep(0.1)
print(Cursor.BACK(17) + Cursor.UP(1) + """[■■■■■■■■■■] 100%""")
            
print("¡Palabra cargada con exito! ;)\n")
           
       
print(Fore.RED + "¡INSTRUCCIONES!\n")
print("A continuacion deberas ingresar una palabra para empezar a jugar.\n")
print("Al ingresar una palabra, si esta contiene letras que existan en la palabra a adivinar, la forma en la que las letras apareceran sera la siguiente.\n\nSi la letra existe y esta en la posicion correcta aparecera de color verde, asi:")
print(Fore.GREEN + "letra existente en posicion correcta")
print("\n")
print("Si la letra existe, pero no esta en la posicion correcta, aparecera de color amarillo, asi:")
print(Fore.YELLOW +"letra existente pero en posicion incorrecta")
print("\n¡Recuerda que solo tienes 6 intentos para adivinar la palabra!, suerte ;)\n")

for i in Palabras:
    L1.add_tail(i)

print(F"La palabra a adivinar es de {L1.get_size()} letras recuerda no ingresar palabras mas grandes a este tope de letras, ya que perderas un turno, suerte")
  
Intentos_gastados = 1
Tope_intentos = 6
Ganar = False
while(Intentos_gastados <= Tope_intentos and Ganar == False):
    lista_intentos = {1:"Primer", 2:"Segundo", 3:"Tercer", 4:"Cuarto", 5:"Quinto", 6:"ÚLTIMO"}
    Palabra_a_evaluar = input("Por favor ingresa una palabra: ")
    while(len(Palabra_a_evaluar) < L1.get_size()):
        print(f"Recuerda que la palabra debe ser de {L1.get_size()} letras...")
        Palabra_a_evaluar = input(f"Por favor ingresa una palabra: ")
    while(len(Palabra_a_evaluar) > L1.get_size()):
        print(f"Has ingresado una palabra con mas letras que la palabra a adivinar, pierdes un turno :,(")
        break
    print(f"Llevas: {Intentos_gastados} intentos")

    for i in Palabra_a_evaluar:
        L2.add_tail(i)

    L1_node = L1.head
    L2_node = L2.head
    while(L2_node is not None):   
        Pinte = en_verde(L1_node, L2_node)
        L3.add_tail(Pinte)         
        L2_node = L2_node.next

    current_node = L1.head
    while(current_node != None):            
        if(current_node.used == False):
            break
        elif(current_node.next == None and L1.get_size() == L2.get_size()):
            Ganar = True
        current_node = current_node.next

    L3_node = L3.head
    while(L3_node is not None):    
        Pinte = en_amarillo(L1_node, L3_node)
        L4.add_tail(Pinte)          
        L3_node = L3_node.next
    L4.print_LinkedList()
            
    while(L1_node is not None):    
        L1_node.used = False
        L1_node = L1_node.next
    L2 = LinkedList_Wordle.LinkedList()
    L3 = LinkedList_Wordle.LinkedList()
    L4 = LinkedList_Wordle.LinkedList()
        
    print(".....................................................")
    Intentos_gastados += 1
if(Ganar is True):
    print("HAS GANADO")
else:
    print(f"La palabra era: {Palabras}") 
    print(Fore.RED + """
 ██░ ██  ▄▄▄        ██████     ██▓███  ▓█████  ██▀███  ▓█████▄  ██▓▓█████▄  ▒█████   ▐██▌ 
▓██░ ██▒▒████▄    ▒██    ▒    ▓██░  ██▒▓█   ▀ ▓██ ▒ ██▒▒██▀ ██▌▓██▒▒██▀ ██▌▒██▒  ██▒ ▐██▌ 
▒██▀▀██░▒██  ▀█▄  ░ ▓██▄      ▓██░ ██▓▒▒███   ▓██ ░▄█ ▒░██   █▌▒██▒░██   █▌▒██░  ██▒ ▐██▌ 
░▓█ ░██ ░██▄▄▄▄██   ▒   ██▒   ▒██▄█▓▒ ▒▒▓█  ▄ ▒██▀▀█▄  ░▓█▄   ▌░██░░▓█▄   ▌▒██   ██░ ▓██▒ 
░▓█▒░██▓ ▓█   ▓██▒▒██████▒▒   ▒██▒ ░  ░░▒████▒░██▓ ▒██▒░▒████▓ ░██░░▒████▓ ░ ████▓▒░ ▒▄▄  
 ▒ ░░▒░▒ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░   ▒▓▒░ ░  ░░░ ▒░ ░░ ▒▓ ░▒▓░ ▒▒▓  ▒ ░▓   ▒▒▓  ▒ ░ ▒░▒░▒░  ░▀▀▒ 
 ▒ ░▒░ ░  ▒   ▒▒ ░░ ░▒  ░ ░   ░▒ ░      ░ ░  ░  ░▒ ░ ▒░ ░ ▒  ▒  ▒ ░ ░ ▒  ▒   ░ ▒ ▒░  ░  ░ 
 ░  ░░ ░  ░   ▒   ░  ░  ░     ░░          ░     ░░   ░  ░ ░  ░  ▒ ░ ░ ░  ░ ░ ░ ░ ▒      ░ 
 ░  ░  ░      ░  ░      ░                 ░  ░   ░        ░     ░     ░        ░ ░   ░    
                                                        ░           ░                     
 """)
    print(Fore.BLACK + """░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░▓████████████████████████▒░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░▓█████▓▒░░░░░░░░░░░░░░░▒██████▒░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░████▒░░░░░░░░░░░░░░░░░░░░░░░░░▓███▒░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░███░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░███░░░░░░░░░░░░░░░
░░░░░░░░░░░░░▒██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒██░░░░░░░░░░░░░░
░░░░░░░░░░░░▒██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░░░░░░░░░░░░
░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░░░░░░░░░░░
░░░░░░░░░░░██▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒░░██░░░░░░░░░░░░
░░░░░░░░░░░██░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░██░░░░░░░░░░░
░░░░░░░░░░░██░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░██░░░░░░░░░░░
░░░░░░░░░░░██░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░██░░░░░░░░░░░
░░░░░░░░░░░██▒░██▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██▓░▒██░░░░░░░░░░░
░░░░░░░░░░░░██░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░██░░░░░░░░░░░░
░░░░░░░░░░░░██▒░██░░░░░▒▒▓███▒░░░░░░░▒███▓▒▒░░░░░██░▓██░░░░░░░░░░░░
░░░░░░░░░░░░░██░██░░██████████▒░░░░░▓██████████░░██▒██░░░░░░░░░░░░░
░░░░░░░░░░░░░░████░████████████░░░░░████████████░████░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░███░▒██████████░░░░░░░██████████▒░██▒░░░░░░░░░▒░░░░░
░░░▒████░░░░░░░▓█▒░░█████████░░░░░░░░░█████████░░▒█▓░░░░░░▓████░░░░
░░░██░▒██▒░░░░░██░░░░██████▓░░░░█░█░░░░███████░░░░██░░░░░███░░██░░░
░░░██░░░██▓░░░░██░░░░░░▒▓▓░░░░▒██░██░░░░░▓▓▒░░░░░▒██░░░░███░░░██░░░
░▓██▒░░░░████▓░░██░░░░░░░░░░░░███░███░░░░░░░░░░░░██░░█████░░░░▓██▒░
██▓░░░░░░░░▒████████▓░░░░░░░░████░███▓░░░░░░░▒▓████████░░░░░░░░░███
██▓▒▓███▓░░░░░░▓████████▓░░░░████░███▓░░░░▓████████▓░░░░░░████▓▓███
░███████████▒░░░░░░███████░░░░██░░░██░░░░██████▓░░░░░░▓███████████░
░░░░░░░░░░▓█████░░░░██▓▓░██░░░░░░░░░░░░░██░█▒██░░░▒█████▓░░░░░░░░░░
░░░░░░░░░░░░░▒█████▒▒█▓█░███▓▓▒▒▒▓▒▒▓▓▓███▒███░▓█████░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░▒████▒▓█▒▒█░█▒█░█░█▓█▒█▓░█░█████▒░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░██░░██▓█▓█▓█▒█▒█▓█▓████░▓█▓░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░▓████▓░▓█▓█░█▒█░█░█▒█▒███▒░██████░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░▓█████░░██░░░▒█████▓█▓█████▒░░░██░▒█████▓░░░░░░░░░░░░░
░░░░▒██████████▓░░░░░███░░░░░░░░░░░░░░░░░░░██▒░░░░░▓██████████▒░░░░
░░░░██░░░▓▓▓░░░░░░▒██████▓░░░░░░░░░░░░░░░███████▒░░░░░░▓▓▒░░▒██░░░░
░░░░▓██░░░░░░░░▓████▓░░░█████▒░░░░░░▒▓█████░░░▓████▓░░░░░░░▒██▓░░░░
░░░░░░███░░░░████▒░░░░░░░░▓█████████████▒░░░░░░░░▒████░░░░███░░░░░░
░░░░░░░██░░░██▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓██░░░██░░░░░░░
░░░░░░░██▒▓██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒██▒▓██░░░░░░░
░░░░░░░░████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░████░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
""")                                                                    

    
 

   
        
        
        
    
        