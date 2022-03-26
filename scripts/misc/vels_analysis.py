import numpy as np

tvs = np.array([
    1.0000,
    4.0000,
    1.7889,
    1.7889,
    0.0000,
    0.0000,
    2.2361,
    3.3541,
    1.4046,
    1.6152,
    0.0000,
    0.0000,
    1.4142,
    4.2426,
    1.9077,
    1.9077,
    0.0000,
    0.0000,
    2.2361,
    3.3541,
    1.4046,
    1.6152,
    0.0000,
    0.0000,
    1.0000,
    4.0000,
    1.7889,
    1.7889,
    0.0000,
    0.0000,
    2.2361,
    3.3541,
    1.4046,
    1.6152,
    0.0000,
    0.0000,
    1.4142,
    4.2426,
    1.9077,
    1.9077,
    0.0000,
    0.0000,
    2.2361,
    3.3541,
    1.4046,
    1.6152,
    0.0000,
    0.0000,
    1.0000,
    4.0000,
    1.7889,
    1.7889,
    0.0000,
    0.0000,
    2.2361,
    3.3541,
    1.4046,
    1.6152,
    0.0000,
    0.0000,
    1.4142,
    4.2426,
    1.9077,
    1.9077,
    0.0000,
    0.0000,
    2.2361,
    3.3541,
    1.4046,
    1.6152,
    0.0000,
    0.0000,
    1.0000,
    4.0000,
    1.7889,
    1.7889,
    0.0000,
    0.0000,
    2.2361,
    3.3541,
    1.4046,
    1.6152,
    0.0000,
    0.0000,
    1.4142,
    4.2426,
    1.9077,
    1.9077,
    0.0000,
    0.0000,
    2.2361,
    3.3541,
    1.4046,
    1.6152,
    0.0000,
    0.0000
])

rvs = np.array([
    123456,
    123456,
    0.1362,
    -0.1362,
    0.3927,
    0.3927,
    123456,
    123456,
    0.0600,
    -0.1480,
    0.3927,
    0.3927,
    123456,
    123456,
    0.1027,
    -0.1027,
    0.3927,
    0.3927,
    123456,
    123456,
    -0.0600,
    0.1480,
    0.3927,
    0.3927,
    123456,
    123456,
    0.1362,
    -0.1362,
    0.3927,
    0.3927,
    123456,
    123456,
    0.0600,
    -0.1480,
    0.3927,
    0.3927,
    123456,
    123456,
    0.1027,
    -0.1027,
    0.3927,
    0.3927,
    123456,
    123456,
    -0.0600,
    0.1480,
    0.3927,
    0.3927,
    123456,
    123456,
    0.1362,
    -0.1362,
    0.3927,
    0.3927,
    123456,
    123456,
    0.0600,
    -0.1480,
    0.3927,
    0.3927,
    123456,
    123456,
    0.1027,
    -0.1027,
    0.3927,
    0.3927,
    123456,
    123456,
    -0.0600,
    0.1480,
    0.3927,
    0.3927,
    123456,
    123456,
    0.1362,
    -0.1362,
    0.3927,
    0.3927,
    123456,
    123456,
    0.0600,
    -0.1480,
    0.3927,
    0.3927,
    123456,
    123456,
    0.1027,
    -0.1027,
    0.3927,
    0.3927,
    123456,
    123456,
    -0.0600,
    0.1480,
    0.3927,
    0.3927
])

tvs_unique = np.unique(tvs)
print(np.mean(tvs_unique))

rvs_unique = np.unique(rvs)
rvs_unique = np.delete(rvs_unique, np.where(rvs_unique == 123456))
print(np.mean(rvs_unique))