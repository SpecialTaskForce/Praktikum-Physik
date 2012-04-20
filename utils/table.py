data = [[1.01, 0.61, 0.84, 1.23],
        ["5.5\cdot 10^{-7}", "8.33333\cdot 10^{-8}", "2.875\cdot 10^{-7}", "1.08333\cdot 10^{-6}"],
        ["6.02818\cdot 10^{-7}", "8.02084\cdot 10^{-8}", "2.88415\cdot 10^{-7}", "1.32593\cdot 10^{-6}"],
        ["5.39329\cdot 10^{-7}", "7.88514\cdot 10^{-8}", "2.72238\cdot 10^{-7}", "1.07411\cdot 10^{-6}"]]

data = [[x[i] for x in data] for i in range(len(data[0]))]


m = len(data[0])

caption = "$h$ [cm]&$Q$ [m$^3$s$^{-1}$&$Q_H$ [m$^3$s$^{-1}$&$Q_E$ [m$^3$s$^{-1}$]"

print "\\begin{tabular}{|" + "l|"*m + "}"
print "\\hline"
print caption + "\\\\"
print "\\hline"

for row in data:
    print "&".join(["$"+str(x)+"$" for x in row]) + "\\\\"


print "\\hline"
print "\\end{tabular}"
