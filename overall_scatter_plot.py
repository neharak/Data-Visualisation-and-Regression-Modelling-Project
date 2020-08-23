import csv
from collections import defaultdict
import numpy
import matplotlib.pyplot as plt


columns = defaultdict(list)
with open('./demo.csv') as f:
	reader = csv.DictReader(f)
	for row in reader:
		for (k,v) in row.items():
			columns[k].append(v)

#x = numpy.array(columns['NovaR']).astype(numpy.float)
y = numpy.array(columns['ph']).astype(numpy.float)
#a = numpy.array(columns['NovaG']).astype(numpy.float)
b = numpy.array(columns['NovaB']).astype(numpy.float)
temp1 = numpy.divide(b - 61.931,31.917)
temp2 = numpy.divide(numpy.sqrt(b) - 7.602, 2.035)
temp3 = numpy.divide(numpy.log10(b) - 1.7284, 0.247)
print(temp1)
print(temp2)
print(temp3)
#y2 = 7.5732 - (0.0004224 * temp1 ) + (0.767972 * temp2)
y2 = 7.5732 - (0.02845 * temp1 ) + (0.3688 * temp2) + (0.4408 * temp3)
print(y2)
#plt.scatter(x, y, color = 'red')
#plt.scatter(a, y, color = 'green')
plt.scatter(b, y, color = 'blue')
plt.plot(b, y2 , color = 'black')
plt.show()
ssr = numpy.sum((y2 - y)**2)
sst = numpy.sum((y - numpy.mean(y))**2)
print(ssr)
print(sst)
r2 = 1 - (ssr/sst)
print(r2)
