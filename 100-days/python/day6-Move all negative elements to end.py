class Solution:
    def segregateElements(self, arr):
        n = len(arr)
        positive = []  # List to store positive numbers
        negative = []  # List to store negative numbers

        # Separate positive and negative numbers
        for num in arr:
            if num >= 0:
                positive.append(num)
            else:
                negative.append(num)

        # Combine positive and negative numbers
        arr[:] = positive + negative  # In-place modification of the original array
        
        return arr     
