import http.client

conn  = http.client.HTTPConnection('www.google.com', 80)
conn.request("OPTIONS", "/")
r2 = conn.getresponse()
print(r2.status, r2.reason, r2.version)
headers = r2.getheaders()
for header in headers:
    print(header)
data = r2.read()
print("**********************************************************************")
conn.request("HEAD", "/")
r2 = conn.getresponse()
print(r2.status, r2.reason, r2.version)
headers = r2.getheaders()
for header in headers:
    print(header)
data = r2.read()


