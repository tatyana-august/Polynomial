##Class for a polynomial
class Polynomial (object):
    ##Constructor of class
    def __init__(self, objCoeffs):

        self.coeffs=[] ##List of Coefficiants

        if isinstance(objCoeffs, (int,float)): ##if oblCoeffs is number
            self.coeffs.append(objCoeffs)
        elif isinstance(objCoeffs, list):
            if not objCoeffs:
                self.coeffs=[0]
            else:
                for elements in objCoeffs:
                    if not isinstance(elements, (int, float)):
                        raise TypeError('Incorrect type of coefficiants', elements, objCoeffs)
                        break; ## break from for
                else:
                    self.coeffs = objCoeffs
        elif isinstance(objCoeffs, Polynomial):
            self.coeffs = objCoeffs.coeffs[:]
        else:
            raise ValueError('Incorrect value of coefficiants', objCoeffs, objCoeffs)

        self.degree = 0## Degree of Polynom

        if self.coeffs:
            self.degree = len(self.coeffs) - 1
        else:
            self.degree = 0

        if self.coeffs:
            if not (isinstance(objCoeffs, (int, float))or isinstance(objCoeffs, Polynomial)):  ##if oblCoeffs is number
                for elements in range( len(objCoeffs)):
                    if (len(self.coeffs) > 1 and self.coeffs[0] == 0):
                        self.coeffs.pop(0)
                    else:
                        break;

        if len(self.coeffs) >= 1:
            self.degree = len(self.coeffs) - 1
        else:
            self.degree =0

    ## TO STRING
    def __str__(self):
        result = ""
        sign = ""
        for pow, coeff in enumerate(self.coeffs):
            if coeff:
                if self.degree > 0:
                    if coeff >0:
                        if (pow==0):
                            sign = ""
                        else:
                            sign = "+"
                    else:
                        sign = "-"
                    if abs(coeff) == 1:
                        if (self.degree == pow):
                            result += sign+"1"
                        else:
                            result += sign ##add coeff in string without 1
                    else:
                        result+=sign+str(abs(coeff)) ##add coeff in string

                    if(self.degree - pow==1):
                        result+="x"
                    elif (self.degree - pow==0):
                        result += ""
                    else:
                        result +="x" + (("^" + str(self.degree - pow)))
                elif self.degree == 0:
                    result +=  str(coeff)
                else: ##self.degree < 0:
                    raise ValueError('Incorrect value of degree ')
        if result:
            return result.lstrip("+")
        else:
            return "0"

    ## NEGATIVE *(-1)
    def __neg__(self):
        return Polynomial([-coeff  for coeff in self.coeffs])

    ## EQUALITY ==
    def __eq__(self, values):
        if isinstance(values, Polynomial):
            return self.coeffs == values.coeffs
        elif isinstance(values, (int, float)) and self.degree == 0:
            return self.coeffs[0] == values
        elif isinstance(values, str):
            ValueError('STR!!!!!!! '+str(self))
            return str(self) == values
        else:
            return False
    # not EQUALITY !=
    def __ne__(self, values):
        return not self == values

    ## ADD
    def __add__(self, values):
        result = []
        if isinstance(values, Polynomial):
            if values.degree < self.degree :
                result = self.coeffs[:]
                for i in range(0, values.degree + 1, 1):
                    result[self.degree - values.degree + i] += values.coeffs[i]
            else:
                result = values.coeffs[:]
                for i in range(0, self.degree + 1, 1):
                    result[values.degree - self.degree + i] += self.coeffs[i]

        elif isinstance(values, (int, float)):
            if self.coeffs:  # non-empty list of polynomial coeffs
                result = self.coeffs[:]
                result[-1] += values
            else:  # zero polynomial
                result = values
        else:
            raise TypeError('Incorrect type in __add__ (or __radd__) method ', values)
        return Polynomial(result)
    def __radd__(self, values):
        return self + values

    ##MUL
    def __mul__(self, values):
        if isinstance(values, Polynomial):
            result = [0] * (self.degree + values.degree + 1)
            for selfPow, selfCoeff in enumerate(self.coeffs):
                for valuesPow, valuesCoeff in enumerate(values.coeffs):
                    result[selfPow + valuesPow] += selfCoeff * valuesCoeff
        elif isinstance(values, (int, float)):
            return Polynomial([coeff * values for coeff in self.coeffs])
        else:
            raise TypeError('Incorrect type in __mul__ (or __rmul__) method ', values)
        return Polynomial(result)
    def __rmul__(self, values):
        return self * values

    ## SUB
    def __sub__(self, values):
        if isinstance(values, (int, float, Polynomial)):
            return self.__add__(-values)
        else:
            raise TypeError('Incorrect type in __sub__ (or __rsub__) method ', values)
    def __rsub__(self, values):
        return (self.__neg__()).__add__(values)





