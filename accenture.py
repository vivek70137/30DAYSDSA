def soln(arr,n):
    arr.sort()
    sumu=0
    for i in range(1,n):
        sumu+=abs(arr[i]-arr[i-1])
    return sumu
def main():
    n=int(input("enter"))
    arr=list(map(int,input().strip().split()))
    print(soln(arr,n))
main()
