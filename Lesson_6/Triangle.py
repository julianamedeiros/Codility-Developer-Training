#(P, Q, R) if 0<P<Q<R (linear) and:
#A[P] + A[Q] > A[R]
#A[Q] + A[R] > A[P]
#A[R] + A[P] > A[Q]

def solution(A):
    A.sort() #sort limits the number of if conditions
    n = len(A)
    for i in range(n-2):
        for j in range(i+1, n-1):
            if A[i] + A[j] > A[j+1]: #if it will not be higher than the next, it will never be a triplet
                return 1
    return 0


print(solution([10, 2, 5, 1, 8, 20])) #1, 2, 5, 8, 10, 20