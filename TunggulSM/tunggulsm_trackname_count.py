# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 15:32:44 2018

@author: asus
"""

from mrjob.job import MRJob


class MyMapReduceJob(MRJob):
    def mapper(self, _, line):
        lagu = line.split('\t')
        nama_lagu = lagu[5]
        yield nama_lagu, 1
    
    def reducer(self, key, values):
        yield key, sum(values)

if __name__ == '__main__':
    MyMapReduceJob.run()