from mrjob.job import MRJob


class MyMapReduceJob(MRJob):

	def mapper(self, _, line):
		if line:
			yield "Jumlah aktivitas berbeda/unik (bukan perulangan lagu) yang tercatat oleh sistem dalam periode waktu tersebut adalah sejumlah", 1

	def reducer(self, key, values):
		yield key, sum(values)


if __name__ == '__main__':
	MyMapReduceJob.run()
