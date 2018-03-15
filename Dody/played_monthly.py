from mrjob.job import MRJob
from datetime import datetime

class DodyPlayedMonthly(MRJob):

    def mapper(self, _, line):
        data = line.split('\t')
        timestamp = data[1]
        month = datetime.strptime(timestamp[5:7], '%m').strftime('%B')

        yield month, 1

    def reducer(self, key, values):
        yield key, sum(values)

if __name__ == '__main__':
    DodyPlayedMonthly.run()