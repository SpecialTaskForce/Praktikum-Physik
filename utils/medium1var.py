data = [[[22, 1.3], [20, 2.1], [18, 1.05], [16, 0.45], [21, 1.9], [21.5, 
  1.7], [19, 1.4], [20.5, 2.15]], [[20.5, 3.45], [19, 1.5], [19.5, 2.9], [20, 3.55], [20.2, 3.6], [18.2,
   1.25], [19.1, 2.5]],

[[19.1, 4.1], [20, 8.6], [20.5, 4.3], [22.0, 1.7], [21, 2.9], [18.5, 
  1.5], [19.5, 6]]]

caption = lambda i: "%.1f" % i[0]
value = lambda x: "%.1f" % x[1]

m = 10

def avg(_list):
    return "%.2f" % (sum(_list)/float(len(_list)))

for row in data:
    n = len(row)
    
    print "\\begin{tabular}{|l|" + "l|"*m + "}"
    print "\\hline"

    for j in range((n-1)/m+1):
        captions = "$10T$[s]&"
        values = "$A$&"
        for i in range(m):
            k = j*m+i
            if k >= n: break
            captions += "%s&" % caption(row[k])
            values += "%s&" % value(row[k])
        print captions[:-1] + "\\\\"
        print "\\hline"
        print values[:-1] + "\\\\"
        print "\\hline"
        if k < n - 1:
            print "\\hline"
    print "\\end{tabular}"
    print
