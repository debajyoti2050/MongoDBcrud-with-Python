from flask import Flask,render_template,request,make_response
import pymongo
import numpy


def conn():
     myclient=pymongo.MongoClient(" use your own connection key here")
     mydb=myclient["use your cluster name"]
     collection=mydb["your collection name"]
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
        try:
            #mydb.db[mydb.mongo_collection].create_index("user_id", unique=True)
            #mycol.create_index("user_id",unique=True)        ######## must be used only once ######
            list={"user_id":userid,"name":name,"phone":phone,"email":email,"address":address}
            mycol.insert_one(list)
            return render_template('output.html',dname=name,dphone=phone,dmail=email,dadd=address)
        except:
            return render_template('error.html')
        
            
    
    
@app.route('/read',methods=['POST'])
def read():
    if request.method=='POST':
        mycol=conn()
        id=request.form.get('id')
        query={"user_id":id}
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
        dropvalue=int(request.form.get('fvalue'))
        #dropvalue=int(dvalue)
        #print(type(dropvalue))
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
            
           
        return render_template('update.html',mdata=data)    
        
        
            
        
       ## mycol.update_one(present_data,new_data)
        #query2={"user_id":userid}
        #data=mycol.find_one(query2)
       # return render_template('read.html',mdata=data)#
    
    
@app.route('/delete',methods=['POST'])
def delete():
    if request.method=='POST':
        mycol=conn()
        uid=request.form.get('uid')
        query={"user_id":uid}
        mycol.delete_one(query)
        return render_template('delete.html')
        
       
    
    
if __name__=='__main__':
    app.run(debug=True)







