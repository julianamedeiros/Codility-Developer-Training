#rotate a list 'A' for 'K' times

def solution(A, K):
    #print(A)
    if A == []:
        print(A)
    else:
        for i in range(K):
            last = A[(len(A)-1)]
            A.pop((len(A)-1))
            A.insert(0, last)
        print(A)
    #return A






solution([1, 2, 3, 4], 4)