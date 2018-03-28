from bs4 import BeautifulSoup
import csv as csv

def telegramHTML2CSV (html_input, csv_output):

    # Read local HTML file into a BeautifulSoup object

    # (Note - I had to manually save the HTML into a file since
    # the Telegram web app is password protected. Logging in
    # programmatically and requesting the URL is possible,
    # just beyond the scope of this miniproject.)
    soup = BeautifulSoup(open(html_input), 'html.parser')

    # Find all divs of appropriate class, returns an array
    msg_body_media_raw_messages = soup.findAll('div', {'class': 'im_history_message_wrap'})

    # Open a csv to write output
    with open(csv_output, 'wb') as csvfile:
        spamwriter = csv.writer(csvfile)

        # Loop through array of .im_history_message_wrap divs
        for msg in msg_body_media_raw_messages:

            # Initiate variables for each message

            # This is because not every .im_history_message_wrap div has a message
            msg_text = ''
            name = ''
            time = ''
            msg_flag = False    # This will help us avoid errors

            # Based on the structure of the Telegram HTML, date gets set when it
            # exists and persists through the loop until the next date is encountered,
            # in which case it is updated
            try:
                date = msg.find('span', {'class': 'im_message_date_split_text'}).text
                date_flag = True
               # print date
            except:
                date_flag = False

            # Divs that don't have a date *probably* have a message, including name and time
            if not date_flag:

                # Extract name, message text and time to store in variables
                try:
                    name = msg.find('a', {'class' : 'im_message_author'}).text
                except:
                    name = ''

                try:
                    msg_text = msg.find('div', {'class': 'im_message_text'}).text
                    msg_flag = True
                except:
                    msg_text = ''

                try:
                    time = msg.find('span', {'ng-bind': '::historyMessage.date | time'}).text

                except:
                    time = ''

            # Write messages as rows in the csv we opened
            if msg_flag:
                spamwriter.writerow( [date.encode('ascii', 'ignore'), time.encode('ascii', 'ignore'), name.encode('ascii', 'ignore') , msg_text.encode('ascii', 'ignore')])


# Define input and output files
html_input = './ixo-telegram-raw.html'
csv_output = './ixo-telegram-messages.csv'

telegramHTML2CSV(html_input, csv_output)
