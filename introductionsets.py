def average(array):
    # your code goes here
    distinct=set(arr)
    result=sum(distinct)/len(distinct)
    return round(result,3)
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)