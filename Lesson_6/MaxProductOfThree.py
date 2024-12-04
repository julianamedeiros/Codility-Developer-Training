def solution(A):
    A.sort()
    n = len(A)
    count1 = A[n-1] * A[n-2] * A[n-3]
    count2 = A[n-1] * A[n-2] * A[0]
    count3 = A[n-1] * A[0]  * A[1]
    count4 = A[0] * A[1] * A[2]
    result = max(count1, count2, count3, count4)
    return result


print(solution([-3, 1, 2, -2, 5, 6]))
