import os
from pathlib import Path
# 免密
hostNames=["hdp01","hdp02","hdp03"]
error_host_names=[]
fileName=input("文件:")
path=Path(fileName)
if path.exists()==True:
    isLoop=False
else:
    print("文件不存在")
    exit()    

go_dir=input("传输到那个目录")
for host in hostNames:
    cmd="scp -r "+ fileName +" "+ host+":"+go_dir
    status = os.system(cmd)
    if status !=0:
        error_host_names.append(host)
if len(error_host_names)==0:
    print("success")
else:
    print("error hosts:",error_host_names)           
    