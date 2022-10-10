import Logica_Juego
def Bienvenida(s):
    s=input("Bienvenido a wordle, por favor ingrese la letra s: ")
    if s=="S"or s=="s":
        print("¡Has ingresado a Wordle!, cargando palabra....")
        Palabra=Logica_Juego.Wordle.Pasar_Palabra_A_LinkedList()
        print("¡Palabra cargada con exito! ;)")
    else:
        print("Has ingresado un caracter erroneo, intentalo de nuevo! ")
        return Bienvenida("")



Bienvenida(1)
