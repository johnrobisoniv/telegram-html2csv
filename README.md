# Telegram Parser

In trying to review message conversations of groups I'm added to, I've been finding that I want to get the message history into a format that I can manipulate with code.

There is a huge amount of potential here - generating user lists, measuring user engagement (number and frequency of messages), sentiment analysis on messages, easily pulling all links shared to a group into a list, etc.

First step, though, is transforming the message thread from the raw output, either downloaded txt files (as Whatsapp provides) or, in this case, parsing through HTML downloaded from the Telegram web app.

This script and iPython notebook extracts relevant information - date, time, user and message - and writes a csv file with a line for each message using the python library [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/).

This *should* work with any HTML downloaded from the Telegram web application, at least in its current form (as of late March 2018).
