from flask import Flask , request ,render_template
from PIL import Image
app = Flask(__name__)


@app.route("/add"  , methods =["GET", "POST"])
def webcam():
    if request.method == "POST":
    #    Details from the form
       Spic = request.form.get('picture')
       Sname = request.form.get("Name")
       Senroll = request.form.get("Enroll") 
       Sbatch = request.form.get("Batch")
       
       
       return "Details :  "+ Spic +  "<br>"+Sname +  " " +Senroll + " " + Sbatch
    return render_template('webcam.html')

@app.route("/")
def index():
    return "This is main page "


if __name__ == '__main__':
    app.run()
