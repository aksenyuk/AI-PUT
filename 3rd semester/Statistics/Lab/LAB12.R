## Lab 12 List 12

## Ex 1

alpha = 0.1
retired = 300
observed = c(122, 85, 76, 17)
expected = c(0.38, 0.32, 0.23, 0.07) * retired
degrees_of_freedom = length(observed)

## Test Statistics: X^2  = sum((v_i - n_i)^2 / n_i_0)_i

X_hat = sum((observed - expected) * (observed - expected) / expected)

## Critical interval: R = ((X_alpha, k - 1)^2; Inf)

R = qchisq(1 - alpha, degrees_of_freedom - 1)

## X^2 = 3.29 does NOT belong to R = (6.25, Inf), therefore:
## Interpretation: At significance level = 0.1,
## -> we do NOT reject H_0 in favor of H_1.


## OR WE CAN USE JUST R-FUNCTION WHICH CALCULATE ALL THE STUFF ABOVE:

chisq.test(observed, p=expected / retired)

## Ex 3

b1 = c(7, 20, 10, 7, 14)
b2 = c(20, 5, 5, 13, 17)
b3 = c(4, 16, 13, 21, 4)
b4 = c(12, 9, 16, 3, 17)

alpha = 0.05
observed = b1 + b2 + b3 + b4
expected = rep(0.2, length(b1))

chisq.test(observed, p=expected)

## Ex 4

alpha = 0.05
f = c(7, 19, 31, 17, 3, 1)
x = c(1, 3, 5, 7, 9, 11)

## mean(x) = sum(x_i - n_i)_i / n:

n = sum(f)
m = sum(x * f) / n
m

## S^2 = 1 / (n - 1) * (sum((x_i)^2)_i - n * mean(x)^2):

s_2 = 1 / (n - 1) * (sum(x^2 * f) - n * m^2)
s_2

s = sqrt(s_2)
s

## CDF(x) = P(X <= x)

a1 = pnorm(2, m, s)
a2 = pnorm(4, m, s) - pnorm(2, m, s)
a3 = pnorm(6, m, s) - pnorm(4, m, s)
a4 = pnorm(8, m, s) - pnorm(6, m, s)
a5 = pnorm(10, m, s) - pnorm(8, m, s)
a6 = 1 - pnorm(10, m, s)

expected = c(a1, a2, a3, a4, a5, a6)

chisq.test(f, p=expected)

## Since alpha = 0.05 < p_value = 0.942:
## Interpretation: At significance level = 0.05,
## -> we do NOT reject H_0 in favor of H_1.

## Ex 5

f=c(10,25,35,20,10)

## Ex 6

u = c(15, 12, 8)
s = c(8, 15, 9)
r = c(6, 8, 7)

alpha = 0.05

E_ij = matrix(rep(0, length(u) * 3), nrow = 3)
E_ij

data = data.frame(u, s, r)
data

for (i in 1:length(u)) {
  for (j in 1:length(u)){
    E_ij[i, j] = (sum(data[i,]) * sum(data[,j])) / sum(data)
  }
}
E_ij

## Test Statistics: X^2  = sum(sum((n_ij - E_ij)^2 / E_ij)_i)_j
## E_ij = (n_i0 * n_0j) / n

X_hat = sum((data - E_ij) * (data - E_ij) / E_ij)
X_hat

## Critical interval: R = ((X_alpha, (k_x - 1) * (k_y - 1))^2; Inf)

R = qchisq(1 - alpha, 4)
R

## X^2 = 3.005 does NOT belong to R = (9.49, Inf), therefore:
## Interpretation: At significance level = 0.05,
## -> we do NOT reject H_0 in favor of H_1.


## OR WE CAN USE JUST R-FUNCTION WHICH CALCULATE ALL THE STUFF ABOVE:

chisq.test(data)

## Ex 7 

y=c(10,7,4)
n=c(90,93,96)