# Pure python implementation of SampleData.cpp

def sample_data(file_name, sample_idx):
    """
    Samples data on disk

    Params:
        file_name:str
            A str describing the location of data file ex. data/data_file.csv
        sample_idx:list of ints
            A list of ints corresponding to index of rows to sample
    Returns
        sample:list
            A list of samples rows from the data file
    """
    target_sample_size = len(sample_idx)
    sample = []

    with open(file_name) as data_file:
        for line, line_num in enumerate(data_file):
            if line_num in sample_idx:
                sample.append(line)
            # Early stopping prevents excessive file reading
            if len(sample) == target_sample_size:
                return sample

