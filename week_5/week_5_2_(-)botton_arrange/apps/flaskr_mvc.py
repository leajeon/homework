# -*- coding: utf-8 -*-
# all the imports

from flask import request, redirect, url_for,\
	render_template
from apps import app
from database import Database

dataStorage = Database()

@app.route('/', methods=['GET', 'POST'])
def show_entries():
	entries = dataStorage.out()
	return render_template('show_entries.html', entries=entries)

@app.route('/add', methods=['POST'])
def add_entry():
	num = 0
	storage={}
	storage["num"] = dataStorage.num
	storage["count"] = 0
	storage["discount"] = 0
	storage['title'] = request.form['title']
	storage['contents'] = request.form['contents']
	
	dataStorage.put(storage)

	dataStorage.num += 1
	return redirect(url_for('show_entries'))

@app.route('/arrange', methods=['GET'])
def arrange_entry():
	dataStorage.database = sorted(dataStorage.database, key = lambda list: list["count"])

	return redirect(url_for("show_entries"))

@app.route('/arrange_x', methods=['GET'])
def arrange_entry_x():
	dataStorage.database = sorted(dataStorage.database, key = lambda list: list["count"], reverse = True)

	return redirect(url_for("show_entries"))

@app.route('/arrange_entry_hata', methods=['GET'])
def arrange_entry_hate():
	dataStorage.database = sorted(dataStorage.database, key = lambda list: list["discount"])

	return redirect(url_for("show_entries"))

@app.route('/arrange_hate_x', methods=['GET'])
def arrange_entry_hate_x():
	dataStorage.database = sorted(dataStorage.database, key = lambda list: list["discount"], reverse = True)

	return redirect(url_for("show_entries"))

@app.route('/del/<idx>', methods=['GET'])
def del_entry(idx):
	for data in dataStorage.database:
		if int(idx) == data["num"]:
			dataStorage.database.remove(data)
			break

	return redirect(url_for("show_entries"))

@app.route('/plus/<idx>', methods=['GET'])
def plus_entry(idx):
	for data in dataStorage.database:
		if int(idx) == data["num"]:
			data["count"] += 1
			break

#	dataStorage.database = sorted(dataStorage.database, key = lambda list: list["count"], reverse = True)

	return redirect(url_for("show_entries"))

@app.route('/minus/<idx>', methods=['GET'])
def minus_entry(idx):
	for data in dataStorage.database:
		if int(idx) == data["num"]:
			data["discount"] += 1
			break

#	dataStorage.database = sorted(dataStorage.database, key = lambda list: list["count"], reverse = True)
	#sorted(첫번째, 두번째, 세번째)기본적으로 오름차순으로 정렬함.

	return redirect(url_for("show_entries"))

@app.route('/modify/<idx>', methods=['GET'])
def modify_entry(idx):
	for data in dataStorage.database:
		if int(idx) == data['num']:
			data['title'] = request.args['title']
			data['contents'] = request.args['contents']
			break

	return redirect(url_for('show_entries'))