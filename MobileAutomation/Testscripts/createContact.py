from MobileAutomation.Utils import Contacts

obj=Contacts.Contacts()
#obj.swipeUp()
# for i in range(3):
obj.launchContactui()
obj.clickOnPlus()
obj.nameEntryAdb()
obj.clickOnMobile()
obj.phoneNumberEntryAdb()
obj.saveContact()
obj.pressBack2()

# obj.editContact()
# obj.editMoreName()
# obj.editName()
# obj.saveContact()
# obj.pressBack()
# obj.selForMore()
# obj.blockContact()
# obj.pressBack()
# obj.selContacttoUnblock()
# obj.unBlockContact()
# obj.pressBack()
# obj.selForMore()
# obj.deleteContact()
# obj.pressBack()
# obj.pressBack()
# obj.lockScreen()
#
#
# ######################################################
# obj.swipeUp()
# obj.launchContactui()
# time.sleep(2)
# obj.clickOnPlus1()
# obj.nameEntryAdb()
#from uiautomator import Device
#d=Device("55fc7c16")
#
# d(text="Contacts").click()
