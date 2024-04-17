from flask import Flask,request,render_template
import warnings
warnings.filterwarnings('ignore')

application=Flask(__name__)

app=application

## Route for a home page

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    return render_template('index.html')
    

if __name__=="__main__":
    app.run()        


