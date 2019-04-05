vector_1 = [2, 3, 4, 5, 6]
vector_2 = [4, 5, 6, 2, 3]

if len(vector_1) != len(vector_2):
    raise Exception('Both vectors should have the same length')

def skalar_multiply(v1, v2):
    l = len(v1)

    return sum([ v1[i] * v2[i] for i in range(l) ])
