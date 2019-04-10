# Ejercicio 1

def dividers(number):
    dividersArr = [tentativeDivisor for tentativeDivisor in range(1,number+1) if number%tentativeDivisor==0]
    return dividersArr

print("DIVISORES DEL NUMERO HARCODEADO")
print(dividers(55))

#Ejercicio 2

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

even_numbers_in_a = [evenNumber for evenNumber in a if evenNumber%2==0]

print("Numeros pares en a")
print(even_numbers_in_a)

#Ejercicio 3

def primeNumber(number):
    if len(dividers(number))==2 or len(dividers(number))==1:
        return True
    else:
        return False

print("Es primo el numero harcodeado?")
print(primeNumber(15))

#Ejercicio 4

def fibonacci(number):
    if number==1:
        return [1]
    elif number == 2:
        return [1,1]
    else:
        fibonacciNumbers = [1,1]
        for i in range(1,number-1):
            fibonacciNumbers = fibonacciNumbers + [fibonacciNumbers[i]+fibonacciNumbers[i-1]]
        return fibonacciNumbers

print("Numeros de fibonacci")
print(fibonacci(10))

#Ejercicio 5

array_with_duplicates = [1,2,2,3,4,5,5,6,7,8,8,9]

no_duplicates = list(dict.fromkeys(array_with_duplicates))

print("Lista sin duplicados")
print(no_duplicates)

#Ejercicio 6

def inverse_order(phrase):
    phrase_list = phrase.split()
    inverse_order = [phrase_list[len(phrase_list)-1-i] for i in range(len(phrase_list))]
    return ' '.join(inverse_order)

print("Frase invertida")
print(inverse_order("Hola Nico, como estas?"))
