cost = float (input ("Bonjour, S'il vous plait,mettez le prix de votre déjeuner"))

tip = cost*0.18
tax = 0.25*cost

print ("Vos allez payer por le tip le combien de " "%.2f" % tip, "$" )
print ("Vos allez payer por le tax le combien de " "%.2f" % tax, "$" )

print ("Le prix total est : " "%.2f" % (tip + cost + tax), "$" )