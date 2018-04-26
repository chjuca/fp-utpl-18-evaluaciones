def main():
    a=int(input("Ingrese valor para la variabe A: "))
    b=int(input("Ingrese valor para la variabe B: "))
    d=int(input("Ingrese valor para la variabe D: "))
    e=int(input("Ingrese valor para la variabe E: "))
    c=a+b
    f=d+e
    x=((c*e)-(b*f))/((a*e)-(b*d))
    y=((c*e)-(b*f))/((a*e)-(b*d))
    print("El valor de x es igual a: ",x,", mientras que el valor de Y es: ",y)
main()
