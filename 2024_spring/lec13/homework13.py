import bs4, gtts

def extract_stories_from_NPR_text(text):
    '''
    Extract a list of stories from the text of the npr.com webpage.
    
    @params: 
    text (string): the text of a webpage
    
    @returns:
    stories (list of tuples of strings): a list of the news stories in the web page.
      Each story should be a tuple of (title, teaser), where the title and teaser are
      both strings.  If the story has no teaser, its teaser should be an empty string.
    '''
    from bs4 import BeautifulSoup

    soup = BeautifulSoup(text, 'html.parser')
    stories = []

    # Find the elements that contain the stories.
    for item in soup.find_all('article'):
        title_element = item.find('h3', class_='title')  
        teaser_element = item.find('p')  

        if title_element:
            title = title_element.get_text(strip=True)
        else:
            title = "No Title"

        if teaser_element:
            teaser = teaser_element.get_text(strip=True)
        else:
            teaser = ""

        stories.append((title, teaser))
    
    return stories

def read_nth_story(stories, n, filename):
    '''
    Read the n'th story from a list of stories.
    
    @params:
    stories (list of tuples of strings): a list of the news stories from a web page
    n (int): the index of the story you want me to read
    filename (str): filename in which to store the synthesized audio

    Output: None
    '''
    from gtts import gTTS

    if n < 0 or n >= len(stories):
        raise IndexError('Index out of range.')

    title, teaser = stories[n]
    text_to_read = f"Title: {title}. Teaser: {teaser}"

    tts = gTTS(text=text_to_read, lang='en')
    tts.save(filename)
