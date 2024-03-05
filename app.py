# import flask 

from flask import Flask,request,make_response,render_template
import pickle
# create Falsk 
app = Flask(__name__);

# create end points 
@app.route("/")
def home():
    return render_template('index.html',message="Welcome")
@app.route('/login', methods=["POST"])
def login():
    username = request.form['username']
    return       "Login success"+username
@app.route("/<ename>")
def index(ename):
    return "<h1>Hello World"+ename+"</h1>";
#------------------------------------
@app.route("/post", methods=["POST"])
def postMethod():
    # name = request.args['name']
      
     loanapplication=request.get_json();
     
     print(loanapplication)
     status = isEligibleforLoan(loanapplication)
     if status==1:
         return "<h1>Eligible for loan</h1>"
     else :

        return "<h1>Not Eligible for loan</h1>"



def isEligibleforLoan(loan):
   
      # open the file in rb 
    with open('logisticloan.pkl',"rb") as f:
        model = pickle.load(f)
       # load that file using pickle
       #  call predict funtion 
        result= model.predict([[loan['dependents'],loan['education'],loan['income'],loan['amount'],loan['credithistory'],loan['area']]])
        print(result[0])
        return result[0]
# Run the application

@app.route("/user",methods=["POST"])
def createUser():
    res = make_response("User created",201)
    return res;

if __name__=="__main__":
    
    app.run(debug=True)
