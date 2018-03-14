from mrjob.job import MRJob
import numpy as np

class MapReduceSong(MRJob):
    def mapper(self, _, line):
        yield "lagu" , len(line.split('\t'))

    def reducer(self, key, values):
        yield key, sum(values)

if __name__ == '__main__':
    MapReduceSong.run()
        







        

