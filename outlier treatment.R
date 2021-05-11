

#outlier treatment
library(readr)

boston <-read.csv("C:\\Users\\hp\\Desktop\\DataSets\\boston_data.csv")

str(boston)
attach(boston)

#Outlier detection through box plot

boxplot(boston$crim)
boxplot(boston$zn)
boxplot(boston$indus)
boxplot(boston$chas)
boxplot(boston$nox)
boxplot(boston$rm)
boxplot(boston$age)
boxplot(boston$dis)
boxplot(boston$rad)
boxplot(boston$tax)
boxplot(boston$ptratio)
boxplot(boston$black)
boxplot(boston$lstat)
boxplot(boston$medv)

#Except indus,nox,age,rad and tax all inputs have outliers

#Outlier treatment for crim column

qunt_crim <- quantile(boston$crim,probs = c(.25,.75))
qunt_crim 
caps_crim <- quantile(boston$crim, probs = c(.01,.99), na.rm = T)
caps_crim 
H <- 1.5*IQR( boston$crim,na.rm = T)
H 
boston$crim[boston$crim<(qunt_crim[1]-H)] <- caps_crim[1]
boston$crim[boston$crim>(qunt_crim[2]+H)] <- caps_crim[2]
boxplot(boston$crim)

#Outlier treatment for zn column

qunt_zn <- quantile(boston$zn,probs = c(.25,.75))
qunt_zn 
caps_zn <- quantile(boston$zn, probs = c(.01,.99), na.rm = T)
caps_zn 
H <- 1.5*IQR( boston$zn,na.rm = T)
H 
boston$zn[boston$zn<(qunt_zn[1]-H)] <- qunt_zn[1]
boston$zn[boston$zn>(qunt_zn[2]+H)] <- qunt_zn[2]
boxplot(boston$zn)


#Outlier treatment for chas column

qunt_chas <- quantile(boston$chas,probs = c(.25,.75))
qunt_chas 
caps_zn <- quantile(boston$chas, probs = c(.01,.99), na.rm = T)
caps_zn 
H <- 1.5*IQR( boston$chas,na.rm = T)
H 
boston$chas[boston$chas<(qunt_chas[1]-H)] <- qunt_zn[1]
boston$chas[boston$chas>(qunt_chas[2]+H)] <- qunt_zn[2]
boxplot(boston$chas)

#Outlier treatment for rm column
qunt1 <- quantile(boston$rm,probs = c(.25,.75))
qunt1 
caps <- quantile(boston$rm, probs = c(.01,.99), na.rm = T)
caps
H <- 1.5*IQR( boston$rm,na.rm = T)
H # 42539.92
boston$rm[boston$rm<(qunt1[1]-H)] <- caps[1]
boston$rm[boston$rm>(qunt1[2]+H)] <- caps[2]
boxplot(boston$rm)

#Outlier treatment for dis column
qunt1 <- quantile(boston$dis,probs = c(.25,.75))
qunt1 
caps <- quantile(boston$dis, probs = c(.01,.99), na.rm = T)
caps 
H <- 1.5*IQR( boston$dis,na.rm = T)
H 
boston$dis[boston$dis<(qunt1[1]-H)] <- caps[1]
boston$dis[boston$dis>(qunt1[2]+H)] <- caps[2]
boxplot(boston$dis)


#Outlier treatment for black column
qunt1 <- quantile(boston$black,probs = c(.25,.75))
qunt1 
caps <- quantile(boston$black, probs = c(.01,.99), na.rm = T)
caps 
H <- 1.5*IQR( boston$black,na.rm = T)
H 
boston$black[boston$black<(qunt1[1]-H)] <- caps[1]
boston$black[boston$black>(qunt1[2]+H)] <- caps[2]
boxplot(boston$black)

#Outlier treatment for lstat column
qunt1 <- quantile(boston$lstat,probs = c(.25,.75))
qunt1 
caps <- quantile(boston$lstat, probs = c(.01,.99), na.rm = T)
caps 
H <- 1.5*IQR( boston$lstat,na.rm = T)
H 
boston$lstat[boston$lstat<(qunt1[1]-H)] <- caps[1]
boston$lstat[boston$lstat>(qunt1[2]+H)] <- caps[2]
boxplot(boston$lstat)

#Outlier treatment for medv column
qunt1 <- quantile(boston$medv,probs = c(.25,.75))
qunt1 
caps <- quantile(boston$medv, probs = c(.01,.99), na.rm = T)
caps 
H <- 1.5*IQR( boston$medv,na.rm = T)
H 
boston$medv[boston$medv<(qunt1[1]-H)] <- caps[1]
boston$medv[boston$medv>(qunt1[2]+H)] <- caps[2]
boxplot(boston$medv)


