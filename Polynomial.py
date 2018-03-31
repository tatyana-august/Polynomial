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
    @property
    def __str__(self):
        result = ""
        sign = ""
        for pow, coeff in enumerate(self.coeffs):
            if coeff:
                if self.degree > 0:
                    if coeff >0:
                        if (self.degree == pow):
                            sign = ""
                        else:
                            sign = "+"
                    else:
                        sign = "-"
                    if abs(coeff) == 1:
                        result += sign ##add coeff in string without 1
                    else:
                        result+=sign+str(abs(coeff)) ##add coeff in string

                    if(self.degree - pow==1):
                        result+="x"
                    elif (self.degree - pow==0):
                        result += ""
                    else:
                        result +="x" + (("^" + str(self.degree - pow))+" ")
                elif self.degree == 0:
                    result +=  str(coeff)
                else: ##self.degree < 0:
                    raise ValueError('Incorrect value of degree ')
        if result:
            return result.lstrip("+")
        else:
            return "0"

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
    def __radd__(self, other):
        return self + other
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
    def __rmul__(self, other):
        return self * other






