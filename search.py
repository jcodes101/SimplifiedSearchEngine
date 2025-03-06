from wiki import article_titles, ask_search, ask_advanced_search
'''
Jadin
'''
# 1) 
#
# Function: search
#
# Parameters:
#   keyword - search word to look for in article titles
#
# Returns: list of article titles containing given keyword (case insensitive).
# If the keyword is empty or no results are found, return an empty list.
#
# Hint: to get list of existing article titles, use article_titles()
'''
- the variable titles is assigned the list of articles "article_titles",
- if the keyword is equal to an empty string an empty list is returned,
- the for loop iterates over the list and checks if the keyword is in the list of articles 
(both set to case insensitive) and if so that article is appended to the empty list and returned
'''
def search(keyword):
    titles = article_titles()
    search_results = []

    if keyword == '':
        return search_results
        
    for title in titles:
        if keyword.lower() in title.lower():
            search_results.append(title)
    return search_results

# 2) 
#
# Function: title_length
#
# Returns 
#
# Parameters:
#   max_length - max character length of article titles
#   titles - list of article titles to search through
#
# Returns: list of article titles from given titles with a length that does
# not exceed max_length number of characters
'''
- max_tl is set as an empty list and then the for loop iterates over the list of articles
and if the length of the list of articles is less than or equal to the max char length of the titles
titles that don't go over the max length are appended to the empty list and returned
'''
def title_length(max_length, titles):
    max_tl = []
    for title in titles:
        if len(title) <= max_length:
            max_tl.append(title)
    return max_tl


    

# 3) 
#
# Function: article_count
#
# Parameters:
#   count - max number of returned articles
#   titles - list of article titles to search through
#
# Returns: list of articles in given titles starting from the 
# beginning that do not exceed given count in total. If there are no 
# given article titles, return an empty list regardless of the count.
# If the max is larger than the # of titles, just return all titles.
'''
- "returned" is set to an empty list and if the list is equal to an empty string
it returns "returned"
- although if the the count is greater than the length of list "titles"
it returns the entire list of articles
- lastly, the for loop uses 'cnt' and iterates through up to the range of count
and appends each title in the lists that was iterated through and is returned
'''
def article_count(count, titles):
    returned = []
    if titles == '':
        return returned
    elif count > len(titles):
        return titles
    else:
        for cnt in range(count):
            returned.append(titles[cnt])
        return returned


# 4) 
#
# Function: random_article
#
# Parameters:
#   index - index at which article title to return
#   titles - list of article titles to search through
#
# Returns: article title in given titles at given index. If
# index is not valid, return an empty string
'''
- the variable indexes is set to an empty string
- if the index is greater than or equal to 0 and less than the length of the 
list of titles, the given index in the titles list is returned, although if not
the variable "indexes" is returned
'''
def random_article(index, titles):
    indexes = ''
    if 0 <= index < len(titles):
        return titles[index]
    else:
        return indexes


    
# 5) 
#
# Function: favorite_article
#
# Parameters:
#   favorite - favorite article title
#   titles - list of article titles to search through
#
# Returns: True if favorite article is in the given articles
# (case insensitive) and False otherwise
'''
- the for loop iterates through the list "titles" and if the favorite article
is equal to the title/article that was iterated over, True is returned if not,
then False is returned
'''
def favorite_article(favorite, titles):
    for title in titles:
        if favorite.lower() == title.lower():
            return True
    return False
        

# 6) 
#
# Function: multiple_keywords
#
# Parameters:
#   keyword - additional keyword to search
#   titles - article titles from basic search
#
# Returns: searches for article titles from entire list of available
# articles and adds those articles to list of article titles from basic 
# search
'''
the function firstly calls the search function and returns the articles list 
and that is assigned to the variable "x" and then the variable 
"combined_lists" is assigned the list titles plus search(keyword) 
and then combined_lists is returned
'''
def multiple_keywords(keyword, titles):
    x = search(keyword)

    combined_lists = titles + x
    return combined_lists


# Prints out articles based on searched keyword and advanced options
def display_result():
    # Stores list of articles returned from searching user's keyword
    articles = search(ask_search())

    # advanced stores user's chosen advanced option (1-5)
    # value stores user's response in being asked the advanced option
    advanced, value = ask_advanced_search()

    if advanced == 1:
        # value stores max article title length in number of characters
        # Update article titles to contain only ones of the maximum length
        articles = title_length(value, articles)
    if advanced == 2:
        # value stores max number of articles
        # Update article titles to contain only the max number of articles
        articles = article_count(value, articles)
    elif advanced == 3:
        # value stores random number
        # Update articles to only contain the article title at index of the random number
        articles = random_article(value, articles)
    elif advanced == 4:
        # value stores article title
        # Store whether article title is in the search results into a variable named has_favorite
        has_favorite = favorite_article(value, articles)
    elif advanced == 5:
        # value stores keyword to search
        # Updated article titles to contain article titles from the first search and the second search
        articles = multiple_keywords(value, articles)

    print()

    if not articles:
        print("No articles found")
    else:
        print("Here are your articles: " + str(articles))

    if advanced == 4:
        print("Your favorite article is" + ("" if has_favorite else " not") + " in the returned articles!")

if __name__ == "__main__":
    display_result()
