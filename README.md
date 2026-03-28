# A-B-testing-and-linear-regression
The primary objective is to conduct a comparative analysis of two marketing campaigns (Facebook and Google Adwords) to determine which platform is more effective in terms of clicks, conversions, and cost-effectiveness. Ultimately, the goal is to provide data-driven recommendations that maximize the Return on Investment (ROI) for clients by identifying where to allocate advertising resources most efficiently.


**Project Process**


The analysis follows a comprehensive data science workflow:
Data Preparation & Cleaning: Loading a dataset containing 365 days of 2019 data. This includes converting the "Date" column to the correct format and stripping currency ($) and percentage (%) symbols to transform categorical strings into float values for calculation.
Exploratory Data Analysis (EDA): Checking data distributions using histograms and subplots to ensure data symmetry and identify any outliers.
Comparative Performance Analysis: Categorizing daily conversions (e.g., "Less than 6," "10 to 15") and using side-by-side bar charts to visualize how often each platform hits specific performance tiers.
Statistical Validation: Moving beyond simple observation to use statistical tests to confirm if the differences in performance are mathematically significant.
Predictive Modeling: Building a model based on the "best" performing campaign to forecast future results.
Trend & Cost Analysis: Examining performance across different timeframes (weekly and monthly) and calculating the Cost Per Conversion (CPC) to measure actual efficiency.


**Techniques Used**


A/B & Hypothesis Testing (T-test): Used to compare the mean conversions of both platforms. A T-test was performed to determine if the performance gap was significant enough to reject the null hypothesis.
Correlation Analysis: Calculating correlation coefficients to determine the strength of the relationship between clicks and actual sales/conversions.
Linear Regression: Fitting a "best-fit line" to predict how many conversions can be expected based on a specific number of clicks.
Evaluation Metrics: Using R-squared (R2) score and Mean Squared Error (MSE) to measure the accuracy and "loss" of the regression model.


**Key Results and Insights**


Facebook Dominance: The analysis revealed that Facebook is significantly more effective, with a mean conversion of 11.7 compared to Adwords' 5.0.
Stronger Conversion Correlation: Facebook showed a strong positive correlation (0.87) between clicks and conversions, whereas Adwords had a much weaker relationship (0.45), indicating that more clicks on Adwords do not necessarily lead to more sales.
Predictive Power: The regression model achieved an R2 score of 76%, allowing the business to predict that 80 Facebook clicks should yield approximately 19 conversions.
Temporal Trends:
Mondays and Tuesdays consistently showed higher user engagement and conversion rates compared to the rest of the week.
The yearly trend is generally upward, but significant drops were identified in February, April, August, and November, suggesting a need to review seasonal strategies.
Cost Effectiveness: May and November were identified as the most cost-effective months (lowest CPC), while February had the highest cost per conversion, indicating lower advertising efficiency during that month



