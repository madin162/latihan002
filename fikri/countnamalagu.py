from mrjob.job import MRJob
#import numpy as np

class MapReduceSong(MRJob):
    def mapper(self, _, line):
        kolomlst = line.split("\t")
        namalagu = kolomlst[5]
        yield namalagu, 1

    def reducer(self, key, values):
        yield key, sum(values)

if __name__ == '__main__':
    MapReduceSong.run()
        







        

