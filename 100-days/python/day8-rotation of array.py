class Solution:
    def rotation(self, arr):
        last = arr[-1]
        if len(arr) == 1 or not arr:
            return
        for i in range(len(arr)):
            arr[i], last = last, arr[i]
        return arr


if __name__ == "__main__":
    input_arr = list(map(int, input("Enter array that you want to rotate: ").split()))
    print("Your input array is:", input_arr)
    sol = Solution()
    rotated = sol.rotation(input_arr)
    print("Your rotated array:", rotated)
