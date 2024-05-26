import os

import kivy
import pandas as pd
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from pyzbar.pyzbar import decode
from PIL import Image as PILImage
from plyer import camera  # Importing camera from plyer module
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import io

# Authenticate and create a PyDrive client
gauth = GoogleAuth()
gauth.LoadClientConfigFile(r"C:\Users\rydel\PycharmProjects\pythonProject\BFJI\client_secret_334044019453"
                           "-0t62eb5jbatiute61kelvhpu1eft2ds9.apps.googleusercontent.com.json")

# Authenticate and create a PyDrive client
gauth.LocalWebserverAuth()  # Creates local webserver and auto handles authentication.
drive = GoogleDrive(gauth)

# Google Drive file ID of the Excel file
file_id = "1RfWR_4gKt1YEaQttETnlkVDwM-HNguKU"

# Create a file instance using the file ID
file_instance = drive.CreateFile({'id': file_id})

# Fetch the content of the Excel file from Google Drive
content_file_path = "temp_excel.xlsx"
file_instance.GetContentFile(content_file_path)

# Read the Excel file into a pandas DataFrame
df = pd.read_excel(content_file_path, sheet_name='Database', header=4)

# Remove the temporary file
os.remove(content_file_path)



def vlookup_flange(fm_id):
    # Perform lookup based on FM ID
    result_flange = df.loc[df['FM ID'] == fm_id, ['Flange Rating', 'Flange Size ', 'Flange Material', 'Flange Standard',
                                                  'Flange Type']]
    # Return the answer to 'result' by the first value found
    return result_flange.iloc[0]


def vlookup_gasket(fm_id):
    result_gasket = df.loc[
        df['FM ID'] == fm_id, ['Gasket Type', 'Gasket Material', 'Gasket Dimensions', 'Alt. Gasket Type',
                               'Alt. Gasket Material']]
    return result_gasket.iloc[0]


def vlookup_bolt(fm_id):
    result_bolt = df.loc[df['FM ID'] == fm_id, ['Bolt Type', 'Bolt Size (Inch)', 'Bolt Length (mm)', 'Bolt Material',
                                                'Bolt Quantity', 'Alt. Stud Bolt Type', 'Alt. Stud Bolt Material',
                                                'Nut Size (mm)']]
    return result_bolt.iloc[0]


class ResultWindow(Popup):
    def __init__(self, flange_info, gasket_info, bolt_info, **kwargs):
        super().__init__(**kwargs)

        # Create labels to display the information
        self.flange_label = Label(text=f"Flange Information:\n"
                                       f"Size: {flange_info.get('Flange Size ', 'NaN')} \n"
                                       f"Rating: {flange_info.get('Flange Rating', 'NaN')} \n"
                                       f"Material: {flange_info.get('Flange Material', 'NaN')} \n"
                                       f"Standard: {flange_info.get('Flange Standard', 'NaN')} \n"
                                       f"Face: {flange_info.get('Flange Type', 'NaN')} \n")

        self.gasket_label = Label(text=f"Gasket Information:\n"
                                       f"Type: {gasket_info.get('Gasket Type', 'NaN')} \n"
                                       f"Material: {gasket_info.get('Gasket Material', 'NaN')} \n"
                                       f"Dimension: {gasket_info.get('Gasket Dimensions', 'NaN')} \n"
                                       f"Alt. Type: {gasket_info.get('Alt. Gasket Type', 'NaN')} \n"
                                       f"Alt. Material: {gasket_info.get('Alt. Gasket Material', 'NaN')} \n")

        self.bolt_label = Label(text=f"Bolt Information:\n"
                                     f"Type: {bolt_info.get('Bolt Type', 'NaN')} \n"
                                     f"Size: {bolt_info.get('Bolt Size (Inch)', 'NaN')} \n"
                                     f"Nut Size: {bolt_info.get('Nut Size (mm)', 'NaN')} \n"
                                     f"Length: {bolt_info.get('Bolt Length (mm)', 'NaN')} \n"
                                     f"Material: {bolt_info.get('Bolt Material', 'NaN')} \n"
                                     f"Quantity: {bolt_info.get('Bolt Quantity', 'NaN')} \n"
                                     f"Alt. Type: {bolt_info.get('Alt. Stud Bolt Type', 'NaN')} \n"
                                     f"Alt. Material: {bolt_info.get('Alt. Stud Bolt Material', 'NaN')} \n")

        # Create an "Exit" button
        self.exit_button = Button(text="Return To Homepage", size_hint=(1, None), height=40)
        self.exit_button.bind(on_press=self.dismiss)  # Close the popup when the button is pressed

        # Add labels and button to the popup content
        self.content = BoxLayout(orientation='vertical')
        self.content.add_widget(self.flange_label)
        self.content.add_widget(self.gasket_label)
        self.content.add_widget(self.bolt_label)
        self.content.add_widget(self.exit_button)


