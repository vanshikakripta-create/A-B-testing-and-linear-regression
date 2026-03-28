import os
os.makedirs('images', exist_ok=True)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as st
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import coint
from scipy.stats import ttest_ind
import warnings
warnings.filterwarnings('ignore')
# Load dataset
df = pd.read_csv("C:/Users/vansh/Downloads/marketing_campaign.csv")
print(df.head())
print(df.info())
print(df.shape)
print(df.dtypes)
# Convert Date column to datetime
df['Date'] = pd.to_datetime(df['Date'])
print(df.dtypes)
print(df.describe())
# distribution of the clicks and conversions 
plt.figure(figsize=(15,6))
plt.subplot(1,2,1)
plt.title('Facebook Ad Clicks')
sns.histplot(df['Facebook Ad Clicks'], bins = 7, edgecolor = 'k', kde = True)
plt.subplot(1,2,2)
plt.title('Facebook Ad Conversions')
sns.histplot(df['Facebook Ad Conversions'], bins = 7, edgecolor = 'k', kde = True)
#plt.show()
plt.tight_layout()
plt.savefig('images/02_facebook_distributions.png', dpi=300, bbox_inches='tight', facecolor='white')
plt.figure(figsize=(15,6))
plt.subplot(1,2,1)
plt.title('AdWords Ad Clicks')
sns.histplot(df['AdWords Ad Clicks'], bins = 7, edgecolor = 'k', kde = True)
plt.subplot(1,2,2)
plt.title('AdWords Ad Conversions')
sns.histplot(df['AdWords Ad Conversions'], bins = 7, edgecolor = 'k', kde = True)
#plt.show()
plt.tight_layout()
plt.savefig('images/02_adwords_distributions.png', dpi=300, bbox_inches='tight', facecolor='white')
'''All histograms exhibit symmetrical distributions, indicating that clicks and conversions 
are evenly distributed across the dataset with minimal outliers at either extreme.'''
#How frequently do we observe days with high numbers of conversions compared to days with low numbers of conversions?
# creating function to calculate the category for the conversions
def create_conversion_category(conversion_col):
    category = []
    for conversion in df[conversion_col]:
        if conversion < 6:
            category.append('less than 6')
        elif 6 <= conversion < 11:
            category.append('6 - 10')
        elif 11 <= conversion < 16:
            category.append('10 - 15')
        else:
            category.append('more than 15')
    return category

# applying function of different campaign's conversions
df['Facebook Conversion Category'] = create_conversion_category('Facebook Ad Conversions')
df['AdWords Conversion Category'] = create_conversion_category('AdWords Ad Conversions')
print(df[['Facebook Ad Conversions','Facebook Conversion Category','AdWords Ad Conversions','AdWords Conversion Category']].head())
print(df['Facebook Conversion Category'].value_counts())
facebook = pd.DataFrame(df['Facebook Conversion Category'].value_counts()).reset_index().rename(columns = {'Facebook Conversion Category':'Category'})
print(facebook)
print(df['AdWords Conversion Category'].value_counts())
adwords = pd.DataFrame(df['AdWords Conversion Category'].value_counts()).reset_index().rename(columns = {'AdWords Conversion Category':'Category'})
print(adwords)
category_df = pd.merge(facebook, adwords, on = 'Category', how = 'outer').fillna(0)
print(category_df)
category_df = category_df.iloc[[3,1,0,2]]
print(category_df)
X_axis = np.arange(len(category_df)) 
print(X_axis)
X_axis = np.arange(len(category_df)) 
plt.figure(figsize = (15,6))
plt.bar(X_axis - 0.2, category_df['count_x'], 0.4, label = 'Facebook', color = '#03989E', linewidth = 1, edgecolor = 'k') 
plt.bar(X_axis + 0.2, category_df['count_y'], 0.4, label = 'Adwords', color = '#A62372', linewidth = 1, edgecolor = 'k') 
  
