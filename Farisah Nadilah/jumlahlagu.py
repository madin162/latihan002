from mrjob.job import MRJob

class MyMapReduceJob(MRJob):
	def mapper(self, _, line):
		radio = line.split("\t")
		lagu = radio[4]
		yield lagu, 1

	def reducer(self, key, values):
		yield key, sum(values)

if __name__ == '__main__': 
	MyMapReduceJob.run()
