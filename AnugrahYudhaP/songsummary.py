from mrjob.job import MRJob


class MyMapReduceJob(MRJob):

	def mapper(self, _, line):
		lastfm = line.split("\t")
		nama_lagu = lastfm[5]
		yield nama_lagu, 1

	def reducer(self, key, values):
		yield key, sum(values)


if __name__ == '__main__':
	MyMapReduceJob.run()
