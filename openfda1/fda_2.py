import http.client
import json

headers = {'User-Agent': 'http-client'}

conn = http.client.HTTPSConnection("api.fda.gov")
conn.request("GET", "/drug/label.json?limit=10", None, headers)
r1 = conn.getresponse()
print(r1.status, r1.reason)
repos_raw = r1.read().decode("utf-8")
conn.close()

repos = json.loads(repos_raw)
repo1=repos['meta']
repo2=repos['results']


print("That´s the drug id", repo2[0]['openfda']['spl_id'])


print("That´s the drug id", repo2[1]['id'])

print("That´s the drug id", repo2[2]['id'])

print("That´s the drug id", repo2[3]['id'])

print("That´s the drug id", repo2[4]['id'])

print("That´s the drug id", repo2[5]['id'])

print("That´s the drug id", repo2[6]['id'])

print("That´s the drug id", repo2[7]['id'])

print("That´s the drug id", repo2[8]['id'])

print("That´s the drug id", repo2[9]['id'])






