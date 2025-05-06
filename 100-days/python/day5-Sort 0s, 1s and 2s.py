class Solution:
    def sort012(self , arr):
        low, mid , hight = 0 ,0 , len(arr)-1 
        while(mid<=hight):
            if arr[mid] == 0:
                arr[low], arr[mid] = arr[mid], arr[low]
                low+=1
                mid+=1
            elif arr[mid] == 1:
                mid+=1
            else:
                arr[mid] , arr[hight] = arr[hight], arr[mid]
                hight-=1
        return arr                






if __name__ =="__main__":

    user_input =list(map(int, input("enter 0s ,1s and 2s in any order: ").split()))
    print("given input: ", user_input)

    sol = Solution()

    sort012s = sol.sort012(user_input.copy())

    print("Sorted values are : ", sort012s)
   