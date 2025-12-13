import requests
from bs4 import BeautifulSoup
import random
from pathlib import Path
import string

# constants
MERRIAM_WEBSTER_URL = "https://www.merriam-webster.com/"
WORD_OF_THE_DAY_URL = MERRIAM_WEBSTER_URL + "word-of-the-day/calendar"
SEARCH_DEFINITION_URL = MERRIAM_WEBSTER_URL + "dictionary/"

WORDS_REPO_FILE = "words.in"

def get_word_definition(word):
    # scrape definition from merriam webster website
    response = requests.get(SEARCH_DEFINITION_URL + word)
    content = response.content
    soup = BeautifulSoup(content, "html.parser")
    def_tag = soup.find("a", class_="share-icon-link d-flex justify-content-center align-items-center fb-social-link share-link fb")
    definition = def_tag["data-share-description"]

    # polish the definitions
    index = definition.find("… See the full definition")
    definition = definition[:index]
    definitions = definition.split("; ")

    return definitions
    

def scrape_words_from_merriam_web():
    # scrape word of the day url to collect words
    response = requests.get(WORD_OF_THE_DAY_URL)
    content = response.content
    soup = BeautifulSoup(content, "html.parser")
    word_containers = soup.find_all("div", class_="more-words-of-day-container")
    
    # save all words in a list
    words = []
    for container in word_containers:
        words_tag = container.find_all("a")
        for word in words_tag:
            words.append(word.get_text())

    # save words to offline file
    words_file = Path(WORDS_REPO_FILE)
    with open(words_file, "w") as f:
        for word in words:
            f.write(f"{word}\n")
    
    print(f"Saved in {words_file}!")

    return words

def scrape_words_from_file(filepath):
    words = []
    with open(filepath, "r") as f:
        for word in f:
            words.append(word.strip())
    return words

def get_words():
    # check if the input file exists
    word_file = Path(WORDS_REPO_FILE)
    if word_file.is_file():
        return scrape_words_from_file(word_file)
    else:
        return scrape_words_from_merriam_web()



def game_loop(words, choices_per_level = 5):
    NO_OF_LIVES = 5
    score = 0
    lives = NO_OF_LIVES

    while(lives != 0):
        print("-" * 20)
        print(f"LIVES: {lives}")
        
        # set correct answer
        choices = random.sample(words, choices_per_level)
        word = random.choice(choices)
        definitions = get_word_definition(word)
        lowercase = string.ascii_lowercase

        # display definition and choices
        print(f"\nDef: {definitions[0]}\n")
        for i in range(len(choices)):
            print(f"({lowercase[i]}) {choices[i]}")

        # get answer
        answer = input("\nAnswer: ")
        if answer in lowercase[0:len(choices)]:
            i = lowercase.index(answer)
            # check if correct
            if word == choices[i]:
                score += 1
                print("Correct!")
            else:
                lives -= 1
                print(f"Incorrect! Answer: {word}")
        else:
            print("Invalid answer!")
        print()

    print(f"\nSCORE: {score}")



def main():
    # quiz

    words = get_words()
    given_words = random.sample(words, 100)
    game_loop(given_words)

if __name__ == "__main__":
    main()
    
