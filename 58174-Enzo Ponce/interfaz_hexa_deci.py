import os
from decimal_hexa import decimal_hexadecimal
def main():
    
    print("Bienvenido al convertidor de numeros")
    print("Ingrese un numero decimal para convertirlo en hexadecimal")
    decimal = input(':')
    res = check(decimal)
  
def check(decimal):
    if not decimal:
        return 'ERROR'
    if decimal.isdigit() == False :
        return 'ERROR'
    else:
        resp = decimal_hexadecimal(int(decimal))
    return resp

main()















    

    
