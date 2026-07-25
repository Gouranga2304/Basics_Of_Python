name = input("Enter a name: ")
adjective = input("Enter an adjective: ")
noun = input("Enter a noun: ")
verb = input("Enter a verb (past tense): ")
place = input("Enter a place: ")

story = f"""
Once upon a time, {name} went to {place}.
It was a {adjective} day, and {name} decided to {verb} a {noun}.
Everyone who saw it thought it was the most {adjective} thing ever!
"""

print(story)