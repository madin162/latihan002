from mrjob.job import MRJob


class MyMapReduceJob(MRJob):

    def mapper(self, _, line):
        pecahan = line.split("\t")
        judul = pecahan[5]
        yield judul, 1

    def reducer(self, key, values):
        yield key, sum(values)


if __name__ == '__main__':
    MyMapReduceJob.run()

