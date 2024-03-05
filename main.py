class IntegerSet:
    def __init__(self, integers):
        self.integers = set(integers)

    def sum_of_elements(self):
        return sum(self.integers)
    def arithmetic_mean(self):
        return sum(self.integers)/len(self.integers)

    def maximum_element(self):
        return max(self.integers)

    def minimum_element(self):
        return min(self.integers)


