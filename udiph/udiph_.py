from scipy import optimize
from scipy.sparse.csgraph import shortest_path
from sklearn.neighbors import NearestNeighbors
import numpy as np
import matplotlib.pyplot as plt

def UDIPH(X, n_neighbors=15, distance_matrix=False,return_complex=False):
    """
    Returns a distance matrix corresponding to a local uniform distribution of the points.
    Basically creates a new metric space where points are uniformly sampled in space.
    Think of UMAP but with a shortest path algo on top.

    Input
    -----------
    X: numpy array
        dataset (n_samples, n_features) or distance matrix (n_samples,n_samples)

    n_neighbors: int
        number of nearest neighbours considered when creating the proximity graph.
        Too many and topo features are dissolved, too few are artifacts are created.
        Fairly robust.

    distance_matrix: bool
        Whether X is a distance matrix or not.

    Returns
    ------------
    x: np.array(n_samples,n_samples)
        distance matrix of new space.
    A: np.array(n_samples,n_samples)
        adjacency matrix of 1-d simplicial complex
    """
    if distance_matrix:
        neigh = NearestNeighbors(n_neighbors=n_neighbors, metric='precomputed').fit(X)
    else:
        neigh = NearestNeighbors(n_neighbors=n_neighbors).fit(X)
    D, idx = neigh.kneighbors()
    
    A = np.zeros([len(X), len(X)])
    for i in range(A.shape[0]):
        for j in range(n_neighbors):
            A[i,idx[i,j]] = j
    scaled = D/np.max(D, axis=1)[:,None]

    sigs=[]
    for i in range(scaled.shape[0]):
        def f(sigma):
            return np.sum(np.exp(-scaled[i]/sigma))-np.log2(n_neighbors)
        sol = optimize.root_scalar(f, x0=0.5,x1=0.07,method='secant')
        sigs.append(sol.root)
 
    D = np.exp(-(scaled/((np.array(sigs))[:,None])))
    D[:,0]=np.zeros(D.shape[0])
    for i in range(A.shape[0]):
        A[i,:]=D[i,A[i,:].astype(int)]
    
    A=A+np.eye(len(X))
    A=A+A.T-(A*A.T)
    A[A!=0]=np.abs(1-A[A!=0])
    np.fill_diagonal(A,0)
    
    if return_complex:
        return A

    x = shortest_path(A,directed=False)
    return x
