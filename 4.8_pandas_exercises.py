from datetime import datetime
from env import user, host, pw
import pandas as pd
import numpy as np
from pydataset import data
import matplotlib.pyplot as plt

d = pd.Series(['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80',
               '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23'])

d = d.str.replace('$', '').str.replace(',', '')
# d = d.str.replace(',', '')

pd.to_numeric(d)
# print(d)

mpg = data('mpg')

mpg.shape  # 234 rows, 11 columns

mpg.sample(5)

mpg.ftypes

# manufacturer     object:dense
# model            object:dense
# displ           float64:dense
# year              int64:dense
# cyl               int64:dense
# trans            object:dense
# drv              object:dense
# cty               int64:dense
# hwy               int64:dense
# fl               object:dense
# class            object:dense

# Do any cars have better city mileage than highway mileage?

(mpg.cty > mpg.hwy).any()

# False

# Create a column named milelage_difference this column should contain
# the difference between highway and city milelage for each car.

mil_diff = mpg.hwy - mpg.cty
mpg['mileage_difference'] = mil_diff

mpg.head()

# On average, which manufacturer has the best miles per gallon?

cty_mpg = mpg.sort_values(['cty'], ascending=False).head(3)
hwy_mpg = mpg.sort_values(['hwy'], ascending=False).head(3)
cty_mpg
hwy_mpg

# volkswagen has the top 3

# How many different manufacturers are there?

len(mpg.manufacturer.unique())

# 15

# How many different models are there?

mpg.model.unique().shape[0]

# 38

# Do automatic or manual cars have better miles per gallon?

# manual has a higher cty + hwy

mam = data('Mammals')

mam.shape

# 107 rows, 4 columns

# What are the data types?

mam.ftypes

# weight      float64:dense
# speed       float64:dense
# hoppers        bool:dense
# specials       bool:dense

# What is the the weight of the fastest animal?

mam.sort_values(by='speed', ascending=False).head()

# 55.

# What is the overal percentage of specials?

special_pct = mam.specials.sum() / mam.specials.shape[0]
special_pct = special_pct * 100
special_pct

# 9.35%

# How many animals are hoppers that are above the median speed?
# What percentage is this?

# speed_avg = mam.speed.mean()
# speed_avg

# hop_over_med = mam[['hoppers', 'speed']].sort_values('speed', ascending=False).where(mam.speed > 46)
# hop_over_med.head()

med = mam.speed.median()
med

hoppers = mam[mam.hoppers]
hoppers_above_median = hoppers[hoppers.speed >= mam.speed.median()]
hoppers_above_median

hoppers_above_med_pct = 100 * \
    (hoppers[hoppers.speed >= mam.speed.median()].shape[0] / hoppers.shape[0])
hoppers_above_med_pct

# 63.63%


def get_db_url(db, user, host, password):
    from sqlalchemy import create_engine
    url = f'mysql+pymysql://{user}:{password}@{host}/{db}'
    return create_engine(url)


conn = get_db_url('employees', user, host, pw)

emp = pd.read_sql('employees', conn)
emp.head()
title = pd.read_sql('titles', conn)
title.head()

#
employees = pd.read_sql('SELECT * FROM employees', conn)
titles = pd.read_sql('titles', conn)
employees.head()
titles.head()

%matplotlib qt

titles.title.value_counts().plot.bar()
plt.xticks(rotation=30)
plt.subplots_adjust(left=0.15, right=0.95, top=0.95, bottom=0.2)
current_titles = titles[titles.to_date > datetime.now().date()]
current_titles.title.value_counts().plot.bar()

#


#
new_df = pd.read_sql('SELECT * from employees e \
    JOIN titles t ON e.emp_no = t.emp_no', conn)
new_df.head()


new_df = new_df.iloc[:, 1:]

new_plot = new_df.groupby('emp_no').count()

new_plot = new_df.groupby('emp_no').count()['title']
new_plot
new_plot.plot.hist()

t_count = new_df['title'].value_counts(dropna=True, sort=True)
t_count.plot.bar()

emp_titles = new_df.emp_no.shape[0], new_df.title.unique()
emp_titles

conn2 = get_db_url('chipotle', user, host, pw)
chip = pd.read_sql('SELECT * from orders', conn2)
chip.head()

total_price = chip.item_price * chip.quantity
total_price

stripped = chip.item_price.str.replace('$', '')
stripped.head()
chip.drop[['item_price']]

chip[['item_price']] = stripped
chip.head(10)

prices = [[chip.groupby('order_id'), chip.item_price.sum()]]
prices
