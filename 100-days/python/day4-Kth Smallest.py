import random

class Solution:
    def kthSmallest(self, arr, k):
        # Helper function using Quickselect algorithm
        def quickselect(arr, k):
            if len(arr) == 1:
                return arr[0]

            pivot = random.choice(arr)

            lows = [el for el in arr if el < pivot]
            highs = [el for el in arr if el > pivot]
            pivots = [el for el in arr if el == pivot]

            if k <= len(lows):
                return quickselect(lows, k)
            elif k <= len(lows) + len(pivots):
                return pivots[0]
            else:
                return quickselect(highs, k - len(lows) - len(pivots))

        # Validate k
        if k < 1 or k > len(arr):
            raise ValueError("k is out of bounds of the array")

        return quickselect(arr, k)

# --- Main block for user input ---
if __name__ == "__main__":
    try:
        # Get input from the user
        user_input = input("Enter the array elements separated by spaces: ")
        print("your input array: ", user_input)
        arr = list(map(int, user_input.strip().split()))

        k = int(input("Enter the value of k: "))

        # Create an instance of Solution and call the method
        sol = Solution()
        result = sol.kthSmallest(arr, k)
        print(f"{k}th smallest element is: {result}")

    except ValueError as e:
        print("Error:", e)
    except Exception as e:
        print("Unexpected error:", e)
