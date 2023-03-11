from kivy.app import App
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import StringProperty, BooleanProperty, ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
import qrcode

class MainWindow(Screen):
    pass

class FormWindow(Screen):

    fullName = "-"
    personalNumber = "-"
    emergencyNumber = "-"
    emailAddress = "-"
    gender = "-"
    homeAddress = "-"
    medSymptoms = "-"
    medication = "-"
    allergies = "-"
    medDiagnosis = "-"
    pastConditions = "-"
    tobacco = "-"
    alcohol = "-"

    # count = 0
    # pathold = StringProperty("")
    # pathnew = StringProperty("")


    def on_text_validate_fullName(self, widget):
        self.fullName = widget.text

    def on_text_validate_personalNumber(self, widget):
        self.personalNumber = widget.text

    def on_text_validate_emergencyNumber(self, widget):
        self.emergencyNumber = widget.text

    def on_text_validate_emailAddress(self, widget):
        self.emailAddress = widget.text

    def on_text_validate_gender(self, widget):
        self.gender = widget.text

    def on_text_validate_homeAddress(self, widget):
        self.homeAddress = widget.text

    def on_text_validate_medSymptoms(self, widget):
        self.medSymptoms = widget.text

    def on_text_validate_medication(self, widget):
        self.medication = widget.text

    def on_text_validate_allergies(self, widget):
        self.allergies = widget.text

    def on_text_validate_medDiagnosis(self, widget):
        self.medDiagnosis = widget.text

    def on_text_validate_pastConditions(self, widget):
        self.pastConditions = widget.text        

    def on_text_validate_tobacco(self, widget):
        self.tobacco = widget.text

    def on_text_validate_alcohol(self, widget):
        self.alcohol = widget.text


    def on_button_release_qrGenerate(self):

        self.data = ""
        self.data += ("Full Name: "+ self.fullName + "  ")
        self.data += ("Personal Number: " + self.personalNumber + "  ")
        self.data += ("Emergency Number: " + self.emergencyNumber + "  ")
        self.data += ("Email Address: " + self.emailAddress + "  ")
        self.data += ("Gender: " + self.gender + "  ")
        self.data += ("Home Address: " + self.homeAddress + "  ")
        self.data += ("Medical Symptoms: " + self.medSymptoms + "  ")
        self.data += ("Medication: " + self.medication+ "  ")
        self.data += ("Allergies: " + self.allergies + "  ")
        self.data += ("Medical Diagnosis: " + self.medDiagnosis + "  ")
        self.data += ("Past Health Conditions: " + self.pastConditions + "  ")
        self.data += ("Tobacco consumption: " + self.tobacco + "  ")
        self.data += ("Alcohol consumption: " + self.alcohol + "  ")
        print(self.data)

        features = qrcode.QRCode(version=1, box_size=40, border=3)
        features.add_data(self.data)
        features.make(fit=True)
        generate_image = features.make_image(fill_color="green", back_color="black")

        generate_image.save("images/qr.png")



class ScanWindow(Screen):
    pass

class DevWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass


class MainApp(App):
        Window.clearcolor = (153/255, 242/255, 218/255, 1)


if __name__ == '__main__':
    MainApp().run()
