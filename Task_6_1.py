res=[]
file='nginx_logs.txt'
with open(file) as f:
    for line in f:
        line=line.split()
        ip=line[0]
        func=line[5].strip('"')
        action=line[6]
        res.append((ip,action,func))

print(res)





