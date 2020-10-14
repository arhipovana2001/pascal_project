class Pascal:
    """class describe pascal array"""
    def __init__(self, array):
        """initialization method"""
        self.array = array

    def __str__(self):
        """str method"""
        return str(self.array)

    def __getitem__(self, item):
        """getting an item by index"""
        if -1 < item - 1 < len(self.array):
            return self.array[item - 1]
        else:
            raise IndexError('list index out of range')

    def __setitem__(self, key, value):
        """setting an item by index"""
        if -1 < key - 1 < len(self.array):
            self.array[key - 1] = value
        else:
            raise IndexError('list index out of range')
