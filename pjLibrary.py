import string

# Create a alphabet list
alphabet = list(string.ascii_lowercase)

# Resolve ties by giving single-letter precedence over letter groups
  then alphabetically
# Pass in two strings needs to be compared
def resolveTie(stringA, stringB):
    # Check which string is shorter, return two strings as tuple so the shorter
    # string is the first element in the tuple
    if len(stringA) < len(stringB):
        return (stringA, stringB)
    elif len(stringB) < len(stringA):
        return (stringB, stringA)
    else:
    #resolve ties by multiple letter groups
        # return 1 for test
        return 1
