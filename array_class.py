class Array:

    def __init__(self, initialElements):
            self.size = len(initialElements)
            self.max_length = self.size
            self.values = initialElements
            self.type = type(initialElements[0])
    
    def insert(self, value):
        if self.size >= self.max_length:
            # resize the array
            self.values += ([None] * self.max_length)
            self.max_length *= 2 # self.max_length = self.max_length * 2

        self.values[self.size] = value
        self.size += 1 