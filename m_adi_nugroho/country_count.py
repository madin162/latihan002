from mrjob.job import MRJob

class MyMapReduceJob (MRJob):
	def mapper(self, _, line):
		this_line = line.split("\t")
		country_name = this_line[3]
		yield country_name,1

	def reducer(self, key, values):
		yield key, sum(values)

if __name__ == '__main__':
	MyMapReduceJob.run()
