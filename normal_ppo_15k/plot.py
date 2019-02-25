''' Script to plot results of SpinningUp Tests author: Chirag date: 14-02-2019 '''
from matplotlib import pyplot as plt
import sys
import json
if len(sys.argv) < 2:
	print('Please enter the path of progress.txt as an argument') 
else:
	path = sys.argv[1]
	title = ''
	with open(path + '/config.json', 'r') as config_file:
		config = json.loads(config_file.read())
		title = config['exp_name']
	x_axis, y_axis = [], []
	with open(path + '/progress.txt', 'r') as data_file:
		x_label, y_label = data_file.readline().split()[:2]
		for line in data_file:
			x_axis.append(float(line.split()[0]))
			y_axis.append(float(line.split()[1]))
	plt.title(title)
	plt.xlabel(x_label)
	plt.ylabel(y_label)
	graph, = plt.plot(x_axis, y_axis)
	graph.set_color('orange')
	plt.show()
