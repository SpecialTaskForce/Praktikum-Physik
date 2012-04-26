data = [[19.98, 40.7, 60.9, 79.3, 99.7, 88.8, 92.7, 89.0,  89.9, 90.4, 91.2],[1.97, 4.09, 6.09, 7.92, 9.95, 4.34, 13747,  28943, 40260, 49030, \
56750]]

data = [[x[i] for x in data] for i in range(len(data[0]))]

c = 3
m = len(data[0])
n = len(data)

caption = "$U$ [V]&$I [\\mu $A]"

print "\\begin{tabular}{|" + "r|"*m*c + "}"
print "\\hline"
print "&".join([caption]*c) + "\\\\"
print "\\hline"

rows = (n+c-1)/c

for i in range(rows):
    print "&".join("&".join([str(x) for x in row]) for row in data[i::rows]) + "\\\\"


print "\\hline"
print "\\end{tabular}"
