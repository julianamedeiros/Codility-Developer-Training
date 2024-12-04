def solution(A):
    m = max(A)
    n = len(A)
    count = [0] * (m+1)
    for num in range(n):
        count[A[num]] += 1
    #print(count)
    total = sum(count[1:])
    #print(total)
    if total == m:
        return 1
    return 0



print(solution([4, 1, 3, 2]))