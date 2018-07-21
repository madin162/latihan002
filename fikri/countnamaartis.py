from mrjob.job import MRJob

class MapReduceSong(MRJob):
    def mapper(self, _, line):
        kolom = line.split("\t")
        namaartis = kolom[3]
        yield namaartis, 1

    def reducer(self, key, values):
        yield key, sum(values)

if __name__ == '__main__':
    MapReduceSong.run()
        







        

