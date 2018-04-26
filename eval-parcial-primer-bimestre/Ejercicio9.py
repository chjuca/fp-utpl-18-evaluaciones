def main():
    print("***\tPrimer Triangulo\t***")
    ladoA1=int(input("Ingrese el valor de sus lado A: "))
    ladoB1=int(input("Ingrese el valor de sus lado B: "))
    ladoC1=int(input("Ingrese el valor de sus lado C: "))
    anguloA1=int(input("Ingrese el valor de su angulo A: "))
    anguloB1=int(input("Ingrese el valor de su angulo B: "))
    anguloC1=int(input("Ingrese el valor de su angulo C: "))
    print("***\tFin Primer Triangulo\t***")
    print("***\tSegundo Triangulo\t***")
    ladoA2=int(input("Ingrese el valor de sus lado A: "))
    ladoB2=int(input("Ingrese el valor de sus lado B: "))
    ladoC2=int(input("Ingrese el valor de sus lado C: "))
    anguloA2=int(input("Ingrese el valor de su angulo A: "))
    anguloB2=int(input("Ingrese el valor de su angulo B: "))
    anguloC2=int(input("Ingrese el valor de su angulo C: "))
    print("***\tFin Segundo Triangulo\t***")
    if(ladoA1!=ladoA2 or ladoB1!=ladoB2 or ladoC1!=ladoC2):
	    print("Los triangulos no son congruentes")
    else:
	    if(anguloA1!=anguloA2 or anguloB1!=anguloB2 or anguloC1!=anguloC2):
		    print("Los triangulos no son congruentes")
	    else:
		    print("Los triangulos son congruentes")
main()
