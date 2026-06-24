with open("alice.txt", "r") as alice_file:

    alice_str = ""
    while True:

        current_line = alice_file.readline()
        if current_line == "":
            break
        alice_str += current_line

    alice_str = alice_str.replace(".", "")
    alice_str = alice_str.replace(",", "")
    alice_str = alice_str.replace("!", "")
    alice_str = alice_str.replace("?", "")
    alice_str = alice_str.replace(";", "")
    alice_str = alice_str.replace(":", "")

    alice_list = alice_str.split()

alice_dict = dict()
for word in alice_list:
    alice_dict[word] = alice_dict.get(word, 0) + 1

alice_sorted_words = sorted(
    alice_dict.items(),
    key=lambda item: item[1],
    reverse=True
)

for tuple_word_count in alice_sorted_words:
    print(f'the word "{tuple_word_count[0]}" appeared {tuple_word_count[1]} times.')
