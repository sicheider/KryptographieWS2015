#uploaded by:
#Simon Heider
#2069102

def binaryRepresantation(x):
    """returns binary list of x"""
    result = []
    if (x == 0):
        result = [0]
    else:
        while (x > 0):
            temp1 = x // 2
            temp2 = x - 2 * temp1
            result = [temp2] + result
            x = temp1
    return result

def getDecimal(x):
    """returns decimal of binary list"""
    result = 0
    for i in range(len(x) - 1, -1, -1):
        if x[len(x) - 1 - i] == 1:
            result += 2**i 
    return result

def polynomialModulo(x, y):
    """returns polynomial x modulo polynomial y"""
    while len(binaryRepresantation(x)) > len(binaryRepresantation(y)):
        tempPolynomial = binaryRepresantation(y) 
        for i in range(0, len(binaryRepresantation(x)) - len(binaryRepresantation(y))):
            tempPolynomial += [0]
        x = x ^ getDecimal(tempPolynomial)
    result = x ^ y
    return result

def polynomialMult(x, y):
    """returns polynomial x * polynomial y"""
    binX = binaryRepresantation(x)
    binY = binaryRepresantation(y)
    listPolynomial = []
    for i in range(len(binX) - 1, -1, -1):
        indicesPolynomial = []
        polynomial = []
        for j in range(len(binY) - 1, -1, -1):
            if binX[len(binX) - i - 1] == 1 and binY[len(binY) - j - 1] == 1:
                indicesPolynomial += [i + j]
        if len(indicesPolynomial) > 0:
            k = 0 
            for j in range(indicesPolynomial[0], -1, -1):
                if j == indicesPolynomial[k]:
                    polynomial += [1]
                    if k < len(indicesPolynomial) - 1:
                        k += 1
                else:
                    polynomial += [0]
            listPolynomial += [getDecimal(polynomial)]
    result = listPolynomial[0]
    for i in range(1, len(listPolynomial)):
        result = result ^ listPolynomial[i] 
    return result

def f256Add(x, y):
    result = x ^ y
    return result

def f256Mult(x, y):
    x = polynomialMult(x, y)
    result = polynomialModulo(x, 283)
    return result
