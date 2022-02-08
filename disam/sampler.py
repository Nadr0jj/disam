# Pure python implementation of SampleData.cpp

def sample_disk(file_name, sample_idx):
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
    sampled = []

    with open(file_name) as data_file:
        for line, line_num in enumerate(data_file):
            if line_num in sample_idx:
                sampled.append(line)
            # Early stopping prevents excessive file reading
            if len(sampled) == target_sample_size:
                return sampled

