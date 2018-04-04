from mrjob.job import MRJob


class MyMapReduceJob(MRJob):

    def mapper(self, _, line):
        pecahan = line.split("\t")
        uid = pecahan[0]
        yield uid, 1

    def reducer(self, key, values):
        yield key, sum(values)


if __name__ == '__main__':
    MyMapReduceJob.run()

