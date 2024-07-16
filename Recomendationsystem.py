
def recommend(self, preference):
    recommendation = []
    for item, genres in self.Item.Item():
        if any(genre in preference for genre in genres):
            recommendation.append(item)
    return recommendation
recomendations = {
    "Toy Story (1995)": ["Adventure", "Animation", "Children", "Comedy", "Fantasy"],
    "Jumanji (1995)": ["Adventure", "Children", "Fantasy"],
    "Grumpier Old Men (1995)": ["Comedy", "Romance"],
    "Waiting to Exhale (1995)": ["Comedy", "Drama", "Romance"],
    "Father of the Bride Part II (1995)": ["Comedy"],
    "Heat (1995)": ["Action", "Crime", "Thriller"],
    "Sabrina (1995)": ["Comedy", "Romance"],
    "Tom and Huck (1995)": ["Adventure", "Children"],
    "Sudden Death (1995)": ["Action"],
    "GoldenEye (1995)": ["Action", "Adventure", "Thriller"],
    "American President, The (1995)": ["Comedy", "Drama", "Romance"],
    "Dracula: Dead and Loving It (1995)": ["Comedy", "Horror"],
    "Balto (1995)": ["Adventure", "Animation", "Children"],
    "Nixon (1995)": ["Drama"],
    "Cutthroat Island (1995)": ["Action", "Adventure", "Romance"],
    "Casino (1995)": ["Crime", "Drama"],
    "Sense and Sensibility (1995)": ["Drama", "Romance"],
    "Four Rooms (1995)": ["Comedy"],
    "Ace Ventura: When Nature Calls (1995)": ["Comedy"],
    "Money Train (1995)": ["Action", "Comedy", "Crime", "Drama", "Thriller"],
    "Get Shorty (1995)": ["Comedy", "Crime", "Thriller"]}

user_input = input("Enter your movie preferences (separated by commas): ")
preference = [p.strip() for p in user_input.split(',')]
recommendation = recommend(preference)
print("Recommended movies for the preference:")
for movie in recommendation: 
    print("-", movie)
