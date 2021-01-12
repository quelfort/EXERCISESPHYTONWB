print ("Bonjour, Cette programme est pour calculer votre BMI")

taille = float (input ("s'il vous plait, informer votre taille:"))

poids = float (input ("s'il vous plait, informer votre poids:"))

BMI = poids/(taille**2)

print ("Votre BMI est:  ", "%.2f" %BMI)