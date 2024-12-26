from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

# List of names
names = ["Jyothi","Bhavya", "Keerthi", "Geetanjali", "Sravya", "Ratna Kumari", "Dinisha","Pavani","Sushma", "Aswanth", "Killer", "Gana", "Madhu", "Narsingh", "Pandu", "Amith Marisetty", "Akhilesh", "Prudhvi","Sravan", "Aravind Sir", "Amar Sir", "Bhaskar Sir"]

# List of tasks
tasks = [
        "Do 10 jumping jacks",
        "Sing a song",
        "Draw something in 2 minutes: A dinosaur riding a skateboard. (Or) A cat wearing sunglasses and sipping a milkshake.",
        "SING A SONG IN OPPOSITE GENDER VOICE",
        "SING A ROMATIC FEEL SONG IN CRY MOOD",
        "Act like your favorite animal",
        "Imitate your favorite movie character",
        "DO CATWALK",
        "Do a quick sketch of your friend",
        "Spell your name backwards",
        "DANCE A SAD SONG IN HAPPY MANNER",
        "Do a tongue twister:  I scream, you scream, we all scream for ice cream",
        "Pick random objects around you and pose with them like they’re props in a fashion shoot",
        "Pretend to be a statue for 30 seconds",
        "Spin around 10 times and walk in a straight line",
        "Recreate Relangimavayya",
        "IMITATE LIKE CHANDRAMUKI AND TELL A DIALOGUE",
        "Act like you’re stuck in slow motion",
        "Invent and perform a secret handshake.",
        "behave like a u have ocd",
        "Balance on one foot for 20 seconds",
        "Pretend to take a call from a famous person: Jagan Maya",
        "Make a face and hold it for 15 seconds",
        "Act like you’re on a cooking show and describe making a weird dish",
        "Say something nice about everyone in the room",
        "Mime swimming in an imaginary pool",
        "Make up a song about your favorite food",
        "Try to balance a spoon on your nose",
        "Pretend to be a newscaster reporting on a ridiculous event",
        "Act out a scene from your favorite movie",
        "Create a commercial ad for an imaginary product: Black Lipstick",
        "Write a message using your non-dominant hand",
        "Make up a new dance move and name it",
        "Play air guitar to an imaginary rock song",
        "Act like you’re climbing a very steep mountain"
    ]

# Tracks assigned tasks for names
assigned_names = set()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_task', methods=['GET'])
def get_task():
    if names and tasks:
        # Get a random name that hasn't been assigned yet
        available_names = list(set(names) - assigned_names)
        if available_names:
            name = random.choice(available_names)
            assigned_names.add(name)
        else:
            name = None

        # Get a random task
        task = random.choice(tasks)
        tasks.remove(task)

        # Return name and task if name is available
        if name:
            return jsonify({"name": name, "task": task})
        else:
            return jsonify({"name": "", "task": task})

    elif tasks:
        # Only tasks remain
        task = random.choice(tasks)
        tasks.remove(task)
        return jsonify({"name": "", "task": task})
    else:
        return jsonify({"task": "No more tasks left! You've completed them all."})

if __name__ == '__main__':
    app.run(debug=True)
