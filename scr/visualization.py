import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

def attacks_yoy (sub_df2):
    attacks_yoy_fig = sns.countplot(x=sub_df2.Year_Unique, palette="rocket")
    sns.set_context("poster")
    plt.title("Attacks evolution YoY")
    sns.set(rc={"figure.figsize": (30 ,6)})
    sns.set_style("whitegrid")
    attacks_yoy_fig.figure.savefig("C:/Users/maria/Desktop/Project_1_Pandas_Mariano/images/attacks_yoy_fig.jpg", dpi=500)
#attacks_yoy(sub_df2)

def attacks_mom (sub_df2):
    attacks_mom_fig = sns.countplot(x=sub_df2.Month, palette="rocket", order=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
    sns.set_context("poster")
    plt.title("Attacks evolution MoM", size=17)
    sns.set(rc={"figure.figsize": (30 ,6)})
    sns.set_style("whitegrid")
    attacks_mom_fig.figure.savefig("C:/Users/maria/Desktop/Project_1_Pandas_Mariano/images/attacks_mom_fig.jpg", dpi=500)
#attacks_mom (sub_df2)

def top_5_yoy (top_5_df):
    top_5_yoy_fig = sns.histplot(data=top_5_df, x= "Year_Unique", hue="Country", multiple="stack", palette="rocket", bins=10, alpha=1)
    plt.title("Riskiest 5 Countries evolution YoY", size=17)
    sns.set_style("whitegrid")
    top_5_yoy_fig.figure.savefig("C:/Users/maria/Desktop/Project_1_Pandas_Mariano/images/top_5_yoy_fig.jpg", dpi=500)
#top_5_yoy (top_5_df)

def risk_time_yoy (sub_df2):
    risk_time_yoy_fig = sns.countplot(x=sub_df2["Year_Unique"], hue=sub_df2["Time_Range"], palette="rocket")
    plt.legend(labels = ['Afternoon', 'Morning', 'Evening'], loc='upper right')
    plt.title("Riskiest Time Range by Year", size=17)
    sns.set_style("whitegrid")
    risk_time_yoy_fig.figure.savefig("C:/Users/maria/Desktop/Project_1_Pandas_Mariano/images/risk_time_yoy_fig.jpg", dpi=500)
#risk_time_yoy (sub_df2)

def fatality_yoy (sub_df2):
    fatality_yoy_fig = sns.countplot(x=sub_df2["Year_Unique"], hue=sub_df2["Fatal"], palette="rocket")
    plt.legend(labels = ['Not Fatal', 'Fatal'], loc='upper right')
    plt.title("Fatality by Year", size=17)
    plt.axhline(sub_df2.groupby('Year_Unique')['Fatal'].value_counts().unstack().fillna(0).loc[[2011]]['Y'].max(), c="r", linewidth=2, label="Max");
    plt.axhline(sub_df2.groupby('Year_Unique')['Fatal'].value_counts().unstack().fillna(0).loc[[2015]]['N'].max(), c="g", linewidth=2, label="Max");
    sns.set_style("whitegrid")
    fatality_yoy_fig.figure.savefig("C:/Users/maria/Desktop/Project_1_Pandas_Mariano/images/fatality_yoy_fig.jpg", dpi=500)
#fatality_yoy (sub_df2)

def top_5_mom (top_5_df):
    top_5_mom_fig = sns.countplot(x=top_5_df["Month"], hue=top_5_df["Country"], palette="rocket", 
                  order=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
    plt.axhline(top_5_df.groupby('Country')['Month'].value_counts().unstack().fillna(0).loc[['Australia']]['Jan'].max(), c="g", linewidth=2, label="Max");
    plt.title("Riskiest 5 Countries evolution MoM", size=17)
    sns.set_style("whitegrid")
    top_5_mom_fig.figure.savefig("C:/Users/maria/Desktop/Project_1_Pandas_Mariano/images/top_5_mom_fig.jpg", dpi=500)
#top_5_mom (top_5_df)

def top_5_time_range (sub_df2):
    top_5_time_range_fig = sns.countplot(y="Country", hue="Time_Range", data=sub_df2, palette="rocket",
                  order=sub_df2.Country.value_counts().iloc[:5].index)
    plt.title("Riskiest 5 Countries by Time Range", size=17)
    plt.axvline(sub_df2.groupby('Country')['Time_Range'].value_counts().unstack().fillna(0).loc[['Australia']]['Afternoon'].max(), c="g", linewidth=2, label="Max");
    sns.set_style("whitegrid")
    top_5_time_range_fig.figure.savefig("C:/Users/maria/Desktop/Project_1_Pandas_Mariano/images/top_5_time_range_fig.jpg", dpi=500)
#top_5_time_range (sub_df2)

def top_5_time_range_por (sub_df2):
    top_5_time_range_por_fig = top_5_df.groupby('Country')['Time_Range'].value_counts(normalize = True).unstack().fillna(0).plot(kind="bar", title="Deadliest Time")
    sns.set_palette("rocket")
    plt.axhline(top_5_df.groupby('Country')['Time_Range'].value_counts(normalize = True).unstack().fillna(0).loc[['Australia']]['Afternoon'].max(), c="g", linewidth=2, label="Max");
    plt.title("% of attacks by Time Range of the Riskiest 5 Countries", size=17)
    plt.xticks(rotation=0.5)
    top_5_time_range_por_fig.figure.savefig("C:/Users/maria/Desktop/Project_1_Pandas_Mariano/images/top_5_time_range_por_fig.jpg", dpi=500)
#top_5_time_range_por(top_5_df)

def top_5_activity (top_5_df):
    top_5_activity_fig = sns.countplot(x="Country", hue="Activity_Category", data=top_5_df, palette="rocket",
                  order=top_5_df.Country.value_counts().index)
    plt.title("Attacks by Activity Riskiest 5 Countries", size=17)
    top_5_activity_fig.figure.savefig("C:/Users/maria/Desktop/Project_1_Pandas_Mariano/images/top_5_activity_fig.jpg", dpi=500)
#top_5_activity (top_5_df)

def top_5_activity_por (top_5_df):
    top_5_activity_por_fig = top_5_df.groupby('Country')['Activity_Category'].value_counts(normalize = True).unstack().fillna(0).plot(kind="bar", title="% Riskiest Activity of top 5 Countries")
    plt.axhline(top_5_df.groupby('Country')['Activity_Category'].value_counts(normalize = True).unstack().fillna(0).loc['Australia']['Surfing'].max(), c="g", linewidth=2, label="Max");
    plt.title("% Riskiest Activity of top 5 Countries", size=17)
    sns.set_palette("rocket")
    plt.xticks(rotation=0.5)
    top_5_activity_por_fig.figure.savefig("C:/Users/maria/Desktop/Project_1_Pandas_Mariano/images/top_5_activity_por_fig.jpg", dpi=500)
#top_5_activity_por (top_5_df)

def top_5_time_range_act_por (top_5_df):
    top_5_time_range_act_por_fig =top_5_df.groupby('Country')['TimeRange-ActCategory'].value_counts(normalize = True).unstack().fillna(0).plot(kind="bar", title="% Riskiest Time & Activity by Country")
    plt.axhline(top_5_df.groupby('Country')['TimeRange-ActCategory'].value_counts(normalize = True).unstack().fillna(0).loc[['Australia']]['AfternoonSurfing'].max(), c="g", linewidth=2, label="Max");
    plt.title("% Riskiest Time & Activity by Country", size=17)
    sns.set_palette("rocket")
    plt.xticks(rotation=0.5)
    top_5_time_range_act_por_fig.legend(bbox_to_anchor=(1.0, 1.0))
    top_5_time_range_act_por_fig.figure.savefig("C:/Users/maria/Desktop/Project_1_Pandas_Mariano/images/top_5_time_range_act_por_fig.jpg", dpi=500)
#top_5_time_range_act_por (top_5_df)

def australia_activities_mom (top_5_df):
    australia_activities_mom_fig =sns.countplot(x="Month", hue="Activity_Category", data=top_5_df[top_5_df['Country']=='Australia'], palette="rocket",
                 order=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
    plt.axhline(top_5_df[top_5_df['Country']=='Australia'].groupby('Month')['Activity_Category'].value_counts().unstack().fillna(0).loc['Mar']['Surfing'].max(), c="g", linewidth=2, label="Max");
    plt.title("Attacks by Activity MoM in Australia", size=17)
    australia_activities_mom_fig.legend(bbox_to_anchor=(1.0, 1.0))
    australia_activities_mom_fig.figure.savefig("C:/Users/maria/Desktop/Project_1_Pandas_Mariano/images/australia_activities_mom_fig.jpg", dpi=500)
#australia_activities_mom (top_5_df)