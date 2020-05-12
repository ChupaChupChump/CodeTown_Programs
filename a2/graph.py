import requests
from bs4 import BeautifulSoup
​
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline
from bubbly.bubbly import bubbleplot
​
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly as py
import plotly.graph_objs as go
init_notebook_mode(connected=True) #do not miss this line
from plotly import tools

web_page=“https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(PPP)_per_capita"
req=requests.get(web_page)
page = req.text
soup = BeautifulSoup(page, ‘html.parser’)
soup.title

table = soup.find_all(“table”, “wikitable”)
len(table)
from IPython.display import IFrame, HTML
HTML(str(table))

GDP_PC = table[0]
table_rows = GDP_PC.find_all(‘tr’)
header = table_rows[1]
table_rows[1].a.get_text()

countries = [table_rows[i].a.get_text() for i in range(len(table_rows))[1:]]
cols = [col.get_text() for col in header.find_all(‘th’)]

country = []
for i in range(len(table_rows))[1:]:
 country.append(table_rows[i].a.get_text())

 temp = GDP_PC.find_all(‘td’)
temp[5].get_text()

temp = GDP_PC.find_all(‘td’)
GDP_per_capita = [temp[i].get_text() for i in range(len(temp)) if “,” in temp[i].get_text()]
GDP_per_capita = [i for i in GDP_per_capita if ‘\xa0’ not in i]
temp_list = []
for i in range(len(temp)):
 temp_list.append(temp[i].get_text())
new_list = temp_list[-11:]
numbers = [i for i in new_list if “\n” in i]
for i in numbers:
 GDP_per_capita.append(i)
rank = list(range(len(countries)))

data = zip(rank[0:21],countries[0:21], GDP_pc[0:21])
import pandas as pd
cols = [‘Rank’, ‘Country’, ‘GDP Per Capita’]
data1 = pd.DataFrame(list(data), columns = cols)
data2 = zip(rank[-21:],countries[-21:], GDP_pc[-21:])
data2 = pd.DataFrame(list(data2), columns = cols)

data1['GDP Per Capita'] = data1['GDP Per Capita'].apply(lambda x: x.replace('\n', '')).astype(int)
data2['GDP Per Capita'] = data1['GDP Per Capita'].apply(lambda x: x.replace(',', '')).astype(int)

trace1 = go.Bar(
 x = data1.Country,
 y = data1[‘GDP Per Capita’])
data = [trace1]
layout = go.Layout(
 title=’Top 20 countries ranked by GDP per Capita’)
fig = go.Figure(data = data, layout = layout)
py.offline.iplot(fig)

data = [ dict(
 type=’choropleth’,
 locations = data_all[‘Country’],
 autocolorscale = True,
 z = data_all[‘GDP Per Capita’],
 locationmode = ‘country names’,
 marker = dict(
 line = dict (
 color = ‘rgb(255,255,255)’,
 width = 2
 )
 ),
 colorbar = dict(
 title = “Millions USD”
 )
 ) ]
layout = dict(
 title = ‘Top Countries by GDP per capital’)
fig = go.Figure(data = data, layout = layout)
py.offline.iplot(fig)

gdp = pd.read_csv(“gdp_per_capota.csv”, engine = “python”)
life = pd.read_csv(“LifeExp.csv”, engine = “python”)
pop = pd.read_csv(“population.csv”, engine = “python”)
gapminder_indicators = pd.read_csv(“gapminder_indicators.csv”, engine = “python”)
countries = gapminder_indicators.country.unique()
continents = gapminder_indicators.continent.unique()
years = gapminder_indicators.year.unique()
[‘Country Name’,
 ‘1982’,
 ‘1987’,
 ‘1992’,
 ‘1997’,
 ‘2002’,
 ‘2007’,
 ‘2010’,
 ‘2013’,
 ‘2016’]
# Filter countries first
gdp_new = gdp[gdp[‘Country Name’].isin(countries)]
life_new = life[life[‘Country Name’].isin(countries)]
pop_new = pop[pop[‘Country Name’].isin(countries)]
# # Now filter years
years = [str(year) for year in years]
years = years[6:]
for i in [‘2010’, ‘2013’, ‘2016’]:
 years.append(i)
years.insert(0,”Country Name”)
gdp_new = gdp_new[years]
life_new = life_new[years]
pop_new = pop_new[years]