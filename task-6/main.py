def f(x):
    return 3*x**4 + - 4*x**3 - x**2 + 2*x - 6

start = -1.5
end = 1.8
epsilon = 0.01

def frange(start, stop=None, step=None):
    sequence = []
    stop = stop - step
    if stop == None:
        stop = start + step
        start = 0.0
    if step == None:
        step = 1.0
    while True:
        if step > 0 and start >= stop:
            break
        elif step < 0 and start <= stop:
            break
        yield start
        start = start + step

sequence_range = frange(start, end, epsilon)

old_sequence_value = None
old_f_value = None
roots = []

for sequence_value in sequence_range:
    f_value = f(sequence_value)
    if abs(f_value) < epsilon:
        roots.append(sequence_value)

    if len(roots) > 0 and old_sequence_value == roots[-1]:
        continue

    if old_sequence_value == None:
        old_sequence_value = sequence_value
        old_f_value = f_value
        continue

    if old_f_value > 0 and f_value < 0 or old_f_value < 0 and f_value > 0:
        middle = (old_sequence_value + sequence_value) / 2
        roots.append(middle)

    old_sequence_value = sequence_value
    old_f_value = f_value

print(roots)
