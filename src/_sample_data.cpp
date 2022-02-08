#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <list>

std::vector<std::string> sample_data(std::string file_name, std::vector<int> sample_idx){

    int sample_size = sample_idx.size();
    std::vector<std::string> samples; // To be returned

    std::ifstream myFile;
    myFile.open(file_name); 
    
    std::string line; // Will contain a line from opened data file

    int i = 0; // Used to iterate through sample idxs
    int j = 0; // Tracks line number 

    while (i < sample_size) { // Prevents extra reading of file after sample gathered
        while (getline(myFile, line)) {
            if (j == sample_idx[i]) {
                samples.push_back(line);
                i += 1;
            } // implicit else - throws away line on each iteration
            j += 1; 
        }
    }

    return samples;

}

PYBIND11_MODULE(SampleData, m) {
    m.doc() = "Samples data from csv file";
    m.def("SampleData", &SampleData, "Samples data from csv file");
}
