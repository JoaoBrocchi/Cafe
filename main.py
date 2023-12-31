from flask import Flask, render_template,request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired,Length,URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    url = StringField('url', validators=[URL(),Length(max=200)])
    open_time = StringField('Open time', validators=[DataRequired(), Length(max=200)])
    closing_time = StringField('Closing time', validators=[DataRequired(), Length(max=200)])
    coffe_rating = StringField('Coffe_rating', validators=[DataRequired(), Length(max=200)])
    wifi_rating = StringField('Wifi_rating', validators=[DataRequired(), Length(max=200)])


    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add',methods=['POST', 'GET'])
def add_cafe():
    form = CafeForm()
    cafe = request.form.get("cafe")
    url = request.form.get("url")
    open_time = request.form.get("open_time")
    closing_time = request.form.get("closing_time")
    coffe_rating = request.form.get("coffe_raating")
    wifi_rating = request.form.get("wifi_rating")
    row =[cafe,url,open_time,closing_time,coffe_rating,wifi_rating]
    string =""
    for s in range(len(row)):
        string += row[s]
        string += ","
    f = open("cafe-data.csv", "a")
    f.write(string)

    f.close()
    return render_template('add.html', form=form)

@app.route('/cafes',methods=['POST', 'GET'])
def cafes():
    with open('cafe-data.csv', newline='',encoding="utf8") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html',cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
