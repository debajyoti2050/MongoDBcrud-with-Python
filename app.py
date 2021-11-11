from flask import Flask,render_template,request,make_response
import pymongo

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create',methods=['POST'])
def create():
    if request.method=='POST':
        myclient=pymongo.MongoClient("mongodb+srv://debajyoti:admin@crudapp.bpiim.mongodb.net/crudapp?retryWrites=true&w=majority")
        mydb=myclient["crudapp"]
        mycol=mydb["information"]
        name=request.form.get('name')
        phone=request.form.get('phone')
        email=request.form.get('email')
        address=request.form.get('address')
        list={"name":name,"phone":phone,"email":email,"address":address}
        mycol.insert_one(list)
        return render_template('output.html',dname=name,dphone=phone,dmail=email,dadd=address)
    
    
if __name__=='__main__':
    app.run(debug=True)







