import math

# Problema 5: Qual fração é maior, 4/7 ou 5/8?
# Problema 6: Qual fração é menor, 3/11 ou 2/7?

def egyptian_fraction(numerator, denominator):

    print("\nA representação egípicia da fração {}/{} é: ".
          format(numerator, denominator))

    fraction_elements = []

    while numerator != 0:
        auxiliar = math.ceil(denominator / numerator)
        fraction_elements.append(auxiliar)
        numerator = auxiliar * numerator - denominator
        denominator = denominator * auxiliar

    for elem in range(len(fraction_elements)):
        if elem != len(fraction_elements) - 1:
            print(" 1/{0} +" .
                  format(fraction_elements[elem]), end=" ")
        else:
            print(" 1/{0}" .
                  format(fraction_elements[elem]), end=" ")
    print('\n')


def main():
    numerator = int(input("Insira o numerador da fração desejada: "))
    denominator = int(input("\nInsira o denominador da fração desejada: "))

    conditional = 0
    while conditional != 1:
        conditional = int(input(
            "\nA fração desejada é {}/{} ? Se sim, digite 1. Caso contrário digite 3: ".format(numerator, denominator)))
        if conditional != 1:
            numerator = int(input("Insira o numerador da fração desejada\n"))
            denominator = int(
                input("\n\nInsira o denominador da fração desejada\n"))

    egyptian_fraction(numerator, denominator)


if __name__ == '__main__':
    main()
