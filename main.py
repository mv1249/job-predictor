from flask import Flask
import pickle
from flask import render_template,request
app = Flask(__name__)


file = open('employee.pkl','rb')
rf = pickle.load(file)
file.close()

"""
#<!-- 'number_project', 'average_montly_hours', 'time_spend_company',
       'department', 'salary', 'satisfaction_level', 'last_evaluation'],
      dtype='object') -->
"""

@app.route('/',methods = ["GET","POST"])
def hello_world():
    if request.method == "POST":
        my_dict = request.form
        projects = int(my_dict['projects'])
        monthly_hours = int(my_dict['monthly_hours'])
        timespend = int(my_dict['timespend'])
        department = int(my_dict['department'])
        salary = int(my_dict['salary'])
        satisfaction = float(my_dict['satisfaction'])
        last_evaluation = float(my_dict['last_evaluation'])
        input_features = [projects,monthly_hours,timespend,department,salary,satisfaction,last_evaluation]
        inf = rf.predict([input_features])
        if inf == 1:
            inf = "YES"
        else:
            inf = "NO"
        print(inf)
        """predicted = bool(inf)
        print(predicted)
        if predicted == "True":
            inf = "YES"
        elif predicted == "False":
            inf = "NO"
        """
        return render_template('new.html',inf = inf)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)