import data_treatment


def selector():
    print("What do you want to visualize?")
    data = input("[f]astest rowers, [s]lowest rowers, [h]eaviest, [l]ightest, [o]ldest, [y]oungest ")

    match data:
        case 'f':
            return data_treatment.fastest
        case 's':
            return data_treatment.slowest
        case 'h':
            return data_treatment.heaviest
        case 'l':
            return data_treatment.lightest
        case 'o':
            return data_treatment.oldest
        case 'y':
            return data_treatment.youngest
