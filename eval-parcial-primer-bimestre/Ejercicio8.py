def main():
   x=input("Ingrese la primera letra: ")
   y=input("Ingrese otra letra: ")
   z=input("Ingrese otra letra: ")
   if(x<y):
       may=x
   else:
        if(y<z):
            may=y
        else:
            may=z
   print("La primera letra que aparece en el abecedario es ",may)

main()
