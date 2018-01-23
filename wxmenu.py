import wx

class windowClass(wx.Frame):
	def __init__(self,*args ,**kwargs):#constructor
		super(windowClass,self).__init__(*args,**kwargs) #super __init__
		self.OurGui()

	def OurGui(self):
		menuBar=wx.MenuBar()
		fileButton=wx.Menu()
		editButton=wx.Menu()
		exitItem = fileButton.Append(wx.ID_EXIT,"Exit","Our status message")
		editItem = editButton.Append(wx.ID_FIND,"Find","Our status message")
		menuBar.Append(fileButton,'File')
		menuBar.Append(editButton,'Edit')
		self.SetMenuBar(menuBar)
		self.Bind(wx.EVT_MENU,self.Quit,exitItem)

		self.SetTitle("new window")
		self.Show()


	def Quit(self,e):
		self.Close()





def main():
	app=wx.App()
	windowClass(None)
	app.MainLoop()


main()	