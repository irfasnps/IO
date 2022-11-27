import requests;
import json;
def list(url,token,name=None):
    Headers = {
        "Authorization":"Bearer "+token
    }
    if name==None:
        response = requests.get(url,headers=Headers)
        return print(response.json())
    else:
        response = requests.get(url+"?name="+name,headers=Headers)
        return print(response.json())

#postscanPolicy.list("https://io11.codedx.synopsys.com/api/ioiq/api/policy/post-scan-policies","I565ZPTRQNF53FORSGOT3BYCMUDFBLBCM432I56A5453K74NU2IQ====","Synopsys Default")

def create(url,token,Data=None):
    Headers = {
        "Authorization":"Bearer "+token,
        "Content-Type":"application/vnd.synopsys.io.post-scan-policy-2+json"
    }
    
    # Data = {
    # "description": "Test Post Scan Policy",
    # "name": "Post Scan Policy Test from Postman",
    # "postScanRules": {
    #     "asocRules": [
    #     {
    #         "action": "BREAK_THE_BUILD",
    #         "asocScore": 0,
    #         "enabled": true
    #     }
    #     ],
    #     "cveRules": [],
    #     "issueClassificationRules": [
    #     {
    #         "classificationName": "2020 CWE Top 25",
    #         "vulnerabilities": [
    #         {
    #             "actions": [
    #             {
    #                 "action": "BREAK_THE_BUILD",
    #                 "enabled": true,
    #                 "issueCountThreshold": 10
    #             }
    #             ],
    #             "categoryName": "Improper Control of Generation of Code ('Code Injection')"
    #         }
    #         ]
    #     }
    #     ],
    #     "severityRules": [
    #     {
    #         "action": "BREAK_THE_BUILD",
    #         "activities": [],
    #         "enabled": true,
    #         "severity": [
    #         "HIGH"
    #         ]
    #     }
    #     ]
    # }
    # }

    if Data == None:
        print("Please provide Json Data")
        exit()
    response = requests.post(url,headers=Headers,json=Data)
    return print(response.json())
    # postscanPolicy.create("https://io11.codedx.synopsys.com/api/ioiq/api/policy/post-scan-policies","I565ZPTRQNF53FORSGOT3BYCMUDFBLBCM432I56A5453K74NU2IQ====",data) 

def delete(url,policyId,token):
    url = url+"/api/policy/post-scan-policies/"+policyId
    headers = {
        'Authorization': 'Bearer '+token
    }
    payload = {}
    response = requests.delete(url, data=payload, headers=headers)
    return print(response.text)

#policy.delete("https://io11.codedx.synopsys.com/api/ioiq/","1559957a-efb0-4b38-8ad1-4096c098bcb0","I565ZPTRQNF53FORSGOT3BYCMUDFBLBCM432I56A5453K74NU2IQ====") 

def edit(url,token,policyId,Data=None):
    Headers = {
        "Authorization":"Bearer "+token,
        "Content-Type":"application/vnd.synopsys.io.post-scan-policy-2+json"
    }
    url = url+"/api/policy/post-scan-policies/"+policyId
    # Data = {
    # "description": "Test Post Scan Policy",
    # "name": "Post Scan Policy Test from Postman",
    # "postScanRules": {
    #     "asocRules": [
    #     {
    #         "action": "BREAK_THE_BUILD",
    #         "asocScore": 0,
    #         "enabled": true
    #     }
    #     ],
    #     "cveRules": [],
    #     "issueClassificationRules": [
    #     {
    #         "classificationName": "2020 CWE Top 25",
    #         "vulnerabilities": [
    #         {
    #             "actions": [
    #             {
    #                 "action": "BREAK_THE_BUILD",
    #                 "enabled": true,
    #                 "issueCountThreshold": 10
    #             }
    #             ],
    #             "categoryName": "Improper Control of Generation of Code ('Code Injection')"
    #         }
    #         ]
    #     }
    #     ],
    #     "severityRules": [
    #     {
    #         "action": "BREAK_THE_BUILD",
    #         "activities": [],
    #         "enabled": true,
    #         "severity": [
    #         "HIGH"
    #         ]
    #     }
    #     ]
    # }
    # }

    if Data == None:
        print("Please provide Json Data")
        exit()
    response = requests.patch(url,headers=Headers,json=Data)
    return print(response.json())

#postscanPolicy.edit("https://io11.codedx.synopsys.com/api/ioiq","I565ZPTRQNF53FORSGOT3BYCMUDFBLBCM432I56A5453K74NU2IQ====","de999146-30a3-454c-bb7c-10528e312e37",data)

def attach(url,policyId,token, Data=None):
    url = url+"/"+policyId+"/projects"

    payload = json.dumps(Data)
    headers = {
        'Accept': 'application/vnd.synopsys.io.projects-2+json',
        'Content-Type': 'application/vnd.synopsys.io.projects-2+json',
        'Authorization': 'Bearer '+token
    }

    response = requests.post(url, data=payload, headers=headers)
    return print(response.status_code)
#postscanPolicy.attach("https://io11.codedx.synopsys.com/api/ioiq/api/policy/post-scan-policies","de999146-30a3-454c-bb7c-10528e312e37","I565ZPTRQNF53FORSGOT3BYCMUDFBLBCM432I56A5453K74NU2IQ====",["2f6d112e-4e73-4cb7-b249-f93fdf39bb64"])

def editAttach(url,policyId,token, Data=None):
    url = url+"/"+policyId+"/projects"

    payload = json.dumps(Data)
    headers = {
        'Accept': 'application/vnd.synopsys.io.projects-2+json',
        'Content-Type': 'application/vnd.synopsys.io.projects-2+json',
        'Authorization': 'Bearer '+token
    }

    response = requests.post(url, data=payload, headers=headers)
    return print(response.status_code)
#postscanPolicy.editAttach("https://io11.codedx.synopsys.com/api/ioiq/api/policy/post-scan-policies","de999146-30a3-454c-bb7c-10528e312e37","I565ZPTRQNF53FORSGOT3BYCMUDFBLBCM432I56A5453K74NU2IQ====",["2f6d112e-4e73-4cb7-b249-f93fdf39bb64"])
def listSCMEventRules(url,token,name=None):
    Headers = {
        "Authorization":"Bearer "+token
    }
    if name==None:
        response = requests.get(url,headers=Headers)
        return print(response.json())
    else:
        response = requests.get(url+"?name="+name,headers=Headers)
        return print(response.json())