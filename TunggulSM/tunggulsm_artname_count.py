from mrjob.job import MRJob


class MyMapReduceJob(MRJob):

	def mapper(self, _, line):
		table_artname = line.split("\t")
		artname = table_artname[3]
		yield artname, 1

	def reducer(self, key, values):
		yield key, sum(values)


if __name__ == '__main__':
	MyMapReduceJob.run()