from uiautomator import Device
import time

class uiLibrary():
    def __init__(self):
        self.d=Device("KJRKLNDAYLEYVO8T")
        #self.d = Device("55fc7c16")#off2ndmobile
        pass
    def clickOnText(self,textName):
        self.d(text=textName).click()
    def clickOnPlus(self):
        self.d(resourceId="com.android.dialer:id/menu_add").click()
    def clickOnPlus1(self):
        self.d(resourceId="com.android.contacts:id/floating_action_button").click()#officeph2
        self.d.click(900,1950)#[864,1888][1032,2014]#officeph2
    def clickOnFullName(self,inputName):
        self.d(text=inputName).click()

    def clickOnMobile(self):
     self.d(className="android.widget.EditText",instance=3).click()
     time.sleep(2)
    def saveContact(self):
        self.d.click(950,100)
        time.sleep(2)
    def editContact(self):
        self.d(text="sisi").click()
        time.sleep(2)
    def editContact1(self):
        self.d(text="sisindri").click()
        time.sleep(2)
    #[107,1872][163,1912]
    def editMoreName(self):
        self.d.click(130,1900)
    #[919,63][1038,168]
    # def clickOnMobile(self):
    #     self.d(700,700).click()
    def pressBack2(self):
        for i in range(2):
            self.d.press.back()

    def pressBack(self):
        self.d.press.back()

    #[913, 1798][976, 1861]
    def deleteContact(self):
        self.d(text="sisindri").click()  # select contacts
        time.sleep(2)
        self.d.click(950,1830)
        self.d(text="Remove from Contacts").click()
        time.sleep(2)
        self.d(text="Delete sisindri").click()
        time.sleep(2)
    def seltoBlock(self):
        self.d(text="sisindri").click()
        time.sleep(2)
    def blockContact(self):
        self.d.click(950, 1830)
        self.d(text="Add to blacklist").click()
        time.sleep(2)
        self.d(text="Add to blacklist").click()
        time.sleep(2)
    def selContacttoUnblock(self):
        self.d(text="sisindri").click()  # select contacts
        time.sleep(2)
    def unBlockContact(self):
        self.d.click(950, 1830)
        self.d(text="Unblock").click()
        self.d(text="Unblock").click()
        time.sleep(2)
    def selForMore(self):
        self.d(text="sisindri").click()
        time.sleep(2)

    # def videoStart(self, filename):
    #     global TS1
    #     global rec
    #     TS = str(datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + '.mp4')
    #     TS1 = filename + TS
    #     command = ['adb', 'shell', 'screenrecord', '//sdcard/' + TS1]
    #
    #     rec = subprocess.Popen(command)
    #     print("video recording started")
    #
    # def videoStop(self, d_path):
    #     rec.terminate()
    #     time.sleep(2)
    #     cmd = ['adb', 'pull', 'sdcard/' + TS1, f'{d_path}']
    #     subprocess.run(cmd)
    #     print("video captured")