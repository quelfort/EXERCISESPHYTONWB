print ("ce programme va ecrire les nombres de plus haut a plus bas ")

n = input ("s'il tu plait, ecrire un integer avec trois numeros")

n0 = int (n[0])
n1 = int (n[1])
n2 = int (n[2])


mn = min (n0,n1,n2)
mx = max (n0,n1,n2)

soma = n0 + n1 + n2

md = soma - mn - mx

t1 = mx*100+md*10+mn
print(t1)
