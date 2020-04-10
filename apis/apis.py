import requests
from us import states


def get_data_for_state(locale_name):
	"""
	A crude first API to get Covid case data for US states based on a name, abbreviation, or FIPS code.
	Made modular because I hope to swap out the data source for a more general one soon.
	"""
	abbr = get_state_abbr(locale_name)
	return filter_cases_and_deaths(check_cases_for_state(abbr))


def get_state_abbr(state_name):
	state = states.lookup(state_name)
	if state is not None:
		return state.abbr
	else:
		raise NameError(f'No state found for {state_name}.')


def check_cases_for_state(abbr):
	base_url = "https://covidtracking.com/api"
	states_url = "/v1/states/current.json"
	url = base_url + states_url
	response = requests.get(url)
	if response.ok:
		return list(filter(lambda state: state['state'] == abbr, response.json()))[0]


def filter_cases_and_deaths(state_data):
	keys = ['state', 'positive', 'death', 'dateChecked']
	return {key: state_data[key] for key in keys}
