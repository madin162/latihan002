from mrjob.job import MRJob
from mrjob.step import MRStep

class MyMapReduceJob (MRJob):

	def mapper(self, _, line):
		this_line = line.split("\t")
		yield this_line[0],this_line[1]


	def reducer(self, key, values):
		yield None, (values, key)

if __name__ == '__main__':
	MyMapReduceJob.run()
