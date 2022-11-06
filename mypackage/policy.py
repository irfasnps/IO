import requests;

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


def create(url,token):
    Headers = {
        "Authorization":"Bearer "+token,
        "Accept":"application/vnd.synopsys.io.risk-profile-policy-2+json",
        "Content-Type":"application/vnd.synopsys.io.risk-profile-policy-2+json"
    }
    
    Data = {
        "description": "Risk Policy Test",
        "name": "Test_Policy_using_Library",
        "policy": {
            "riskProfile": {
            "accessibility": {
                "value": "Internet",
                "weightage": 15
            },
            "businessCriticality": {
                "value": "Critical",
                "weightage": 15
            },
            "changeSignificance": {
                "weightage": 15
            },
            "dataClassification": {
                "value": "Highly_Restricted",
                "weightage": 25
            },
            "openVulnerability": {
                "weightage": 30
            }
            },
            "riskScale": {
            "high": {
                "higherBound": 100,
                "lowerBound": 81
            },
            "low": {
                "higherBound": 40,
                "lowerBound": 0
            },
            "medium": {
                "higherBound": 80,
                "lowerBound": 41
            }
            }
        }
    }

    response = requests.post(url,headers=Headers,json=Data)
    return print(response.json())

create("https://io11.codedx.synopsys.com/api/ioiq/api/policy/risk-profile-policies","I565ZPTRQNF53FORSGOT3BYCMUDFBLBCM432I56A5453K74NU2IQ====")