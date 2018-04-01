from mrjob.job import MRJob


class MyMapReduceJob(MRJob):

	def mapper(self, _, line):
		user = line.split("\t")
		timestamp = user[4]
		date = timestamp.split(" ")
		bulan = date[0]
		yield  date[-1] , 1

	def reducer(self, key, values):
		yield key, sum(values)


if __name__ == '__main__':
	MyMapReduceJob.run()
