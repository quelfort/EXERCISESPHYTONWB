
'''if  condiçãoo :
    bloco verdadeiro
elif condição:
    bloco verdadeiro
else:
    bloco falso

'''

#Évaluation du personnel
ev = float( input("Informer la evaluation professionnelle"))

if ev == 0.0:
    print ("Performance inacceptable")
elif ev==0.4:
    print ("Performance acceptable")
    raises = 2400*0.4
    #print ('le rayon du circle est :', "%.2f" % area, "cm²")
    print ("Il va recoi:  ", "%.2f" %raises)
elif ev==0.6:
    print ("Performance meritoire")
    raises = 2400*0.6
    print ("Il va recoi:  ", "%.2f" %raises)
else:
    print ("la valeur n'existe pas")