from mrjob.job import MRJob


class MyMapReduceJob(MRJob):

	def mapper(self, _, line):
		if line:
			yield "Jumlah lagu berbeda (berbeda judul dan/atau berbeda band) yang didengarkan dalam periode waktu tersebut adalah", 1

	def reducer(self, key, values):
		yield key, sum(values)


if __name__ == '__main__':
	MyMapReduceJob.run()
