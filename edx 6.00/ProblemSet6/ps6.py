# 6.00x Problem Set 6
# RSS Feed Filter

import feedparser
import string
import time
from project_util import translate_html
from Tkinter import *


#-----------------------------------------------------------------------
#
# Problem Set 6

#======================
# Code for retrieving and parsing RSS feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        summary = translate_html(entry.summary)
        try:
            subject = translate_html(entry.tags[0]['term'])
        except AttributeError:
            subject = ""
        newsStory = NewsStory(guid, title, subject, summary, link)
        ret.append(newsStory)
    return ret
#======================

#======================
# Part 1
# Data structure design
#======================

# Problem 1

class NewsStory(object):
    def __init__(self, guid, title, subject, summary, link):
        self.guid = guid
        self.title = title
        self.subject = subject
        self.summary = summary
        self.link = link
        
    def getGuid(self):
        return self.guid
        
    def getTitle(self):
        return self.title
        
    def getSubject(self):
        return self.subject
        
    def getSummary(self):
        return self.summary
        
    def getLink(self):
        return self.link


#======================
# Part 2
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        raise NotImplementedError

# Whole Word Triggers
# Problems 2-5

class WordTrigger(Trigger):
    def __init__(self, word):
        word = word.lower()
        self.word = word
    
    def isWordIn(self, story):
        """
        Returns True if a word is in a given news item, or False otherwise.
        Assumes story is a string. Returns word in story.
        """
        wordList = []
        story = story.lower()
        import string
        for e in string.punctuation:
            if e in story:
                story = story.replace(e, ' ')
        wordList = story.split(' ')

        if self.word in wordList:
            if wordList[wordList.index(self.word)] == self.word:
                return True
        return False

                    

# TODO: TitleTrigger

class TitleTrigger(WordTrigger):
    """
    returns True if word in the title
    """
    def evaluate(self, story):
        if self.isWordIn(story.getTitle()):
            return True
        else:
            return False


# TODO: SubjectTrigger
class SubjectTrigger(WordTrigger):
    """
    returns True if word in subject
    """
    def evaluate(self, story):
        if self.isWordIn(story.getSubject()):
            return True
        else:
            return False
    


# TODO: SummaryTrigger
class SummaryTrigger(WordTrigger):
    """
        returns True if word in summary
        """
    def evaluate(self, story):
        if self.isWordIn(story.getSummary()):
            return True
        else:
            return False

# Composite Triggers
# Problems 6-8

# TODO: NotTrigger
class NotTrigger(Trigger):
    """
    takes story (x) and trigger (T) returns a bool
    equivalent to not T.evaluate(x)
    """
    def __init__(self, t):
        self.trigger = t
    
    def evaluate(self, story):
        res = self.trigger.evaluate(story)
        if res == True:
            return False
        if res == False:
            return True


# TODO: AndTrigger
class AndTrigger(Trigger):
    """
    This trigger should take two triggers as arguments to its constructor, and should fire on a news story only if both of the inputted triggers would fire on that item.
    """
    def __init__(self, t1, t2):
        self.trig1 = t1
        self.trig2 = t2

    def evaluate(self, story):
        return self.trig1.evaluate(story) and self.trig2.evaluate(story)


# TODO: OrTrigger

class OrTrigger(Trigger):
    """
    This trigger should take two triggers as arguments to its constructor, and should fire if either one (or both) of its inputted triggers would fire on that item.
    """
    def __init__(self, T1, T2):
        self.trig1 = T1
        self.trig2 = T2
    def evaluate(self, story):
        return self.trig1.evaluate(story) or self.trig2.evaluate(story)
 


# Phrase Trigger
# Question 9

# TODO: PhraseTrigger
class PhraseTrigger(Trigger):
    """
     fires when a given phrase is in any of the story's subject, title, or summary. The phrase should be an argument to the class's constructor
    """

    def __init__(self, phrase):
        self.phrase = phrase
    def evaluate(self, story):
        if self.phrase in story.getTitle():
            return True
        if self.phrase in story.getSubject():
            return True
        if self.phrase in story.getSummary():
            return True
        return False



#======================
# Part 3
# Filtering
#======================

def filterStories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    # TODO: Problem 10
    triggerStories = []
    for i in stories:
        for e in triggerlist:
            if e.evaluate(i) == True:
                triggerStories.append(i)
                break
    return triggerStories

#======================
# Part 4
# User-Specified Triggers
#======================

