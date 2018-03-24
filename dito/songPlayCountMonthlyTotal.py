from mrjob.job import MRJob


class MyMapReduceJob(MRJob):

    def mapper(self, _, line):
        koloms = line.split('\t')
        bulan = koloms[1][:7]
        yield bulan, 1

    def reducer(self, key, values):
        yield key, sum(values)


if __name__ == '__main__':
    MyMapReduceJob.run()
