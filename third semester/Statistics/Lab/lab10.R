## Lab 10 List 10

## Ex 1

x=c(8, 12, 15, 20, 22, 31)
y=c(74, 129, 182, 220, 260, 410)

## 1a)

plot(x, y) ## shows the linear regression in this case

## 1b)

cor(x, y) ## function to check correlation

## checking correlation by formula: r = Sxy / sqrt(Sx^2 * Sy^2) = Sxy / (Sx * Sy)
## --> where Sxy - covariance between x and y;
## --> Sx^2, Sy^2 - variance of x and y.

cov(x, y) / (sd(x) * sd(y))

## Interpretations:
## --> when we have positive value and x increase, then y also increase;
## --> when we have negative value and x increase, then y also decrease.

## Answer: When the number of elves helping with packing increases, then the number of wrapped gifts also increases.
## --> Since correlation = 0.99, there is very strong linear relation between these two features.

## 1c) Calculating the linear regression:

## y_hat = b0_hat + b1_hat * x (hat since it is estimation)
## --> where b1_hat = Sxy / Sx^2; b0_hat = mean(y) - b1_hat * mean(x).
## --> b1_hat - linear regression coefficient

b1_hat = cov(x, y) / var(x) ## var() can be replaced with sd()^2
b0_hat = mean(y) - b1_hat * mean(x)
b1_hat
b0_hat

## In this case: y_hat = 14.22 * x - 43.488.
## Answer: If the number of elves helping with packing increases by 100 (just for convenience to have integer value)
## --> then the number of wrapped gifts will increase by 1422.

## OR WE CAN USE JUST THESE R-FUNCTIONS (THAT DO THE SAME) WHICH CALCULATE ALL THE STUFF ABOVE:

summary(lm(y~x)) ## where column "Estimate" is the most important for us, since it shows b0_hat and b1_hat.

## 1d) Checking the significance of linear regression:

## t0 = r * sqrt(n - 2) / sqrt(1 - r^2)
## Since in this case: b1 = 0; b1 != 0, 
## --> the critical interval is two-sided: R = (-inf; -t(alpha/2, n - 2)) U (t(alpha/2, n - 2); inf).

r = cor(x, y)
n = length(x)
alpha = 0.05
t0 = r * sqrt(n - 2) / sqrt(1 - r^2)
t0

qt(1 - alpha / 2, n - 2)

## t0 belongs to R, therefore:
## --> Answer: At significance level alpha = 0.05, we REJECT H_0 in favor of H_1.
## --> Thus, b1_hat coefficient is significant.

## OR WE CAN USE JUST THESE R-FUNCTIONS (THAT DO THE SAME) WHICH CALCULATE ALL THE STUFF ABOVE:

summary(lm(y~x)) ## but now we are interested in the second line of column Pr(>|t|) (p-value).

## which gives us p_values = 5.83e-05 < alpha = 0.05 which confirms our answer above.

2 * (1 - pt(17.818, n - 2)) ## the same calculation but using CDF-function (i.e., pt)

## 1e) Adding a linear regression function to an existing scatter plot:

curve(14.22 * x - 43.488, add=TRUE)

## 1f) Adding a linear regression function to an existing scatter plot:

## to do that we have to replace x in 14.22 * x - 43.488 by 25, i.e.:

14.22 * 25 - 43.488

## 1g) Determining and interpret the coefficient of determination:

## R^2 = r^2

r^2

## Interpretation: since R^2 = 0.98 in this case, we have very good linear regression model to the data.

## OR WE CAN USE JUST THESE R-FUNCTIONS (THAT DO THE SAME) WHICH CALCULATE ALL THE STUFF ABOVE:

summary(lm(y~x)) ## but now we are interested in the line of 'Multiple R-squared'.

## Ex 2

x=c(2, 4, 5, 7, 10)
y=c(120, 100, 87, 60, 30)

## 2a)

plot(x, y)

## 2b)

cor(x, y)

## Interpretation: When the time of delivering gifts increases then:
## --> the weight of Santa's sleight decreases
## --> Since correlation = 0.99, there is very strong linear relation between these two features.

## 2c)

summary(lm(y~x))

## In this case: y_hat = -11.51 * x + 143.86
## Answer: If the time of delivering gifts increases by 1 (hour), then:
## --> the weight of Santa's sleight decreases by 11.51 (tonns).

## 2d)

## p-value = 9.56e-05

## --> Answer: At significance level alpha = 0.05, we REJECT H_0 in favor of H_1.
## --> Thus, b1_hat coefficient is significant.

## 2e)

curve(-11.51 * x + 143.86, add=TRUE)

## 2f)

-11.51 * 8 + 143.86

## 2g)

## Interpretation: since R^2 = 0.9963 in this case, we have very good linear regression model to the data.

#3
x=c(145, 260, 405, 600, 620, 763)
y=c(4.5, 9, 14.4, 17.5, 24, 26.7)
#4
x=seq(5,35,by=5)
y=c(14.1, 13.8, 12.7, 12.3, 11.5, 11.0, 10.3)
#5
x=c(18, 20, 18, 17, 15)
y=c(2, 3, 3, 4, 5)