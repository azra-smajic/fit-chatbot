import numpy as np
from scipy.sparse import csr_matrix

def cosine_similarity_single_vs_all(query_vector, matrix):
    if not isinstance(query_vector, csr_matrix) or not isinstance(matrix, csr_matrix):
        raise TypeError("Inputs must be CSR sparse matrices.")
    
    dot_product = matrix.dot(query_vector.T).toarray().flatten()
    
    norms = np.sqrt(matrix.multiply(matrix).sum(axis=1)).A1
    query_norm = np.sqrt(query_vector.multiply(query_vector).sum())
    
    if query_norm == 0:
        return np.zeros_like(norms)
    
    similarities = dot_product / (norms * query_norm)
    return similarities