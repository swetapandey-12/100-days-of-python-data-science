class Solution:
    def maxsubsumarry(self , arr):
        max_cr = curr_cr = arr[0]
        for i in arr[1:]:
            curr_cr = max(i, curr_cr+i)
            max_cr = max(max_cr, curr_cr)
        return max_cr    


if __name__ == "__main__":     
    input_arr = list(map(int, input("Enter array : ").split()))  
    print("Your input array is :", input_arr)   
    sol = Solution()  
    maxsub = sol.maxsubsumarry(input_arr) 
    print("Your max sum Value :", maxsub) 