class BFJI(App):
    def build(self):
        self.orientation = "vertical"
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}

        # Add Image Widget
        self.logo = Image(source="LenogB.png")
        self.window.add_widget(self.logo)

        # Add Label for QR Scanner
        self.qrscan = Label(text="Scan QR Code", font_size=18, color='15b08b')
        self.window.add_widget(self.qrscan)

        # Add Button for QR Scan
        self.scanbutton = Button(text="SCAN", size_hint=(1, 0.5), bold=True, background_color='2ba486',
                                 background_normal="")
        self.window.add_widget(self.scanbutton)

        # Add Label for FM ID
        self.fmidlabel = Label(text="Enter FM ID", font_size=18, color='15b08b')
        self.window.add_widget(self.fmidlabel)

        # Add TextInput for User to input FM ID
        self.userinputfmid = TextInput(hint_text="Search for FM ID", multiline=False, font_size=15, size_hint=(1, 0.5),
                                       padding_y=(12, 12))
        self.window.add_widget(self.userinputfmid)

        # Add Button to search FM ID
        self.searchfmidbutton = Button(text="SEARCH", size_hint=(1, 0.5), bold=True, background_color='2ba486',
                                       background_normal="")
        self.window.add_widget(self.searchfmidbutton)

        # Define the search function
        def search_fm_id(instance):
            # Get the FM ID entered by the user
            fm_id = self.userinputfmid.text

            # Look up information based on FM ID
            try:
                flange_info = vlookup_flange(fm_id)
                gasket_info = vlookup_gasket(fm_id)
                bolt_info = vlookup_bolt(fm_id)

                # Create and display the result window
                result_window = ResultWindow(title="Search Result", flange_info=flange_info, gasket_info=gasket_info,
                                             bolt_info=bolt_info)
                result_window.open()

            except IndexError:
                print("FM ID not found in the database")

        # Bind the search function to the button press event
        self.searchfmidbutton.bind(on_press=search_fm_id)

        # Define the function to handle the camera scan
        def scan_qr_code(instance):
            # Define the function to handle the camera scan
            def scan_qr(instance, filename, decoded_objects):
                decoded_objects = decode(PILImage.open(filename))
                if decoded_objects:
                    # Extract the FM ID from the decoded QR code
                    qr_fm_id = decoded_objects[0].data.decode('utf-8')

                    # Set the extracted FM ID to the user input field
                    self.userinputfmid.text = qr_fm_id

                    # Automatically trigger the search when FM ID is extracted from QR code
                    search_fm_id(self.searchfmidbutton)

            # Request camera access permission and open camera
            camera.take_picture(filename="camera_capture.jpg", on_complete=scan_qr)

        # Bind the scan function to the button press event
        self.scanbutton.bind(on_press=scan_qr_code)

        return self.window


# Run the application
if __name__ == "__main__":
    BFJI().run()
