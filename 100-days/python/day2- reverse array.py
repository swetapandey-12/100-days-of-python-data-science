class Solution:
    def reverseArray(self, arr):
        end = len(arr) - 1
        start = 0
        while end > start:
            # Swap using a temporary variable
            temp = arr[start]
            arr[start] = arr[end]
            arr[end] = temp

            start += 1
            end -= 1

        return arr


if __name__ == "__main__":
    # Take space-separated integers from the user
    user_input = list(map(int, input("Enter integers separated by space: ").split()))

    # Print the original input array
    print("Original array:", user_input)

    # Create an object of the Solution class
    sol = Solution()

    # Call the reverseArray method
    reversed_array = sol.reverseArray(user_input.copy())  # use copy to preserve original

    # Display the reversed array
    print("Reversed array:", reversed_array)
