class Key(object):
    """A class to represent a cryptographic key."""
    def __init__(self, input):
        """Initialize an instance of Key."""
        self.chars = list(input)
        

    def rotate(self):
        """Rotate the elements in the list of chars of a key."""
        self.chars = self.chars[1:] + self.chars[:1] 
        return self.chars