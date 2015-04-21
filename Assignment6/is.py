import requests
import pandas 
import csv
'''Function I.1:
This function takes an artist ID as its only argument 
and returns a list of related artists IDs.'''
def getRelatedArtists(artistID):
	url = "https://api.spotify.com/v1/artists/" + artistID + "/related-artists"
	req = requests.get(url)
	assert req.ok, 'No record found.'
	data = req.json()
	assert data.get('artists'), 'No artist found.'

	relatedartist_List = [] 
	for relatedartist in data['artists']:
		relatedartist_List.append(relatedartist['name'])

	return relatedartist_List

print getRelatedArtists("6deZN1bslXzeGvOLaLMOIF")
