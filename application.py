from flask import Flask, render_template, request, jsonify, redirect
import os
from bin.DecisionTree import Model
import pandas as pd
import matplotlib.pyplot as plt

server = Flask(__name__)
model = Model()

@server.route('/main_index', methods = ['GET',])
def main_body():
	return render_template('main_body.html')


@server.route('/', methods = ['GET', 'POST'])
def running_tasks():

	if request.method == 'GET':
		return render_template('index.html')

	elif request.method == 'POST':
		
		user_input = request.form.getlist('userInput[]')

		if len(user_input) > 0:
			result = model.predicting([user_input])[0]
			if result == 'male':
				return render_template('male.html')
			elif result == 'female':
				return render_template('female.html')

		inputFile = request.files['userFile']

		if inputFile.filename == '':
			return redirect(request.url)

		fName = inputFile.filename
		data = open(inputFile.filename, 'r').readlines()
		X, Y = [], []

		for line in data:
			line = line.replace('\n', '').split(',')
			X.append(line[0])
			Y.append(line[-1])

		plt.plot(X, Y)
		plt.xlabel('Bedrooms')
		plt.ylabel('Price')
		plt.savefig('static/images/plot_result.jpg')

		return render_template('plotting_result.html')


	return render_template('index.html')



if __name__ == "__main__":
	server.run(debug = True)


