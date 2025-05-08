
class Solution:
    def unionofarr(self , a , b):
        unique_element = []

        for num in a+b:
            if num not in unique_element:
                unique_element.append(num)
        return len(unique_element)        



if __name__ == "__main__":
    user_input1 = list(map(int , input("Enter 1st array : ").split()))
    user_input2 = list(map(int , input("Enter 2nd array : ").split()))

    print("your first array : ", user_input1)
    print("your 2nd array is : ", user_input2)

    sol = Solution()
    union = sol.unionofarr(user_input1, user_input2)
    print("Count of union elements is:", union)