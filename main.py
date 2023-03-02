# from crypt import methods
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from flask import Flask, render_template,send_file,request
from io import BytesIO
import base64

from func import *

# lis=0
app = Flask(__name__)
@app.route('/images/<cropzonekey>',methods=["GET","POST"])
def images(cropzonekey):
    # kk=0
    if request.method=="POST":
        cropzonekey=request.form["foo"]
        # figr = plotFunc(kk)
        # print(kk)

    return render_template("images.html", title=cropzonekey,cropzonekey=cropzonekey)

@app.route('/fig/<cropzonekey>')
def fig(cropzonekey):
    # fig=plotFunc(cropzonekey)
    num=[cropzonekey]*4
    fig = plt.plot(num, [1,2,3,4])
    img = BytesIO()
    plt.savefig(img)
    img.seek(0)
    return send_file(img, mimetype='image/png',num=num[0])

  
  

if __name__ == '__main__':
    app.run(debug=True)
