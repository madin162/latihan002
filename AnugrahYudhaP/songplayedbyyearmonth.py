from mrjob.job import MRJob


class MyMapReduceJob(MRJob):

	def mapper(self, _, line):
		lastfm = line.split("\t")
		waktu = lastfm[1]
		nama_lagu = lastfm[5]
		pisah = waktu.split('-')
		tahun = pisah[0]
		bulan = pisah[1]
		month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
		yield "Total number of tracks played for year " + tahun + " on month " + month[int(bulan) - 1] + " is", 1

	def reducer(self, key, values):
		yield key, sum(values)


if __name__ == '__main__':
	MyMapReduceJob.run()
