def main():
    ventas=int(input("Ingrese el numero de ventas del empleado: "))
    if ventas<=500:
        proc=float(360.40*5/100)
    else:
        if ventas>500 and ventas<=1000:
            proc=float(360.40*8/100)
        else:
            if ventas>1000 and ventas<=5000:
                proc=float(360.40*10/100)
            else:
                proc=float(360.40*15/100)
    print("El empleado con ventas de: ",ventas,",tendra un sueldo de: $",360.40+proc," dolares")
main()
