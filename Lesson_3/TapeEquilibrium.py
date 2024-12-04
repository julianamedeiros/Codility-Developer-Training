#it has a loop but does not iterate over the array, its accessing directly by the index, so its ok

def solution(a):
    dict = {}
    n = len(a)
    #n is the number of nums in the list
    for p in range(1, n):
        #sum(a[0]:a[p-1]) - sum(a[p]: a[n-1)])
        s1 = sum(a[0: (p)]) #the sum stops before p
        s2 = sum(a[p : (n)]) #the sums stops before n
        d = abs(s1 - s2)
        dict[p] = d
        #print(d)
    #print(min(dict.values()))
    return min(dict.values())


solution([3, 1, 2, 4, 3])

