import numpy as np
import pandas as pd
import re

def data_clean(df):

    """Description: 
                This function is meant for cleaning a DataFrame by dropping unnecesary columns, dropping NAs and splitting and creating new colums for better data exploration.
                The DF used was a csv file from Kaggle for Shark attacks analysis.-
        arguments:
            df - DataFrame to be worked upon which should contain the columns used in this function.
        return: 
            a cleaner and better structured DF.
    """
    df=pd.read_csv(df, engine= 'python')
    #Remove Columns Unnamed 22 and 23 since they don't have data at all
    df.drop(['Unnamed: 22','Unnamed: 23'], axis=1, inplace=True)
    #Capitalizing Counties since the data was all in upper
    df.Country = df.Country.str.capitalize()
    #Removing all the raws that contain too many NAN values
    df.dropna(thresh=14, inplace=True)
    #Rename Columns with spaces or too much info
    df.rename(columns={"Sex ":"Sex", "Species ":"Species","Fatal (Y/N)":"Fatal"}, inplace=True)
    #Creating a new column for last part of url -- objective- replace current pdf column as it's not complete
    df['Url2'] = df['href'].str.split('/').str[-1]
    #Creating a Last Name column from the url
    df['Last_Name'] = df['Url2'].str.extract('([a-zA-Z]{4,})', expand=True)
    #Creating First Name Column
    df['First_Name'] = df['Name'].str.split(' ').str[0]
    #Creating a 2nd date column from new url column
    df['Date2'] = df['Url2'].str.extract('(\d{4}.\d{2}.\d{2})', expand=True)
    #Creating columns for Day, Month and Year to check
    df['Day'] = df['Date'].str.split('-').str[0]
    df['Month'] = df['Date'].str.split('-').str[1]
    #To consolidate mainly to Jan-Feb type of month strings (many inconsitencies before)
    df['Month'] = df['Month'].str.extract('([a-zA-Z]{3,})', expand=True)
    df['Year2'] = df['Date2'].str.extract('([0-9]{4})', expand=True)
    #Creating Hour column
    df['Hour'] = df['Time'].str.extract('([0-9]{2})', expand=True)
    #Splitting Inv.Source into 2 columns>
    df['Investigator'] = df['Investigator or Source'].str.split(',').str[0]
    df['Source'] = df['Investigator or Source'].str.split(',').str[1]

    return df


def year_unique (row):
    """Description: 
                This function compares 2 columns to determinate a correct final Year based on differences from both columns.
        arguments:
            Year: The orignal year column from the DF.
            Year2: A column created from data_clean function
        return: 
            a final year column with more accuarate information from both columns checked.
    """
    if str(row['Year']) != 'nan' and str(row['Year2']) != 'nan':
        if str(row['Year']) == str(row['Year2']):
            return int(row['Year'])
        elif len(str(row['Year'])) <= 5:
            return int(row['Year'])
        elif len(str(row['Year2'])) <= 5:
            return int(row['Year2'])
        else:
            return 0
    elif str(row['Year']) == 'nan' and str(row['Year2']) != 'nan':
        if len(str(row['Year2'])) <= 5:
            return int(row['Year2'])
        else:
            return 0
    else:
        return 0


def time_range (row):
    """Description: 
                This function is needed to create a time range to determine the moment of the day from given hours.
        arguments:
            Time: This column belongs to the orignal DF and was not complete, but it also included some strings with time range, that's why is needed for further use.
            Hour: This column was previously created based from the hours of the Time column.
        return: 
            a final time_range based on Time or Hour column with the range for analysis.
    """
    if str(row['Hour']) != 'nan':
        if int(row['Hour']) > 6 and int(row['Hour']) < 14:
            return 'Morning'
        elif int(row['Hour']) >= 14 and int(row['Hour']) < 22:
            return 'Afternoon'
        else:
            return 'Evening'
    #There were many Uknown in the past since many rows in Time were strings with words contaning time-range, by adding this
    #we avoid having situations of unknowns but still is an option in case there is any
    elif str(row['Time']).lower().find('afternoon'):
        return 'Afternoon'
    elif str(row['Time']).lower().find('morning'):
        return 'Morning'
    elif str(row['Time']).lower().find('evening'):
        return 'Evening'
    else:
        return 'Unknown'

