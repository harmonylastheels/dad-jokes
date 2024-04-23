import random


def dad_joke():
    dad_jokes = [
        "Why couldn't the bicycle stand up by itself? It was two-tired.",
        "I'm reading a book on anti-gravity. It's impossible to put down!",
        "Why don't skeletons fight each other? They don't have the guts.",
        "Did you hear about the cheese factory that exploded? There was nothing left but de-brie.",
        "I used to play piano by ear, but now I use my hands.",
        "I'm on a seafood diet. I see food and I eat it."
    ]
    return random.choice(dad_jokes)

def main():
    input("Hit Enter to generate a random joke")
    joke = dad_joke()
    print("Here it goes:")
    print(joke)

if __name__ == "__main__":
    main()
