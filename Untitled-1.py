Curso = input("ingrese nombre del curso: ")
Num_alumnos =int(input("ingrese número de alumnos: "))
Nombre_Alumnos= []
z = 1
for i in range (Num_alumnos):
    N_A = input(f"ingrese nombre de alumnos {z}: ")
    Nombre_Alumnos.append(N_A)
    z += 1

Numer_evaluaciones=int(input("ingrese el número de solemnes que hará: "))

Pondera_Solemne=[
]

z = 1
for i in range(Numer_evaluaciones):
    print(f'evaluación {z}')
    N_V= input("ingrese la ponderación de cada evaluación: ")
    Pondera_Solemne.append(N_V)
    z += 1

Asistencia=[]

z = 0
for i in range(Num_alumnos):
    print(f'para el alumno {Nombre_Alumnos[(z)]}')
    Asist=input("ingrese la asistencia general de cada alumno: ")
    Asistencia.append(Asist)
    z += 1

Notas_solemne1=[]

z = 0
for i in range(Numer_evaluaciones):
    print(f'para el alumno {Nombre_Alumnos[(z)]}')
    S_1=input("ingrese notas de solemne 1: ")
    Notas_solemne1.append(S_1)
    z += 1

Notas_solemne2=[]
z = 0
for i in range(Numer_evaluaciones):
    print(f'para el alumno {Nombre_Alumnos[(z)]}')
    S_2=input("ingrese notas de solemne 2: ")
    Notas_solemne2.append(S_2)
    z += 1

Notas_solemne3=[]
z = 0
for i in range(Numer_evaluaciones):
    print(f'para el alumno {Nombre_Alumnos[(z)]}')
    S_3=input("ingrese notas de solemne 3: ")
    Notas_solemne3.append(S_3)
    z += 1


print(Curso)

while True:
    Saludo = int(input("""
       Bienvenido al Menu de la escuela, Saludos
       (1) Menu de Ponderaciones 
       () Menu de Calificaciones
            (2)Notas solemne 1
            (3)Notas solemne 2
            (4)Notas solemne 3
       (5)Menu de asistencia
       (6)Calculadora de promedio
       """))

    if Saludo == 1:
            print("Ponderacion de cada evaluacion",Pondera_Solemne)


    elif Saludo == 2:
        print(Notas_solemne1)

    elif Saludo == 3:
        print(Notas_solemne2)

    elif Saludo == 4:
        print(Notas_solemne3)

    elif Saludo == 5:
        print(Asistencia)

    elif Saludo==6:
        J1=float(input("ingrese la primera nota"))
        p1=float(input("Ingrese el porcentaje de esta evaluacion en decimales"))
        J2=float(input("ingrese su segunda nota"))
        p2=float(input("Ingrese el porcentaje de esta evaluacion en decimales"))
        J3=float(input("ingrese su tercera nota"))
        p3=float(input("Ingrese el porcentaje de esta evaluacion en decimales"))
        Z=((J1*p1)+(J2*p2)+(J3*p3))
        print("su promedio ponderado es "+ str(Z) )
    if z >=4.5:
        print("su promedio ponderado es "+ str(z),"felicidades pasas de curso")
    elif z <=3.9:
        print("su promedio ponderado es "+ str(z),"lo lamento debes dar recuperativa")
    else:
        print("Falta rendir una evaluación")





