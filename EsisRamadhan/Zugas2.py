from mrjob.job import MRJob
class MyMapReduceJob(MRJob):
    def mapper(self, _, line):
	pecahan = line.split("\t")
	nama_artis=pecahan[3]
	song=pecahan[5]
	yield "Nama Artis="+nama_artis+"-"+"Lagu= "+song,1
    def reducer(self, key, values):
        yield key, sum(values)
if __name__ == '__main__':
    MyMapReduceJob.run()
