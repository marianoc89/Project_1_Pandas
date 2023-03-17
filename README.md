# Project 1: Pandas - Data cleaning & wrangling - Shark Attack 
---
---

<p align="center">
    <img width="500" src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExYjZhODVlMTM4MmU0ZmQ5MmVjZmNkZTJjODRlNDQwOGE4YzQwODgzZCZjdD1n/41fVADWFuH310BFLvt/giphy.gif" alt="Tom&Jerry-Shark-Image">
</p>

---
---

The goal of this project is to implement all the skills learnt during the Module 1 form Data Analysis Bootcamp mainly implementing data wrangling, cleaning, and manipulation with Pandas as well as visualization with different Python libraries such as Matplotlib and Seaborn.

The original DataFrame was obtain from the website Kaggle*(reference links below), which contained a messy data set of Shark Attacks. 
The main objective of this project is to finally obtain a dataset which is possible to analyze and visualize in order to be able to answer the questions placed in the hypothesis section.

---
---
##  Table of Content:
   #### 1. Organization of the repo/project
   #### 2. Hypothesis of this project
   #### 3. Data
   #### 4. Sub-Dataframes
   #### 5. Visualizations
   #### 6. Conclusions
   #### 7. Links and Resources

***
### 1. Organization of the repo/project
***
```python
/images
    attacks_mom_fig.jpg
    attacks_yoy_fig.jpg
    australia_activities_mom_fig.jpg
    fatality_yoy_fig.jpg
    risk_time_yoy_fig.jpg
    top_5_activity_fig.jpg
    top_5_activity_por_fig.jpg
    top_5_mom_fig.jpg
    top_5_time_range_act_por_fig.jpg
    top_5_time_range_fig.jpg
    top_5_time_range_por_fig.jpg
    top_5_yoy_fig.jpg
/notebooks
    Project_Data_Exploration.ipynb
    Analysis.ipynb
/scr
    cleaning.py
    visualization.py
original_df_limpio.csv
.gitignore
README.md
sub_df2.csv
top_5_df.csv
```
***
### 2. Hypothesis of this project
***
#### Hypothesis --> Understand if Australia is the riskiest country to go surfing specially in the afternoon

   ##### a) Is there a trend YoY?
   ##### b) Is this risk fatal?
   ##### c) Is there any specific riskier Month?

***
### 3. Data
***
The original data downloaded from the Kaggle website was very messy containing incorrect formatting data, misplaced data and, in some instances, unnecessary data.
For that, I have created the cleaning.py file that will take the original structure of the DataFrame and perform the following:
1. Drop unnecessary columns.
2. Capitalize and rename columns.
3. Split and create new columns from other columns to have better and more accurate information.
4. Create new columns based in categories such as Time_Range and Activity_Category to bucketize data under certain parameters:
Time_Range: attacks happened from 6AM to 2PM as "Morning", 2PM to 10PM as "Afternoon" and past 10PM as "Evening".
Activity_Category: group similar activities under the same scope to better categorize the impact of the attack such as "Diving" for activities compelled by 'Diving','Snorkeling','Spearfishing','Scuba diving'.

***
### 4. Sub-Dataframes
***
The creation of Sub-DataFrames is needed to further reduce some of the corrupt columns and not needed for this investigation since they contained irrelevant information.
For this reason, I have created 2 Sub-DataFrames that are based from the cleaned DataFrame.
The shape of the cleaned DataFrame was (6302, 36), for which I only needed the following columns: ['Year_Unique', 'Date2', 'Day', 'Month', 'Hour', 'Time_Range','Country', 'Area', 'Type', 'Injury', 'Fatal', 'Species','First_Name','Last_Name','Sex', 'Age','Activity_Category','TimeRange-ActCategory'] for the years 2000's onwards. For that reason I have created the sub_df with a shape of (1978, 18) and finally for visualization purposes, a 2nd sub-DataFrame was created considering the top-5 countries impacted with shark attacks which were: 'Usa','Australia','South africa','Brazil','Bahamas', giving me a final shape of (1581, 18).

***
### 5. Visualizations
***
1. Understanding if Australia is the riskies countries from shark attacks reported from 2000's onwards:

![Alt text](images/top_5_time_range_fig.jpg)

- Australia is the 2nd Country with 19% of the attacks registered during 2000's, USA is the first one with over 48%. There is a trend of being the afternoon the top offender time rage of the attacks in every country during this period.

2. Understanding if surfing is the riskiest activity:

![Alt text](images/top_5_activity_fig.jpg)

![Alt text](images/top_5_activity_por_fig.jpg)

- In Australia and USA is noticeable that surfing is the most impacted activity, not only in the number of attacks but also in the porcentage that they represent from all those attacks.

3. Getting a better understanding if the attacks occurs the most in the affternoon:

![Alt text](images/risk_time_yoy_fig.jpg)

![Alt text](images/top_5_time_range_por_fig.jpg)

- YoY the top impacting time rage among all the countries reported from 2000's onwards is constantly during the afternoon. Also from the top 5 countries attacked the most, the porcentage of attacks reported during the afternoon are higher than other time rages.

4. Is there a pattern in time_range and activities?

![Alt text](images/top_5_time_range_act_por_fig.jpg)

- The porcentage of attacks reported in the afternoon due to surfing reasons are the highest being Australia the one that reported the most.

5. Understnading if there is any trend YoY:

![Alt text](images/attacks_yoy_fig.jpg)

![Alt text](images/top_5_yoy_fig.jpg)

- There are no trend YoY, USA and Australia are constantly being the countries reporting the most (in that order).

6. Understanding if the attacks reported YoY are fatal:

![Alt text](images/fatality_yoy_fig.jpg)

- During this time frame, the attacks reported are not fatal having the highest number of attacks not fatal reported in 2015 and the highest amout fatal in 2011 and 2004.

7. Understanding if there is any riskier month:

![Alt text](images/attacks_mom_fig.jpg)

![Alt text](images/top_5_mom_fig.jpg)

![Alt text](images/australia_activities_mom_fig.jpg)

- The month with the highest attacks reportes was July. In Australia the highest number of attacks reported was in January and in terms of activities, March was the riskiest month for Surfing.
***
### 6. Conclusions
***
Based on the hypothesis of this project and after analyzing the data and visualizing the results, we can conclude the following:
- Australia is the 2nd Country with 19% of the attacks registered during 2000's, USA is the first one with over 48%.
- Surfing is the main cause of the attacks registered (38% of them) and surfing during the afternoon represets over 20% of the attacks in Australia.
- Over 57% of the attacks occurs during the Afternoon in Australia.
- There is no clear trend YoY during 2000's but ever since 2000's the registration of attacks recorrded increased drastically, this would be a good point to investigate the reason behind this spike.
- We can confirm that most of the attacks are not fatal -> Only 24% of them are but over 33% are fatal in Australia during this period of time (which is more in comparison to the rest of the top 5 countries).
- The riskiest month where attacks were registerd the most for Surfing activity is March.
***
### 7. Links and Resources
***
- Data source: https://www.kaggle.com/teajay/global-shark-attacks
- Library used:
    - https://numpy.org/doc/1.18/
    - https://pandas.pydata.org/
    - https://docs.python.org/3/library/functions.html
    - https://plotly.com/python/
    - https://matplotlib.org/
    - https://seaborn.pydata.org/
    - https://pandas.pydata.org/docs/