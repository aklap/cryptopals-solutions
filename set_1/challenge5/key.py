class Key(object):
    def __init__(self, input):
        self.input = input
        self.chars = list(input)

    def rotate(self):
        self.chars = self.chars[1:] + self.chars[:1] 
        return self.chars