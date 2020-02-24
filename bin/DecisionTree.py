from sklearn import tree
from flask import Flask, request, jsonify
from flask_restful import Resource, Api

class Model:
	def __init__(self):
		self.X = [	[181, 80, 44], [177, 70, 43], [160, 60, 38], 
					[154, 54, 37],[166, 65, 40], [190, 90, 47], [175, 64, 39],
					[177, 70, 40], [159, 55, 37], [171, 75, 42], 
					[181, 85, 43], [168, 75, 41], [168, 77, 41]]
		
		self.Y = [	'male', 'male', 'female', 'female', 'male', 'male',
					'female','female','female', 'male', 'male',
					'female', 'female']

	def training(self, ):
		self.decisionTree = tree.DecisionTreeClassifier()
		self.decisionTree = self.decisionTree.fit(self.X, self.Y)
		return self.decisionTree

	def predicting(self, x):
		model = self.training()
		return model.predict(x)
