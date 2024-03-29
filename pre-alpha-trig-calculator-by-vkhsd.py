﻿import math
import parser

print("Welcome to Trig Function Calculator by VKHSD")
print("Would you like to solve for all side lengths of the triangle?")
print("Y/N")

if input() == "y":
    print(f"Initiate Pythagorean Theorem")
    while True:
        missingside = input("Which side is missing? A/B/C ")

        if missingside == "a":
            B = float(input("Input side 'B' "))
            C = float(input("Input side 'C' "))
            A = C ** 2 - B ** 2
            if B >= C:
                print(f"B CANNOT BE GREATER THAN OR EQUAL TO C")
                continue
            print("Side A = ", round(math.sqrt(A), 3))
            break
        elif missingside == "b":
            A = float(input("Input side 'A' "))
            C = float(input("Input side 'C' "))
            B = C ** 2 - A ** 2
            if B >= C:
                print(f"A CANNOT BE GREATER THAN OR EQUAL TO C")
                continue
            print("Side B = ", round(math.sqrt(B), 3))
            break
        elif missingside == "c":
            A = float(input("Input side 'A' "))
            B = float(input("Input side 'B' "))
            C = A ** 2 + B ** 2
            print("Side C = ", round(math.sqrt(C), 3))
            break
        else:
            print(f"{missingside.upper()} is not a valid input!")
