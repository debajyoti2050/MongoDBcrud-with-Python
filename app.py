from flask import Flask,render_template,request,make_response
import pymongo

def conn():
     myclient=pymongo.MongoClient("mongodb+srv://arijit:Arijit10*@cluster0.gjpbh.mongodb.net/test?retryWrites=true&w=majority")
     mydb=myclient["test"]
     collection=mydb["demo"]
     return collection
        
        
    

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create',methods=['POST'])
def create():
    if request.method=='POST':
        mycol=conn()
        name=request.form.get('name')
        phone=request.form.get('phone')
        email=request.form.get('email')
        address=request.form.get('address')
        list={"name":name,"phone":phone,"email":email,"address":address}
        mycol.insert_one(list)
        return render_template('output.html',dname=name,dphone=phone,dmail=email,dadd=address)
    
    
@app.route('/read',methods=['POST'])
def read():
    if request.method=='POST':
        mycol=conn()
        name=request.form.get('name')
        query={"name":name}
        data=mycol.find_one(query)
        return render_template('read.html',mdata=data)
    
    
@app.route('/update',methods=['POST'])
def update():
    if request.method=='POST':
        mycol=conn()
        name=request.form.get('name')
        newaddr=request.form.get('address')
        query={"name":{"$eq":name}}
        present_data=mycol.find_one(query)
        new_data={'$set':{"address":newaddr}}
        mycol.update_one(present_data,new_data)
        query2={"name":name}
        data=mycol.find_one(query2)
        return render_template('read.html',mdata=data)
        
       
    
    
if __name__=='__main__':
    app.run(debug=True)







