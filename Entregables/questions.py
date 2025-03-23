import random
import sys #para poder usar el exit

# Preguntas para el juego
questions = [
"¿Qué función se usa para obtener la longitud de una cadena en Python?",
"¿Cuál de las siguientes opciones es un número entero en Python?",
"¿Cómo se solicita entrada del usuario en Python?",
"¿Cuál de las siguientes expresiones es un comentario válido en Python?",
"¿Cuál es el operador de comparación para verificar si dos valores son iguales?",
]
# Respuestas posibles para cada pregunta, en el mismo orden que las preguntas
answers = [
("size()", "len()", "length()", "count()"),
("3.14", "'42'", "10", "True"),
("input()", "scan()", "read()", "ask()"),
(
"// Esto es un comentario",
"/* Esto es un comentario */",
"-- Esto es un comentario",
"# Esto es un comentario",
),
("=", "==", "!=", "==="),
]

# Índice de la respuesta correcta para cada pregunta, en el mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1]
# El usuario deberá contestar 3 preguntas
for _ in range(3):
    # Se selecciona una pregunta aleatoria
    question_index = random.randint(0, len(questions) - 1)
 
    # Se muestra la pregunta y las respuestas posibles
    print(questions[question_index])
    for i, answer in enumerate(answers[question_index]):
        print(f"{i + 1}. {answer}")
 
# El usuario tiene 2 intentos para responder correctamente
    for intento in range(2):    
        user_imput = input("Respuesta: ")
        #armo una lista que por cada caracter en la respuesta gaurde true si es un digito false si no lo es
        contiene_numero=[caracter.isdigit() for caracter in user_imput]
        if not any (contiene_numero): #devuelve true si al menos uno de los elementos de la lista es true
            print ('Respuesta no valida')
            sys.exit(1)
        else:
            user_answer= int(user_imput)-1
            # Se verifica si la respuesta es correcta
            if user_answer<0 or user_answer>= len(answers[question_index]): 
            #si lo que ingresa es menor a 0 o mayor o igual a 3 da error 
                print ('Respuesta no valida')
                sys.exit (1) #termina el programa
            elif user_answer ==  correct_answers_index[question_index]:
                print("¡Correcto!")
                break #es la sentencia para salir del bucle en caso de condicion correcta
    else:
        # Si el usuario no responde correctamente después de 2 intentos,
        # se muestra la respuesta correcta
        print("Incorrecto. La respuesta correcta es:")
        print(answers[question_index][correct_answers_index[question_index]])
    # Se imprime un blanco al final de la pregunta
    print()