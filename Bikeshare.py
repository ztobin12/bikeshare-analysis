#!/usr/bin/env python
# coding: utf-8

# In[35]:


import pandas as pd


# In[36]:


NYC = pd.read_csv('/Users/zacktobin/Downloads/all-project-files/new_york_city.csv')
Chicago = pd.read_csv('/Users/zacktobin/Downloads/all-project-files/chicago.csv')
Washington = pd.read_csv('/Users/zacktobin/Downloads/all-project-files/washington.csv')


# In[37]:


# Add a new column to indicate the city
Chicago['City'] = 'Chicago'
NYC['City'] = 'New York City'
Washington['City'] = 'Washington'

# Combine the DataFrames
bike = pd.concat([Chicago, NYC, Washington], ignore_index=True)
bike.head()


# In[38]:


#modify start time and end time format
bike['Start Time'] = pd.to_datetime(bike['Start Time'], format='%Y-%m-%d %H:%M:%S')
bike['End Time'] = pd.to_datetime(bike['End Time'], format='%Y-%m-%d %H:%M:%S')


# In[39]:


#Create a column for months
month_names = {
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December'
}

bike['Month'] = bike['Start Time'].dt.month
bike['Month'] = bike['Month'].apply(lambda x: month_names[x])


# In[46]:


# limit to the three cities and then group
common_months = (
    bike[bike['City'].isin(['New York City', 'Chicago', 'Washington'])]
      .groupby('City')['Month']
      .agg(lambda x: x.mode()[0])    # mode()[0] picks the top mode
)

for city, month in common_months.items():
    print(f"In {city} the most common month is {month}")


# In[41]:


bike.head()


# In[47]:


day_of_week =  {
    0: 'Monday',
    1: 'Tuesday',
    2: 'Wednesday',
    3: 'Thursday',
    4: 'Friday',
    5: 'Saturday',
    6: 'Sunday'
}

bike['Day of Week'] = bike['Start Time'].dt.dayofweek
bike['Day of Week'] = bike['Day of Week'].apply(lambda x: day_of_week[x])


# In[48]:


common_dow = (
    bike[bike['City'].isin(['New York City', 'Chicago', 'Washington'])]
      .groupby('City')['Day of Week']
      .agg(lambda x: x.mode()[0])    # mode()[0] picks the top mode
)

print(common_dow)


# In[49]:


# 1) Compute the most-common day of week per city
common_dow = (
    bike[bike['City'].isin(['New York City','Chicago','Washington'])]
      .groupby('City')['Day of Week']
      .agg(lambda x: x.mode()[0])
)

# 2) Iterate and print, using a sensible variable name for the day
for City, dow in common_dow.items():
    print(f"In {City} the most common Day of Week is {dow}")


# In[51]:


#find the most common hour

# 1) ensure datetime
bike['Start Time'] = pd.to_datetime(bike['Start Time'])

# 2) extract hour into its own column
bike['hour'] = bike['Start Time'].dt.hour

# 3) compute most‐common hour for each city
common_hour = (
    bike[bike['City'].isin(['New York City','Chicago','Washington'])]
      .groupby('City')['hour']
      .agg(lambda x: x.mode()[0])
)

# 4) print nice sentences
for City, hr in common_hour.items():
    print(f"In {City} the most common start hour is {hr}:00")


# In[53]:


#Find the most common start station, end station, and trip
common_stations = bike.groupby('City').apply(
    lambda df: pd.Series({
        'most_common_start': df['Start Station'].mode()[0],
        'most_common_end'  : df['End Station'].mode()[0],
        'most_common_trip' : (df['Start Station'] + " → " + df['End Station']).mode()[0]
    })
).loc[['New York City','Chicago','Washington']]

print(common_stations)


# In[57]:


#Find average and total time
stats = (
    bike.groupby('City')['Trip Duration']
      .agg(total_travel_time='sum', average_travel_time='mean')
)

print(stats)


# In[60]:




# 1) Counts of each User Type by city
user_type_counts = (
    bike
      .groupby('City')['User Type']
      .value_counts()
      .unstack(fill_value=0)
)
print("User Type counts:\n", user_type_counts)

# 2) Counts of each Gender
#    drop rows where Gender is NaN so Washington (which has no data) is excluded
gender_counts = (
    bike
      .dropna(subset=['Gender'])
      .groupby('City')['Gender']
      .value_counts()
      .unstack(fill_value=0)
)
print("\nGender counts:\n", gender_counts)

# 3) Birth‐Year stats (earliest, most recent, most common)
birth_stats = (
    bike
      .dropna(subset=['Birth Year'])
      .groupby('City')['Birth Year']
      .agg(
          earliest    = 'min',
          most_recent = 'max',
          most_common = lambda x: x.mode()[0]
      )
)
print("\nBirth Year stats:\n", birth_stats)


# In[ ]:




