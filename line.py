def line():
    A = input("Ingrese el coeficiente A: ")
    B = input("Ingrese el coeficiente B: ")
    X1 = input("Ingrese el coeficiente X1: ")
    X2 = input("Ingrese el coeficiente X2: ")
    A = float (A)
    B = float (B)
    X1 = float (X1)
    X2 = float (X2)

    print (f"El coeficiente A de su ecuación de la recta es: {A}")
    print (f"El coeficiente B de su ecuación de la recta es: {B}")
    print (f"El coeficiente X1 de su ecuación de la recta es: {X1}")
    print (f"El coeficiente X2 de su ecuación de la recta es: {X2}")

    print ("")
    print ("Para la siguiente ecuación:")
    print (f"\tY = {A}X + {B}")
    Y1 = A*X1 + B
    Y2 = A*X2 + B

    print ("")
    print ("Dados los siguientes puntos:")
    print (f"\tP1 ({X1}, {Y1})\n\tP2 ({X2}, {Y2})")
    print ("")

    distancia = (((X1-X2)**2) + ((Y1 - Y2)**2))**0.5
    print (f"La distancia entre ellos es: {distancia}")
