data = [[13.0, 12.9, 12.9, 12.95, 12.9, 13.0, 12.8, 12.85, 12.95, 12.9],
        [25.5, 25.1, 25.1, 25.05, 25.25, 25.55, 25.3, 25.3, 25.55, 25.45],
        [11.85, 11.7, 12.0, 11.8, 11.7, 11.8, 11.9, 11.8, 11.95, 11.7],
        [12.7, 12.8, 13.0, 12.95, 12.65, 12.7, 12.95, 12.7, 12.7, 12.85],
        [14.95, 15.1, 14.6, 15.0, 15.15, 15.05, 15.1, 15.1, 15.0, 15.0]]

caption = lambda i: "$T_{%s}$" % i
value = lambda x: "%s s" % x

m = 5

def avg(_list):
    return "%.2f" % (sum(_list)/float(len(_list)))

for row in data:
    n = len(row)
    
    print "\\begin{tabular}{|" + "l|"*m + "}"
    print "\\hline"

    for j in range((n-1)/m+1):
        captions = ""
        values = ""
        for i in range(m):
            k = j*m+i
            if k >= n: break
            captions += "%s&" % caption(k+1)
            values += "%s&" % value(row[k])
        print captions[:-1] + "\\\\"
        print "\\hline"
        print values[:-1] + "\\\\"
        print "\\hline"
        print "\\hline"
    print "\\end{tabular}"
    print
