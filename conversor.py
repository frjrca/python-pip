def conversor (tipo_moneda, valor_dolar):
    pesos = input ("Cuantos pesos " + tipo_moneda + " tienes? ")
    pesos = float (pesos)
    dolar = pesos / valor_dolar
    dolar = round (dolar, 2)
    dolar = str (dolar)
    print ("Tienes u$ " + dolar + " dolares")
menu = """
Conversor de monedas
1 - Pesos Colombianos
2 - Pesos Argentinos
3 - Pesos Mexicanos

"""

opcion = input (menu)

if opcion == '1':
    conversor ('colombianos', 4669)
elif opcion == '2':
    conversor ('argentinos', 190)
elif opcion == '3':
    conversor('mexicanos', 18)
else:
    print ('Opcion incorrecta')

