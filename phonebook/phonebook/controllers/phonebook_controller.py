
from flask import Flask, render_template,request,redirect,session

from phonebook import app

# from .. models.dojo import Dojo
# from .. models.ninja import Ninja

import json

# function to add to JSON
def update_phone_book(new_contact, filename='phonebook.json'):
	with open(filename,'r+') as file:
		# First we load existing data into a dict.
		phone_data = json.load(file)
		# Add new contact
		phone_data.append(new_contact)
		# Sets file's current position at offset.
		#replace record with updated record
		file.seek(0)
		# convert back to json.
		json.dump(phone_data, file, indent = 4)

def get_contacts(filename='phonebook.json'):
	with open(filename,'r') as file:
		phone_data = json.load(file)
	return phone_data

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/allcontact")
def show_contacts():
	values = get_contacts()
	return render_template("all_contact.html", all_contacts = values)

@app.route("/getcontact", methods=['post', 'get'])
def get_contact_form():
	if request.method == "POST":
		name = request.form.get('name')
		contacts = [k for k in get_contacts() if k['Name'] == name]
		if len(contacts) > 0:
			return render_template("contact.html", contacts=contacts)
		else:
			return render_template("index.html", missing_name=name)
	return render_template("index.html")

@app.route("/newcontact", methods=['post', 'get'])
def new_contact_form():
	if request.method == "POST":
		return redirect('/contact')
	return render_template("new_contact.html")