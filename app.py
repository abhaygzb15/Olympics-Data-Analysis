import streamlit as st
import pandas as pd
import preprocessor,helper
import plotly.express as px
import plotly.figure_factory as ff
import matplotlib.pyplot as plt
import seaborn as sns
import scipy
st.set_option('deprecation.showPyplotGlobalUse', False)

df=pd.read_csv(r'C:\Users\ABHAY\Desktop\Probability_Project\all_athlete_games.csv')
regions=pd.read_csv(r'C:\Users\ABHAY\Desktop\Probability_Project\all_regions.csv')
df=preprocessor.preprocess(df,regions)

st.sidebar.title("Olympics Analysis")
st.sidebar.image('https://encrypted-tbn0.gstatic.com/'
'images?q=tbn:ANd9GcTDuRW3nBuxJRI0oZeCUpr3yrm1CuDO5wVqB8ZntkhC9BQVuWHsKs_JNimaSj7FgvewxNY&usqp=CAU')
user_menu=st.sidebar.radio(
    'Select an Option',
    ('Medal Tally','Overall Analysis','Country-wise Analysis','Athlete-wise Analysis')
)
if user_menu=='Medal Tally':
    st.sidebar.header("Medal Tally")
    years,country=helper.country_year_list(df)

    selected_year=st.sidebar.selectbox("Select Year",years)
    selected_country=st.sidebar.selectbox("Select Country",country)
    medal_tally=helper.fetch_medal_tally(df,selected_year,selected_country)
    if selected_country=='Overall' and selected_year=='Overall':
        st.title("Overall Tally")
    if selected_year!='Overall' and selected_country=='Overall':
        st.title('Medal Tally in'+str(selected_year)+" Olympics")
    if selected_year=='Overall' and selected_country!='Overall':
        st.title(selected_country+" overall performance")
    if selected_year!='Overall' and selected_country!='Overall':
        st.title(selected_country+" performance in "+str(selected_year))
    st.table(medal_tally)

