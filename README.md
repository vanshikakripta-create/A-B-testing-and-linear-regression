# A-B-testing-and-linear-regression
The primary objective is to conduct a comparative analysis of two marketing campaigns (Facebook and Google Adwords) to determine which platform is more effective in terms of clicks, conversions, and cost-effectiveness. Ultimately, the goal is to provide data-driven recommendations that maximize the Return on Investment (ROI) for clients by identifying where to allocate advertising resources most efficiently.

**Project Process**

The analysis follows a comprehensive data science workflow:<br>
 <u>1.Data Preparation & Cleaning: </u> Loading a dataset containing 365 days of 2019 data. This includes converting the "Date" column to the correct format and stripping currency ($) and percentage (%) symbols to transform categorical strings into float values for calculation.<br>
 <u>2.Exploratory Data Analysis (EDA): </u> Checking data distributions using histograms and subplots to ensure data symmetry and identify any outliers.<br>
 <u>3.Comparative Performance Analysis: </u> Categorizing daily conversions (e.g., "Less than 6," "10 to 15") and using side-by-side bar charts to visualize how often each platform hits specific performance tiers.<br>
Statistical Validation: Moving beyond simple observation to use statistical tests to confirm if the differences in performance are mathematically significant.<br>
 <u>4.Predictive Modeling: </u> Building a model based on the "best" performing campaign to forecast future results.
 <u>5.Trend & Cost Analysis:</u> Examining performance across different timeframes (weekly and monthly) and calculating the Cost Per Conversion (CPC) to measure actual efficiency.

**Techniques Used**

 <u>1.A/B & Hypothesis Testing (T-test):</u> Used to compare the mean conversions of both platforms. A T-test was performed to determine if the performance gap was significant enough to reject the null hypothesis.
 <u>2.Correlation Analysis:</u> Calculating correlation coefficients to determine the strength of the relationship between clicks and actual sales/conversions.<br>
 <u>3.Linear Regression:</u> Fitting a "best-fit line" to predict how many conversions can be expected based on a specific number of clicks.<br>
 <u>4.Evaluation Metrics:</u> Using R-squared (R2) score and Mean Squared Error (MSE) to measure the accuracy and "loss" of the regression model.<br>

**Key Results and Insights**

 <u>1.Facebook Dominance:</u> The analysis revealed that Facebook is significantly more effective, with a mean conversion of 11.7 compared to Adwords' 5.0.<br>
 <u>2.Stronger Conversion Correlation:</u> Facebook showed a strong positive correlation (0.87) between clicks and conversions, whereas Adwords had a much weaker relationship (0.45), indicating that more clicks on Adwords do not necessarily lead to more sales.<br>
 <u>3.Predictive Power:</u> The regression model achieved an R2 score of 76%, allowing the business to predict that 80 Facebook clicks should yield approximately 19 conversions.<br>
 <u>4.Temporal Trends:</u>
Mondays and Tuesdays consistently showed higher user engagement and conversion rates compared to the rest of the week.
The yearly trend is generally upward, but significant drops were identified in February, April, August, and November, suggesting a need to review seasonal strategies.<br>
Cost Effectiveness: May and November were identified as the most cost-effective months (lowest CPC), while February had the highest cost per conversion, indicating lower advertising efficiency during that month



