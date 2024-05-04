def decode(message_file):
    # initialize the words array
    words = []
    # try to open the file
    try:
        with open(message_file, 'r') as file:  
            # for every line that the file has  
            for line in file:
                # store it in a variable called parts
                parts = line.strip().split()
                # append the parts to tne words array
                words.append(parts)
    # catch io exception
    except IOError:
        print("Can't open the file")
        return ""

    # Sort the words array based on the first element of each sub array (the number)
    sorted_words = sorted(words, key=lambda x: int(x[0]))

    print(sorted_words)
    #  this will be the decoded message that will be returned
    decoded_message = ""
    # index of an array
    index = 0
    # increment amount
    i = 1

    # loop as long as the index is less than the length of the words array
    while index <= len(sorted_words):
        # extract the word from the sub array
        word = sorted_words[index][1]
        # append it in the decoded message
        decoded_message += word + " "  
        # increment the amount
        i += 1
        # increment the index
        # by this logic, index will go from 0,2,5,...
        index += i  

    # return the decoded message
    return decoded_message.strip()




# Example usage:
decoded_message = decode("/Users/dongjoolee/Desktop/abacuus/coding_qual_input.txt")
print(decoded_message)