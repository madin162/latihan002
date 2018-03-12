from mrjob.job import MRJob
import string
import numpy


class MyMapReduceJob(MRJob):

    def mapper(self, _, line):
     pecahan = line.split("\t")
     nama_lagu = pecahan[5]
     #sales = float(pecahan[4]) 
     #yield nama_produk, sales
     yield nama_lagu, 1
    def reducer(self, key, values):
        yield key, sum(values)

if __name__ == '__main__':
    MyMapReduceJob.run()