plt.xticks(X_axis, category_df['Category']) 
plt.xlabel("Conversion Category") 
plt.ylabel("Number of days") 
plt.title("Frequency of Daily Conversions by Conversion Categories", fontsize = 15) 
plt.legend(fontsize = 15) 
plt.tight_layout()
plt.savefig('images/03_conversion_categories.png', dpi=300, bbox_inches='tight', facecolor='white')
#plt.show() 
'''The data suggests Facebook had more frequent higher conversion days than AdWords, which either had very low conversion rates (less than 6) or moderate ones (6 - 10).
There is a significant variance in the number of high-conversion days between two different campaigns.
The absence of any days with conversions between 10 - 15 and more than 15 in AdWords indicates a need to review what strategies were changed or what external factors could have influenced these numbers.'''
#Do more clicks on the ad really lead to more sales?
plt.figure(figsize=(15,6))
plt.subplot(1,2,1)
plt.title('Facebook')
sns.scatterplot(x = df['Facebook Ad Clicks'],y = df['Facebook Ad Conversions'], color = '#03989E')
plt.xlabel('Clicks')
plt.ylabel('Conversions')
plt.subplot(1,2,2)
plt.title('AdWords')
sns.scatterplot(x = df['AdWords Ad Clicks'],y = df['AdWords Ad Conversions'], color = '#03989E')
plt.xlabel('Clicks')
plt.ylabel('Conversions')
plt.tight_layout()
plt.savefig('images/04_clicks_conversions_scatter.png', dpi=300, bbox_inches='tight', facecolor='white')
#plt.show()
facebook_corr = df[['Facebook Ad Conversions','Facebook Ad Clicks']].corr()
print(facebook_corr)
adwords_corr = df[['AdWords Ad Conversions','AdWords Ad Clicks']].corr()
print(adwords_corr)
print('Correlation Coeff \n--------------')
print('Facebook :',round(facebook_corr.values[0,1],2))
print('AdWords : ',round(adwords_corr.values[0,1],2))
'''A correlation of 0.87 between Facebook ad clicks and sales shows a strong positive relationship—more clicks generally mean higher sales, indicating Facebook ads are highly effective. 
In contrast, a correlation of 0.45 between AdWords clicks and sales shows a moderate relationship—AdWords contributes to sales but is less impactful, suggesting other factors affect its performance and further optimization is needed.'''

'''Hypothesis: Advertising on Facebook will result in a greater number of conversions compared to advertising on AdWords.
Null Hypothesis (H0): There is no difference in the number of conversions between Facebook and AdWords, or the number of conversions from AdWords is greater than or equal to those from Facebook.
H0: µ_Facebook ≤ µ_AdWords
Alternate Hypothesis (H1): The number of conversions from Facebook is greater than the number of conversions from AdWords.
H1: µ_Facebook > µ_AdWords'''
print('Mean Conversion \n--------------')
print('Facebook :', round(df['Facebook Ad Conversions'].mean(),2))
print('AdWords :', round(df['AdWords Ad Conversions'].mean(),2))
t_stats, p_value = st.ttest_ind(a = df['Facebook Ad Conversions'], b = df['AdWords Ad Conversions'], equal_var = False)
print('\nT statistic', t_stats, '\np-value',p_value)
# comparing the p value with the significance of 5% or 0.05
if p_value < 0.05:
    print("\np-value is less than significance value, Reject the null hypothesis")
else:
    print("\np-value is greater than significance value, Accept the null hypothesis")
'''The mean conversions from Facebook ads (11.74) are much higher than from AdWords ads (5.98), indicating greater effectiveness. 
The large T statistic (32.88) and extremely small p-value (9.35e-134) provide strong evidence that Facebook generates significantly more conversions. 
Thus, reallocating more resources to Facebook ads could further enhance conversions.'''
#What will happen when I do go with the Facebook Ad? How many facebook ad conversions can I expect given a certain number of facebook ad clicks?
# independent variable
X = df[['Facebook Ad Clicks']]

# dependent variable
y = df[['Facebook Ad Conversions']]

# initializing and fitting Linear Regression model
reg_model = LinearRegression()
reg_model.fit(X,y)
prediction = reg_model.predict(X)

# model evaluation
r2 = r2_score(y, prediction)*100
mse = mean_squared_error(y, prediction)
print('Accuracy (R2 Score):',round(r2,2),'%')
print('Mean Squared Error:', round(mse,2))
plt.figure(figsize=(8,6))
sns.scatterplot(x = df['Facebook Ad Clicks'],y = df['Facebook Ad Conversions'], color = '#03989E', label = 'Actual data points')
plt.plot(df['Facebook Ad Clicks'], prediction, color = '#A62372', label = 'Best fit line')
plt.legend()
plt.show()
plt.tight_layout()
plt.savefig('images/05_facebook_regression.png', dpi=300, bbox_inches='tight', facecolor='white')
print(f'For {50} Clicks, Expected Conversion : {round(reg_model.predict([[50]])[0][0],2)}')
print(f'For {80} Clicks, Expected Conversion : {round(reg_model.predict([[80]])[0][0],2)}')
'''The model shows good predictive power with an R² of 76.35%, indicating it effectively predicts Facebook ad conversions from ad clicks.
 These insights help businesses optimize budgets, set realistic goals, and improve ROI for Facebook ad campaigns.'''
