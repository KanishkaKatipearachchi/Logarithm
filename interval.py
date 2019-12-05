"""
Things remaining to be done:
--Documentation
--Abstraction of numbers as intervals
----One can construct an interval with one argument, making an "empty" interval; 
----We can also add a constructor that creates an interval from an interval
--Parameter error raising in operators to ensure no unintended behavior
--Other TODO throughout the code
"""


class Interval():
    """
    A class representing a closed interval of real numbers
    """
    def __init__(self, left, right=None):
        """
        TODO: add proper assertions/exception throws 
        such that the arguments can only be floats (or maybe ints?)
        """
        if right == None:
            right = left
        try:
            left = float(left)
            right = float(right)
        except:
            raise ValueError("arguments must be castable to type float")
        if left <= right:
            self.left = left
            self.right = right
        else:
            self.right = left
            self.left = right

    def __add__(self, other):
        return Interval(self.left + other.left, self.right + other.right)

    def __sub__(self, other):
        return Interval(self.left - other.left, self.right - other.right)

    def __mul__(self, other):
        """
        TODO: try to clean this up? Make it more compressed?
        Is it true that for all real numbers that the product of the rights is greater than any other of the products?
        """
        return Interval(min([self.left * other.left, self.left * other.right, self.right * other.left, self.right * other.right]),
                max([self.left * other.left, self.left * other.right, self.right * other.left, self.right * other.right]))

    def __div__(self, other):
        """
        TODO: same as mul; 
        Also, better way to handle div by zero errors?
        """
        return Interval(min([self.left / other.left, self.left / other.right, self.right / other.left, self.right / other.right]),
                max([self.left / other.left, self.left / other.right, self.right / other.left, self.right / other.right]))

    def __pow__(self, power):
        """
        TODO: The definition is a bit odd;
        It looks as though it can only be defined for integer powers
        """
        if type(power) != int:
            raise ValueError("power must be an integer")
        if power % 2 == 0:
            if self.left >= 0:
                return Interval(self.left**power, self.right**power)
            elif self.right < 0:
                return Interval(self.right**power, self.left**power)
            else:
                return Interval(0, max([self.right**power, self.left**power]))
        return Interval(self.left**power, self.right**power)

    def __contains__(self, item):
        return item >= self.left and item <= self.right

    def __str__(self):
        return "[%s, %s]" % (self.left, self.right)


def main():
    """
    Main function;
    For testing purposes only
    """
    inter1 = Interval(1.0, 3.0)
    print(inter1)
    inter2 = Interval(0.0, 2.5)
    print(inter1 + inter2)
    print(inter1 - inter2)
    print(inter1 * inter2)
    print(inter2 / inter1)
    print(inter1**2)
    inter3 = Interval(-1.0, 4.0)
    print(inter3**2)

    

if __name__ == "__main__":
    main()
    