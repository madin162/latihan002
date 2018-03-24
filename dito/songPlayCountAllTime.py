from mrjob.job import MRJob


class MyMapReduceJob(MRJob):

    def mapper(self, _, line):
        koloms = line.split('\t')
        nama_lagu = koloms[5]
        yield nama_lagu, 1

    def reducer(self, key, values):
        yield key, sum(values)


if __name__ == '__main__':
    MyMapReduceJob.run()
