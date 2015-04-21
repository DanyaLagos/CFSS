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
		relatedartist_List.append(relatedartist['id'])

	return relatedartist_List

'''Next need function that will take these lists and convert them to names. Then string tuples.'''
def fetchArtistInfo(artist_id):
    """Using the Spotify API, takes a string representing the id and
`   returns a dictionary including the keys 'followers', 'genres', 
    'id', 'name', and 'popularity'.
    """
    

    artist_info = {}
    artist_info['followers'] = data['followers']['total']
    artist_info['genres'] = data['genres']
    artist_info['id'] = data['id']
    artist_info['name'] = data['name']
    artist_info['popularity'] = data['popularity']
    
    relatedartist_Names = []
    for relatedartist in data['lists']:
        relatedartist_Names.append(relatedartist['name'])


    return relatedartist_Names


print getRelatedArtists("6deZN1bslXzeGvOLaLMOIF")
print fetchArtistInfo("6deZN1bslXzeGvOLaLMOIF")