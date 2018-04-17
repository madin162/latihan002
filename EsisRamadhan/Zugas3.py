from mrjob.job import MRJob
import re
regex=r"([a-zA-Z]+) (\d+)"
class MyMapReduceJob(MRJob):
	def mapper(self, _, line):
		pecahan = line.split("\t")
		if re.search(regex,"Jan")=="Jan":
			pecahan[1]="January"
		elif re.search(regex,"Feb")=="Feb":
			pecahan[1]="February"
		elif re.search(regex,"Mar")=="Mar":
			pecahan[1]="March"
		elif re.search(regex,"Apr")=="Apr":
			pecahan[1]="April"
		elif re.search(regex,"May")=="May":
			pecahan[1]="May"
		elif re.search(regex,"Jun")=="Jun":
			pecahan[1]="June"
		elif re.search(regex,"Jul")=="Jul":
			pecahan[1]="July"
		elif re.search(regex,"Aug")=="Aug":
			pecahan[1]="August"
		elif re.search(regex,"Sep")=="Sep":
			pecahan[1]="September"
		elif re.search(regex,"Oct")=="Oct":
			pecahan[1]="October"
		elif re.search(regex,"Nov")=="Nov":
			pecahan[1]="November"
		else:
			pecahan[1]="December"
		time=pecahan[1]
		song=pecahan[5]
		yield "Dates="+time+"__"+"Lagu="+song,1
	def reducer(self, key, values):
        	yield key, sum(values)
if __name__ == '__main__':
    MyMapReduceJob.run()
