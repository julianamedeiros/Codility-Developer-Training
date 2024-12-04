#find the maximal sequence of consecutive zeros in a binary 'n'
#1000
#0000
#10001

def solution(n):
    binary = bin(n)
    result = 0
    lst = []
    print(binary)
    for i in binary[2:]:
        #print(i)
        if i == '0':
            result = result + 1
        else:
            lst.append(result)
            result = 0
    gap = max(lst)
    #print(gap)
    return gap

solution(32)