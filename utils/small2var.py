data = [[12.4, 12.3, 12.4, 12.65, 12.45],
 	[12.55, 12.7, 12.75, 12.7, 12.55],
 	[12.4, 13.55, 13.25, 13.4, 13.25],
 	[14.5, 14.5, 14.4, 14.5, 14.5],
 	[16, 15.8, 15.8, 16, 16.05],
 	[17.6, 17.55, 17.7,  17.65, 17.5],
 	[19.35, 19.5, 19.7, 19.45, 19.45]]



caption = "$t$"
nr = "\\#"
m=5

print "\\begin{tabular}{|l|" + "r|"*m + "r|}"
print "\\hline"
print "$d$&" + "&".join(["$T_%s$" % (d+1) for d in range(5)]) + "&$10\\overline{T}$\\\\"
print "\\hline"

def avg(_list):
    return sum(_list)/float(len(_list))

for d in range(len(data)):
    row = data[d]
    print "%scm&%s&%ss\\\\" % (d, "&".join(["%ss" % t for t in row]), "%.2f" % avg(row))



print "\\hline"
print "\\end{tabular}"
