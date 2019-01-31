

class Fraction(object):
    def __init__(self,num,denom):
        self.num=num
        self.denom=denom
    def addition(self,other):
        finalx=other.num*self.denom+other.denom*self.num
        finaly=self.denom*other.denom
        return finalx/finaly
    def substraction(self,other):
        finalx=other.num*self.denom-other.denom*self.num
        finaly=self.denom*other.denom
        return finalx/finaly
    def multiplication(self,other):
        finaly=self.denom*other.denom
        finalx=self.num*other.num
        return finalx/finaly
    def division(self,other):
        finaly=self.num*other.denom
        finalx=self.denom*other.num
        return finalx/finaly
    def inverse(self):
        finaly=self.num
        finalx=self.denom
        return finalx/finaly
exm=Fraction(4,7)
exm2=Fraction(3,6)
print(exm.addition(exm2))
print(exm.substraction(exm2))
print(exm.multiplication(exm2))
print(exm.division(exm2))
print(exm.inverse())
