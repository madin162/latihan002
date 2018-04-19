from mrjob.job import MRJob


class MyMapReduceJob(MRJob):

	def mapper(self, _, line):
		main_table = line.split("\t")
		userid = main_table[0]
		traname = main_table[5]
		yield userid + " played song " + traname + ", in the following number times =",1

	def reducer(self, key, values):
		yield key, sum(values)


if __name__ == '__main__':
	MyMapReduceJob.run()