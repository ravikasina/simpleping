import os

ip_list=["8.8.8.8","192.168.1.11","8.8.4.4","192.168.1.1"]
for i in ip_list:
    response=os.popen(f"ping  {i} -c 4").read()
    if "4 packets received" in response:
        print(f"the ping is successful for  {i}")
    else:
        print(f"the ping is unsuccessful for {i}")

