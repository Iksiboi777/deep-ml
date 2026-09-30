import numpy as np

def empirical_pmf(samples):
    """
    Given an iterable of integer samples, return a list of (value, probability)
    pairs sorted by value ascending.
    """
    # TODO: Implement the function
    vals, counts = np.unique(samples, return_counts = True)
    ratios = [cnt/len(samples) for cnt in counts]
    return list(zip(vals.tolist(), ratios))