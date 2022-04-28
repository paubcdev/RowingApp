import data_treatment


def selector():
    print("What do you want to visualize?")
    data = input("[f]astest rowers, [s]lowest rowers, [h]eaviest, [l]ightest, [o]ldest, [y]oungest ")

    match data:
        case 'f' | 'F' | 'fastest':
            return data_treatment.fastest
        case 's' | 'S' | 'slowest':
            return data_treatment.slowest
        case 'h' | 'H' | 'heaviest':
            return data_treatment.heaviest
        case 'l' | 'L' | 'lightest':
            return data_treatment.lightest
        case 'o' | 'O' | 'oldest':
            return data_treatment.oldest
        case 'y' | 'Y' | 'youngest':
            return data_treatment.youngest
