import pandas as pd
import pycountry

# instatiate data frame
subdivs = pd.DataFrame()
outfile = '~/DocMatter/country_data/output/autooutput.csv'

# these objects are of a pycountry.Subdivisions class so we cast as list
subdivs['divisions'] = list(pycountry.subdivisions)

def parseSubdivs(df):
	df = subdivs
	# cast as string to make easier to extract as a text blob via regex
	subdivs['divisions'] = subdivs.astype(str)
	# grab the subdivision name
	subdivs['name'] = subdivs['divisions'].str.extract(r"name='(.*?)',", expand=False)
	# grab the country code
	subdivs['country_code'] = subdivs['divisions'].str.extract(r"country_code='(.*?)',", expand=False)
	# grab the division type
	subdivs['division_type'] = subdivs['divisions'].str.extract(r"type='(.*?)'", expand=False)
	
	# country name isn't stored in the subdivision object but we can use the country code to grab it
	country_name_list = []
	for i in subdivs['country_code']:
		country_name = pycountry.countries.get(alpha_2=i).name
		country_name_list.append(country_name)

	return country_name_list

if __name__ == '__main__':
	parseSubdivs(subdivs)
	subdivs.to_csv(outfile,encoding="utf-8-sig",index=False)