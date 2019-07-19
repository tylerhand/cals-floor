main_massage='''Welcome to the setup utility!\n\n
If you exit this tool, your work will not be saved. You can use this to edit your configuration file. You
can also edit this by editing the config.py file Here are some quick options...

[1] Add/Delete the site notification banner
[2] Add/delete a link in the navigation bar
[3] Change a password
[4] Add/delete a list moderator
[5] Full setup
'''

def option_single(option_list):
    from config import config
    config_temp = config
    print('You have selected to change the following settings. Type q at any time to quit.\n')

def option5():
    print('You have chosen to complete the full setup')
    config_temp = {}

while True:
    print(main_message)