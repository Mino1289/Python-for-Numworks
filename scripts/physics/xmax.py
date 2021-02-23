nbr_react = int(input("Nombre de réactif(s) : "))

n1 = float(input("\nQuantité du 1er réactif : "))
co1 = int(input("Coeficient stoechiométrique\ndu 1er réactif : "))

if nbr_react >= 2:
    n2 = float(input("\nQuantité du 2ème réactif : "))
    co2 = int(input("Coeficient stoechiométrique\ndu 2ème réactif : "))
    if nbr_react == 3:
        n3 = float(input("\nQuantité du 3ème réactif : "))
        co3 = int(input("Coeficient stoechiométrique\ndu 3ème réactif : "))

xmax_1 = n1/co1
if nbr_react >= 2:
    xmax_2 = n2/co2
    if nbr_react == 3:
        xmax_3 = n3/co3

if nbr_react == 1:
    print("\nLe réactif limitant est \nle 1er (il est le seul) avec xmax = " + str(xmax_1))

if nbr_react == 2:
    if xmax_1 == xmax_2:
        print("\nLa réaction est totale\nxmax = " + str(xmax_2))
    elif xmax_2 > xmax_1:
        print("\nLe réactif limitant est\nle 1er avec xmax = " + str(xmax_1) + " mol\
            \ndonc xf_2 = " + str(n2-xmax_1) + " mol")
    else:
        print("\nLe réactif limitant est\nle 2nd avec xmax = " + str(xmax_2) + " mol\
            \ndonc xf_1 = " + str(n1-xmax_2) + "mol")

if nbr_react == 3:
    if xmax_1 == xmax_2 == xmax_3:
        print("\nLa réaction est totale\nxmax = " + str(xmax_2))
    elif xmax_2 > xmax_1 and xmax_3 > xmax_1:
        print("\nLe réactif limitant est\nle 1er avec xmax = " + str(xmax_1) + " mol\
            \ndonc xf_2 = " + str(n2-xmax_1) + " mol\net xf_3 = " + str(n3-xmax_1) + " mol")
    elif xmax_1 > xmax_2 and xmax_3 > xmax_2:
        print("\nLe réactif limitant est\nle 2ème avec xmax = " + str(xmax_2) + " mol\
            \ndonc xf_1 = " + str(n1-xmax_2) + " mol\net xf_3 = " + str(n3-xmax_2) + " mol")
    else:
        print("\nLe réactif limitant est\nle 3ème avec xmax = " + str(xmax_3) + " mol\
            \ndonc xf_1 = " + str(n1-xmax_3) + " mol\net xf_2 = " + str(n2-xmax_3) + " mol")
