from mrjob.job import MRJob

class DodyPlayedSong(MRJob):

    def mapper(self, _, line):
        data = line.split('\t')
        song = data[5]

        yield song, 1

    def reducer(self, key, values):
        yield key, sum(values)

if __name__ == '__main__':
    DodyPlayedSong.run()