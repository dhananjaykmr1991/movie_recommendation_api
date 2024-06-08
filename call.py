import requests

# Function to get movie recommendations
def get_recommendations(movie_name):
    base_url = "http://127.0.0.1:5000/recommend"
    params = {'movie': movie_name}
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        recommendations = response.json().get('recommendations', [])
        return recommendations
    else:
        return response.json()

# Movie name
movie_name = "Thor: The Dark World"
# Get recommendations
recommendations = get_recommendations(movie_name)
print(recommendations)
