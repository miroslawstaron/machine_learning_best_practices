# 
# Flask application to count lines of code in a file
#
from fileinput import filename 
from flask import *  
app = Flask(__name__)   

# dictionary to store the metrics for the file submitted
# metrics: lines of code
metrics = {}
  
# method to render the index.html page
@app.route('/')   
def main():   
    return render_template("index.html")    


# method to upload the file and count the lines of code
@app.route('/success', methods = ['POST'])   
def success():   
    if request.method == 'POST':   
        f = request.files['file'] 

        # save the file to the server
        f.save(f.filename)
        
        # count the lines in the file
        lines = sum(1 for line in open(f.filename))
        
        # store the metrics in the dictionary
        metrics[f.filename] = lines   

        # return the metrics for the file
        return {f.filename: metrics[f.filename]}  

# method to return the metrics for all files
# that were counted in this session
# mostly for debugging purposes
@app.route('/metrics', methods = ['GET'])
def get_metrics():
    if request.method == 'GET':
        return metrics

# run the application
if __name__ == '__main__':   
    app.run(host='0.0.0.0', debug=True)