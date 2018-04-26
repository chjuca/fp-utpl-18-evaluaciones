def main():
    seg=int(input("Ingrese el valor en segundos: "))
    if(seg>=60):
        minu=int(seg/60)
        aux=int(seg%60)
        print(seg," segundos es igual a ",minu," minuto(s) y ",aux,"segundos")

main()
