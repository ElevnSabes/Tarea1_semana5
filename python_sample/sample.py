def imprimir_resultados():
    print('Resultados hasta la fecha:')
    with open("data.txt", "r") as read_file:
        print(read_file.read())

def ingresar_comentarios():
    while True:
        point = obtener_puntuacion()
        comment = obtener_comentario()
        guardar_comentario(point, comment)
        break

def obtener_puntuacion():
    while True:
        print('Por favor, introduzca una puntuación en una escala de 1 a 5:')
        point = input()
        if point.isdecimal():
            point = int(point)
            if 1 <= point <= 5:
                return point
            else:
                print('Por favor, introduzca un valor entre el 1 y 5')
        else:
            print('Por favor, introduzca el punto de evaluación como un número')

def obtener_comentario():
    print('Introduzca sus comentarios:')
    return input()

def guardar_comentario(point, comment):
    post = f'Punto: {point}, Comentario: {comment}\n'
    with open("data.txt", 'a') as file_pc:
        file_pc.write(post)

# Función principal para ejecutar el programa
def main():
    while True:
        print("Seleccione una opción:")
        print("1. Ingresar comentarios")
        print("2. Ver resultados")
        print("3. Salir")
        opcion = input()

        if opcion == '1':
            ingresar_comentarios()
        elif opcion == '2':
            imprimir_resultados()
        elif opcion == '3':
            print("Saliendo del programa.")
            break
        else:
            print("Por favor, seleccione una opción válida.")

# Ejecutar la función principal
if __name__ == "__main__":
    main()
