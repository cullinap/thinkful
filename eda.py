import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from IPython.display import display, HTML

FAT_BAR = '='*50


def eda(df: pd.DataFrame, target_variable: None):

	'''quick way of getting a snapshot of the data'''

	non_numeric_columns = df.select_dtypes(['object']).columns
	numeric_columns = df.select_dtypes(['int64', 'float64']).columns



	print('basic info for this dataframe...')
	print(FAT_BAR)
	display(HTML(df.head().to_html()))
	print(FAT_BAR)
	print(non_numeric_columns)
	print("The number of non-numerical columns is {}".format(len(non_numeric_columns)))
	print(FAT_BAR)
	print(numeric_columns)
	print("The number of numerical columns is {}".format(len(numeric_columns)))
	print(FAT_BAR)
	print('missing data/column names....')
	print(pd.DataFrame(df.isnull().sum().sort_values(ascending=False)))
	print(FAT_BAR)
	print(df.info())
	print(FAT_BAR)
	print(df.describe())
	print(FAT_BAR)

	if target_variable != None:
		top_corr = pd.DataFrame(np.abs(df[numeric_columns].iloc[:,1:].corr().loc[:,target_variable]
	                ).sort_values(
	            ascending=False
	        ))
		print(FAT_BAR)
		print('top 5 correlations')
		print(top_corr.head(5))
		print(FAT_BAR)
	else:
		pass

	if target_variable != None:
		sns.distplot(df[target_variable])
		plt.title('target variable: {}'.format(target_variable))
		plt.show()
	else:
		pass


def numeric_feature_corr(df):

	numeric_columns = df.select_dtypes(['int64', 'float64']).columns
	numeric_df = df.loc[:, [col for col in numeric_columns]]

	sns.pairplot(numeric_df)

	plt.title('Numeric Feature Correlation')
	plt.show()

