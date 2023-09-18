#def imprimir_mensaje ():
#    print ("Mensaje especial: ")
#    print ("Estoy aprendiendo a usar funciones! ")
#
#
#imprimir_mensaje ()


def conversacion (opcion):
    print ('Hola')
    print ('Como estas')
    print ('Elegiste la opcion ' + (opcion))
    print ('Adios!')


opcion = input ('Elige una opcion 1, 2, 3: ')
if opcion == '1':
        conversacion (opcion)
elif opcion == '2':
        conversacion (opcion)
elif opcion  == '3':
        conversacion (opcion)
else: 
        print ('opcion erronea')

