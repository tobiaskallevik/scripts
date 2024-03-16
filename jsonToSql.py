import json

# Read the JSON document
with open('exercises.json', 'r') as f:
    data = json.load(f)

# Convert the JSON data into the specified format
formatted_data = []
for item in data:
    name = item['name']
    muscleGroup = item['muscleGroup']
    requiresGym = item['requiresGym']  # No need to convert to int
    gifUrl = item['gifUrl']
    formatted_data.append((name, muscleGroup, requiresGym, gifUrl))

# Write the formatted data to a text document
with open('output.txt', 'w') as f:
    for item in formatted_data:
        f.write(str(item) + ',\n')
