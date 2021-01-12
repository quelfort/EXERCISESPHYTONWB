import math 

print('''Bonjour, cet exercise consiste a calculer l aire du cercle et le volume de la sphere''')

raio = float (input ('informe le rayon en centimetres'))

area = math.pi*raio**2
volume = (4/3)*math.pi*raio**3

print ('le rayon du circle est :', "%.2f" % area, "cm²")


print ('le volume de la sphere est :', "%.2f" % volume, "cm³")