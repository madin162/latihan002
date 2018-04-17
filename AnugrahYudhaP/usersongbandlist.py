from mrjob.job import MRJob


class MyMapReduceJob(MRJob):

	def mapper(self, _, line):
		lastfm = line.split("\t")
		user_id = lastfm[0]
		nama_lagu = lastfm[5]
		nama_band = lastfm[3]
		yield user_id + " listened to " + nama_lagu + " by " + nama_band + " as many as", 1

	def reducer(self, key, values):
		yield key, sum(values)


if __name__ == '__main__':
	MyMapReduceJob.run()
