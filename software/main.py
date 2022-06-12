import PySimpleGUI as sg
# import requests
from sms_api import send_sms
from utils import verify
import configparser


config = configparser.ConfigParser()
config.read('config.cfg')

SENDER = os.environ.get('SENDER')

layout = [[sg.Text('Enter contacts for messages: ')],
          [sg.Multiline(size=(40, 10), key='contacts')],
          [sg.Text('Enter message: ')],
          [sg.Multiline(size=(40, 10), key='message')],
          [sg.Button('SEND')]]

window = sg.Window('Window Title', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break

    if event == 'SEND':
        contacts = verify(values["contacts"])
        # two counters for messages sent and errors
        sent = 0
        errors = 0
        for number in contacts:
            response = send_sms(SENDER, number, values["message"])

            if not response['submitted']:
                errors += 1
                sg.popup_annoying(f'Greska, broj: {number}, detalji greske: {response}')
            else:
                sent +=1

        if errors:
            sg.popup_ok(f'SMS su poslati na {sent} brojeva i {errors} gresaka.')
            sg.popup_notify(f'SMS su poslati na {sent} brojeva i {errors} gresaka.')            
        else:
            sg.popup_ok(f'SMS su poslati na {sent} brojeva bez gresaka.')
            sg.popup_notify(f'SMS su poslati na {sent} brojeva bez gresaka.')


    window.close()
#
