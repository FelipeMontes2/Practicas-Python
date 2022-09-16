#git add Proyecto.py
#git commit -m "Prueba" 
##git push origin main##
#Calcular el IMC de las personas

P = int(input( " Cuantas personas son?: "))
while P > 0:
    nombre = input("Cual es su nombre? :")
    edad = int(input("Cual es su edad en años? :"))
    altura = float(input("Cual es su altura en metros? :"))
    peso = float(input("Cual es su peso? :" ))
    IMC = peso/altura**2
    if(edad < 18):
        print("Es un menor de edad")
    else:
        print("Es mayor de edad")

    
    print("Su IMC es :" + str(IMC) )

    if IMC >=0 and IMC <= 15.99 :
        print("Esta demasiado delgado, debería de ponerse en dieta o se va a enfermar")
    elif IMC >= 16.00 and IMC <= 16.99 :
        print("Esta delgado, debería comer más")
    elif IMC >= 17.00 and IMC <= 18.49 :
        print("Solo esta un poco delgado, no hay problemas")
    elif IMC >= 18.50 and IMC <= 24.99 :
        print("Esta muy bien, Siga así :D")
    elif IMC >= 25.00 and IMC <= 29.99 :
        print("Esta un poco pasado de su peso, pero nada de que preocuparse")
    elif IMC >= 30.00 and IMC <= 34.99 :
        print("Esta pasado de su peso, quizá debería considerar una dieta")
    elif IMC >= 35.00 and IMC <= 39.99 :
        print("Tiene obesidad, debería hacer una dieta estricta")
    elif IMC >= 40.00 :
        print("Tiene obesidad morbida, vaya con un doctor inmediatamente")

    P = P - 1
