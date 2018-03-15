from mrjob.job import MRJob

class DodyPlayedAnually(MRJob):

    def mapper(self, _, line):
        data = line.split('\t')
        timestamp = data[1]
        year = timestamp[:4]

        yield year, 1

    def reducer(self, key, values):
        yield key, sum(values)

if __name__ == '__main__':
    DodyPlayedAnually.run()