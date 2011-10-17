#! /usr/bin/python
import matplotlib.pyplot as plot

x0 = [i/100. - 1 for i in range(100)]
y0 = [0 for i in x0]
x1 = [i/1000. for i in range(1000)]
y1 = [i*i/2. for i in x1]
x2 = [i/100. + 1 for i in range(100)]
y2 = [1./2 for i in x2]
x3 = [i/100. + 2 for i in range(100)]
y3 = [(1/2. + i**3/38. - 8/38.) for i in x3]
x4 = [i/100. + 3 for i in range(100)]
y4 = [1 for i in x4]

plot.title(r'CDF')
plot.xlabel('$x$')
plot.ylabel('$F(x)$', rotation='horizontal')
plot.plot(x0, y0, color = "black")
plot.plot(x1, y1, color = "black")
plot.plot(x2, y2, color = "black")
plot.plot(x3, y3, color = "black")
plot.plot(x4, y4, color = "black")
plot.axis([-1,4,-.1,1.1])
plot.show()
