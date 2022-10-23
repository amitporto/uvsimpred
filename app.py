from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)
app.config["SECRET_KEY"] = "mysecret"

st=''

class inputform(FlaskForm):
      d1l1=StringField("Lambda1 of Drug_1")
      d1l2=StringField("Lambda1 of Drug_2")
      d2l1=StringField("Lambda2 of Drug_1")
      d2l2=StringField("Lambda2 of Drug_2")
      ul1=StringField("Lambda1 of Unknown")
      ul2=StringField("Lambda2 of Unknown")
      conc=StringField("Concentration(in µg/ml)")
      submit=SubmitField("Submit")


def calc_sim(d1l1,d1l2,d2l1,d2l2,ul1,ul2,conc):
    ad1l1=d1l1/conc
    ad1l2=d1l2/conc
    ad2l1=d2l1/conc
    ad2l2=d2l2/conc
    conc1=(ul2*ad2l1 - ul1*ad2l2)/(ad1l2*ad2l1-ad1l1*ad2l2)
    conc2=(ul1*ad1l2 - ul2*ad1l1)/(ad1l2*ad2l1-ad1l1*ad2l2)
    return conc1,conc2

@app.route("/", methods=["GET","POST"])

def index():
    input=inputform()
    strn1, strn2='', ''
    d1l1,d1l2,d2l1,d2l2,ul1,ul2,conc='','','','','','',''
    if input.validate_on_submit():
       strn1=strn1+str(calc_sim(float(request.form["d1l1"]),float(request.form["d1l2"]),float(request.form["d2l1"]),float(request.form["d2l2"]),
       float(request.form["ul1"]),float(request.form["ul2"]),float(request.form["conc"]))[0])
       strn2=strn2+str(calc_sim(float(request.form["d1l1"]),float(request.form["d1l2"]),float(request.form["d2l1"]),float(request.form["d2l2"]),
       float(request.form["ul1"]),float(request.form["ul2"]),float(request.form["conc"]))[1])
    return render_template('index.html', template_form=input, template_list1=strn1,template_list2=strn2)


if __name__=='__main__':
  app.run(debug=True)
