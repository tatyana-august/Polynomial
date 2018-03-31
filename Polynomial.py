##Class for a polynomial
class Polynomial (object):
    ##Constructor of class
    def __init__(self, objCoeffs):

        self.coeffs=[] ##List of Coefficiants

        if isinstance(objCoeffs, (int,float)): ##if oblCoeffs is vector of number
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

