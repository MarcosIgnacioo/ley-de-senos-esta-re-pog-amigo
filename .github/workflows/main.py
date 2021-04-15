import math
lado = float(input('el primer lado '))
angulo = float(input('el angulo '))
dato2 = float(input('el dato extra puede ser lado u angulo '))

pregunta = input('quieres saber angulo o lado ')

if pregunta == 'a':
    br = lado/math.sin(angulo)
    casi_final = math.sin(dato2)/br
    print(math.asin(casi_final))

elif pregunta == 'l':
    br = lado/math.sin(angulo)
    casi_final = math.sin(dato2)*br
    print(casi_final)


