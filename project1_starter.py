"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: [Your Name Here]
Date: [Date]

AI Usage: [Document any AI assistance used]
Example: AI helped with file I/O error handling logic in save_character function
"""

import os
def create_character(name, character_class):
    """
    Creates a new character dictionary with calculated stats
    Returns: dictionary with keys: name, class, level, strength, magic, health, gold
    
    Example:
    char = create_character("Aria", "Mage")
    # Should return: {"name": "Aria", "class": "Mage", "level": 1, "strength": 5, "magic": 15, "health": 80, "gold": 100}
    """
    character = {"name": name,
                "class": character_class,
                "level": 1,
                "gold": 100}
    
    # Calculate initial stats based on class and level
    strength, magic, health = calculate_stats(character_class, 1)
    character["strength"] = strength
    character["magic"] = magic
    character["health"] = health
    
    return character

# Calculates the stats based on character class and level
def calculate_stats(character_class, level):
    if character_class == "Warrior":
        strength = 10 + (level * 5)
        magic = 2 + (level * 1)
        health = 100 + (level * 10)
    elif character_class == "Mage":
        strength = 3 + (level * 1)
        magic = 10 + (level * 5)
        health = 70 + (level * 10)
    elif character_class == "Rogue":
        strength = 6 + (level * 3)
        magic = 5 + (level * 3)
        health = 50 + (level * 5)
    elif character_class == "Healer":
        strength = 5 + (level * 3)
        magic = 8 + (level * 3)
        health = 100 + (level * 10)
    else:
        strength = 0
        magic = 0
        health = 0
    return (strength, magic, health)
    # TODO: Implement this function
    # Return a tuple: (strength, magic, health)
    


def save_character(character, filename):
    """
    Saves character to text file in specific format
    Returns: True if successful, False if error occurred
    """
    # validate filename
    if filename == "" or filename is None:
        print("Error: Invalid filename")
        return False 

    # check if directory exists
    directory = os.path.dirname(filename)
    if directory and not os.path.exists(directory):
        print("Error: Directory does not exist")
        return False

    # write character data to file using UTF-8 encoding
    # Needed to add encoding to open function to handle special characters error
    # AI helped with this part
    with open(filename, 'w', encoding='utf-8') as save_character_file:
        save_character_file.write(f"Character Name: {character.get('name')}\n")
        save_character_file.write(f"Class: {character.get('class')}\n")
        save_character_file.write(f"Level: {character.get('level')}\n")
        save_character_file.write(f"Strength: {character.get('strength')}\n")
        save_character_file.write(f"Magic: {character.get('magic')}\n")
        save_character_file.write(f"Health: {character.get('health')}\n")
        save_character_file.write(f"Gold: {character.get('gold')}\n")
    return True
    # TODO: Implement this function
    # Remember to handle file errors gracefully
    

def load_character(filename):
   """
    Loads character from text file
    Returns: character dictionary if successful, None if file not found
    """
    # Handle file not found error
    if not os.path.exists(filename):
        print("Error: File not found")
        return None

    # read the character data from the file using UTF-8 encoding
    # Needed to add encoding to open function to handle special characters error
    with open(filename, 'r', encoding='utf-8') as load_character_file:
        lines = load_character_file.readlines()

    # Creates empty character dictionary and fills it with data from file
    character = {}
    for line in lines:
        value = line.split(": ")[1].strip()
        # Helps to map the file lines to the character dictionary keys
        if "Character Name" in line:
            character['name'] = value
        elif "Class" in line:
            character['class'] = value
        elif "Level" in line:
            character['level'] = int(value)
        elif "Strength" in line:
            character['strength'] = int(value)
        elif "Magic" in line:
            character['magic'] = int(value)
        elif "Health" in line:
            character['health'] = int(value)
        elif "Gold" in line:
            character['gold'] = int(value)
    return character
    # TODO: Implement this function
    # Remember to handle file not found errors
    

def display_character(character):
    """
    Prints formatted character sheet
    Returns: None (prints to console)
    
    Example output:
    === CHARACTER SHEET ===
    Name: Aria
    Class: Mage
    Level: 1
    Strength: 5
    Magic: 15
    Health: 80
    Gold: 100
    """
    # How to display character information in a readable format
    print("=== CHARACTER SHEET ===")
    print(f"Name: {character['name']}")
    print(f"Class: {character['class']}")
    print(f"Level: {character['level']}")
    print(f"Strength: {character['strength']}")
    print(f"Magic: {character['magic']}")
    print(f"Health: {character['health']}")
    print(f"Gold: {character['gold']}")

    # TODO: Implement this function


def level_up(character):
    """
    Increases character level and recalculates stats
    Modifies the character dictionary directly
    Returns: None
    """
    # Increase level by 1
    character['level'] += 1
    # Recalculate stats for the new level
    # This function modifies the character dictionary directly using calculate_stats
    strength, magic, health = calculate_stats(character['class'], character['level'])
    character['strength'] = strength
    character['magic'] = magic
    character['health'] = health
    # TODO: Implement this function
    # Remember to recalculate stats for the new level
    

# Main program area (optional - for testing your functions)
if __name__ == "__main__":
    print("=== CHARACTER CREATOR ===")
    print("Test your functions here!")
    
    # Example usage:
    # char = create_character("TestHero", "Warrior")
    # display_character(char)
    # save_character(char, "my_character.txt")
    # loaded = load_character("my_character.txt")
