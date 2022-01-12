# Uniform Distributed Persistent Homology (UDiPH)


[![Downloads](https://pepy.tech/badge/udiph)](https://pepy.tech/project/udiph) [![PyPI license](https://img.shields.io/pypi/l/ansicolortags.svg)](https://github.com/Antonio-Leitao/dbsampler/blob/main/LICENSE) [![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-03a80e.svg)](https://github.com/Antonio-Leitao) [![version ](https://img.shields.io/badge/release-0.0.1-blue.svg)](https://pypi.org/project/dbsampler/) [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

UDiPH is a package that creates a new metric space where the points are uniformly sampled with respect to a global metric. It is oriented for creating Vietoris-Rips filtrations that are independent of the metric of the initial space. This work is very influced on UMAP.

Standard Vietoris-Rips filtration:
<p align="center">
  <img src="images/2filtrations_std.png" width="600"/>
</p>
Vietoris-Rips filtration using metric space created by UDiPH is based on local density:
<p align="center">
  <img src="images/2filtrations_udiph.png" width="600"/>
</p>

## Installation
Dependencies:
  - Numpy
  - Scipy
  - Sklearn

UDIPH is available on PyPI,

```sh
pip install udiph
```

## Usage
```python
import udiph
cover = udiph.UDIPH(X=X, n_neighbors=15, distance_matrix=False, return_complex=False)
```
**Parameters:**
-  ``X``: numpy array of shape=(samples,features) or shape=(samples,samples) containing the data. If data is a pairwise distance matrix then ``distance_matrix`` must be set to True.
 -  ``n_neighbors``: This determines the number of points sampled from the decision boundary. More points equates for a denser sample but slows the algorithm. Default is 1000.
 -  ``distance_matrix``: Boolean value indicating if input data is or not a distance_matrix 
 -  ``return_complex``: Initial point distribution, it is also the distribution of    the points in the decision boundary. Currently supports only _uniform_         (default).
 
**Returns:**
 -  ``cover``: numpy array (n_points, n_features) of points in the decision boundary.

## How does it work?
The basic assumption on UDiPh relies on the idea that data comes uniformly sampled from an unknown Riemmannian manifold. As a consequence, "bigger" holes in the governing manifold are respresented by having a higher number of points sampled from their boundary, and "small" holes will have less points sampled.

For an in-depth explanation look at this [post](https://antonio-leitao.netlify.app/post/ph/). 
 
## Citation
If you use UDiPH in your work or parts of the algorithm please consider citing:
> Paper coming soon
