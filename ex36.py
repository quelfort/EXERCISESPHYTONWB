#voyelle ou consonne
# Ce program lire une lettre et parle si est une voyelle ou une consonne
''' If and else

if  condiçãoo :
    bloco verdadeiro
else:
    bloco falso'''


lettre = input ("Quelle est la lettre que vous voulez savoir?  ")

if lettre=="a" or lettre=="e" or lettre=="i" or lettre=="o" or lettre=="u":
    print ("La lettre", lettre, "est une voyelle")
else:
    print ("La lettre", lettre, "est une consonne")
