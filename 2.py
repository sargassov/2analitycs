import pandas as pd
df = pd.read_csv('sample_data/kc_house_data.csv')

# Вывести на экран первые 5 строк. Посмотреть на описание признаков и на их содержание
df.head()

# Проведите первичный анализ данных. Изучите типы данных
df.dtypes

# Найдите количество пропущенных ячеек в данных
df.isnull().sum()

# В каком диапазоне изменяются стоимости недвижимости?
df['price'].min(), df['price'].max()

# Какую долю в среднем занимают жилая площадь от всей площади по всем домам?
mid_liv = df['sqft_living'].mean()
mid_ultimate = df['sqft_lot'].mean()
mid_liv / (mid_ultimate / 100)

# Как много домов с разными этажами в данных?
df['floors'].nunique()

# Насколько хорошие состояния у домов в данных?
df['grade'].value_counts()

# Найдите года, когда построили первый дом, когда построили последний дом в данных?
df['yr_built'].min(), df['yr_built'].max()

# Сколько в среднем стоят дома, у которых 2 спальни?
df[df['bedrooms'] == 2]['price'].mean()

# Какая в среднем общая площадь домов, у которых стоимость больше 600 000?
df[df['price'] > 600000]['sqft_lot'].mean()

# Как много домов коснулся ремонт?
df[df['yr_renovated'] > 0].shape[0]

# Насколько в среднем стоимость домов с оценкой grade домов выше 10 отличается от стоимости домов с оценкой grade меньше 4?
high_grd = df[df['grade'] > 10]['price'].mean()
low_grd = df[df['grade'] < 4]['price'].mean()
high_grd - low_grd

# Клиент хочет дом с видом на набережную, как минимум с тремя ванными и с подвалом. Сколько вариантов есть у клиента?
df[(df['waterfront'] > 0) & (df['bathrooms'] >= 3) & (df['sqft_basement'] > 0)].shape[0]

# Клиент хочет дом либо с очень красивым видом из окна, либо с видом на набережную, в очень хорошем состоянии и год постройки не меньше 1980 года. В какой ценовом диапазоне будут дома?
max_grade = df['grade'].max()
rdf = df[(df['waterfront'] > 0) & (df['grade'] == max_grade) & (df['yr_built'] >= 1980)]
rdf['price'].min(), rdf['price'].max()

# Клиент хочет дом без подвала, с двумя этажами, стоимостью до 150000. Какая оценка по состоянию у таких домов в среднем?
df[(df['sqft_basement'] == 0) & (df['floors'] == 2.0) & (df['price'] < 150000)]['grade'].mean()