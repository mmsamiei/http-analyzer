import http.client
import tkinter as tk
from tkinter import ttk


win = tk.Tk()
win.title("http analyzer")
url = tk.StringVar()
url_entered = ttk.Entry(win, width=15, textvariable=url)
url_entered.grid(row=1, column=0, sticky='W')
ttk.Label(win, text="Server Information").grid(row=2, column=0, sticky='W')
server_information_label = ttk.Label(win)
server_information_label.grid(row=2, column=1)
ttk.Label(win, text="Allowable Methods").grid(row=3, column=0, sticky='W')
allowable_methods_label = ttk.Label(win)
allowable_methods_label.grid(row=3, column=1)
ttk.Label(win, text="cookie information").grid(row=4, column=0, sticky='W')
cookie_information_label = ttk.Label(win)
cookie_information_label.grid(row=4, column=1)
ttk.Label(win, text="cache information").grid(row=5, column=0, sticky='W')
cache_information_label = ttk.Label(win)
cache_information_label.grid(row=5, column=1)
ttk.Label(win, text="Authentication information").grid(row=6, column=0, sticky='W')
authentication_information_label = ttk.Label(win)
authentication_information_label.grid(row=6, column=1)
ttk.Label(win, text="error information").grid(row=7, column=0, sticky='W')
error_information_label = ttk.Label(win)
error_information_label.grid(row=7, column=1)
ttk.Label(win, text="persistent connection?").grid(row=8, column=0, sticky='W')
persistent_connection_label = ttk.Label(win)
persistent_connection_label.grid(row=8, column=1)

for child in win.winfo_children():
    child.grid_configure(padx=10, pady=10)



def update():
    print(url.get())
    conn = http.client.HTTPConnection(url.get())
    conn.request("OPTIONS","/")
    r1 = conn.getresponse()
    headers = r1.getheaders()

    allowable_methods = None
    server_information = None
    persistent_connection = None
    cache_information = None

    for header in headers:
        if header[0] == "Allow":
            allowable_methods = header[1]
            allowable_methods_label.configure(text=allowable_methods, foreground="black")
        if header[0] == "Server":
            server_information = header[1]
            server_information_label.configure(text=server_information, foreground="black")

    r1.read() # this is very important!
    conn.request("HEAD","/")
    r2 = conn.getresponse()
    headers = r2.getheaders()
    for header in headers:
        print(header[0])
        if header[0] == "Cache-Control":
            cache_information = header[1]
            cache_information_label.configure(text=cache_information, foreground="black")
        if header[0] == "Connection":
            persistent_connection = header[1]
            persistent_connection_label.configure(text=persistent_connection, foreground="black")

    if allowable_methods is None:
        allowable_methods_label.configure(text="can't reach it",foreground="red")
    if server_information is None:
        server_information_label.configure(text="can't reach it", foreground="red")
    if persistent_connection is None:
        persistent_connection_label.configure(text="can't reach it", foreground="red")
    if cache_information is None:
        cache_information_label.configure(text="can't reach it", foreground="red")



conn  = http.client.HTTPConnection("www.google.com")
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
print("**********************************************************************")
conn.request("GET", "/")
r2 = conn.getresponse()
print(r2.status, r2.reason, r2.version)
headers = r2.getheaders()
for header in headers:
    print(header)
data = r2.read()


action = ttk.Button(win, text="Submit", command=update)
action.grid(row=1, column=1, padx=40)







win.mainloop()
