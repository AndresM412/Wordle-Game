import random
import Lista_Enlazada
class Wordle:
    def Pasar_Palabra_A_LinkedList():
        L1=Lista_Enlazada.LinkedList()
        Palabras=["Bóxer","Busto","Burro","Burla","Bufón","Bufet","Bueno","Bucal","Bingo","Códex"]
        Palabra_Elegida=random.choice(Palabras)
        for i in Palabra_Elegida:
           L1.add_at_head(i)
        L1.reverse()
        L1.traverse()  #Para mostrar la palabra

