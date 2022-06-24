options(digits=10)
library(xlsx)
library(lmtest)
library(openxlsx)
data1 <- read.xlsx("M://maintextTable.xlsx", sheet=1)

maxUHI<-data1$MaxUHI
popSize<-data1$Population

logPopSize<-log(popSize,base=10)

model1<-lm(maxUHI~0+logPopSize)	

summary(model1)
manualR<-1-deviance(model1)/sum(anova(model1)[,2])
manualR

waldtest(model1)
