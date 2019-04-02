vector = [1,2,3,4,5,6,7,8,9]

def skalar_multiply(v1, v2):
    l = len(v1)

    return sum([ v1[i] * v2[i] for i in range(l) ])

def length(v):
    return skalar_multiply(v, v)**0.5

print(length(vector))
