from mrjob.job import MRJob


class MyMapReduceJob(MRJob):

	def mapper(self, _, line):
		main_table = line.split("\t")
		traname = main_table[5]
		artname = main_table[3]
		yield traname + " performed by " + artname + ", in the following number times =",1

	def reducer(self, key, values):
		yield key, sum(values)


if __name__ == '__main__':
	MyMapReduceJob.run()