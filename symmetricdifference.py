# Enter your code here. Read input from STDIN. Print output to STDOUT
m = int(input())
set_a = set(map(int, input().split()))
n = int(input())
set_b = set(map(int, input().split()))
result=set_a.symmetric_difference(set_b)
li=list(result)
li.sort()
for i in li:
    print(i)
    
