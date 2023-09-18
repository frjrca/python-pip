import random


def run():
    numero_aleatorio = random.randint(1, 100)
    numero_usuario = int(input('Elige un numero: '))
    while numero_aleatorio != numero_usuario:
        if numero_aleatorio < numero_usuario:
            print('Elige un numero mas pequeño')
        else:
            print('Elige un numero mas grande')
        numero_usuario = int(input('Elige otro numero: '))
    print('¡Ganaste!')


if __name__ == '__main__':
    run()