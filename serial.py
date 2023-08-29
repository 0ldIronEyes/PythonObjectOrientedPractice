"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        """create SerialGenerator instance with given number as the start number"""
        self.current = start
        self.start = start


    def generate(self):
        """return the next number in the SerialGenerator"""
        self.current += 1
        return self.current
    
    def reset(self):
        """" reset the serial number to the start number that was given when the SerialGenerator was created"""
        self.current = self.start
