#importo el módulo random para utilizarlo más tarde
import random as rd
#creo la función horca con un total de 7 intentos
def horca(intento):
    if intento ==0:
        print("""
      .____       
      |   |
      |
      |
      |
    __|____
              
        """)
    elif intento ==1:
          print("""
      .____       
      |   |
      |   O
      |   
      |
    __|____
              
        """)
    elif intento ==2:
              print("""
      .____       
      |   |
      |   O
      |   |
      |
    __|____
              
        """)
    elif intento ==3:
              print("""
      .____       
      |   |
      |   O
      |  /|
      |
    __|____
              
        """)
 

    elif intento ==4:
        print("""
      .____       
      |   |
      |   O
      |  /|\ 
      |
    __|____
              
        """)
    elif intento ==5:
        print("""
      .____       
      |   |
      |   O
      |  /|\ 
      |  /
    __|____
              
        """)
    elif intento ==6:
        print("""
    GAME OVER
      .____       
      |   |      
      |   O
      |  /|\ 
      |  / \ 
    __|____
              
        """)
def elegir_palabra():
    #el ahorcado va a contener temática de ríos de todo el mundo 
    palabras=["Nilo", "Tajo", "Misisipi","Amazonas","Ganges", "Danubio","Niger","Colorado",
              "Lena", "Ebro", "Tigris","Misuri","Sena", "Volga", "Rin", "Obi", "Congo",
              "Orange", "Orinoco"]
    palabra_secreta=rd.choice(palabras)#eliijo una palabra al azar
    return palabra_secreta.lower()#minimizamos la letras para evitar preblemas entre minúsculas y mayúsculas

lista_palabra=list(elegir_palabra())#ejecutamos la función y la guardamos en una variable para luego uslarla


def pedir_letra(): #definimos función pedir letra
    letra=(input("Dame una letra, por favor: ")).lower()#minimizamos la letras para evitar preblemas entre minúsculas y mayúsculas
    return letra

#esta función nos comprueba si existe la letra dentro de la lista_palabra 
def comprobador_letras(letra, lista_palabra):
    #si está nos devuelve True
    if letra in lista_palabra:
        return True
    #sino está False
    else:
        return False

#Esta función se ejecutará una vez hayamos comprobados las letras y estas estén.
#En ella se produce el intercambio de rayas por letras, y por ende conseguimos la actualización del tablero 
def imprimir_tablero(letra, tablero, lista_palabra):
    for elem in range(len(lista_palabra)):#manipulamos el for con índices, recordar que tanto lista palabras, como tablero tienen las mismas líneas
            if lista_palabra[elem]==letra:
                tablero[elem]=letra
    return tablero #el tablero se me actualiza
#Iniciamos juego
print("""Buenos días, bienvenido al juego del ahorcado
Dispones de 7 intentos para resolver una palabra 
PISTA: Las palabras son ríos muy importantes  """)
count=0 #creamos esta variable a fin de contar los intentos
tablero="_"*len(lista_palabra) #creamos el tablero con las rayas y la misma longitud que la lista_palabra que contiene la palabra a buscar
tablero=list(tablero)#lo transformamos en lista
resultado=False #esta vairable la usaremos para saber si el jugador a ganado o no, la dejamos en false que significará que ha perdido
horca(count) #dibujaremos la horca base, osea la horca con los 7 intentos
print(tablero)#imprimimos el tablero con las rayitas
while count!=7: #el blucle se rompe si el numero de intentos es igual a  7
    letra=pedir_letra() #llamamos a la función para pedir una letra y la guardamos en una varible para usarla depués
    comprobador=comprobador_letras(letra, lista_palabra) #comprobamos si la letra está o no y lo guardamos en una variable que puede dar True o False
    if comprobador==True: 
        tablero=imprimir_tablero(letra, tablero, lista_palabra)# si es verdad se ejecuta y actualiza el tablero
        horca(count) #mostramos horca y tablero
        print(tablero)
        if tablero==lista_palabra:#observamos si el tablero esta completp igualando ambas funciones
            resultado=True #si está completo, cambiamos el resultado a True
            break #rompemos el bucle
        else: #no ha acabado, continuamos con el bucle
            continue
    else:
         count+=1 #sino ha acertado sumamos a la varible 1
         print(f"Te quedan {7-count} intentos")#restamos al número total de intentos los consumidos para mostrarlos totales
         horca(count) #mostramos horca y tablero
         print(tablero)
#una vez fuera de bucle se comprueba si ha ganado o no 
if resultado==True:
     print("Enhorabuena,¡Has ganado!")
else:
     print("Lo siento, has perdido")

