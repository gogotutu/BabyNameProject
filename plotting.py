import matplotlib.pyplot as plt
import pandas as pd

# Birth Rate Trends
br_df = pd.read_csv('Birth_Trends.csv', sep=',', header=None)
br_df[[1, 2]] = br_df[[1, 2]].astype(int)
# Pivot on year and state
br_df = br_df.pivot(index=1, columns=0)
br_df.columns = [state for _, state in br_df.columns.values]

# Plot the birth rate for New York, California, Pennsylvania, Florida,
# and Massachusetts

br_df[['NY','CA','PA','FL','MA']].plot()
plt.show()

# Name Origins Trends
no_df = pd.read_csv('Origins_By_State.csv', sep=',', header=None)
print(no_df)
no_df.columns = ['state', 'year', 'origin', 'cnt']
no_df[['cnt']] = no_df[['cnt']].astype(int)

# Take a slice of no_df
s_df = no_df[((no_df.state=='CA') & (no_df.year >= 2010) &
              (no_df.cnt >= 8000))]
del s_df['state']
#print(s_df)
# Take a look the naming origins for California from the year 2010 to 2014
# Pivot on origin and year
s_df = s_df.pivot(index='year', columns='origin')
s_df.columns = [state for _, state in s_df.columns.values]
s_df.plot(kind='bar', stacked=True)
plt.show()