def makeTrigger(triggerMap, triggerType, params, name):
    """
    Takes in a map of names to trigger instance, the type of trigger to make,
    and the list of parameters to the constructor, and adds a new trigger
    to the trigger map dictionary.

    triggerMap: dictionary with names as keys (strings) and triggers as values
    triggerType: string indicating the type of trigger to make (ex: "TITLE")
    params: list of strings with the inputs to the trigger constructor (ex: ["world"])
    name: a string representing the name of the new trigger (ex: "t1")

    Modifies triggerMap, adding a new key-value pair for this trigger.

    Returns a new instance of a trigger (ex: TitleTrigger, AndTrigger).
    """
    # TODO: Problem 11
    #initially fogot to define 'trigger' -- but that probably didn't matter
    trigger = None
    #originally did not have to correct mappings for params and modified triggerMap with each if statement, modified to accept correct params now, need to spend more time reading code to understand how params are formatted (list format is important)
    #returned a $%@$%$# error -- need to make sure to call invidual items off of the list
    if triggerType == "TITLE":
        trigger = TitleTrigger(params[0])
    elif triggerType == "SUBJECT":
        trigger = SubjectTrigger(params[0])
    elif triggerType == "SUMMARY":
        trigger = SummaryTrigger(params[0])
    #special case -- needs to contcantrate params to make a phrase
    elif triggerType == "PHRASE":
        trigger = PhraseTrigger(" ".join(params))
    #the below triggers take other triggers as arguments, so they necessarily require that the params be already in the triggerMap!!!
    elif triggerType == "NOT":
        trigger = NotTrigger(triggerMap[params[0]])
    elif triggerType == "AND":
        trigger = AndTrigger(triggerMap[params[0]], triggerMap[params[1]])
    elif triggerType == "OR":
        trigger = OrTrigger(triggerMap[params[0]], triggerMap[params[1]])
    #single assignment step makes for cleaner and more maintainable code
    triggerMap[name] = trigger
    #forgot to return trigger
    return trigger

def readTriggerConfig(filename):
    """
    Returns a list of trigger objects
    that correspond to the rules set
    in the file filename
    """

    # Here's some code that we give you
    # to read in the file and eliminate
    # blank lines and comments
    triggerfile = open(filename, "r")
    all = [ line.rstrip() for line in triggerfile.readlines() ]
    lines = []
    for line in all:
        if len(line) == 0 or line[0] == '#':
            continue
        lines.append(line)

    triggers = []
    triggerMap = {}

    # Be sure you understand this code - we've written it for you,
    # but it's code you should be able to write yourself
    for line in lines:

        linesplit = line.split(" ")

        # Making a new trigger
        if linesplit[0] != "ADD":
            trigger = makeTrigger(triggerMap, linesplit[1],
                                  linesplit[2:], linesplit[0])

        # Add the triggers to the list
        else:
            for name in linesplit[1:]:
                triggers.append(triggerMap[name])

    return triggers
    
import thread

SLEEPTIME = 60 #seconds -- how often we poll


def main_thread(master):
    # A sample trigger list - you'll replace
    # this with something more configurable in Problem 11
    try:
        # These will probably generate a few hits...
        t1 = TitleTrigger("Obama")
        t2 = SubjectTrigger("Romney")
        t3 = PhraseTrigger("Election")
        t4 = OrTrigger(t2, t3)
        triggerlist = [t1, t4]
        
        # TODO: Problem 11
        # After implementing makeTrigger, uncomment the line below:
        triggerlist = readTriggerConfig("triggers.txt")

        # **** from here down is about drawing ****
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT,fill=Y)
        
        t = "Google & Yahoo Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica",14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)

        # Gather stories
        guidShown = []
        def get_cont(newstory):
            if newstory.getGuid() not in guidShown:
                cont.insert(END, newstory.getTitle()+"\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.getSummary())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.getGuid())

        while True:

            print "Polling . . .",
            # Get stories from Google's Top Stories RSS news feed
            stories = process("http://news.google.com/?output=rss")

            # Get stories from Yahoo's Top Stories RSS news feed
            stories.extend(process("http://rss.news.yahoo.com/rss/topstories"))

            # Process the stories
            stories = filterStories(stories, triggerlist)

            map(get_cont, stories)
            scrollbar.config(command=cont.yview)


            print "Sleeping..."
            time.sleep(SLEEPTIME)

    except Exception as e:
        print e


if __name__ == '__main__':

    root = Tk()
    root.title("Some RSS parser")
    thread.start_new_thread(main_thread, (root,))
    root.mainloop()

