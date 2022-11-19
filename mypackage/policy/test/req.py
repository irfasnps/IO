import requests
import json

url = "https://io11.codedx.synopsys.com/api/ioiq/api/policy/prescan-policies/ced5b523-95ce-49be-a43c-ff074e3771e5/projects"

payload = json.dumps([
  "50bdecd8-9ce8-4b58-85ff-e30de5f91fed"
])
headers = {
  'Accept': 'application/vnd.synopsys.io.projects-2+json',
  'Content-Type': 'application/vnd.synopsys.io.projects-2+json',
  'Authorization': 'Bearer I565ZPTRQNF53FORSGOT3BYCMUDFBLBCM432I56A5453K74NU2IQ===='
}

response = requests.patch(url, data=payload, headers=headers)

print(response.text)