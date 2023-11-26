from flask import Flask , request ,render_template

# from model import extract_facial_features 

app = Flask(__name__ , static_url_path='/static')


@app.route("/webcam"  , methods =["GET", "POST"])
def webcam():
    if request.method == "POST":
    #    Details from the form
       Spic = request.form.get('picture')
       Sname = request.form.get("Name")
       Senroll = request.form.get("Enroll") 
       Sbatch = request.form.get("Batch")
       
    #    features = extract_facial_features(Spic)
       
       

       return "Details :  "+ Spic +  "<br>"+Sname +  " " +Senroll + " " + Sbatch
    return render_template('webcam.html')

@app.route("/")
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
