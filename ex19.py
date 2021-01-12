import math

print ('''Cette programme calcule la velocite finale d un object lorsqu'il touche le sol''')

altitude = float(input ("Informe la altitude:  "))

vi = float (input ("Informe la velocite initial:  "))


acceleration = 9.8


vf= math.sqrt(vi**2 + 2*altitude*acceleration)

print (" La velocite finale est: ", "%.2f" % vf, "m/s")