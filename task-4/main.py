def p(M, N, S):
    success_probabilities = ((7 - S) / 6) ** M
    failure_probabilities = (S / 6)**(N - M)

    return success_probabilities * failure_probabilities

print(p(2, 3, 3))
