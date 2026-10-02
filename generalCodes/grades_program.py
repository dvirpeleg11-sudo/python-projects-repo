# main function
def main():
    # have a dictionary of names and dapar grades with megama in a tuple
    dapar_and_megama_dict = {"dvir": (80, "CS"), "noam": (70, "physics"), "sagi": (90, "CS"), "daniel": (60, "chemistry")}
    # pass the keys (names) list to a filter which will want more than 60 and are in megama "CS"
    will_get_miyoonim_of_gamma = list(filter(will_get_miyoonim_of_gamma_func, dapar_and_megama_dict.values()))
    # printing the names of the poeple who gets the miyoonim_of_gamma
    print("the ones that are going to get miyoonim for gamma are: ")
    for key, value in dapar_and_megama_dict.items():
        # if the current value is equal to one of the tuples from wlil get minomum filtered list
        for get_miyoonim_tuple in will_get_miyoonim_of_gamma:
            if value == get_miyoonim_tuple:
                print(key)
                will_get_miyoonim_of_gamma.remove(get_miyoonim_tuple)

# is gamma method
def will_get_miyoonim_of_gamma_func(a_tuple):
    # check if the tuple[0] is bigger than 60 and the megama is "CS"
    if a_tuple[0] > 60 and a_tuple[1] == "CS":
        # return true
        return True
    # if it isnt, return false
    return False

if __name__ == "__main__":
    main()