def es_primo(Numero):
    if Numero == 1:
        return False
    else:
        contador = 0
        for i in range (1, Numero + 1):
            if i == 1 or i == Numero:
                continue
            if Numero % i == 0:
                contador = +1
        if contador == 0:
            return True
        else:
            return False


def run():
    Numero = int(input('Digite un Nuemro: '))
    if es_primo(Numero):
        print('Es primo')
    else:
        print('No es primo')
    

if __name__ == '__main__':
    run()