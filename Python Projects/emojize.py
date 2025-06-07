# import emoji
# user = input("Input:")
# print("Output: ",emoji.emojize(user))

import emoji

# Prompt user for input
# text = input("Input: ")
text = input()


# Convert emoji alias to actual emoji
emojized_text = emoji.emojize(text)

# Print result
print(f"Output: {emojized_text}")
