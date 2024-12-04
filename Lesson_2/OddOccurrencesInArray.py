
def solution(A):
    dict = {}
    for i in A:
        if i not in dict:
            dict[i] = 1
        else: 
            dict[i] +=1
    for j in dict:
        if dict[j] == 1:
            print(j)



solution([1, 2, 45, -1, 3, 4, 908, 3, 2, 1, 45, -1, 908])