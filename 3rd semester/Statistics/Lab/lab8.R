## Lab 8 List 8

## Ex 1

n1 = 8
m1 = 29.13
s1 = 4.59
n2 = 21
m2 = 33.14
s2 = 7.44
alpha = 0.02

## Test for two variances:

f0 = s1^2 / s2^2
1 / qf(1 - alpha/2, n2 - 1, n1 - 1)
qf(1 - alpha/2, n1 - 1, n2 - 1)

## => f0 does NOT belong to the critical interval => we do NOT reject H_0 in favor of H_1. => we may assume that H_0 could be the true one (sigma1^2 = sigma2^2).


## Test for two means: 
## Assumption: homogeneity of variance (sigma1^2 = sigma2^2):

t0 = (m1 - m2) / sqrt(((n1 - 1)*s1^2 + (n2 - 1)*s2^2) / (n1 + n2 - 2))
t0 = t0 / sqrt((n1 + n2) / (n1 * n2))
-qt(1 - alpha/2, n1 + n2 - 2)
qt(1 - alpha/2, n1 + n2 - 2)

## => t0 does NOT belong to the critical interval => we do NOT reject H_0 in favor of H_1.

## Ex 2 

x=c(6.01, 5.48, 5.92, 6.12, 5.76, 5.88)
y=c(5.32, 5.66, 5.87, 5.99, 5.59)
alpha = 0.02

## Assumption: no homogeneity of variance (sigma1^2 != sigma2^2):
## since H_0 : mu1 >= mu2; H_1: mu1 < mu2:

n1 = length(x)
n2 = length(y)
s1_2 = var(x)
s2_2 = var(y)
f0 = s1_2 / s2_2
1 / qf(1 - alpha, n2 - 1, n1 - 1)

## => f0 does NOT belong to the critical interval => we do NOT reject H_0 in favor of H_1. => we may assume that H_0 could be the true one (sigma1^2 >= sigma2^2). 

var.test(x, y, alternative = "less", conf.level = 1 - alpha)

## => p-value = 0.3658 > conf.level = 0.02 confirms that we do NOT reject H_0 in favor of H_1.

## Ex 3

## Test for fractions:
## H_0: p1 <= p2; H_1: p1 > p2:

n1 = 300
t1 = 250
n2 = 220
t2 = 135
alpha = 0.01
p1_hat = t1 / n1
p2_hat = t2 / n2
p_hat = (t1 + t2) / (n1 + n2)
p_hat
z0 = (p1_hat - p2_hat) / sqrt((1 - p_hat) * p_hat) / sqrt(1 / n1 + 1 / n2)
z0
qt(1 - alpha, Inf)

## => z0 belongs to the critical interval => we do reject H_0 in favor of H_1. Thus, it is true that a greater percentage of people susceptible to the supplement is in the first group.

## OR WE CAN USE JUST THESE R-FUNCTIONS (THAT DO THE SAME) WHICH CALCULATE ALL THE STUFF ABOVE:

prop.test(c(t1, t2), c(n1, n2), alternative = "greater", conf.level = 1 - alpha)

## => p-value < conf.level confirms that we reject H_0 in favor of H_1.


#Ex 4

x=c(8.9, 9.5, 9.0, 9.4, 9.9, 8.7, 9.1, 9.1, 9.3, 8.9, 9.3)
y=c(9.6, 8.5, 8.9, 9.4, 9.5, 9.3, 8.4, 9.0, 9.7, 9.2, 9.0, 9.1, 8.9, 9.4)

alpha = 0.1

## Test for mean value:
## H_0: sigma1^2 = sigma2^2; H_1: sigma1^2 != sigma2^2:

var.test(x, y, alternative = "two.sided", conf.level = 1 - alpha)

## => p-value = 0.67 > conf.level = 0.1 => we do NOT reject H_0 in favor of H_1.

## Assumption: homogeneity of variance (sigma1^2 = sigma2^2):

t.test(x, y, var.equal = TRUE, alternative = "greater", conf.level = 1 - alpha)

## => p-value = 0.3554 > conf.level = 0.02 confirms that we do NOT reject H_0 in favor of H_1.

#Ex 5
x=c(4.6, 3.9, 4.3, 4.5, 4.4)
y=c(5.1, 4.6, 6.5, 4.1, 4.1, 3.9)

#Ex 7
x=c(41, 40, 34, 62, 39, 54, 28)
y=c(30, 51, 46, 27, 31, 29, 35)