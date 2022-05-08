## Lab 11 List 11

## Ex 1

tv=c(12, 10, 15, 9, 12, 18, 14, 8, 9, 20)
radio=c(15, 17, 6, 6, 4, 9, 1, 4, 3, 13)
income=c(70, 77, 81, 70, 66, 82, 68, 61, 65, 85)

## 1a)

plot(tv, income)
plot(radio, income)

## 1b)

cor(tv, income) ## = 0.81 => strong correlation relationship
cor(radio, income) ## = 0.55 => moderate correlation relationship

## Interpretation:
## -> If TV advertising increases, then company's income increases as well.
## -> If radio advertising increases, then company's income increases as well.

## 1c)

## Since we have TWO independent variables (TV, radio) in this case:
## y_hat = b0_hat + b2_hat * x_tv + b1_hat * x_radio

## So we have to use matrices in this case:

y = income
x = cbind(rep(1, length(tv)), tv, radio)

b = solve(t(x) %*% x) %*% t(x) %*% y
b

## Interpretation: According to results of b, y_hat = 1.46*x_tv + 0.58*x_radio + 49.41
## -> b1_hat = 0.58 => If radio advertising increases by 1000 EUR, then company's weekly income increases by 580 EUR.
## -> b2_hat = 1.46 => If TV advertising increases by 1000 EUR, then company's weekly income increases by 1460 EUR.
## -> b0_hat = 49.41 => Weekly income of company without advertising is 49410 EUR.

## OR WE CAN USE JUST THESE R-FUNCTIONS (THAT DO THE SAME) WHICH CALCULATE ALL THE STUFF ABOVE:

summary(lm(income~tv+radio))

## where column "Estimate" is the most important for us, since it shows b0_hat, b1_hat and b2_hat.


## 1d)

## now we are interested in the second line of column Pr(>|t|) (p-value).
## which gives us p_value of radio = 0.0616 > alpha = 0.05
## -> and p_value of TV = 0.0044 < alpha = 0.05

## Interpretation: At significance level 0.05:  
## -> In case of b2_hat (TV), we REJECT H_0 in favor of H_1. 
## -> Thus, coefficient b2_hat is significant (b2_hat != 0).
## -> In case of b1_hat (radio), we do NOT reject H_0 in favor of H_1.

## 1e)

## First case: x_tv = x_radio = 0 => y_hat = 49.41
## Second case: x_tv = 16 and x_radio = 6 => y_hat = 1.46 * 16 + 0.58 * 6 + 49.41:

1.46*16 + 0.58*6 + 49.41 ## which gives us 76250 EUR for the second case

## 1f)

## "Multiple R-squared" is the most important for us, which gives us R^2 = 0.799.
## -> Therefore, we get satisfying fit of the model of regression with data.

## Ex 5

x=c(1, 4, 7, 8, 10, 13, 18, 22, 25, 28)
y=c(35, 45, 59, 77, 62, 50, 39, 47, 54, 71)

## 5a)

plot(x, y) ## it is noticeable that we are dealing with polynomial relation of third degree.

## 5b)

cor(x, y) ## linear relationship is weak which confirms 5a) assumption.

## So we are dealing with y_hat = b0_hat + b1_hat * x + b2_hat * x^2 + b3_hat * x^3.

## 5c)

Y = y
X = cbind(rep(1, length(x)), x, x*x, x*x*x)

b = solve(t(X) %*% X) %*% t(X) %*% Y
b

## => y_hat = 0.02*x^3 - 0.96*x^2 + 11.28*x + 22.25

## OR WE CAN USE JUST THESE R-FUNCTIONS (THAT DO THE SAME) WHICH CALCULATE ALL THE STUFF ABOVE:

summary(lm(y~x+I(x^2)+I(x^3)))

## 5e)

curve(0.02215*x^3 - 0.95805*x^2 + 11.28161*x + 22.24553, add=TRUE)

## 5f)
x = 15
0.02215*x^3 - 0.95805*x^2 + 11.28161*x + 22.24553
x = 48
0.02215*x^3 - 0.95805*x^2 + 11.28161*x + 22.24553

## 5g)

## "Multiple R-squared" is the most important for us, which gives us R^2 = 0.7659.
## -> Therefore, we get satisfying fit of the model of regression with data.

#Ex6
x=c(5, 15, 30, 40, 55, 65, 80, 90)
y=c(130, 98, 78, 65, 58, 73, 104, 147)