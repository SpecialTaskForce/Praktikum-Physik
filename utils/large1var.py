data = [38, 45, 48, 38, 45, 50, 41, 43, 41, 41, 41, 41, 45, 45, 46, 43, 41,
        45, 41, 44, 43, 41, 48, 41, 44, 44, 43, 44, 42, 42, 46, 42, 47, 45,
        41, 39, 41, 43, 44, 42, 41, 45, 42, 46, 44, 41, 44, 41, 41, 37, 37,
        43, 43, 41, 40, 48, 43, 38, 40, 44, 41, 45, 45, 44, 44, 43, 43, 41,
        45, 43, 41, 41, 45, 42, 45, 41, 44, 44, 45, 41, 45, 43, 41, 45, 48,
        45, 40, 43, 44, 45, 43, 41, 47, 45, 45, 44, 42, 40, 42, 41]

m = 6
caption = "$t$"
nr = "\\#"

while len(data) % m != 0:
    data.append("")
n = len(data)
h = n/m

print "\\begin{tabular}{|" + "r|l|"*m + "}"
print "\\hline"
print (("%s&%s&" % (nr, caption))*m)[:-1] + "\\\\"
print "\\hline"

for i in range(h):
    buffer = ""
    for j in range(m):
        index = h*j+i
        cell = data[index]
        if cell == "":
            buffer += "&"
        else:
            buffer += "%s&0.%ss" % (index+1, cell)
        buffer += "&" if j < m - 1 else "\\\\"
    print buffer

print "\\hline"
print "\\end{tabular}"
