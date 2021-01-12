import math
print ("Ce programme vous donnera l aire d um triangle")

s1 = float (input("Ecrire le premier cote du  en cm:  "))

s2 = float (input("Ecrire le deuxieme cote du triangle en cm: "))

s3 = float (input("Ecrire le troisieme cote du triangleen cm:  "))

s=s1+s2+s3

area = math.sqrt (s*(s-s1)*(s-s2)*(s-s3))

print ("%.2f" % area, "cm²")