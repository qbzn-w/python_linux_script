
import paramiko
type_d={"1":"start","2":"stop"}
type_i=input("请输入操作的类型：\n1.start\n2.stop\n")
type_str=type_d.get(type_i,"None")
if type_str == "None":
    print("操作错误")
    exit(0)


hdfsHost = "hdp01"
yarnHost = "hdp02"
cmd_hdfs ="/opt/hadoop-3.1.3/sbin/"+type_str+"-dfs.sh"
cmd_yarn ="/opt/hadoop-3.1.3/sbin/"+type_str+"-yarn.sh"

if "start"==type_str:
    client = paramiko.SSHClient()

    ##自动选择yes
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # 连接服务器
    client.connect(hostname=hdfsHost,
                   port=22,
                   username='root',
                   password='111111')
    stdin, stdout, stderr =client.exec_command(cmd_hdfs)
    result = stderr.read().decode('utf-8')
    print(result)
    client = paramiko.SSHClient()


    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=yarnHost,
                   port=22,
                   username='root',
                   password='111111')
    stdin, stdout, stderr = client.exec_command(cmd_yarn)

    result = stdout.read().decode('utf-8')
    print(result)
    # # 6.关闭连接
    client.close()

elif "stop"==type_str:
    client = paramiko.SSHClient()

    ##自动选择yes
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # 连接服务器
    client.connect(hostname=yarnHost,
                   port=22,
                   username='root',
                   password='111111')

    stdin, stdout, stderr = client.exec_command(cmd_yarn)

    result = stdout.read().decode('utf-8')
    print(result)
    # 6.关闭连接
    client.close()

    client = paramiko.SSHClient()

    ##自动选择yes
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # 连接服务器
    client.connect(hostname=hdfsHost,
                   port=22,
                   username='root',
                   password='111111')

    # 4.执行操作
    stdin, stdout, stderr = client.exec_command(cmd_hdfs)
    # 5.获取命令执行的结果
    result = stdout.read().decode('utf-8')
    print(result)
    # 6.关闭连接
    client.close()



