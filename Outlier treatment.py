
import pandas as pd

#loding the data frame
boston=pd.read_csv("C:/Users/hp/Desktop/DataSets/boston_data.csv")

boston.info()   #For data types and non or null values
# data has no na or nall values 

boston.describe() # for mean ,min, max, IQR 

EDA=pd.DataFrame({"columns_name ":boston.columns,
                  "mean":boston.mean(),
                  "median":boston.median(),
                  "mode":boston.mode(),
                  "standard_deviation":boston.std(),
                  "variance":boston.var(),
                  "skewness":boston.skew(),
                  "kurtosis":boston.kurt()})

EDA            

# Scatter plot between the variables along with histograms
import seaborn as sns
sns.pairplot(boston.iloc[:, :])

import matplotlib.pyplot as plt # for data visualization 
import numpy as np

# let's find outliers in boston
#boxplot for every column
for column in boston:
    plt.figure()
    boston.boxplot([column])

boxplot = boston.boxplot(column=[ 'crim','zn', 'indus',  'chas', 'nox',
                'rm', 'age', 'dis','rad', 'tax' ,'ptratio', 'black',
            'lstat','medv'])

# from all thies boxplot we can see that column 'crim','zn','rm', 'dis','black','lstat','medv' has some outlier 

######## for "rm" column HVO and LVO finding and replacing

# Detection of outliers for rad column(find limits for RM based on IQR)

rm_IQR = boston['rm'].quantile(0.75) - boston['rm'].quantile(0.25)
rm_lower_limit = boston['rm'].quantile(0.25) - (rm_IQR * 1.5)
rm_upper_limit = boston['rm'].quantile(0.75) + (rm_IQR * 1.5)

####################### Replace ############################
# Now let's replace the outliers by the maximum and minimum limit
boston['rm_replaced']= pd.DataFrame(np.where(boston['rm'] > rm_upper_limit, rm_upper_limit, 
                                         np.where(boston['rm'] < rm_lower_limit, rm_lower_limit, boston['rm'])))
sns.boxplot(boston.boston_replaced);plt.title('Boxplot');plt.show()

######## for "crim" column HVO  finding and replacing ##############

# Detection of outliers (find limits for RM based on IQR)
crim_IQR = boston['crim'].quantile(0.75) - boston['crim'].quantile(0.25)
crim_upper_limit = boston['crim'].quantile(0.75) + (crim_IQR * 1.5)

####################### Replace ############################
# Now let's replace the outliers by the maximum and minimum limit
boston['crim_replaced']= pd.DataFrame(np.where(boston['crim'] > crim_upper_limit, crim_upper_limit ,  boston['crim']))
sns.boxplot(boston.crim_replaced);plt.title('Boxplot');plt.show()

######## for "zn" column HVO  finding and replacing ##############

zn_IQR = boston['zn'].quantile(0.75)-boston['zn'].quantile(0.25)
zn_up_lm= boston['zn'].quantile(0.75)+(zn_IQR*1.5)
###########replacling with upper limit ##########
boston['zn_replaced']=pd.DataFrame(np.where(boston['zn']>zn_up_lm,zn_up_lm, boston['zn']))
sns.boxplot(boston.zn_replaced);plt.title('Boxplot');plt.show()


######## for "dis" column HVO  finding and replacing #############
dis_IQR=boston['dis'].quantile(0.75)-boston['dis'].quantile(0.25)
dis_up_lm= boston['dis'].quantile(0.75)+(dis_IQR*1.5)
###########replacling with upper limit ##########
boston['dis_replaced']=pd.DataFrame(np.where(boston['dis']>dis_up_lm,dis_up_lm,boston['dis']))
sns.boxplot(boston.dis_replaced);plt.title('Boxplot');plt.show()


######## for "medv" column HVO  finding and replacing #############
medv_IQR = boston['medv'].quantile(0.75)-boston['medv'].quantile(0.25)
medv_up_lm=boston['medv'].quantile(0.75)+(medv_IQR*1.5)

boston['medv_replaced']=pd.DataFrame(np.where(boston['medv']>medv_up_lm,medv_up_lm,boston['medv']))
sns.boxplot(boston['medv_replaced']);plt.title('Boxplot');plt.show()

######## for "ptratio" column LVO  finding and replacing #############
ptr_IQR=boston['ptratio'].quantile(0.75)-boston['ptratio'].quantile(0.25)
ptr_lo_lm=boston['ptratio'].quantile(0.25)  - (ptr_IQR*1.5)
##########replacing with lv
boston['ptratio_replaced']=pd.DataFrame(np.where(boston['ptratio']<ptr_lo_lm,ptr_lo_lm,boston['ptratio']))
sns.boxplot(boston['ptratio_replaced']);plt.title('Boxplot');plt.show()

################# for "black  " column LVO  finding and replacing #############

bla_IQR=boston['black'].quantile(0.75)-boston['black'].quantile(0.25)
bla_lo_lm=boston['black'].quantile(0.25)  - (bla_IQR*1.5)
##########replacing with lv
boston['black_replaced']=pd.DataFrame(np.where(boston['black']<bla_lo_lm,bla_lo_lm,boston['black']))
sns.boxplot(boston['black_replaced']);plt.title('Boxplot');plt.show()



