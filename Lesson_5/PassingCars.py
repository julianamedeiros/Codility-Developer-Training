#0 are cars going east
#1 are cars going west
#(p, q) = (0, 1)

#not very efficient
def solution(A):
    n = len(A)
    pairs = 0
    for i in range(len(A)): #0, 1, 2, 3, 4
        if A[i] == 0:
            count = sum(A[i:n])
            pairs += count
    return pairs


print(solution([0, 1, 0, 1, 1]))