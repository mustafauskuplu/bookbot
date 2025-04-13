def get_content(filepath):
    with open(filepath) as book:
        return book.read()

def calculate_word_count(content):
    words = content.split()
    return len(words)

def generate_character_count_list(content):
    character_counts = {}
    
    for character in content.lower():
        if character in character_counts:
            character_counts[character] += 1
        else:
            character_counts[character] = 1

    character_count_list = []

    for character in character_counts:
        character_count_dict = {}
        character_count_dict["character"] = character
        character_count_dict["count"] = character_counts[character]

        character_count_list.append(character_count_dict)

    def sort_on(dict):
        return dict["count"]

    character_count_list.sort(reverse=True, key=sort_on)

    return character_count_list

def generate_report(filepath):
    content = get_content(filepath)
    word_count = calculate_word_count(content)
    character_count_list = generate_character_count_list(content)

    report = "============ BOOKBOT ============\n"
    report += f"Analyzing book found at {filepath}...\n"
    report += "----------- Word Count ----------\n"
    report += f"Found {word_count} total words\n"
    report += "--------- Character Count -------\n"

    for character_count_info in character_count_list:
        character = character_count_info["character"]

        if character.isalpha() == False:
            continue

        count = character_count_info["count"]
        report += f"{character}: {count}\n"
        
    report += "============= END ==============="

    return report

    