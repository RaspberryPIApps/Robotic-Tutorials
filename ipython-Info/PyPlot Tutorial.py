#Pyplot tutorials
# from http://matplotlib.org/users/beginner.html
import matplotlib.pyplot as plt
plt.plot([1,2,3,4])  # these are assumed to be y values and x values are generated auto as 0,1,2,3
plt.ylabel('some numbers')
plt.show()

# Example 2
import matplotlib.pyplot as plt
plt.plot([1,2,3,4], [1,4,9,16], 'ro')  # x and y values and red circles
plt.axis([0, 6, 0, 20])
plt.show()

# Example 3
import numpy as np
import matplotlib.pyplot as plt
# evenly sampled time at 200ms intervals
t = np.arange(0., 5., 0.2)
# red dashes, blue squares and green triangles
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^') # 3 plots: t vs t in red dashes; t vs t^2 in blue squaes; t vs t^3 with green hats
plt.show()

#Example 4
import numpy as np
import matplotlib.pyplot as plt

def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

plt.figure(1)
plt.subplot(211) # nrows, ncols, fig#
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
plt.show()

#Example 5
import matplotlib.pyplot as plt
plt.figure(1)                # the first figure
plt.subplot(211)             # the first subplot in the first figure
plt.plot([1,2,3])
plt.subplot(212)             # the second subplot in the first figure
plt.plot([4,5,6])

plt.figure(2)                # a second figure
plt.plot([4,5,6])            # creates a subplot(111) by default

plt.figure(1)                # figure 1 current; subplot(212) still current
plt.subplot(211)             # make subplot(211) in figure1 current
plt.title('Easy as 1,2,3')   # subplot 211 title
plt.show()

#Exercise 6 - histogram
import numpy as np
import matplotlib.pyplot as plt

mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)

# the histogram of the data
n, bins, patches = plt.hist(x, 50, normed=1, facecolor='g', alpha=0.75)

plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$') #r' - raw string - do not treat \ as esc char
plt.axis([40, 160, 0, 0.03])
plt.grid(True)
plt.show()

#Exercise 7 - annotation
import numpy as np
import matplotlib.pyplot as plt

ax = plt.subplot(111)

t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2*np.pi*t)
line, = plt.plot(t, s, lw=2)
#locaction of the point is 2,1; location of text is 3, 1.5
plt.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )

plt.ylim(-2,2)
plt.show()