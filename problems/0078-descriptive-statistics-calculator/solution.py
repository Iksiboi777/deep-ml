import numpy as np

def descriptive_statistics(data: list | np.ndarray) -> dict:
    """
    Calculate various descriptive statistics metrics for a given dataset.
    
    Args:
        data: List or numpy array of numerical values
    
    Returns:
        Dictionary containing mean, median, mode, variance, standard deviation,
        percentiles (25th, 50th, 75th), and interquartile range (IQR)
    """
    # Your code here
    mean = np.mean(data)
    median = np.median(data)
    vals, counts = np.unique(data, return_counts=True)
    mode = vals[counts.argmax()]
    variance = np.var(data)
    std = np.std(data)
    per25, per50, per75 = np.percentile(data, [25, 50, 75])
    iqr = per75 - per25
    
    ret_dict = {
        'mean': mean,
        'median': median,
        'mode': mode,
        'variance': variance,
        'standard_deviation': std,
        '25th_percentile': per25,
        '50th_percentile': per50,
        '75th_percentile': per75,
        'interquartile_range': iqr
    }

    ret_dict = {k: v.astype(float) for k, v in ret_dict.items()}

    return ret_dict