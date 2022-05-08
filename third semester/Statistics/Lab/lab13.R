## Test Preparation List 13

## Ex 1 - Testing hypothesis for mean:

x = c(123.6, 118.5, 131.1, 122.6, 121.9, 125.1, 119.7)

alpha = 0.05

## since sigma is unknown, we use testing hypothesis for mean:
## (otherwise, if sigma would be known, we would use z.test)

t.test(x, mu = 120, alternative="greater", conf.level = 1 - alpha)

## since p-value = 0.042 < alpha = 0.05, we REJECT H_0 in favor of H_1
## => Therefore, the interpretation:
## -> Airport area is dangerous for humans in terms of creative noise.

## same using formula:

n = length(x)
mu_0 = 120
t_0 = (mean(x) - mu_0) * sqrt(n)  / sd(x)
t_0

## Ex 2 Testing hypothesis for variance:

x = c(5.0, 3.8, 4.1, 4.4, 4.0)

alpha = 0.1

## since we are testing variance, we use:

library("TeachingDemos")
sigma.test(x, sigmasq = 0.05, alternative = "two.sided", conf.level = 1 - alpha)

## since p-value = 0.0031 < alpha = 0.1, we REJECT H_0 in favor of H_1
## => Therefore, the interpretation:
## -> The variance of the hole depth is NOT equal to 0.05 cm2.

## same using formula:

n = length(x)
chi_0_2 = (n - 1) * var(x) / 0.05
chi_0_2

## Ex 3

a1 = c(15.1, 14.7, 15.5, 14.1, 15.2, 17.0)
a2 = c(13.8, 15.4, 15.2, 13.3, 14.8)

alpha = 0.05

## testing variance (sigma1_2 = sigma2_2 or not): (if we have homogeneity of variances or not)

var.test(a1, a2, alternative = "two.sided", conf.level = 1 - alpha)

## since p-value = 0.92 > alpha = 0.05, we do NOT reject H_0 in favor of H_1.
## => Therefore, we may assume that we have homogeneity of variances, i.e., sigma1_2 = sigma2_2.

## testing mean hypothesis:

t.test(a1, a2, var.equal = TRUE, alternative = "greater", conf.level = 1 - alpha)

## since, p-value = 0.1 > alpha = 0.05, we do NOT reject H_0 in favor of H_1
## -> which confirms our previous assumption.
## => Interpretation: the second robotic arm performs activities slower than the first.

## Ex 4

m1 = c(4.3, 4.7, 4.8, 4.7)
m2 = c(4.7, 4.8, 4.5, 4.7)
m3 = c(5.1, 4.9, 4.9, 5.2)

alpha = 0.05

## 4a) homogeneity of variance (if sigma1_2 = sigma2_2 = sigma3_2 or not):

names = rep(c("1", "2", "3"), each=length(m1))
values = c(m1, m2, m3)
bartlett.test(values~names)

## since p-value = 0.64 > alpha = 0.05, we do NOT reject H_0 in favor of H_1.
## => Therefore, we may assume that we have homogeneity of variances, i.e., sigma1_2 = sigma2_2 = sigma3_2.

## 4b) equality of the mean (if mu1_2 = mu2_2 = mu3_2 or not):

summary(aov(values~names))

## since Pr(>F) = 0.0178 < alpha = 0.05, we REJECT H_0 in favor of H_1
## => At least, one of means is different.

## 4c) Do m1 and m2 differ significantly from m3 in terms of mean size measured?

TukeyHSD(aov(values~names))

## p-value m1-m3 = 0.022 < alpha = 0.05;
## p-value m2-m3 = 0.042 < alpha = 0.05
## => we REJECT H_0 in favor of H_1 for both m1-m3 and m2-m3 relations
## => Interpretation: m1 and m3 differ significantly in terms of mean size as well as m2 and m3.

## Ex 5

x = c(5, 6, 9, 10, 12, 12, 14, 16, 17, 23)
y = c(31, 45, 40, 55, 72, 74, 68, 93, 79, 105)

## 5a) checking type of relationship between x and y:

plot(x, y) ## => linear relationship

## 5b) correlation coefficient:

cor(x, y) ## = 0.94 => very strong correlation

## 5c) linear regression equation:

summary(lm(y~x)) ## => y_hat = b1_hat * x + b0_hat = 4.1 * x + 15.34 (from "Estimate" column).


## => Interpretation:
## -> when the amount of row material increases by 1 kg, 
## -> the amount of chemical production increases by 4.1.

## 5d) significance of linear regression:

## From "Pr(>|t|)" column: p-value = 4.96e-05 < alpha = 0.05, we REJECT H_0 in favor of H_1
## => Interpretation: b1_hat is NOT equal to zero => it is significant.

## 5e) adding a linear regression function to an existing scatter plot:

curve(4.1014 * x + 15.3430, add = TRUE)

## 5f) Determine the amount of raw material used after using 15 liters of raw material:

4.1014 * 15 + 15.3430 ## 15 instead of x

## or we can use R-function:

predict(lm(y~x), data.frame(x = 15))

## 5g) coefficient of determination:

## From "Multiple R-squared" column R^2 = 0.8853 => that's a good fit.

## Ex 6 (same as Ex 5 but for multiple regression)

time = c(2.1, 3.2, 2.7, 2.5, 3.3, 3.8, 1.9, 3.0)
wind = c(45, 30, 33, 35, 34, 25, 47, 35)
temp = c(10, 12, 9, 13, 5, 4, 11, 7)

## 6a)

plot(wind, time)
plot(temp, time)

## 6b)

cor(wind, time) ## = -0.92 => very strong correlation
cor(temp, time) ## = -0.67 => very strong correlation

## 6c) multiple linear regression equation:

summary(lm(time~wind+temp)) ## y_hat = -0.068 * x_wind -0.065 * x_temp + 5.81

## 6d) significance of multiple linear regression:

## From "Pr(>|t|)" column: 
## -> p-value for wind = 0.001 < alpha = 0.05, we REJECT H_0 in favor of H_1;
## -> p-value for wind = 0.033 < alpha = 0.05, we REJECT H_0 in favor of H_1
## => Interpretation: b1_hat and b2_hat are NOT equal to zero => they are significant.

## 6e) Determine the ship travel time with wind speed 35km/h and 6 C as the temperature at the water surface:

predict(lm(time~wind+temp), data.frame(wind = 35, temp = 6))

## 6f) coefficient of multiple determination:

## From "Multiple R-squared" column R^2 = 0.95 => that's very good fit.

