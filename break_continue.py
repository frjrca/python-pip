def run():
#    for contador in range(100):
#        if contador % 2 != 0:
#            continue
#        print(contador)
#
#    for i in range(100):
#        print(i)
#        if i == 50:
#            break
# texto = input('Escribe un texto: ')
# for letra in texto:
#     if letra == 'O':
#         break
#     print(letra)
    LIMITE = 10
    contador = 1
    while contador < LIMITE:
        if contador % 2 == 0:
             print(contador)
             contador = contador + 1
        else:
             contador = contador +1
#            continue
                

if __name__ =='__main__':
        run()