# Ce programme calcule l'age de le chien

agehuman = int (input("quel age a ton chien ?"))

if agehuman <= 2:
    agechien = agehuman*10.5
    print ("l'age de ton chien est", agechien)

else:
    agechien =2*10.5+(agehuman-2)*4
    print ("l'age de ton chien est", agechien)
