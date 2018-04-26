def main():
    mes=int(input("Igrese el numero del mes: "))
    if mes==2:
        print("El mes tiene 28 dias")
    else:
        if(mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12):
            print("El mes tiene 31 dias")
        else:
            print("El mes tiene 30 dias")
main()
