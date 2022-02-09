# disam
disam is a Python package for on-**di**sk **sam**pling with a C++ backend (and a pure Python fallback). The intended use case for disam is when datasets cannot be loaded in to memory either due to size or memory constraints.

## A simple example

```py
from disam import DiskSampler

data_src = "data/data_file.csv"
batch_size = 32

disk_sampler = DiskSampler(data_src, batch_size)

sample = disk_sampler.sample() # Each call returns a new sample
```

## Requirements
* `numpy`
* `pybind11`

## Installation
Due to the C++ backend, you will have to compile the `_sampler.cpp` file yourself. However, `pybind11` automates the creation of the bindings making the process a breeze. To compile `_sampler.cpp`, navigate to the directory it is (/disam by default) in and run

- `c++ -O3 -Wall -shared -std=c++11 -fPIC $(python3 -m pybind11 --includes) _sampler.cpp -o _sampler$(python3-config --extension-suffix)`

From here, you can call the `DiskSampler` class from `disam.py` to perform on-disk sampling of your data (you may also add to PATH).

## Documentation

### disam.DiskSampler
#### *class* `disam.DiskSampler(batch_size, data_source, num_rows=None, headers=False)`
The disam.DiskSampler class contains the methods and attributes necessary to sample data from the disk. 


Parameter | Data type | Description
:---: | :---: | :---
batch_size | int | The number of rows from the data file to draw as a sample
data_source | str | The path to the data file from which to sample
num_rows (optional)| int | The number of rows contained in the data file. This is optional, and helps speed up the initialization of the class instance. This is due to the fact that the number of rows must be known to generate sample indices. If this number is not provided, it will be determined upon initialization.
headers (optional) | bool | True if the first line of the data file contains column labels (or other non-data items). Otherwise False.

### disam.DiskSampler.sample
#### *method* `disam.DiskSampler.sample(delim=',', last_col_is_y=False)`
the disam.DiskSampler.sample method draws random samples of size self.batch_size from the provided self.data_source

Parameter | Data type | Description
:---: | :---: | :---
delim (optional) | str | The in-line data delimeter character
last_col_is_y (optional) | bool | If your data is structured so that the y-values (if applicable) are appended as the last column, you can set this value to True and the sample will be returned as X, y. If False (default) then the method just returns a single sample X.

**Returns: numpy.array**

Either returns the sample in a single numpy.array or returns the sampple as two numpy.arrays X, y if `last_col_is_y` is set to True. See parameter documentation for `last_col_is_y` for more information.
