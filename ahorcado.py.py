import random


palabras = ["casa","perro","gato","avion","barco","basurero","elefante"]


palabra_secreta = random.choice(palabras)


vidas = 6
letras_adivinadas = []
palabra_oculta = ["_"] * len(palabra_secreta)


def mostrar_palabra():
    print("Palabra: ", " ".join(palabra_oculta))


def ha_ganado():
    return "_" not in palabra_oculta


while vidas > 0 and not ha_ganado():
    mostrar_palabra()
    letra = input("Adivina una letra: ").lower()

    
    if letra in letras_adivinadas:
        print("Ya intentaste con esa letra. Prueba otra.")
        continue

    letras_adivinadas.append(letra)

    
    if letra in palabra_secreta:
        print("¡Bien! La letra está en la palabra.")
        for i in range(len(palabra_secreta)):
            if palabra_secreta[i] == letra:
                palabra_oculta[i] = letra
    else:
        vidas -= 1
        print(f"Incorrecto. Te quedan {vidas} vidas.")


if ha_ganado():
    print(f"\n ¡Ganaste! : {palabra_secreta}")
else:
    print(f"\n Perdiste. : {palabra_secreta}")