import requests;
import json;
def list(url,token,name=None):
    Headers = {
        "Authorization":"Bearer "+token,
        "Accept":"application/vnd.synopsys.io.prescan-policy-2+json",
        "Content-Type":"application/vnd.synopsys.io.prescan-policy-2+json"
    }
    if name==None:
        response = requests.get(url,headers=Headers)
        return print(response.json())
    else:
        response = requests.get(url+"?name="+name,headers=Headers)
        return print(response.json())

#list("https://io11.codedx.synopsys.com/api/ioiq/api/policy/risk-profile-policies","I565ZPTRQNF53FORSGOT3BYCMUDFBLBCM432I56A5453K74NU2IQ====","Test Policy")


def create(url,token,Data=None):
    Headers = {
        "Authorization":"Bearer "+token,
        "Accept":"application/vnd.synopsys.io.prescan-policy-2+json",
        "Content-Type":"application/vnd.synopsys.io.prescan-policy-2+json"
    }
    
    # Data1={
    #     "description": "Test Pre-Scan policy",
    #     "name": "Pre-Scan Test",
    #     "policy": {
    #         "schedulingPolicy": {
    #         "imageScan": {
    #             "enabled": true,
    #             "threshold": 1
    #         }
    #         },
    #         "scoreRanges": {
    #         "high": {
    #             "dast": true,
    #             "dastplusm": true,
    #             "imageScan": true,
    #             "sast": true,
    #             "sastplusm": true,
    #             "sca": true
    #         },
    #         "low": {
    #             "dast": true,
    #             "dastplusm": true,
    #             "imageScan": true,
    #             "sast": true,
    #             "sastplusm": true,
    #             "sca": true
    #         },
    #         "medium": {
    #             "dast": true,
    #             "dastplusm": true,
    #             "imageScan": true,
    #             "sast": true,
    #             "sastplusm": true,
    #             "sca": true
    #         }
    #         }
    #     }
    # }
    if Data == None:
        print("Please provide Json Data")
        exit()
    response = requests.post(url,headers=Headers,json=Data)
    return print(response.json())

#create("https://io11.codedx.synopsys.com/api/ioiq/api/policy/risk-profile-policies","I565ZPTRQNF53FORSGOT3BYCMUDFBLBCM432I56A5453K74NU2IQ====")

def attach(url,policyId,token, Data=None):
    url = url+"/"+policyId+"/projects"

    payload = json.dumps(Data)
    headers = {
        'Accept': 'application/vnd.synopsys.io.projects-2+json',
        'Content-Type': 'application/vnd.synopsys.io.projects-2+json',
        'Authorization': 'Bearer '+token
    }

    response = requests.patch(url, data=payload, headers=headers)
    return print(response.status_code)
#attach("https://io11.codedx.synopsys.com/api/ioiq/api/policy/prescan-policies","ced5b523-95ce-49be-a43c-ff074e3771e5","I565ZPTRQNF53FORSGOT3BYCMUDFBLBCM432I56A5453K74NU2IQ====",["50bdecd8-9ce8-4b58-85ff-e30de5f91fed"])

def edit(url,policyId,token, Data=None):
    url = url+"/api/policy/risk-profile-policies/"+policyId
    payload = json.dumps(Data)
    headers = {
        'Accept': 'application/vnd.synopsys.io.prescan-policy-2+json',
        'Content-Type': 'application/vnd.synopsys.io.prescan-policy-2+json',
        'Authorization': 'Bearer '+token
    }
    response = requests.patch(url, data=payload, headers=headers)
    return print(response.status_code)

    #edit("https://io11.codedx.synopsys.com/api/ioiq","ced5b523-95ce-49be-a43c-ff074e3771e5","I565ZPTRQNF53FORSGOT3BYCMUDFBLBCM432I56A5453K74NU2IQ====",data)