def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def checkNum():
    num = int(input("Ingrese un numero: "))
    try:
        if num < 0:
            raise ValueError("No se puede ingresar un numero negativo")
        print(divisors(num))
        print("Termino")
    except ValueError as ve:
        print(ve)
        checkNum()


def main():
    checkNum()
 
if __name__  == '__main__':
    main()

   # try:
    #     num = int(input("Ingrese un numero: "))
    #     print(divisors(num))
    #     print("Termino")
    # except ValueError:
    #     print("Debes ingresar un numero")