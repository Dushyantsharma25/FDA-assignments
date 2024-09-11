def inputpoly2():
    y = int(input("Enter number of terms in polynomial: "))
    p = []
    for _ in range(y):
        b = int(input("Enter the exponent of term: "))
        a = int(input("Enter the coefficient of term: "))
        p.append([b, a])
    p.sort(reverse=True)
    return p

def printpoly2(p):
    result = []
    for i in range(len(p)):
        coef, exp = p[i][1], p[i][0]
        if coef != 0:
            if exp == 0:
                result.append(f"{coef}")
            elif exp == 1:
                result.append(f"{coef}x")
            else:
                result.append(f"{coef}x^{exp}")
    print(" + ".join(result).replace(" + -", " - "))

def addpoly2(p1, p2):
    result = []
    i, j = 0, 0
    while i < len(p1) and j < len(p2):
        if p1[i][0] == p2[j][0]:
            result.append([p1[i][0], p1[i][1] + p2[j][1]])
            i += 1
            j += 1
        elif p1[i][0] > p2[j][0]:
            result.append(p1[i])
            i += 1
        else:
            result.append(p2[j])
            j += 1
    while i < len(p1):
        result.append(p1[i])
        i += 1
    while j < len(p2):
        result.append(p2[j])
        j += 1
    return result

def multipoly2(p1, p2):
    result = []
    for exp1, coef1 in p1:
        for exp2, coef2 in p2:
            new_exp = exp1 + exp2
            new_coef = coef1 * coef2
            found = False
            for term in result:
                if term[0] == new_exp:
                    term[1] += new_coef
                    found = True
                    break
            if not found:
                result.append([new_exp, new_coef])
    result.sort(reverse=True, key=lambda term: term[0])
    return result

def evaluatepoly2(p, x):
    result = 0
    for exp, coef in p:
        result += coef * (x ** exp)
    return result

p1 = inputpoly2()
p2 = inputpoly2()

print("Polynomial 1:")
printpoly2(p1)

print("Polynomial 2:")
printpoly2(p2)

print("Addition of polynomials:")
printpoly2(addpoly2(p1, p2))

print("Multiplication of polynomials:")
printpoly2(multipoly2(p1, p2))

x = float(input("Enter the value of x to evaluate the polynomials: "))
print("Evaluation of Polynomial 1:", evaluatepoly2(p1, x))
print("Evaluation of Polynomial 2:", evaluatepoly2(p2, x))
