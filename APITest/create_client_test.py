import requests
import names
from random import randint
URL = "http://127.0.0.1:8000/create_clinet_test/"

for i in range(20):
    client_info = {}
    client_name = names.get_full_name()
    client_info.update({"name": client_name,
                        "phone" : str(randint(100, 999))+str(randint(100, 999))+str(randint(1000, 9999)),
                        "email": client_name.split(' ')[1]+"@gmail.com"})
    r = requests.post(URL, data=client_info)
    print(r.status_code)
