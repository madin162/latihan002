from mrjob.job import MRJob


class MyMapReduceJob(MRJob):

	def mapper(self, _, line):
		lastfm = line.split("\t")
		traname = lastfm[5]
		timestamp = lastfm[1]
		waktu = timestamp.split('-')
		tahun = waktu[0]
		bulan = waktu[1]
		yield  traname + "       dimainkan pada  " + tahun + "    jumlahnya = " , 1

	def reducer(self, key, values):
		yield key, sum(values)


if __name__ == '__main__':
	MyMapReduceJob.run()
