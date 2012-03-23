data =  [[7065, 22.1, 22.7],
 [6678, 23.7, 24.6],
 [5875, 25.1, 25.7],
 [5015, 25.8, 26.5],
 [4921, 30.7, 31.7],
 [4713, 36.1, 37.4],
 [4471, 38.7, 40.0]]


m = len(data[0])

caption = "$\\lambda$ [A]&$y_{min} [cm]$&$y_{max} [cm]$"

print "\\begin{tabular}{|" + "l|"*m + "}"
print "\\hline"
print caption + "\\\\"
print "\\hline"

for row in data:
    print "&".join([str(x) for x in row]) + "\\\\"


print "\\hline"
print "\\end{tabular}"
