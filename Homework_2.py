class Interval:
    
    def __init__( self, left_endpoint, right_endpoint= None ) :
        if right_endpoint==None:
            right_endpoint = left_endpoint
        else:
            pass
        if isinstance( left_endpoint, int) and isinstance( right_endpoint, int) :
            self.left_endpoint = left_endpoint
            self.right_endpoint = right_endpoint
            
        elif isinstance( left_endpoint, float) and isinstance( right_endpoint, int) :
            self.left_endpoint = left_endpoint
            self.right_endpoint = right_endpoint
        
        elif isinstance( left_endpoint, int) and isinstance( right_endpoint, float) :
            self.left_endpoint = left_endpoint
            self.right_endpoint = right_endpoint
            
        elif isinstance( left_endpoint, float) and isinstance( right_endpoint, float) :
            self.left_endpoint = left_endpoint
            self.right_endpoint = right_endpoint
        else:
            raise TypeError("left and right intervals must be real numbers")
        
        
    def __add__( self, other):
        l1, r1 = self.left_endpoint, self.right_endpoint
        if isinstance( other, Interval) :
            l2, r2 = other.left_endpoint, other.right_endpoint
        elif isinstance( other, float) or isinstance( other, int):
            l2, r2 = other, other
        else: 
            raise TypeError("Must be Intervals")
        return Interval( l1 + l2, r1 + r2)
    
    def __sub__( self, other):
        l1, r1 = self.left_endpoint, self.right_endpoint
        if isinstance( other, Interval) :
            l2, r2 = other.left_endpoint, other.right_endpoint
        elif isinstance( other, float) or isinstance( other, int):
            l2, r2 = other, other
        else: 
            raise TypeError("Must be Intervals")
        return Interval( l1 - r2, r1 - l2)

    def __mul__( self, other):
        l1, r1 = self.left_endpoint, self.right_endpoint
        if isinstance( other, Interval) :
            l2, r2 = other.left_endpoint, other.right_endpoint
        elif isinstance( other, float) or isinstance( other, int):
            l2, r2 = other, other
        else: 
            raise TypeError("Must be Intervals")
        L=[l1*l2, l1*r2, r1*l2, r1*r2]
        return Interval( min(L), max(L))  
     
    def __truediv__( self, other):
        l1, r1 = self.left_endpoint, self.right_endpoint
        if isinstance( other, Interval) :
            if other.left_endpoint == 0 or other.right_endpoint == 0:
                raise ZeroDivisionError("Neither endpoint can be 0")
            else:
                l2, r2 = other.left_endpoint, other.right_endpoint
        elif isinstance( other, float) or isinstance( other, int):
            if other == 0:
                raise ZeroDivisionError("Cannot be zero")
            else:
                l2, r2 = other, other
        else: 
            raise TypeError("Must be Intervals")
        L=[l1/l2, l1/r2, r1/l2, r1/r2]
        return Interval( min(L), max(L))
     
    def __repr__(self):
         return f"({self.left_endpoint}, {self.right_endpoint})"
    
    def __contains__( self, number):
         if not isinstance( number, float) and not isinstance( number, int):
             raise TypeError("Must give us a real number")
         else:
             return number >= self.left_endpoint and number <= self.right_endpoint
    
    def __radd__(self, other):
        return self + other
    
    def __rsub__(self, other):
        return self - other
    
    def __rmul__(self, other):
        return self*other
    
    def __pow__(self, other):
        interval = self
        if self.left_endpoint >= 0:
            return Interval(self.left_endpoint**other, self.right_endpoint**other)
        elif self.right_endpoint<0:
            return Interval(self.right_endpoint**other, self.left_endpoint**other)
        else:
            L=[0,max[self.left_endpoint**other, self.right_endpoint**other]]
        return interval
        
import matplotlib.pyplot as plt
import numpy as np

x1=np.linspace(0., 1, 1000)
xu=np.linspace(0., 1, 1000)+ 0.5
l=[]
u=[]
for i in range(len(x1)):
    I=Interval(x1[i], xu[i])
    I1=3*I**3-2*I**2-5*I-1
    l.append(I1.left_endpoint)
    u.append(I1.right_endpoint)
plt.plot(x1,u, x1,l)


    
            
            