from flask import Flask
from flask import request
from flask import render_template
from time import sleep
from random import random
import sudoku
import sys


def dic_to_sud(d):
	sud = []
	for i in range(9):
		tmp = []
		for j in range(9):
			k = str(i)+str(j)
			tmp.append(int(d[k]))
		sud.append(tmp)
	return sud


def print_sud(sud):
	result = "<br>"
	for a in range(len(sud)):
		result += " " * 5
		for b in range(len(sud)):
			result += str(sud[a][b]) + "  "
			if b in [2, 5]:
				result += '|'
		if a in [2, 5]:
			result += "<br>"+" " * 5+"- " * 15
		result += "<br>"
	return result


app = Flask(__name__)


@app.route('/')
def sendform():
	return render_template('sudoku_form.html')


@app.route('/sudoku_solve', methods=['POST'])
def recvform():
	d = request.form
	sud = dic_to_sud(d)
	ans, _, _ = sudoku.specSolve(sud)
	resp = "<h1>Solution:</h1>"
	resp += print_sud(ans)
	resp += "<a href='/sudoku_form'>Back</a><br>"
	return resp



if __name__ == '__main__':
	port = 5000
	if len(sys.argv) > 1:
		port = int(sys.argv[1])
	app.run(debug=True, port=port)