from mrjob.job import MRJob


class SatyaEdit(MRJob):
	def mapper(self, _, line):
		user = line.split("\t")
		genderuser = user[1]
		yield genderuser, 1
	def reducer(self, key, values):
		yield key, sum(values)
		
if __name__ == '__main__':
    SatyaEdit.run()