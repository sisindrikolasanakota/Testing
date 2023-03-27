from MobileAutomation.Utils import Contacts


obj=Contacts.Contacts()

obj.launchContactui()
obj.selForMore()
obj.deleteContact()
obj.pressBack2()
obj.lockScreen()