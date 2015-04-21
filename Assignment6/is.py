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

#print getRelatedArtists("6deZN1bslXzeGvOLaLMOIF")

#NEXT STEPS - INCORPORATE THIS SOMEHOW INTO FUNCTION THAT REPLICATES THE FUNCTION OF artistNetworks.py

def getDepthEdges(artistID, depth):
    
    directedPairs = []
    directedPairs_checked = []
    relatedArtists = []
    relatedArtists.append(name)

    for i in range(depth):
    	for relatedartist in relatedArtists: 
    		newartists = getRelatedArtists(relatedartist)
    		for newartist in newartists:
    			directedPairs.append((relatedartist, newartist))
    		relatedArtists = newartists
    	for tple in directedPairs:
    		if tple not in directedPairs_checked:
    			directedPairs_checked.append(tple)

    	return directedPairs_checked

print getDepthEdges("6deZN1bslXzeGvOLaLMOIF", 2)