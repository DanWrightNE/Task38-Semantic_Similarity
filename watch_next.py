import spacy
nlp = spacy.load('en_core_web_md')

# open and read text file
movie_file = open('movies.txt', 'r', encoding='utf-8')

# create list of movie titles to add to dictionary and the dictionary
movie_titles = []
movie_description = []
movie_dict = {}

# for loop adding each movie name and description to the dictionary
for lines in movie_file:
    movie_titles.append(lines.split(":")[0].strip())
    movie_description.append(lines.split(":")[1].strip())

# add movie names to dictionary
movie_dict = dict.fromkeys(movie_titles, 'pass')

# for loop adding descriptions to each key in the dictionary
index = 0
for keys in movie_dict:
    movie_dict[keys] = movie_description[index]
    index += 1

# similarity test looping through all items in the dictionary
planet_hulk = nlp("""Will he save the world or destroy it? When Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator.""")
for keys in movie_dict:
    print("Planet Hulk -", keys, " = ", int(float(planet_hulk.similarity(nlp(movie_dict[keys])))*100), "%")


# close the movie file
movie_file.close()