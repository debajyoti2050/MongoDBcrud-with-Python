from flask import Flask,render_template,request,make_response
import pymongo
import numpy

def conn():
     myclient=pymongo.MongoClient("mongodb://debajyoti:admin@debajyotidb-shard-00-00.bpiim.mongodb.net:27017,debajyotidb-shard-00-01.bpiim.mongodb.net:27017,debajyotidb-shard-00-02.bpiim.mongodb.net:27017/crudapp?ssl=true&replicaSet=atlas-r19gla-shard-0&authSource=admin&retryWrites=true&w=majority")
     mydb=myclient["crudapp"]
     collection=mydb["test4"]
     return collection
#def create_index():
  #  mycol=conn()
   # mycol.create_index("user_id:1",unique=True)
            
        
    

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create',methods=['POST'])
def create():
    if request.method=='POST':
        mycol=conn()
        userid=request.form.get('userid')
        name=request.form.get('name')
        phone=request.form.get('phone')
        email=request.form.get('email')
        address=request.form.get('address')
        #mydb.db[mydb.mongo_collection].create_index("user_id", unique=True)
        #mycol.create_index("user_id",unique=True)        ######## must be used only once ######
        list={"user_id":userid,"name":name,"phone":phone,"email":email,"address":address}
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
        #name=request.form.get('name')
        userid=request.form.get('userid')
        newinfo=request.form.get('info')
        query={"user_id":{"$eq":userid}}
        present_data=mycol.find_one(query)
        dropvalue=request.form.get('fvalue')
        print(dropvalue)
        #print(present_data)
        if (dropvalue==1):
            new_data={'$set':{"name":newinfo}}
            mycol.update_one(present_data,new_data)
            query2={"user_id":userid}
            data=mycol.find_one(query2)
            
        elif (dropvalue==2):
            new_data={'$set':{"phone":newinfo}}
            mycol.update_one(present_data,new_data)
            query2={"user_id":userid}
            data=mycol.find_one(query2)
            
        elif (dropvalue==3):
            new_data={'$set':{"email":newinfo}}
            mycol.update_one(present_data,new_data)
            query2={"user_id":userid}
            data=mycol.find_one(query2)
            
        else:
            new_data={'$set':{"address":newinfo}}
            mycol.update_one(present_data,new_data)
            query2={"user_id":userid}
            data=mycol.find_one(query2)
           
        return render_template('read.html',mdata=data)    
        
        
            
        
       ## mycol.update_one(present_data,new_data)
        #query2={"user_id":userid}
        #data=mycol.find_one(query2)
       # return render_template('read.html',mdata=data)#
    
    
@app.route('/delete',methods=['POST'])
def delete():
    if request.method=='POST':
        mycol=conn()
        name=request.form.get('name')
        query={"name":name}
        data=mycol.delete_one(query)
        return render_template('read.html',mdata=data)
        
       
    
    
if __name__=='__main__':
    app.run(debug=True)







