import wx

class windowClass(wx.Frame):
	def __init__(self,*args ,**kwargs):#constructor
		super(windowClass,self).__init__(*args,**kwargs) #super __init__
		self.OurGui()

	def OurGui(self):
	
		nameBox = wx.TextEntryDialog(None,"What is your age???")
		if nameBox.ShowModal() == wx.ID_OK:
			userAge = nameBox.GetValue()
			if int(userAge) <= 17:
				wx.MessageBox("You cannot access this")
			else:
				wx.MessageBox("Permission Granted")



	



def main():
	app=wx.App()
	windowClass(None)
	app.MainLoop()


main()	