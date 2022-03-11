from flask import Flask
from flask import request
from crypt import methods

app = Flask(__name__)

list = {'Ashe':109,'Nasus':126,'Veigar':98,'Akali':118,'Varus':118,'Xayah':119}

@app.route("/getserv", methods=['GET'])
def len_league():
    return f"List lenght: {len(list.keys())}\n {list} \n"

@app.route("/addtoserv", methods=['GET','POST'])
def add_to_list():
    champion = str(request.form['champion'])
    power = int(request.form['power'])
    if champion in lit.keys():
        return "Champion is already in the list!\n"
    else:
        list[champion] = power
        return "Champion {hampion} added to the list.Power value: {power}\n"
    return "Done"

@app.route("/putinfo", methods=['PUT'])
def change_power():
    champion = str(request.form['champion'])
    power = int(request.form['power'])
    if champion in lit.keys():
        list[champion] = power
        return f"Champions power changed"
    else:
        return "No champion found"
    return "Done"

app.run(host='0.0.0.0', port=5000)