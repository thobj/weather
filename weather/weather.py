# cli.py
import click
import requests

SAMPLE_API_KEY = "e6ad71a4553dc83a7f0038edc84565f2"
# SAMPLE_API_KEY = '2774183cfc38da293ae0701e1d660bd8'

def current_weather (location, api_key=SAMPLE_API_KEY ):
	url = 'https://api.openweathermap.org/data/2.5/weather'

	print ('APIKEY: ', api_key )

	query_params = {
		'q': location,
		'appid': api_key,
	}

	response = requests.get(url, params=query_params)

	return response.json()['weather'][0]['description']

@click.command()
@click.argument('location')
@click.option(
	'--api-key', '-a',
	help='your API key for the OpenWeatherMap API',
)

def main(location, api_key):

	if api_key:
		print ( 'MAINAPIKEY: ', api_key)
	else:
		api_key = SAMPLE_API_KEY

	"""
	OpenWeatherMap

	A Littel Weather Application

	"""

	weather = current_weather(location, api_key)
	print (f"The weather in {location} right now: {weather}.")

if __name__ == "__main__":
	main()
