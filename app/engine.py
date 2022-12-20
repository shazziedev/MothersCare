from flask import Flask,render_template

app = Flask(__name__,template_folder='templates')

@app.route('/')
def home():
    return render_template('index.html')


# RISK REGISTER 
@app.route('/risk-register/demographics/')
def riskRegDemo():
    return render_template('risk_register/demographics.html')

@app.route('/risk-register/details/')
def riskRegDetail():
    return render_template('risk_register/details.html')

@app.route('/risk-register/feedback/')
def riskRegFeedback():
    return render_template('risk_register/demographics2.html')


# REFERAL AND FEEDBACK 
# demographics 
@app.route('/referal/demographics/')
def referalDemo():
    return render_template('referal_feedback/demographic/demo.html')

# physical examination 
@app.route('/referal/demographics/data/')
def referalDemoData():
    return render_template('referal_feedback/demographic/data.html')

@app.route('/referal/physical/examination/')
def referalPEgeneral():
    return render_template('referal_feedback/physical_examination/general_examination.html')

@app.route('/referal/physical/examination/data/')
def referalPEurinalysis():
    return render_template('referal_feedback/physical_examination/data.html')

# abdominal examination 
@app.route('/referal/abdominal/examination/')
def referalAbdominalExam():
    return render_template('referal_feedback/abdominal_examination/abdominal_exam.html')




