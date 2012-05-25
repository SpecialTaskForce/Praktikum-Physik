data = [7, 13, 16, 21, 25, 29, 35, 42, 47, 53, 56, 59, 63, 69, 72, 79, 87, \
89, 94, 99, 105, 108, 115, 118, 123, 130, 130, 135, 143, 149, 156, \
162, 170, 172, 178, 186, 193, 195, 198, 200, 208, 210, 214, 220, 225, \
238, 245, 250, 253, 257, 266, 272, 277, 279, 282, 287, 291, 296, 304, \
308, 313, 315, 322, 327, 332, 335, 342, 349, 352, 361, 365, 371, 379, \
383, 389, 393, 397, 403, 408, 414, 418, 428, 433, 439, 449, 455, 458, \
463, 466, 472, 478, 479, 480, 485, 492, 497, 499, 503, 507, 509, 512, \
520]

m = 7
caption = "$N$"
nr = "$t$"

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
            buffer += "%s&%s" % ((index+1)*10, cell)
        buffer += "&" if j < m - 1 else "\\\\"
    print buffer

print "\\hline"
print "\\end{tabular}"
