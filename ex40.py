#Type de triangle
# == Igual
# != Diferente

print ("Bonjour, ce program va t'informer quel est le type de triangle")

l1 = float(input("S'il tu plais, informer la premiere cote:  "))
l2 = float(input("S'il tu plais, informer la deuxieme cote:  "))
l3 = float(input("S'il tu plais, informer la troisieme cote:  "))

if l1==l2==l3:
    print (" le triangle est equilateral")
elif l1==l2!=l3 or l1!=l2==l3 or l1==l3!=l2:
    print (" le triangle est isocele")
else:
    print (" le triangle est scalene")