while True:

    print("Please select a department: RightRatios, Sine (ratio), SineL (laws), Cosine, Coterminal (cote), "
          "limit solver (lim) or choose to convert with 'convert' ")
    departments = 'rightratios', 'sine', 'sinel', 'cosine', 'convert', 'coterminal', 'cote', 'quit', 'lim'
    func1 = input()

    if func1 == "rightratios":
        print("Initiate Right Triangle Ratios")

        sidea = float(input("Side 'A' length? "))
        sideb = float(input("Side 'B' length? "))
        sqrtc = sidea ** 2 + sideb ** 2
        sidec = math.sqrt(sqrtc)

        sina = sidea / sidec
        cosa = sideb / sidec
        tana = sidea / sideb
        print("Side 'C' length is: ", sidec)

        sinanglea = ((math.asin(sina) * 180) / math.pi)
        cosanglea = ((math.acos(cosa) * 180) / math.pi)
        tananglea = ((math.atan(tana) * 180) / math.pi)

        anglea = (sinanglea + cosanglea + tananglea) / 3
        anglec = 90
        angleb = anglec - anglea

        print("The angle of α is:", round(anglea, 0), "°", "or", round(anglea, 3), "°")
        print("The angle of β is:", round(angleb, 0), "°", "or", round(angleb, 3), "°")
        print("The angle of γ is a '∟'")

        input(f"Enter to retry... ")

    if func1 == "sine":
        print(f"Initiate Sine Ratio")
        while True:
            print(f"Which two factors are known and what is unknown?")
            print(f"Choices are A/B/C (side lengths) ALPHA/BETA/GAMMA (angles)")
            factor1 = str(input("Known 1 "))
            factor2 = str(input("Known 2 "))
            unknown1 = str(input("Solve for "))

            if factor1 == 'a' and factor2 == 'alpha' and unknown1 == 'c':
                sidea = float(input(f"Length of A: "))
                anglea = float(input(f"Angle of α: "))
                missingside = (float(sidea)) / (math.sin(float((anglea * math.pi) / (180))))
                print(f"Length of C = {round(missingside, 2)}")
                input(f"Enter to retry... ")
                break
            elif factor1 == 'b' and factor2 == 'alpha' and unknown1 == 'c':
                sidea = float(input(f"Length of B: "))
                anglea = float(input(f"Angle of α: "))
                missingside = (float(sidea)) / (math.sin(float((anglea * math.pi) / (180))))
                print(f"Length of C = {round(missingside, 2)}")
                input(f"Enter to retry... ")
                break
            elif factor1 == 'a' and factor2 == 'alpha' and unknown1 == 'b':
                sidea = float(input(f"Length of A: "))
                anglea = float(input(f"Angle of α: "))
                missingside = (float(sidea)) / (math.sin(float((anglea * math.pi) / (180))))
                print(f"Length of B = {round(missingside, 2)}")
                input(f"Enter to retry... ")
                break
            elif factor1 == 'b' and factor2 == 'beta' and unknown1 == 'a':
                sideb = float(input(f"Length of B: "))
                angleb = float(input(f"Angle of β: "))
                missingside = (float(sideb)) / (math.sin(float((angleb * math.pi) / (180))))
                print(f"Length of A = {round(missingside, 2)}")
                input(f"Enter to retry... ")
                break
            else:
                print(
                    f"This problem is impossible: Knowns = {factor1.upper()}, {factor2.upper()}; Unknowns = {unknown1.capitalize()}")

    if func1 == "sinel":
        print(f"Initiate Law of Sines")
        while True:
            print(f"What is known? Start with side lengths first and go in alphabetical order! ")
            print(f"Choices are A/B/C (side lengths) ALPHA/BETA/GAMMA (angles)")
            factor1 = str(input("Known 1 "))
            factor2 = str(input("Known 2 "))
            factor3 = str(input("Known 3 "))

            if factor1 == 'b' and factor2 == 'alpha' and factor3 == 'beta':
                sideb = float(input(f"Length of B: "))
                anglea = float(input(f"Angle of α: "))
                angleb = float(input(f"Angle of β: "))
                missingf = sideb * ((math.sin((anglea * math.pi) / 180)) / (math.sin((angleb * math.pi) / 180)))
                print(f"Length of A = {round(missingf, 2)}")
                input(f"Enter to retry... ")
                break
            elif factor1 == 'b' and factor2 == 'beta' and factor3 == 'gamma':
                sideb = float(input(f"Length of B: "))
                angleb = float(input(f"Angle of β: "))
                anglec = float(input(f"Angle of γ: "))
                missingf = sideb * ((math.sin((anglec * math.pi) / 180)) / (math.sin((angleb * math.pi) / 180)))
                print(f"Length of C = {round(missingf, 2)}")
                input(f"Enter to retry... ")
                break
            elif factor1 == 'a' and factor2 == 'alpha' and factor3 == 'beta':
                sidea = float(input(f"Length of A: "))
                anglea = float(input(f"Angle of α: "))
                angleb = float(input(f"Angle of β: "))
                missingf = sidea * ((math.sin((angleb * math.pi) / 180)) / (math.sin((anglea * math.pi) / 180)))
                print(f"Length of B = {round(missingf, 2)}")
                input(f"Enter to retry... ")
                break
            elif factor1 == 'a' and factor2 == 'b' and factor3 == 'beta':
                sidea = float(input(f"Length of A: "))
                sideb = float(input(f"Length of B: "))
                angleb = float(input(f"Length of β: "))
                missingf = sidea * (math.sin((angleb * math.pi) / 180) / sideb)
                print(f"Angle of α = {round((math.asin(missingf) * 180) / math.pi, 2)}")
                input(f"Enter to retry... ")
                break
            elif factor1 == 'a' and factor2 == 'c' and factor3 == 'gamma':
                sidea = float(input(f"Length of A: "))
                sidec = float(input(f"Length of C: "))
                anglec = float(input(f"Angle of γ: "))
                missingf = sidea * (math.sin((anglec * math.pi) / 180) / sidec)
                print(f"Angle of α = {round((math.asin(missingf) * 180) / math.pi, 2)}")
                input(f"Enter to retry... ")
                break
            elif factor1 == 'b' and factor2 == 'c' and factor3 == 'beta':
                sideb = float(input(f"Length of B: "))
                sidec = float(input(f"Length of C: "))
                angleb = float(input(f"Angle of β: "))
                missingf = sidec * (math.sin((angleb * math.pi) / 180) / sideb)
                print(f"Angle of γ = {round((math.asin(missingf) * 180) / math.pi, 2)}")
                input(f"Enter to retry... ")
                break
            else:
                print(f"This problem is impossible: Knowns = {factor1.upper()}, {factor2.upper()}, {factor3.upper()}")

    if func1 == "cosine":
        print(f"Initiate Law of Cosines")
        while True:
            print(f"Which two sides are known?")
            print(f"Choices are A/B/C (side lengths) ALPHA/BETA/GAMMA (angles)")
            factor1 = str(input("Known 1: "))
            factor2 = str(input("Known 2: "))
            factor3 = str(input("Known 3: "))

            if factor1 == 'a' and factor2 == 'b' and factor3 == 'gamma':
                sidea = float(input(f"Length of A: "))
                sideb = float(input(f"Length of B: "))
                anglec = float(input(f"Angle of γ: "))
                missingside = sidea ** 2 + sideb ** 2 - 2 * sidea * sideb * math.cos((anglec * math.pi) / 180)
                print(f"Length of C = {round(math.sqrt(missingside), 2)}")
                input(f"Enter to retry... ")
                break
            elif factor1 == 'a' and factor2 == 'b' and factor3 == 'c':
                sidea = float(input(f"Length of A: "))
                sideb = float(input(f"Length of B: "))
                sidec = float(input(f"Length of C: "))
                missingsidea = float(((sideb ** 2 + sidec ** 2 - sidea ** 2) / (2 * sideb * sidec)))
                missingsideb = float(((sidec ** 2 + sidea ** 2 - sideb ** 2) / (2 * sidec * sidea)))
                missingsidec = float(((sidea ** 2 + sideb ** 2 - sidec ** 2) / (2 * sidea * sideb)))
                print(f"Angle of α = {round(float(math.acos(missingsidea) * 180) / math.pi, 2)}")
                print(f"Angle of β = {round(float(math.acos(missingsideb) * 180) / math.pi, 2)}")
                print(f"Angle of γ = {round(float(math.acos(missingsidec) * 180) / math.pi, 2)}")
                input(f"Enter to retry... ")
                break
            elif factor1 == 'b' and factor2 == 'c' and factor3 == 'alpha':
                sideb = float(input(f"Length of B: "))
                sidec = float(input(f"Length of C: "))
                anglea = float(input(f"Angle of α: "))
                missingside = sideb ** 2 + sidec ** 2 - 2 * sideb * sidec * math.cos((anglea * math.pi) / 180)
                print(f"Length of C = {round(math.sqrt(missingside), 2)}")
                input(f"Enter to retry... ")
                break
            elif factor1 == 'a' and factor2 == 'c' and factor3 == 'beta':
                sidea = float(input(f"Length of A: "))
                sidec = float(input(f"Length of C: "))
                angleb = float(input(f"Angle of β: "))
                missingside = sidea ** 2 + sidec ** 2 - 2 * sidea * sidec * math.cos((angleb * math.pi) / 180)
                print(f"Length of C = {round(math.sqrt(missingside), 2)}")
                input(f"Enter to retry... ")
                break
            else:
                print(f"This problem is impossible: Knowns = {factor1.upper()}, {factor2.upper()}, {factor3.upper()}")

    if func1 == "cote":
        deg = int(input("input degree "))
        print(f"{deg + 360} is the positive coterminal angle")
        print(f"{deg - 360} is the negative coterminal angle")
        deg2 = (deg % 360)
        if deg2 <= int(90):
            print(f'{deg2} is the reference angle')
        elif int(180) >= deg2 > int(90):
            print(f'{180 - deg2} is the reference angle')
        elif 270 >= deg2 > int(180):
            print(f'{deg2 - 180} is the reference angle')
        elif deg2 > int(270):
            print(f'{360-deg2} is the reference angle')

    if func1 == "convert":
        print(f'CHOOSE A CONVERSION: deg, rad')
        conversion = input()
        if conversion == "deg":
            print(f'Input Radian Integer ')
            rad = float(input())
            print(f'{round(rad * (180 / math.pi), 3)}')
        elif conversion == "rad":
            print(f'Input Degree Integer ')
            deg = float(input())
            print(f'{round((deg * math.pi) / 180)}')

    if func1 == "lim":
        print(f"NOTATE ^ AS ** AND SHOW ALL MULTIPLICATION SPOTS SUCH AS (X)Y AS (X)*Y")
        try:
            import math
            formula = input()
            code = parser.expr(formula).compile()
            x = float(input("Find limit around? "))
            xsave = x
            try:
                import math
                print(f"lim   f(x) = {eval(code)}")
                print(f"x→{int(x)}")
                x = xsave - 0.1
                print(f"{x}, {eval(code)}")
                xa = eval(code)
                x = xsave - 0.01
                print(f"{x}, {eval(code)}")
                xb = eval(code)
                x = xsave - 0.001
                print(f"{x}, {eval(code)}")
                try:
                    import math
                    xc = eval(code)
                    x = xsave
                    print(f"{x}, {eval(code)}")
                except ZeroDivisionError:
                    print(f"{int(x)}, Undefined")
                import math
                x = xsave + 0.001
                print(f"{x}, {eval(code)}")
                xe = eval(code)
                x = xsave + 0.01
                print(f"{x}, {eval(code)}")
                xf = eval(code)
                x = xsave + 0.1
                print(f"{x}, {eval(code)}")
                xg = eval(code)
                if xa > xb > xc and xe > xf > xg:
                  print(f"lim   f(x) = -inf")
                  print(f"x→{int(x)}-")
                  print(f"lim   f(x) = inf")
                  print(f"x→{int(x)}+")

            except ZeroDivisionError:
                print(f"lim   f(x) = Undefined")
                print(f"x→{int(x)}")
                import math
                x = xsave - 0.1
                print(f"{x}, {eval(code)}")
                xa = eval(code)
                x = xsave - 0.01
                print(f"{x}, {eval(code)}")
                xb = eval(code)
                x = xsave - 0.001
                print(f"{x}, {eval(code)}")
                xc = eval(code)
                try:
                    import math
                    x = xsave
                    print(f"{x}, {eval(code)}")
                except ZeroDivisionError:
                    print(f"{int(x)}, Undefined")
                import math
                x = xsave + 0.001
                print(f"{x}, {eval(code)}")
                xe = eval(code)
                x = xsave + 0.01
                print(f"{x}, {eval(code)}")
                xf = eval(code)
                x = xsave + 0.1
                print(f"{x}, {eval(code)}")
                xg = eval(code)
                if xa > xb > xc and xe > xf > xg:
                  print(f"lim   f(x) = -inf")
                  print(f"x→{int(x)}-")
                  print(f"lim   f(x) = inf")
                  print(f"x→{int(x)}+")
                if xa > xb > xc and xe < xf < xg:
                  print(f"lim   f(x) = -inf")
                  print(f"x→{int(x)}-")
                  print(f"lim   f(x) = -inf")
                  print(f"x→{int(x)}+")
                if xa < xb < xc and xe > xf > xg:
                  print(f"lim   f(x) = inf")
                  print(f"x→{int(x)}-")
                  print(f"lim   f(x) = inf")
                  print(f"x→{int(x)}+")
        except SyntaxError:
            print("Typed wrong")

    if func1 not in departments:
        print(f"{func1} is either mistyped or not a feature yet. thank you for using trigonometry calculator by VKHSD")
        input(f"Enter to retry... ")

    if func1 == 'quit':
        quit()