# cleaning data ( removing unwanted symbols from the columns and converting them to numerical columns)
df['Facebook Click-Through Rate (Clicks / View)'] = df['Facebook Click-Through Rate (Clicks / View)'].apply(lambda x: float(x[:-1]))
df['Facebook Conversion Rate (Conversions / Clicks)'] = df['Facebook Conversion Rate (Conversions / Clicks)'].apply(lambda x: float(x[:-1]))
df['Facebook Cost per Click (Ad Cost / Clicks)'] = df['Facebook Cost per Click (Ad Cost / Clicks)'].apply(lambda x: float(x[1:]))
df['Cost per Facebook Ad'] = df['Cost per Facebook Ad'].apply(lambda x: float(x[1:]))
# filtering for facebook campaign
df = df[['Date','Facebook Ad Views',
       'Facebook Ad Clicks', 'Facebook Ad Conversions', 'Cost per Facebook Ad',
       'Facebook Click-Through Rate (Clicks / View)',
       'Facebook Conversion Rate (Conversions / Clicks)',
       'Facebook Cost per Click (Ad Cost / Clicks)']]

print(df.head())
#At what times of the month or days of the week do we observe the conversions?
# extracting month and week day from the date column
df['month'] = df['Date'].dt.month
df['week'] = df['Date'].dt.weekday
plt.figure(figsize=(8,5))
plt.title('Weekly Conversions')
weekly_conversion = df.groupby('week')[['Facebook Ad Conversions']].sum()
week_names= ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
plt.bar(week_names, weekly_conversion['Facebook Ad Conversions'], color = '#03989E', edgecolor = 'k')
plt.figure(figsize=(8,5))
plt.title('Monthly Conversions')
monthly_conversion = df.groupby('month')[['Facebook Ad Conversions']].sum()
month_names = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
plt.plot(month_names, monthly_conversion['Facebook Ad Conversions'],'-o', color = '#A62372')
plt.show()
plt.tight_layout()
plt.savefig('images/06_weekly_conversions.png', dpi=300, bbox_inches='tight', facecolor='white')
plt.tight_layout()
plt.savefig('images/07_monthly_conversions.png', dpi=300, bbox_inches='tight', facecolor='white')
'''Conversions remain steady across weekdays, with Mondays and Tuesdays showing the highest rates, indicating stronger engagement early in the week. 
The monthly trend shows overall growth in conversions, though February, April, May, June, August, and November record dips likely due to seasonal or behavioral factors or shifts in marketing strategy.'''
#How does the Cost Per Conversion (CPC) trend over time?
plt.figure(figsize=(8,5))
plt.title('Monthly Cost Per Conversion (CPC)')
monthly_df = df.groupby('month')[['Facebook Ad Conversions','Cost per Facebook Ad']].sum()
monthly_df['Cost per Conversion'] = monthly_df['Cost per Facebook Ad']/monthly_df['Facebook Ad Conversions']
plt.plot(month_names, monthly_df['Cost per Conversion'],'-o', color = '#A62372')
plt.show()
plt.tight_layout()
plt.savefig('images/08_monthly_cpc.png', dpi=300, bbox_inches='tight', facecolor='white')
'''The CPC trend remains relatively stable over 12 months, with May and November showing the lowest values, indicating more cost-effective advertising periods. 
February records the highest CPC, reflecting higher ad costs. Allocating more budget to low-CPC months like May and November could help maximize ROI.'''
#Is there a long-term equilibrium relationship between advertising spend and conversion rates that suggests a stable, proportional impact of budget changes on conversions over time?
score, p_value, _ = coint(df['Cost per Facebook Ad'], df['Facebook Ad Conversions'])
print('Cointegration test score:', score)
print('P-value:', p_value)
if p_value < 0.05:
    print("\np-value is less than significance value, Reject the null hypothesis")
else:
    print("\np-value is greater than significance value, Accept the null hypothesis")
'''The very low p-value leads to rejecting the null hypothesis, confirming a long-term equilibrium relationship between ad spend and conversions.
 This insight enables businesses to optimize strategies by investing in high-ROI campaigns and adjusting budgets to maximize conversions while minimizing costs.'''
import zipfile
import glob

print("\nCreating ZIP package...")
with zipfile.ZipFile('_all_plots.zip', 'w') as zipf:
    for png in glob.glob('images/*.png'):
        zipf.write(png, os.path.basename(png))
print("ZIP CREATED! Contents:")
for png in glob.glob('images/*.png'):
    print(f" {png}")
