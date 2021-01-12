''' Dicionarios  função de relação causa e efeito devariáve-is-
 coleçao mutavel, desordenada, indexada
são descrito por {chaves} e possuem chaves e valores
Funções no dicionário são:

#funcao values() - retorna valores
#funções keys() - retorna chaves
#função items () - retorna items
#função pop () - remove o item com o nome da chave especificado

#Declarando:

#dicionario = {}
#dicionario = {chave:valor}

dicionario = {"A":"Python", "B":"Java", "C":"Android"}
print (dicionario ["B"])
Item é o B:Jave, B é a chave e Java é o valor '''

Meses = {"janvier":31,"février":29,"mars":31,"avril":30,"mai":31, "juin":30, "juillet":31, "août":31, "septembre":30, "octobre":31, "novembro":30,"décembre":31 }

mois = input ("ecrire le mois que tu veux sais conbien de jours il y a")

print( "il y a:", Meses[mois], "de jours dans", mois)