## Lab 9 List 9

## Ex 1

w=c(4.07, 4.09, 4.06, 4.09, 4.08)
c=c(4.06,	4.08,	4.07,	4.07,	4.07)
g=c(4.08,	4.09,	4.08,	4.10,	4.09)

## 1a) homogeneity of the variance:

values = c(w, c, g)
values
names = rep(c("w", "c", "g"), each=length(w))
names

bartlett.test(values~names)
## p = 0.4717 > alpha(conf.level) = 0.05 confirms that we do NOT reject H_0 in favor of H_1.

## the same as 'bartlett.test'-function calculated but using formula:
N = 15
k = 3
Ni = 5
sp2 = (Ni - 1) * (var(w) + var(c) + var(g)) / (N - k)
up = (N - k) * log(sp2) - (Ni - 1)*(log(var(w)) + log(var(c))  + log(var(g)))
down = 1 + 1/(3 * (k - 1)) * (k*(1/(Ni - 1)) - 1/(N - k))
T = up / down
T

## function to determine quantile: (to define critical interval later on)
alpha = 0.05
qchisq(1 - alpha, k - 1)
## T does NOT belong to the interval R which confirms that we do NOT reject H_0 in favor of H_1. 

## 1b) equality of the mean temperature value:

a = aov(values~names) ## aov - analysis of variance
summary(a)

## p-value (Pr(> F) in this function's notation) = 0.0413 < alpha = 0.05, therefore, we REJECT H_0 in favor of H_1. Thus, not all mean temperatures are equal(at least two of these means differ).

## 1c) Do Warsaw and Cracow differ significantly from Gdansk in terms of temperature?

names = factor(names)
a = aov(values~names)
TukeyHSD(a) ## function to check differences
## In Warsaw-Gdansk case: p-value(p adj in this function's notation) = 0.28 > alpha = 0.05 ==> we do NOT reject H_0 in favor of H_1.
## In Gdansk-Cracow case: p-values(p adj in this function's notation) = 0.03 < alpha = 0.05 ==> we REJECT H_0 in favor of H_1. Thus, temperatures in Cracow and Gdansk differ.

 
## Ex 2

l=c(28,	26,	29,	30,	28,	31,	26,	32,	25,	29)
m=c(30, 29, 30, 30,	28,	32,	29,	32,	28,	30)
s=c(31,	29,	33,	33,	29,	33,	28,	32,	27,	32)
h=c(29,	27,	30,	31,	27,	32,	27,	32,	27, 30)

## 2a) homogeneity of the variance:

values = c(l, m, s, h)
values
names = rep(c("l", "m", "s", "h"), each=length(l))
names

bartlett.test(values~names)
## p = 0.5 > alpha(conf.level) = 0.05 confirms that we do NOT reject H_0 in favor of H_1.

## 2b) the equality of the average production value of a certain product from a given type of raw material:

a = aov(values~names) ## aov - analysis of variance
summary(a)

## p-value (Pr(> F) in this function's notation) = 0.0974 > alpha = 0.05 ==> we do NOT reject H_0 in favor of H_1.

## 2c) Do Low and Strong pressure differ significantly from High with regard to the production of the product?

names = factor(names)
a = aov(values~names)
TukeyHSD(a) ## function to check differences
## In all cases: p-value(p adj in this function's notation) > alpha = 0.05 ==> we do NOT reject H_0 in favor of H_1. It happens for all cases because we do NOT reject in 2b).

## Ex 3

m1=c(6.5, 7.8, 6.9, 6.4)
m2=c(7.2, 8.5, 7.3, 7.0)
m3=c(7.2, 7.5, 7.1, 7.5)
m4=c(7.1, 7.0, 7.1, 7.2)
m5=c(7.2, 6.6, 7.4, 7.5)

## Ex 4

non=c(69, 52, 71, 58, 59, 65)
sli=c(91, 72, 81, 67, 95, 84)
med=c(55, 60, 78, 58, 62, 66)
much=c(66, 81, 70, 77, 57, 79)

## 4a) the homogeneity of variance:

values = c(non, sli, med, much)
values
names = rep(c("non", "sli", "med", "much"), each=length(non))
names
bartlett.test(values~names)
## p = 0.8517 > alpha(conf.level) = 0.05 confirms that we do NOT reject H_0 in favor of H_1.

## 4b) equality of the average sinus rhythm in athletes:

a = aov(values~names) ## aov - analysis of variance
summary(a)

## p-value (Pr(> F) in this function's notation) = 0.00398 < alpha = 0.05 ==> we REJECT H_0 in favor of H_1. Thus, not all means of sinus rhythm of athletes are equal.

names = factor(names)
a = aov(values~names)
TukeyHSD(a) ## function to check differences