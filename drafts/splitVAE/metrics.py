import numpy as np

def CPRS(observed, generated, sample_weight= None):
    num_samples = generated.shape[0]
    absolute_error = np.mean(np.abs(generated - observed), axis=0)

    if num_samples == 1:
        return np.average(absolute_error, weights= sample_weight)
    else:
        generated = np.sort(generated, axis= 0)
        B0 = generated.mean(axis= 0)

        B1_values = generated * np.arange(num_samples).reshape((num_samples, 1))
        B1 = B1_values.mean(axis=0) / num_samples

        per_obs_crps = absolute_error + B0 - 2 * B1
    return np.average(per_obs_crps, weights=sample_weight)

# def Freedman_Diaconis(data):
#     """Implement the Freedman-Diaconis rule to select the width of the histogram bins."""
#     IQR = np.percentile(data.reshape(-1),75) - np.percentile(data.reshape(-1),25)
#     numerator = np.max(data.reshape(-1)) - np.min(data.reshape(-1))
#     denominator = 2 * IQR / np.power(len(data.reshape(-1)),(1/3))
#     return int(numerator/denominator)

# def compute_cumulative_distribution(data, target= "observed", normalized= False, num_bins= 0):
#     """
#     Computes the Empirical Cumulative Distribution Function (ECDF) for a given normalized vector.

#     The function determines the number of bins for constructing the Empirical Probability Density Function (EPDF) 
#     based on the type of data in the vector.
#     - If the vector represents observed data, the Freedman-Diaconis Rule is used. 
#     - If the vector represents generated/forecasted data, the number of bins is derived from the ECDF of the observed data.

#     Args:
#         vector (array-like): The input vector for which the ECDF is to be computed. 

#     Returns:
#         array-like: The computed ECDF of the input vector.
#     """
#     if (normalized == True):
#         data = (data - np.mean(data)) / np.std(data, ddof= 1)

#     if (target != "observed"):
#         counts, bins_count = np.histogram(data, bins= num_bins)
#         epdf = counts / sum(counts)  
#         ecdf = np.cumsum(epdf) 
#         return ecdf, counts, bins_count
#     else:
#         bin_width = Freedman_Diaconis(data)
#         counts, bins_count = np.histogram(data, bins= bin_width)
#         epdf = counts / sum(counts)  
#         ecdf = np.cumsum(epdf) 
#         return ecdf, counts, bins_count

# def cprs(observed, generated):
#     """
#     Implements the Univariate Empirical Continuous Probability Ranked Score (CPRS).

#     This function computes the CPRS between two datasets, `observed` and `generated` by measuring the difference 
#     between the empirical cumulative distribution functions (ECDFs) of the two data sets. The ECDFs are computed 
#     using the `compute_cumulative_distribution` method of the class.

#     Args:
#         observed (array-like): The observed data set.
#         generated (array-like): The generated data set.

#     Returns:
#         float: The computed CPRS between the `observed` and `generated` data sets.
#     """
#     observed = observed.reshape(-1); generated = generated.reshape(-1)
#     observed_ecdf, _ , bins_count = compute_cumulative_distribution(observed)
#     generated_ecdf, _ , _ = compute_cumulative_distribution(generated, target= "generated", num_bins= bins_count)
#     score  = sum(np.power(observed_ecdf - generated_ecdf,2)) / (observed_ecdf.shape[0] - 1)
#     return score
    
def fid(observed, generated):
    """
    Implements the Fréchet Inception Distance (FID) between the `observed` and `generated` data sets.

    The FID is a measure of similarity between two datasets. It is calculated as the sum of two terms:
    - The Euclidean distance between the means of the `observed` and `generated` data sets.
    - The trace of the sum of the covariance matrices of the `observed` and `generated` data sets minus 
    twice the square root of the product of these covariance matrices.

    Args:
        observed (array-like): The observed data set.
        generated (array-like): The generated data set.

    Returns:
        float: The computed FID between the `observed` and `generated` data sets.
    """
    mu_observed, cov_observed = np.mean(observed, axis= 0), np.cov(observed, rowvar= False)
    mu_generated, cov_generated = np.mean(generated, axis= 0), np.cov(generated, rowvar= False)
    sqrt_product_covs = sp.linalg.sqrtm(np.dot(cov_observed,cov_generated))

    first_term = sum(np.power(mu_observed - mu_generated,2.0))
    second_term = np.trace(cov_observed + cov_generated - 2 * sqrt_product_covs.real)
    return first_term + second_term
