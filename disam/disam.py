import random
import numpy as np

try:
    from _sampler import sample_disk
except ImportError: # unable to import c++ version of SampleData
    from sampler import sample_disk
    print("Unable to import c++ implementation of sampler")
    print("Defaulting to pure python implementation")
    print("Note: Python implementation is much slower")


class DiskSampler:
    def __init__(self, batch_size, data_source, num_rows=None, headers=False):
        """
        DiskSampler samples data from disk removing the requirement
        of loading the entirety of the data you want to work with into memory

        Params:
            batch_size:int
                The number of rows from the data file to draw for each sample
            data_source:str
                File path to data source.
            num_rows:int (optional)(default val = None)
                If a value is supplied set self.data_size = num_rows
            headers:bool (optional)(default val = False)
                Determines whether underlying data has first row consisting
                of non-data values (such as column names)

        """
        self.batch_size = batch_size
        self.data_source = data_source
        self.num_rows = num_rows if num_rows else sum(1 for line in open(data_source))
        self.headers = False

        if headers:
            self.num_rows -= 1 # One less row since we exclude header row


    def sample(self, delim=',', last_col_is_y=False):
        """
        Draws a random sample of size self.batch_size from the provided
        self.data_souce. The sample is chosen with uniform probability and
        returned

        Params:
            delim:char (optional)(default val = ,)
                data delimeter
            last_col_is_y:bool (optional) (default val = False)
                indicates whether the last data column contains output values
                
        Returns:
            -If last_col_is_y=True returns data, y where y is the last data column
            and data is all of the data minus the last data column
            -If last_col_is_y=False returns data
            
            data:numpy.ndarray
            y:numpy.ndarray
        """ 
        if self.headers:
            sample_idx = sorted(random.sample(range(1, self.num_rows), self.batch_size))
        else:
            sample_idx = sorted(random.sample(range(self.num_rows), self.batch_size))

        data = sample_disk(self.data_source, sample_idx)
        data = np.array([list(map(float, line.split(delim))) for line in data]) 
                            
        if last_col_is_y:
            y = data[:, -1]
            data = data[:, :-1] 
            return data, y
        else:
            return data
