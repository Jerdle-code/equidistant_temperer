# I'm not sure if this is even licensable, but if it is, it's entirely free to use. Hope it's useful.

import fractions

def differences(ratios):
    diffs = []
    for i in range(len(ratios)-1):
        first = ratios[i]
        second = ratios[i+1]
        diffs.append(second/first)
    return sorted(set(diffs))

def fmt(out):
    for x in out:
        print(str(x))

def together(ratios):
    if len(ratios) < 2:
        raise Exception("A ratio can't be tempered together with itself!")
    else:
        return differences(ratios)

def equidistant(ratios):
    if len(ratios) < 3:
        raise Exception("Not enough ratios to be equidistant!")
    else:
        return differences(differences(ratios))



if __name__ == "__main__":
    frac = []
    try:
        while True:
            frac.append(fractions.Fraction(input("Enter the next ratio: ")))
    except:
        frac.sort()
    while True:
        try:
            op = input("Enter T to temper the ratios together or E to temper them to be equidistant: ").upper()
            match op:
                case "E":
                    fmt(equidistant(frac))
                case "T":
                    fmt(together(frac))
                case _:
                    raise ValueError
        except ValueError:
            print("Only T and E are implemented")
        else:
            break

