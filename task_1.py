line = '1h 45m,360s,25m,30m 120s,2h 60s'
new_line = line.split(',')
ls = []
for i in new_line:
    ls.extend(i.split())
total_minutes = 0
for l in ls:
    if 'h' in l:
        minutes = int(l.replace('h','')) * 60
    elif 'm' in l:
        minutes = int(l.replace('m',''))
    elif 's' in l:
        minutes = int(l.replace('s','')) // 60
    total_minutes += minutes
print(total_minutes)