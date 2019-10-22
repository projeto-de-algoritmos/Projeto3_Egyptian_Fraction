import math


def egyptian_fraction(numerator, denominator):

    print("\n\nA representação egípicia da fração {}/{} é: ".
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


def main():
    numerator = int(input("Insira o numerador da fração desejada\n"))
    denominator = int(input("\n\nInsira o denominador da fração desejada\n"))

    conditional = 0
    while conditional != 1:
        conditional = int(input(
            "\n\nA fração desejada é {}/{} ? Se sim, digite 1. Caso contrário digite 3\n".format(numerator, denominator)))
        if conditional != 1:
            numerator = int(input("Insira o numerador da fração desejada\n"))
            denominator = int(
                input("\n\nInsira o denominador da fração desejada\n"))

    egyptian_fraction(numerator, denominator)


if __name__ == '__main__':
    main()