if user_menu=="Overall Analysis":
    editions=df['Year'].unique().shape[0]-1
    cities=df['City'].unique().shape[0]
    sports=df['Sport'].unique().shape[0]
    events=df['Event'].unique().shape[0]
    athletes=df['Name'].unique().shape[0]
    nations=df['Region'].unique().shape[0]

    st.title("Top Statistics")
    col1,col2,col3 = st.columns(3)
    with col1:
        st.header("Editions")
        st.title(editions)
    with col2:
        st.header("Hosts")
        st.title(cities)
    with col3:
        st.header("Sports")
        st.title(sports)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("Events")
        st.title(events)
    with col2:
        st.header("Nations")
        st.title(nations)
    with col3:
        st.header("Athletes")
        st.title(athletes)

    nations_over_time=helper.data_over_time(df,'Region')
    fig = px.line(nations_over_time, x='Edition', y='Region')
    st.title("Participating Nations over the years")
    st.plotly_chart(fig)

    events_over_time = helper.data_over_time(df, 'Event')
    fig = px.line(events_over_time, x='Edition', y='Event')
    st.title("Events over the years")
    st.plotly_chart(fig)

    athletes_over_time = helper.data_over_time(df, 'Name')
    fig = px.line(athletes_over_time, x='Edition', y='Name')
    st.title("Athletes over the years")
    st.plotly_chart(fig)

    st.title("Top 15 Countries with Highest Medals")
    top_15_total=helper.medal_tally(df)
    top_15_total = top_15_total.sort_values(by='total',ascending=False)[:15]
    fig=px.bar(top_15_total,x='Region', y='total',
               labels={'total': 'Total Medals', 'Region': 'Country'})
    st.plotly_chart(fig)

    st.title("Top 15 Countries with Highest Gold Medals")
    top_15_gold = helper.medal_tally(df)
    top_15_gold = top_15_gold.sort_values(by='Gold', ascending=False)[:15]
    fig = px.bar(top_15_gold, x='Region', y='Gold',
                 labels={'total': 'Total Gold Medals', 'Region': 'Country'})
    st.plotly_chart(fig)

    st.title("Age  VS  No. of Participants")
    age_dist = df['Age'].dropna().astype(int).value_counts().sort_values(ascending=False).head(15)
    age_dist= pd.DataFrame({'Age': age_dist.index, 'Participants Count': age_dist.values})
    st.table(age_dist)
    plt.hist(df.Age, color='purple', bins=45)
    plt.xlim(0, 90)
    st.pyplot()

    st.title("Gender Distribution")
    gender_wise=df.drop_duplicates(subset=['Name','Region'])
    gender_wise = gender_wise.Gender.value_counts()
    plt.pie(gender_wise, labels=gender_wise.index, autopct="%.2f%%", startangle=90)
    st.pyplot()

    st.title("Top 15 countries with maximum Participants")
    participation_wise=df.drop_duplicates(subset=['Name','Region'])
    participation_wise = participation_wise.Region.value_counts().sort_values(ascending=False).head(15)
    participation_wise= pd.DataFrame({'Region': participation_wise.index, 'Participants Count': participation_wise.values})
    st.table(participation_wise)
    fig = px.bar(participation_wise, x='Participants Count', y='Region')
    st.plotly_chart(fig)

    st.title("Yearwise Medal Count")
    yearwise_medal = df[df['Medal'].notna() & (df['Medal'] != 0)]
    yearwise_medal = yearwise_medal.drop_duplicates(subset=['Year', 'Event', 'Team', 'Medal'], keep='first')
    yearwise_medal = yearwise_medal.groupby('Year')['Medal'].value_counts().unstack()
    yearwise_medal.index = yearwise_medal.index.astype(int)
    yearwise_medal.index = pd.Categorical(yearwise_medal.index)
    yearwise_medal['total']=yearwise_medal['Gold']+yearwise_medal['Silver']+yearwise_medal['Bronze']
    st.table(yearwise_medal)
    yearwise_medal.drop(columns=['total'],inplace=True)
    fig = px.bar(yearwise_medal, x=yearwise_medal.index, y=yearwise_medal.columns, barmode='stack')
    fig.update_layout(
        xaxis_title='Year',
        yaxis_title='Total Medals',
        xaxis_tickangle=-45,
        legend_title='Medal'
    )
    st.plotly_chart(fig)


if user_menu=='Country-wise Analysis':
    st.title('Country-wise Analysis')
    country_list=df['Region'].dropna().unique().tolist()
    country_list.sort()
    selected_country=st.sidebar.selectbox('Select a Country',country_list)

    country_df=helper.yearwise_medal_tally(df,selected_country)
    fig = px.line(country_df,x='Year', y='Medal')
    st.title(selected_country + " Medal tally over the Years")
    st.plotly_chart(fig)

    st.title("Top 10 athletes of "+selected_country)
    top10df=helper.most_successful_countrywise(df,selected_country)
    st.table(top10df)

if user_menu=="Athlete-wise Analysis":

    st.title('Most successful Athletes')
    sport_list = df['Sport'].unique().tolist()
    sport_list.sort()
    sport_list.insert(0, "Overall")
    selected_sport = st.selectbox("Select a box", sport_list)
    x = helper.most_successful(df, selected_sport)
    st.table(x)

    athlete_df = df.drop_duplicates(subset=['Name', 'Region'])
    x1 = athlete_df['Age'].dropna()
    x2 = athlete_df[athlete_df['Medal'] == 'Gold']['Age'].dropna()
    x3 = athlete_df[athlete_df['Medal'] == 'Silver']['Age'].dropna()
    x4 = athlete_df[athlete_df['Medal'] == 'Bronze']['Age'].dropna()
    fig = ff.create_distplot([x1, x2, x3, x4], ["Overall Age", "Gold Medalist", "Silver Medalist", "Bronze Medalist"],
                             show_hist=False, show_rug=False)
    st.title("Distribution of Age")
    st.plotly_chart(fig)

    st.title("Men Vs Women Participation over the Years")
    final=helper.men_vs_women(df)
    fig = px.line(final, x='Year', y=['Male', 'Female'])
    st.plotly_chart(fig)