from mrjob.job import MRJob
class RezaPlaylist(MRJob):
    def mapper(self, _, line):
        data = line.split("\t")
        lagu = data[5]
        yield lagu, 1
    def reducer(self, key, values):
        yield key, sum(values)
if __name__ == '__main__':
    RezaPlaylist.run()