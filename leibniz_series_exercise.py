def approximate_pi(n_terms):
  list_of_numbers = [1] * n_terms
  approximation_factor = 0
  for i in range(n_terms):
    nominator = (-1) ** i
    denominator = 2 * i + 1
    approximation_factor = approximation_factor + (nominator / denominator)
  return(4 * approximation_factor)