def category (row):
    """Description: 
                This function groups the activities to have a bigger view and not so granular.
        arguments:
            Activity: This column belongs to the orignal DF with a wide variaty of activities.
        return: 
            a final category based on Activity column with a bigger scope of activities in the same category for analysis.
    """
    if str(row['Activity']) != 'nan':
        if str(row['Activity']) in ['Surfing','Standing']:
            return 'Surfing'
        elif str(row['Activity']) in ['Swimming','Bathing']:
            return 'Swimming'
        elif str(row['Activity']) in ['Fishing','Wading']:
            return 'Fishing'
        elif str(row['Activity']) in ['Diving','Snorkeling','Spearfishing','Scuba diving']:
            return 'Diving'
        else:
            return 'Other Activity'
    else:
        return 'Unknown'

def TimeR_ActCat (row):
    """Description: 
                This function creates a time_range + Activity category group for analysis.
        arguments:
            Time_Range: Column created previously with a time range of the day.
            Activity_Category: Column created previously with a bigger scope of activities.
        return: 
            a final group of activities done in the same time range for analysis.
    """
    if str(row['Time_Range']) != 'nan' and str(row['Activity_Category']) != 'nan':
        return str(row['Time_Range']) + str(row['Activity_Category'])
    else:
        return 'Unknown'
    
def col_creation (df):
    """Description: 
                This function creates all the columns needed from the previous functions created.
        arguments:
            year_unique: Function for final Year output.-
            time_range: Function for time_rage output.-
            category: Function for activity_catergory creation output.-
            TimeR_ActCat: Function for time_range+Activity output.-
        return: 
            a final DataFrame with the new columns created.
    """
    df['Year_Unique'] = df.apply(lambda row: year_unique(row), axis=1)
    #Creating Time Range column applying the func
    df['Time_Range'] = df.apply(lambda row: time_range(row), axis=1)
    #Creating Activity Category group column
    df['Activity_Category'] = df.apply(lambda row: category(row), axis=1)
    #Creating TimeRange-Act.Category group column
    df['TimeRange-ActCategory'] = df.apply(lambda row: TimeR_ActCat(row), axis=1)
    
    return df

def sub_df_create (df):
    """Description: 
                This function creates a sub DataFrame from previous DF.
        arguments:
            df: DataFrame previously created
        return: 
            a final sub DataFrame with the reduced information of the columns needed for analysis and with better order.
    """
    sub_df = df[['Year_Unique', 'Date2', 'Day', 'Month', 'Hour', 'Time_Range',
          'Country', 'Area', 'Type', 'Injury', 'Fatal', 'Species',
            'First_Name','Last_Name','Sex', 'Age','Activity_Category','TimeRange-ActCategory']]
    return sub_df

def sub_df2_create (df):
    """Description: 
                This function creates a 2nd sub DataFrame from previous sub df filtered from Year_Unique.
        arguments:
            sub_df: sub DataFrame previously created
        return: 
            a final sub DataFrame with the reduced information from previous sub DF, ordered and from 2000's onwards.
    """
    sub_df = sub_df_create (df)
    sub_df2 = sub_df[sub_df["Year_Unique"] >2000]
    #Modifying value manually in row 463 of Year_Unique column as it was wrong.
    sub_df2.loc[463, "Year_Unique"] = 2014
    #Sorting Data Descending by Year_Unique
    sub_df2 = sub_df2.sort_values(by="Year_Unique", ascending=False)
    return sub_df2

def top_5_df (sub_df2):
    """Description: 
                This function creates a 3rd sub DataFrame from previous sub df2 filtered from Year_Unique and top 5 countries.
        arguments:
            sub_df2: sub DataFrame previously created filtered by Year_Unique > 2000
        return: 
            a final sub DataFrame with the reduced information from previous sub DF, ordered and from 2000's onwards but containing the top 5 impacting countriles.
    """
    #Creating a top 5 Countries with most shark attacks from 2000 onwards (sub_df2)
    top_5_df = sub_df2.query("Country in ('Usa','Australia','South africa','Brazil','Bahamas')")
    return top_5_df

def data_save(df, sub_df2, top_5_df):
    """Description: 
                This function saves all 3 df in 3 different csv files.
        arguments:
            df: original df cleaned.
            sub_df2: sub DataFrame previously created filtered by Year_Unique > 2000 and ordered descending from Year_Unique.
            top_5_df: top 5 countries with the most qty of attacks registered.
        return: 
            a final sub DataFrame with the reduced information from previous sub DF, ordered and from 2000's onwards but containing the top 5 impacting countriles.
    """
    df.to_csv("original_df_limpio.csv", index=False)
    sub_df2.to_csv("sub_df2.csv", index=False)
    top_5_df.to_csv("top_5_df.csv", index=False)
    return 'Files saved in folder'
