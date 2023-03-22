# Libreria para limpiar pantalla
import os
os.system("cls")

import random
import string

# mensajes de inicio
print("Bienvenid@ al generador de passwords")
print("El password debe tener mínimo 4 caracteres")
os.system("pause") #Pasa a la siguiente pantalla


password = [] 

while len(password) == 0:
    # Pantalla para iniciar
    os.system("cls") #limpia la pantalla

    input_str = str(input("¿Cuántos caracteres necesitas para tu password?"))
    
    if not input_str.isdigit() or int(input_str) < 4:
        print("Tienes que ingresar un número de caracteres válido, ¡al menos 4! \n")
        os.system("pause")
    else:
        numero_de_caracteres = int(input_str)
        lista_mayusculas = []
        lista_minusculas = []
        lista_numeros = []
        lista_simbolos = []
        #Genera la lista de letras mayusculas
        letras_mayusculas = [lista_mayusculas.append(chr(i)) for i in range(65, 91)] 
        #Genera la lista de letras minusculas
        letras_minusculas = [lista_minusculas.append(chr(i)) for i in range(97, 122)] 
        #Genera la lista de numeros
        numeros = [lista_numeros.append(str(i)) for i in range(0, 10)]
        #Genera la lista de simbolos
        simbolos = [lista_simbolos.append(i) for i in string.punctuation]

        #Password base de 4 caracteres: una letra mayúscula + una letra minúscula + un número + un simbolo
        letras_mayusculas = password.append(random.choice(lista_mayusculas))
        letras_minusculas = password.append(random.choice(lista_minusculas))
        numeros = password.append(random.choice(lista_numeros))
        simbolos = password.append(random.choice(lista_simbolos))
        random.shuffle(password)

        #Elige los caracteres necesarios para completar y los añade al password
        lista_caracteres_extra = []
        caracteres_para_completar = lista_mayusculas + lista_minusculas + lista_numeros + lista_simbolos
        caracteres_elegidos_para_completar = [password.append(random.choice(caracteres_para_completar)) for i in range(numero_de_caracteres - 4)]
        # print(password)

        #Imprime el password final
        random.shuffle(password)
        password = "".join(password)
        
print(password)