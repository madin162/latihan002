from mrjob.job import MRJob

class DodyPlayedHourly(MRJob):

    def mapper(self, _, line):
        data = line.split('\t')
        timestamp = data[1]
        hour = timestamp[11:13] + ':00'

        yield hour, 1

    def reducer(self, key, values):
        yield key, sum(values)

if __name__ == '__main__':
    DodyPlayedHourly.run()