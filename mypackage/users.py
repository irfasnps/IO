import requests;
import json;

def list(url,token,id=None):
    Headers = {"Authorization":"Bearer "+token,"Content-type":"application/vnd.synopsys.io.user-2+json"}
    if id==None:
        response = requests.get(url,headers=Headers)
    else:
        response = requests.get(url+"?id="+id,headers=Headers)
    return print(response.json())

#list("https://io11.codedx.synopsys.com/api/ioiq/api/auth/users","I565ZPTRQNF53FORSGOT3BYCMUDFBLBCM432I56A5453K74NU2IQ====");

def create(url,token,data):
    Headers = {"Authorization":"Bearer "+token,"Content-type":"application/vnd.synopsys.io.user-2+json"}
    if data==None:
        print("Please provide valid data")
    else:
        payload=json.dumps(data);
        response = requests.post(url, data=payload, headers=Headers)
    return print(response.json())

#users.create("https://io11.codedx.synopsys.com/api/ioiq/api/auth/users","I565ZPTRQNF53FORSGOT3BYCMUDFBLBCM432I56A5453K74NU2IQ====",data)

def edit(url,token,id,data):
    Headers = {"Authorization":"Bearer "+token,"Content-type":"application/vnd.synopsys.io.user-2+json"}
    if id==None:
        print("Please enter user id")
    elif data==None:
        print("Please provide user data")
    else:
        payload=json.dumps("data")
        response = requests.get(url+"/"+id, data=payload, headers=Headers)
    return print(response.json())

#users.edit("https://io11.codedx.synopsys.com/api/ioiq/api/auth/users","I565ZPTRQNF53FORSGOT3BYCMUDFBLBCM432I56A5453K74NU2IQ====","838c381b-7272-4e64-a49e-2c4b158a6b20",data)