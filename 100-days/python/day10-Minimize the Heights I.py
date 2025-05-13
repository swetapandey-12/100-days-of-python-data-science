class solution:
    def minimization(self , arr , k ):
        n = len(arr)
        if n==1:
            return 0
        arr.sort()
        ans = arr[-1]-arr[0]

        smallest = arr[0]+k
        largest = arr[-1]-k

        for i in range(1,n):
            if arr[i] -k <0:
                continue
            min_e = min(smallest, arr[i]-k)
            max_e = max(largest, arr[i-1]+k)
            ans = min(ans, max_e-min_e)
        return ans



if __name__ ==" __main__ " :

    input = list(map(int, input("Enter array in any order: ").split()))   
    print("your input is: ", input)

    kval = int(input("Enter any value of k : "))
    print("value of k : ", kval)

    sol = solution()
    mini = sol.minimization(input)
    print("The difference between the largest and the smallest is ",mini)