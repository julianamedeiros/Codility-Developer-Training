#A[i] = circle's middle point, add and subtract the radius

def solution(A):
    
    if len(A) < 2:
        return 0
    dict = {}
    for i in range(len(A)):
        nums = i - A[i]
        nums2 = i + A[i]
        dict[i] = nums, nums2

    #print(dict)
    result = 0  

    for i in range(len(dict)):
        x = dict[i][0]
        y = dict[i][1]
        #print(x, y)
        for j in range(i, len(dict)):
            z = dict[j][0]
            k = dict[j][1]
            #print(z, k)
            if  x < z and y > z or x>=z and y<k or y > z and y < z or x > z and x < k:
                print(dict[i], 'intersects with', dict[j])
                result += 1
                if result > 10**7:
                    return -1
    return result



print(solution([1, 5, 2, 1, 4, 0]))