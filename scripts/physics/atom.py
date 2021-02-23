def atom(x):
    resp = ""
    if x == 1:
        resp = "Hydrogène [H]\nZ = 1\nM(H) = 1,008g/mol\nStructure électronique :\n1s1"
    elif x == 2:
        resp = "Hélium [He]\nZ = 2\nM(He) = 4,0026g/mol\nStructure électronique :\n1s2"
    elif x == 3:
        resp = "Lithium [Li]\nZ = 3\nM(Li) = 6,94g/mol\nStructure électronique :\n1s2 2s1"
    elif x == 4:
        resp = "Béryllium [Be]\nZ = 4\nM(Be) = 9,0122g/mol\nStructure électronique :\n1s2 2s2"
    elif x == 5:
        resp = "Bore [B]\nZ = 5\nM(B) = 10,81g/mol\nStructure électronique :\n1s2 2s2 2p1"
    elif x == 6:
        resp = "Carbone [C]\nZ = 6\nM(C) = 12,011g/mol\nStructure électronique :\n1s2 2s2 2p2"
    elif x == 7:
        resp = "Azote [N]\nZ = 7\nM(N) = 14,007g/mol\nStructure électronique :\n1s2 2s2 2p3"
    elif x == 8:
        resp = "Oxygène [O]\nZ = 8\nM(O) = 15,999g/mol\nStructure électronique :\n1s2 2s2 2p4"
    elif x == 9:
        resp = "Fluor [F]\nZ = 9\nM(F) = 18,998g/mol\nStructure électronique :\n1s2 2s2 2p5"
    elif x == 10:
        resp = "Néon [Ne]\nZ = 10\nM(Ne) = 20,180g/mol\nStructure électronique :\n1s2 2s2 2p6"
    elif x == 11:
        resp = "Sodium [Na]\nZ = 11\nM(Na) = 22,990g/mol\nStructure électronique :\n1s2 2s2 2p6 3s1"
    elif x == 12:
        resp = "Magnésium [Mg]\nZ = 12\nM(Mg) = 24,305g/mol\nStructure électronique :\n1s2 2s2 2p6 3s2"
    elif x == 13:
        resp = "Aluminium [Al]\nZ = 13\nM(Al) = 26,982g/mol\nStructure électronique :\n1s2 2s2 2p6 3s2 3p1"
    elif x == 14:
        resp = "Silicium [Si]\nZ = 14\nM(Si) = 28,085g/mol\nStructure électronique :\n1s2 2s2 2p6 3s2 3p2"
    elif x == 15:
        resp = "Phosphore [P]\nZ = 15\nM(P) = 30,974g/mol\nStructure électronique :\n1s2 2s2 2p6 3s2 3p3"
    elif x == 16:
        resp = "Soufre [F]\nZ = 16\nM(F) = 32,06g/mol\nStructure électronique :\n1s2 2s2 2p6 3s2 3p4"
    elif x == 17:
        resp = "Chlore [Cl]\nZ = 17\nM(Cl) = 35,45g/mol\nStructure électronique :\n1s2 2s2 2p6 3s2 3p5"
    elif x == 18:
        resp = "Argon [Ar]\nZ = 18\nM(Ar) = 39,948g/mol\nStructure électronique :\n1s2 2s2 2p6 3s2 3p6"
    elif x == 19:
        resp = "Potassium [K]\nZ = 19\nM(K) = 39,098g/mol\nStructure électronique :\n1s2 2s2 2p6 3s2 3p6 4s1"
    elif x == 20:
        resp = "Calcium [Ca]\nZ = 20\nM(Ca) = 40,078g/mol\nStructure électronique :\n1s2 2s2 2p6 3s2 3p6 4s2"
    elif x == 21:
        resp = "Scandium [Sc]\nZ = 21\nM(Sc) = 44,956g/mol\nStructure électronique :\n1s2 2s2 2p6 3s2 3p6 4s2 3d1"
    elif x == 22:
        resp = "Titane [Ti]\nZ = 22\nM(Ti) = 47,867g/mol\nStructure électronique :\n1s2 2s2 2p6 3s2 3p6 4s2 3d2"
    elif x == 23:
        resp = "Vanadium [V]\nZ = 23\nM(V) = 50,942g/mol\nStructure électronique :\n1s2 2s2 2p6 3s2 3p6 4s2 3d3"
    elif x == 24:
        resp = "Chrome [Cr]\nZ = 24\nM(Cr) = 51,996g/mol\nStructure électronique :\n1s2 2s2 2p6 3s2 3p6 4s1 3d5"
    elif x == 25:
        resp = "Manganèse [Mn]\nZ = 25\nM(Mn) = 54,938g/mol\nStructure électronique :\n1s2 2s2 2p6 3s2 3p6 4s2 3d5"
    elif x == 26:
        resp = "Fer [Fe]\nZ = 26\nM(Fe) = 55,845g/mol\nStructure électronique :\n1s2 2s2 2p6 3s2 3p6 4s2 3d6"
    elif x == 27:
        resp = "Cobalt [Co]\nZ = 27\nM(Co) = 58,933g/mol\nStructure électronique :\n1s2 2s2 2p6 3s2 3p6 4s2 3d7"
    elif x == 28:
        resp = "Nickel [Ni]\nZ = 28\nM(Ni) = 58,693g/mol\nStructure électronique :\n1s2 2s2 2p6 3s2 3p6 4s2 3d8\nou 1s2 2s2 2p6 3s2 3p6 4s1 3d9"
    elif x == 29:
        resp = "Cuivre [Cu]\nZ = 29\nM(Cu) = 63,546g/mol\nStructure électronique :\n1s2 2s2 2p6 3s2 3p6 4s1 3d10"
    elif x == 30:
        resp = "Zinc [Zn]\nZ = 30\nM(Zn) = 65,38g/mol\nStructure électronique :\n1s2 2s2 2p6 3s2 3p6 4s2 3d10"
    elif x == 31:
        resp = "Gallium [Ga]\nZ = 31\nM(Ga) = 69,723g/mol\nStructure électronique :\n1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p1"
    elif x == 32:
        resp = "Germanium [Ge]\nZ = 32\nM(Ge) = 72,630g/mol\nStructure électronique :\n1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p2"
    elif x == 33:
        resp = "Arsenic [As]\nZ = 33\nM(As) = 74,922g/mol\nStructure électronique :\n1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p3"
    elif x == 34:
        resp = "Sélénium [Se]\nZ = 34\nM(Se) = 78,971g/mol\nStructure électronique :\n1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p4"
    elif x == 35:
        resp = "Brome [Br]\nZ = 35\nM(Br) = 79,904g/mol\nStructure électronique :\n1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p5"
    elif x == 36:
        resp = "Krypton [Kr]\nZ = 36\nM(Kr) = 83,798g/mol\nStructure électronique :\n1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6"
    else:
        resp = "aled"
    
    return resp

print(atom(int(input("atome Z = "))))