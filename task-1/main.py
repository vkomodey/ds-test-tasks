def math_expectation(inputs):
    m_expectation = sum([input["probability"] * input["value"] for input in inputs])

    return m_expectation

def dispersion(inputs):
    m_expectation = math_expectation(inputs)
    prepared_inputs = [ Random_Values(input["probability"], (input["value"] - m_expectation)**2, ) for input in inputs ]
    disp = math_expectation(prepared_inputs)

    return disp

def result(random_value_input):
    return {
        "math_expectation": math_expectation(random_value_input),
        "dispersion": dispersion(random_value_input),
    }


def Random_Values(probability, value):
    return {
        "probability": probability,
        "value": value
    }

random_value_inputs = [
    Random_Values(0.1, 13),
    Random_Values(0.3, 54),
    Random_Values(0.5, 10),
    Random_Values(0.05, 30),
    Random_Values(0.05, 40)
]

probabilities = map(lambda value: value["probability"], random_value_inputs)

if sum(probabilities) != 1:
    raise Exception('Sum of probabilities should be equal 1')

print(result(random_value_inputs))
