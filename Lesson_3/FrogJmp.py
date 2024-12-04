
import math

def solution (X,Y,D):
    distance = Y-X
    jumps = distance/D
    print(math.ceil(jumps)) #ceil rounds the number up, floor rounds it down

solution(10, 85, 30)