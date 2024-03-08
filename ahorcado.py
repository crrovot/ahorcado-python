#juego del aorcadoen python
# definir una palabra
# numero efinido de intentos    
# pedir al usuario que ingrese una letra a la vez
# mostrar resultado e acierto o perdida


def ahorcado():
    #definir palabra secreta
    palabra_secreta="barbaro"
    letras_adivinadas=[]
    #lista para almecenar
    intentos=5 #numero de intentos

    while intentos > 0
        palabra_mostrada="barbaro"
        for letras in palabra_secreta:
            if letra in letras_adivinadas:
                palabra_mostrada += letras 
            else:
                palabra_mostrada +="_ "
        print(palabra_mostrada)

        if palabra_mostrada == palabra_secreta
                print("haz adivinado la palabra")
                break   
            #pedir al usuario una letra
        letras_usuario=input("ingrese una letra")

            #verificar si la letra a sido adivinada
        if letras_usuario in letras_adivinadas
                print("ya haz adivinado es letra")
                continue
        if letras_usuario in palabra_secreta
                print("bein tu eltra esta en la palabra")
            letras_adivinadas.append(letras_usuario) 
        else:
            intentos -=1
                print("incorrecto pierdes un intento" + intentos) 

            if intentos==0:
                    print("haz agotado todos lso intentos, la palabra era" + palabra_secreta)
#llamar a alfuncion
ahorcado()