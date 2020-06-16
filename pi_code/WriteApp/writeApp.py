import threading

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup

Builder.load_file('bios.kv')
Builder.load_file('status.kv')

class Bios(GridLayout):
    reg = ObjectProperty(None)
    serial_no = ObjectProperty(None)
    phone_no = ObjectProperty(None)
    cardData = ObjectProperty(None)
    keyData = ObjectProperty(None)

class Status(BoxLayout):
    Card = ObjectProperty(None)
    Key  = ObjectProperty(None)

class Writer(BoxLayout):
    def __init__(self,**kwargs):
        super(Writer,self).__init__(**kwargs)
    def collectData(self):
        data_list = []
        reg = self.ids.bios.reg.text
        serial_no = self.ids.bios.serial_no.text
        phone_no = self.ids.bios.phone_no.text
        cardData = self.ids.bios.cardData.text
        keyData = self.ids.bios.keyData.text
        data_list.extend([reg, serial_no, phone_no, cardData, keyData])
        if self.checkList(data_list):
            popup = Popup(title = "Warning" , size_hint=(None, None), size=(160,160),
                          content=Label(markup=True,text="[color=ff0000][b]Field(s) empty[/b][/color]"),
                          auto_dismiss=True)
            popup.open()
        print(data_list)
        #clear window content
        self.clearWindowData()
    def checkList(self, myList):
        global flag
        flag = False
        for item in myList:
            if not item:
                flag = True

        return flag
    def clearWindowData(self):
        self.ids.bios.reg.text = ''
        self.ids.bios.serial_no.text = ''
        self.ids.bios.phone_no.text = ''
        self.ids.bios.cardData.text = ''
        self.ids.bios.keyData.text = ''

    def validate_item(self, item, lock):
        #universal check
        lock.acquire()
        print(item)
        lock.release()
    def validate_reg(self):
        lock = threading.Lock()
        threading.Thread(target=self.validate_item, args=('reg',lock)).start()
class writeApp(App):
    def build(self):
        return Writer()

if __name__ == "__main__":
    writeApp().run()
