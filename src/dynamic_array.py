class DynamicArray:
	def __init__(self, capacity=8):
        self.count = 0 # Count is how much is currrently used
        self.capacity = capacity # How much is currently allocated
        self.storage = [None] * self.capacity