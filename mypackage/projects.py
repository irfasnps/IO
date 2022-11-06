import requests;

def list(url,token,id=None):
    Headers = {"Authorization":"Bearer "+token}
    if id==None:
        response = requests.get(url,headers=Headers)
    else:
        response = requests.get(url+"?id="+id,headers=Headers)
    return print(response.json())
#list("https://io11.codedx.synopsys.com/api/ioiq/api/portfolio/projects","I565ZPTRQNF53FORSGOT3BYCMUDFBLBCM432I56A5453K74NU2IQ====");




def create(url,token):
    Headers = {
            "Authorization":"Bearer "+token,
            "Accept":"application/vnd.synopsys.io.projects-2+json",
            "Content-Type":"application/vnd.synopsys.io.projects-2+json"
            }
    Data = {
    "name": "JDTI",
    "projectType": "WEB_APPLICATION",
    "projectLanguage": "JAVA",
    "platformVersion": "JAVA8",
    "buildSystem": "MAVEN",
    "fileChangeThreshold": 10,
    "sourceFilePattern": ".*\/src\/.*",
    "sensitivePackagePattern": ".*(\\+\\+\\+.*(\/((a|A)pp|(c|C)rypto|(a|A)uth|(s|S)ec|(l|L)ogin|(p|P)ass|(o|O)auth|(t|T)oken|(i|I)d|(c|C)red|(s|S)aml|(c|C)ognito|(s|S)ignin|(s|S)ignup|(a|A)ccess))).*",
    "riskProfilePolicyId": "777f9880-a996-4a0c-8bcd-b13cd717ff43",
    "prescanPolicyId": "fe13146c-1032-400b-8c3c-8e896fcbf46e",
    "pipelineInformation": {}    
    }
    response = requests.post(url,headers=Headers,json=Data)
    return print(response.json())

create("https://io11.codedx.synopsys.com/api/ioiq/api/portfolio/projects","I565ZPTRQNF53FORSGOT3BYCMUDFBLBCM432I56A5453K74NU2IQ====")