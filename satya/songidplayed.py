from mrjob.job import MRJob


class SatyaEdit(MRJob):
	def mapper(self, _, line):
		userid = line.split("\t")
		user = userid[4]
		yield user, 1
	def reducer(self, key, values):
		yield key, sum(values)
		
if __name__ == '__main__':
    SatyaEdit.run()