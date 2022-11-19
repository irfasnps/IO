import requests;
import json;

def list(url,token,name=None):
    Headers = {
        "Authorization":"Bearer "+token,
        "Accept":"application/vnd.synopsys.io.risk-profile-policy-2+json",
        "Content-Type":"application/vnd.synopsys.io.risk-profile-policy-2+json"
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
        "Accept":"application/vnd.synopsys.io.risk-profile-policy-2+json",
        "Content-Type":"application/vnd.synopsys.io.risk-profile-policy-2+json"
    }
    
    # Data1 = {
    #     "description": "Risk Policy Test",
    #     "name": "Test_Policy_using_Library",
    #     "policy": {
    #         "riskProfile": {
    #         "accessibility": {
    #             "value": "Internet",
    #             "weightage": 15
    #         },
    #         "businessCriticality": {
    #             "value": "Critical",
    #             "weightage": 15
    #         },
    #         "changeSignificance": {
    #             "weightage": 15
    #         },
    #         "dataClassification": {
    #             "value": "Highly_Restricted",
    #             "weightage": 25
    #         },
    #         "openVulnerability": {
    #             "weightage": 30
    #         }
    #         },
    #         "riskScale": {
    #         "high": {
    #             "higherBound": 100,
    #             "lowerBound": 81
    #         },
    #         "low": {
    #             "higherBound": 40,
    #             "lowerBound": 0
    #         },
    #         "medium": {
    #             "higherBound": 80,
    #             "lowerBound": 41
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
    url = url+"/api/policy/risk-profile-policies/"+policyId+"/projects"
    print(url)
    payload = json.dumps(Data)
    headers = {
        'Accept': 'application/vnd.synopsys.io.projects-2+json',
        'Content-Type': 'application/vnd.synopsys.io.projects-2+json',
        'Authorization': 'Bearer '+token
    }
    response = requests.patch(url, data=payload, headers=headers)
    return print(response.status_code)

    #attach("https://io11.codedx.synopsys.com/api/ioiq","d454bc40-dac7-4963-80ea-e5429b15c30f","I565ZPTRQNF53FORSGOT3BYCMUDFBLBCM432I56A5453K74NU2IQ====",["50bdecd8-9ce8-4b58-85ff-e30de5f91fed"])