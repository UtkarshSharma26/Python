import wx

class windowClass(wx.Frame):
	def __init__(self,*args ,**kwargs):#constructor
		super(windowClass,self).__init__(*args,**kwargs) #super __init__
		self.OurGui()

	def OurGui(self):
		panel=wx.Panel(self)
		menuBar=wx.MenuBar()
		fileButton=wx.Menu()
		#editButton=wx.Menu()
		exitItem = fileButton.Append(wx.ID_EXIT,"Exit","Our status message")
		#editItem = editButton.Append(wx.ID_FIND,"Find","Our status message")
		
		menuBar.Append(fileButton,'File')
		#menuBar.Append(editButton,'Edit')
		self.SetMenuBar(menuBar)
		self.Bind(wx.EVT_MENU,self.Quit,exitItem)

		nameBox = wx.TextEntryDialog(None,"What is your name???",'welcome' ,'Pranjali')
		if nameBox.ShowModal() == wx.ID_OK:
			userName = nameBox.GetValue()

		yesNoBox = wx.MessageDialog(None,"Do You Really like to code???",'Question',wx.YES_NO)
		yesNOAnswer=yesNoBox.ShowModal() #gives an output or return
		yesNoBox.Destroy()

		wx.TextCtrl(panel,pos=(10,10),size=(250,150))

		if yesNOAnswer == wx.ID_NO:
			userName = "Loser!!"

		chooseOneBox = wx.SingleChoiceDialog(None,"What is ur fvrt color ","Color Question ",['Green','Red','Blue'])
		if chooseOneBox.ShowModal() == wx.ID_OK:
			favColor=chooseOneBox.GetStringSelection()
		#chooseOneBox.Destroy()


		self.SetTitle("Welcome"+userName)
		self.Show(True)


	def Quit(self,e):
		self.Close()





def main():
	app=wx.App()
	windowClass(None)
	app.MainLoop()


main()	