#Profanity Checker
#Jameka Echols
import urllib.request

def read_text():
    quotes = open("/Users/jamekaechols/Downloads/movie_quotes.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)
    
def check_profanity(text_to_check):
    #open the url...update to 3.6.2
    connection = urllib.request.urlopen("http://www.wdylike.appspot.com/?q=QUERY" + urllib.parse.quote(text_to_check))
    output = connection.read()
    print(output)
    connection.close()

    if b'true' in output:
        print("There is a cuss word...ooooooooooo")
    elif b'false' in output:
        print("Squeaky clean language here, mate!")
    else:
        print("There maybe something wrong here.")
                               
    

read_text()
