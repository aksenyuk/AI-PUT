## Test II Statistics Sofya Aksenyuk 150284

## Ex 1.

x=c(77,74,81,78,79,75)
alpha = 0.1

## testing hypothesis for mean, sigma known:
library(TeachingDemos)
z.test(x, stdev=2, mu=75, alternative="greater", conf.level = 1 - alpha)

## Since p_value = 0.002133 < alpha = 0.1, we REJECT H_0 in favor of H_1.
## Interpretation: the vacuum working time is satisfactory.

## Ex 2.

intel=c(1.5, 1.6, 1.3, 1.5, 1.7)
amd=c(1.7, 1.7, 1.5, 1.6, 1.4)
shakti=c(1.7, 1.8, 1.7, 1.9, 1.9)

alpha = 0.05

## 2a) the homogeneity of the variance:

names = rep(c("intel", "amd", "shakti"), each=length(intel))
values = c(intel, amd, shakti)
bartlett.test(values~names)

## since p-value = 0.7596 > alpha = 0.05, we do NOT reject H_0 in favor of H_1.
## => Therefore, we may assume that we have homogeneity of variances, i.e., sigma1_2 = sigma2_2 = sigma3_2.

## 2b) the equality of the mean computer start-up time:

summary(aov(values~names))

## since Pr(>F) = 0.0114 < alpha = 0.05, we REJECT H_0 in favor of H_1
## => At least, one of means is different.

## 2c) Do Intel differs significantly from SHAKTI in terms of the mean of computer start-up time? 

TukeyHSD(aov(values~names))

## p-value shakti-intel = 0.012 < alpha = 0.05;
## => we REJECT H_0 in favor of H_1 for shakti-intel relation
## => Interpretation: Intel and Shakti differ significantly in terms of mean of computer start-up time.

## Ex 3.

x=c(11,18,22,27,30,34)
y=c(37,25,20,12,8,3)

alpha = 0.05

## 3a) type of relationship:

plot(x, y) ## => linear relationship

## 3b) regression equation:

summary(lm(y~x)) ## => y_hat = b1_hat * x + b0_hat = -1.47736 * x + 52.46415 (from "Estimate" column).

## => Interpretation:
## -> when the temperature increases by 1 degree C, 
## -> the dissolution time of an ice cube decreases by 1.47736.

## 3c) significance of regression:

summary(lm(y~x))

## From "Pr(>|t|)" column: p-value = 3.37e-06 < alpha = 0.05, we REJECT H_0 in favor of H_1
## => Interpretation: b1_hat is NOT equal to zero => regression is significant.

## 3d) coefficient of determination:

summary(lm(y~x))

## From "Multiple R-squared" column R^2 = 0.997 => that's a really good fit.

## Ex 4.

f=c(7, 19, 22, 16, 6)
x = c(140, 160, 180, 200, 220)

alpha = 0.05

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

a1 = pnorm(150, m, s)
a2 = pnorm(170, m, s) - pnorm(150, m, s)
a3 = pnorm(190, m, s) - pnorm(170, m, s)
a4 = pnorm(210, m, s) - pnorm(190, m, s)
a5 = 1 - pnorm(210, m, s)

expected = c(a1, a2, a3, a4, a5)

chisq.test(f, p=expected)

## Since alpha = 0.05 < p_value = 0.9872:
## Interpretation: At significance level = 0.05,
## -> we do NOT reject H_0 in favor of H_1.

## Ex 5.

m1=c(3.5, 3.1, 3.3, 3.2, 3.0, 2.9)
m2=c(4.0, 3.5, 3.7, 3.8, 3.7, 3.8)

alpha = 0.01

var.test(m1, m2, alternative = "two.sided", conf.level = 1 - alpha)

## Interpretation: since p-value = 0.5628 > alpha = 0.05, we do NOT reject H_0 in favor of H_1.

