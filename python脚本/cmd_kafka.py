


import paramiko
import sys
type_d={"1":"start","2":"stop","3":"status"}
type_i=input("请输入操作的类型：\n1.start\n2.stop\n3.status \n")
type_str=type_d.get(type_i,"None")
cmd=""
if type_str == "None":
    print("操作错误")
    exit(0)
elif type_i=="1":
    cmd="/opt/kafka/bin/kafka-server-start.sh -daemon /opt/kafka/config/server.properties"
    pass
elif  type_i=="2":
    cmd="/opt/kafka/bin/kafka-server-stop.sh"
    pass

hostNames=["hdp01","hdp02","hdp03"]
for hostName in hostNames:

    client = paramiko.SSHClient()

    ##自动选择yes
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # 连接服务器
    client.connect(hostname=hostName,
                   port=22,
                   username='root',
                   password='111111')

    # 4.执行操作
    stdin, stdout, stderr = client.exec_command(cmd)
    # 5.获取命令执行的结果
    result = stdout.read().decode('utf-8')
    print(result)
    # 6.关闭连接
    client.close()
