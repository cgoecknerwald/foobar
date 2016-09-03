def answer(document, searchTerms): 
    # split document into a list of strings for ease of parsing
    document = document.split()
    # snippet is a list of strings that is a candidate for the answer
    snippet = document
    # snippet list contains all snippets that are valid
    snippet_list = []
    # stop adding to snippet_list when the remainder of the document no longer
    # contains all keywords
    while (containsAllKeywords(document, searchTerms)):
        # prune the document from the head, forgetting all unnecessary words
        while not document[0] in searchTerms:
            document = document[1:]
        snippet = document
        # prune the snippet from the back, forgetting all unnecessary words
        while containsAllKeywords(snippet[:-1], searchTerms):
            snippet = snippet[:-1]
        snippet_list.append(snippet)
        # advance the pruning of the document
        document = document[1:]

    # return the shortest shippet contained in snippet_list
    return ' '.join(min(snippet_list, key=len))

# assume snippet is a list of strings
def containsAllKeywords(doc, searchTerms):
    return set(searchTerms) <= set(doc)

print(answer("1"*500, ["1"]))