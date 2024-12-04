
def counting(A, x):
    count = [0] * (x + 1)
    covered = 0
    
    for index, position in enumerate(A):
        if position <= x and count[position] == 0:
            count[position] = 1
            covered +=1
        
        if covered == x:
            return index
        
    return -1
        


print(counting([1, 3, 1, 4, 2, 3, 5, 4], 5))

