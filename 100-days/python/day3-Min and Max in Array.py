class Solution:
    def min_max_value(self, arr):
        min = arr[0]
        max = arr[1]
        for i in range(len(arr)):
            if (max<arr[i]):
                max = arr[i]
            if (min>arr[i]):
                min = arr[i]
        return(min, max)            


if __name__ =="__main__":
    user_input = list(map(int , input("enter your number by space  : ").split()))
    print("original array :", user_input)

    #create an object 
    sol = Solution()

    #call the min_max method to through the object 
    min_max = sol.min_max_value(user_input.copy())

    print("Min and max value of your given array :", min_max)