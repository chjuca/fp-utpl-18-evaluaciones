def main():
   a=int(input("Ingrese una calificación(0-100): "))
   b=int(input("Ingrese la siguiente calificación(0-100): "))
   c=int(input("Ingrese la siguiente calificación(0-100): "))
   d=int(input("Ingrese la siguiente calificación(0-100): "))
   prom=(a+b+c+d)/4
   if(prom>=90 and prom<=100):
       print("El estudiante con el promedio de calificaciones",prom,",tiene una puntuación de A")
   else:
        if(prom>=80 and prom<90):
            print("El estudiante con el promedio de calificaciones",prom,",tiene una puntuación de B")
        else:
            if(prom>=70 and prom<80):
                print("El estudiante con el promedio de calificaciones",prom,",tiene una puntuación de C")
            else:
                print("El estudiante con el promedio de calificaciones",prom,",tiene una puntuación de D")
           
       
main()
