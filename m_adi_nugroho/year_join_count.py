from mrjob.job import MRJob

class MyMapReduceJob (MRJob):
	def mapper(self, _, line):
		this_line = line.split("\t")
		year_join = this_line[4][-4:]
		yield year_join,1

	def reducer(self, key, values):
		yield key, sum(values)

if __name__ == '__main__':
	MyMapReduceJob.run()
