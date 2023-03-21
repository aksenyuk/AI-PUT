## Statistics Lab Test I 23.11.2021
## Sofya Aksenyuk 150284

##Ex 1

x = c(120.5, 126.9, 124.5, 131.0, 118.8, 123.7, 126.1, 125.3)
## 1a)

#position measures:
mean(x)
quantile(x)
table(x)
#dispersion measures:
var(x)
sd(x)
max(x)-min(x)
quantile(x,0.75) - quantile(x,0.25)  # <==> q3 - q1
sd(x)/mean(x) * 100

## 1b) 
boxplot(x) 

## 1c)
hist(x, col='BLUE', breaks=c(115, 120, 130, 135))

##Ex 2

n = 4
p = 0.8
## 2a)

dbinom(x=0, n, p)
dbinom(x=1, n, p)
dbinom(x=2, n, p)
dbinom(x=3, n, p)
dbinom(x=4, n, p)

## 2b)

## at least 3 arms will be calibrated correctly: P(X >= 3) = 1 - P(X = 3) = 1 - F(3)
1-pbinom(3,n,0.8)
##  no more than two arms will be calibrated (<= 2): P(X <= 2) = F(2)
pbinom(2, n, 0.8)

##Ex 3

## 3a)
# P(X < 183) = P(X <= 182)
pnorm(183, 184, 3/7)                  ## _X ~ N(mu, sigma/sqrt(n)) 
## 3b)
curve(dnorm(x,184,3/7), xlim=c(180, 188))

##Ex 4

means = c()
for (i in 1:300){
  a = rnorm(30,3,3)
  m = mean(a)
  mu = 3
  s = sd(a)
  means[i] = ((m - mu) / s) * sqrt(30)
}

hist(means,prob=T)
curve(dt(x, 29), add=TRUE)

##Ex 5

x = c(2.87, 2.74, 2.71, 2.92, 2.98, 2.83, 2.80, 2.77, 2.89)
## Confidence intervals for the mean:
## sigma is unknown ==> :
## testing hypothesis for mean (sigma is unknown)
t.test(x, conf.level = 0.95) 
## Interpretaton: At significance level = 0.95 we REJECT H_0 in favor of H_1. 




