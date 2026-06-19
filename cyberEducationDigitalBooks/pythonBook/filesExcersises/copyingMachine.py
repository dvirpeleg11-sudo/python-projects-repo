with open("dear_prudence.txt", "r") as dear_prudence_file:
    dear_prudence_text = ""
    while True:
        text_to_add = dear_prudence_file.readline()
        if text_to_add is None:
            break
        dear_prudence_text += text_to_add

    with open("almostEmpty.txt", "a") as almost_empty_file:
        almost_empty_file.write(dear_prudence_text)

print("the end")
