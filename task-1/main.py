probabilities = [ 0.1, 0.3, 0.5, 0.05, 0.05 ]
values = [ 13, 54, 100, 30, 40 ]

if sum(probabilities) != 1:
    raise Exception('Sum of probabilities should be equal 1')

if len(probabilities) != len(values):
    raise Exception('Probabilities and values should be arrays with the same length')

print(set(zip(probabilities, values)))
