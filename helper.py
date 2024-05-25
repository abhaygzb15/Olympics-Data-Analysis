import numpy as np

def fetch_medal_tally(df,year, country):
    medal_tally_new = df.drop_duplicates(subset=['Team', 'NOC', 'Year', 'City', 'Sport', 'Event', 'Medal'])
    flag=0
    if year == 'Overall' and country == 'Overall':
        temp_df = medal_tally_new
    if year == 'Overall' and country != 'Overall':
        flag=1
        temp_df = medal_tally_new[medal_tally_new['Region'] == country]
    if year != 'Overall' and country == 'Overall':
        temp_df= medal_tally_new[medal_tally_new['Year'] == year]
    if year != 'Overall' and country != 'Overall':
        temp_df = medal_tally_new[(medal_tally_new['Region'] == country) & (medal_tally_new['Year'] == year)]
    if flag==1:
        x = temp_df.groupby('Year')[['Gold', 'Silver', 'Bronze']].sum().sort_values('Year').reset_index()
    else:
        x = temp_df.groupby('Region')[['Gold', 'Silver', 'Bronze']].sum().sort_values('Gold',ascending=False).reset_index()
    x['total'] = x['Gold'] + x['Silver'] + x['Bronze']
    x['Gold']=x['Gold'].astype('int')
    x['Silver']=x['Silver'].astype('int')
    x['Bronze']=x['Bronze'].astype('int')
    x['total']=x['total'].astype('int')
    return x

def medal_tally(df):
    medal_tally = df.drop_duplicates(subset=['Team', 'NOC', 'Year', 'City', 'Sport', 'Event', 'Medal'])
    medal_tally = medal_tally.groupby(['Region'])[['Gold', 'Silver', 'Bronze']].sum().sort_values('Gold',
                                                                                          ascending=False).reset_index()
    medal_tally['total'] = medal_tally['Gold'] + medal_tally['Silver'] + medal_tally['Bronze']
    return medal_tally

def country_year_list(df):
    years=df['Year'].unique().tolist()
    years.sort()
    years.insert(0,"Overall")

    country = np.unique(df['Region'].dropna().values).tolist()
    country.sort()
    country.insert(0,"Overall")
    return years,country

def data_over_time(df,col):
    nations_over_time = df.drop_duplicates(['Year', col])[
        'Year'].value_counts().reset_index().sort_values('Year')
    nations_over_time = nations_over_time.rename(columns={'Year': 'Edition', 'count': col})
    return nations_over_time

def most_successful(df,sport):
    temp_df=df.dropna(subset=['Medal'])
    if(sport!="Overall"):
        temp_df=df[df['Sport']==sport]
    x=temp_df['Name'].value_counts().reset_index().head(15)
    x.rename(columns={'Name':'index','count':'Name'},inplace=True)
    x=x.merge(df,left_on='index',right_on='Name',how='left')[['index','Name_x','Sport','Region']].drop_duplicates('index')
    x.rename(columns={'index':'Name','Name_x':'Medals'},inplace=True)
    return x

def yearwise_medal_tally(df,country):
    temp_df = df.dropna(subset=['Medal'])
    temp_df.drop_duplicates(subset=['Team', 'NOC', 'Year', 'City', 'Sport', 'Event', 'Medal'], inplace=True)
    new_df = temp_df[temp_df['Region'] == country]
    final_df = new_df.groupby(['Year'])['Medal'].count().reset_index()
    return final_df

def most_successful_countrywise(df,country):
    temp_df=df.dropna(subset=['Medal'])
    temp_df=temp_df[temp_df['Region']==country]
    x=temp_df['Name'].value_counts().reset_index().head(10)
    x.rename(columns={'Name':'index','count':'Name'},inplace=True)
    x=x.merge(df,left_on='index',right_on='Name',how='left')[['index','Name_x','Sport']].drop_duplicates('index')
    x.rename(columns={'index':'Name','Name_x':'Medals'},inplace=True)
    return x

def men_vs_women(df):
    men = df[df['Gender'] == 'Male'].groupby(['Year'])['Name'].count().reset_index()
    women = df[df['Gender'] == 'Female'].groupby(['Year'])['Name'].count().reset_index()
    final = men.merge(women, on='Year', how='left')
    final.rename(columns={'Name_x': 'Male', 'Name_y': 'Female'}, inplace=True)
    final.fillna(0, inplace=True)
    return final
