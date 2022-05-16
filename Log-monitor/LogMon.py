data = []
print("enter * at the end of data:")
while str!="*":
    str = input()
    data.append(str.split(" "))
data.pop(len(data)-1)

error_list = []
for i in data:
    if i[3]=='ERROR:':
        error_list.append(i[2])
error_logs = {}
for i in error_list:
    error_logs[i]=[]

for i in error_list:
    for j in data:
        if j[2] == i:
            if j[3] == 'ERROR:':
                error_logs[i].append(" ".join(j))
                break
            else:
                error_logs[i].append(" ".join(j))
for i in error_list:
    logs_size = len(error_logs[i])
    if logs_size >3:
        for j in range(logs_size-4,logs_size):
            if j == logs_size-1:
                print(error_logs[i][j]," -----")
            else:
                print(error_logs[i][j])
    else:
        for j in error_logs[i]:
            print(j)
print("messages before this error")