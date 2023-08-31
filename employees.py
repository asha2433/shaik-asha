# Exercise1 : Write a GET Rest API using Python.

from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data for demonstration
Employees = [
{"Employee_id":111,"Employee_name":"Asha", "Date_of_joining":"01.01.2000", "years_of_experience":"5"},
{"Employee_id":222,"Employee_name":"uday", "Date_of_joining":"01.01.2001", "years_of_experience":"4"},
{"Employee_id":333,"Employee_name":"Bhuvana", "Date_of_joining":"01.01.2002", "years_of_experience":"5"},
{"Employee_id":444,"Employee_name":"Diksha", "Date_of_joining":"01.01.2002", "years_of_experience":"6"},
{"Employee_id":555,"Employee_name":"Dinesh", "Date_of_joining":"01.01.2004", "years_of_experience":"5"},
]

@app.route('/', methods=['GET'])
def get():
    return jsonify(Employees)

@app.route('/<Employee_name>', methods=['GET'])
def get_Employees(Employee_name):
    
    return jsonify(Employee_name)

if __name__ == '__main__':
    app.run(debug=True)
