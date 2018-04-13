from mrjob.job import MRJob
class RezaPlaylist(MRJob):
    def mapper(self, _, line):
        data = line.split("\t")
        artis = data[2]
        yield artis, 2
    def reducer(self, key, values):
        yield key, sum(values)
if __name__ == '__main__':
    RezaPlaylist.run()