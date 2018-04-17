from mrjob.job import MRJob

class MyMapReduceJob(MRJob):

	def mapper(self, _, line):
		lastfm = line.split("\t")
		nama_artis = lastfm[3]
		yield nama_artis, 1
			
	def reducer(self, key, values):
		yield key, sum(values)
		
if __name__ == '__main__':
	MyMapReduceJob.run()