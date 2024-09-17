#Brendan Lucas 091724
import numpy as np
from matplotlib import pyplot as plt

#use tex in plot
plt.rcParams['text.usetex'] = True

#aitken algorithm from the book
def aitken(n, p_series):
    if n > len(p_series):
        print('n out of range')
        return 0
    return p_series[n] - (p_series[n+1] - p_series[n])**2/(p_series[n+2] - 2 * p_series[n+1] + p_series[n])

p_0 = 0.5

#a sequence that convergences linearly
def next_p(p_nm1):
    return (2 - np.exp(p_nm1) + p_nm1**2)/3

p_series = [p_0]

for n in range(1, 100):
    p_series.append(next_p(p_series[-1]))

#list comprehension
p_hat_series = np.array([aitken(n, p_series) for n in np.arange(27)])

p_hat_difference_series = np.abs(p_hat_series[:-1] - p_hat_series[1:])

print(p_hat_series)

#log plot
plt.scatter(range(26), np.log(p_hat_difference_series))
plt.title(r'Aitken $\Delta^2$ Convergence')
plt.xlabel(r'Index $n$')
plt.ylabel(r'$\log(|\hat{p}_{n+1} - \hat{p}_n|)$')
plt.show()
