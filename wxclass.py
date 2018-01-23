import wx

class windowClass(wx.Frame):
	def __init__(self,parent ,title):#constructor Inheritance
		super(windowClass,self).__init__(parent, title = title,size = (800,600)) #super __init__ 
		self.Show()




app=wx.App()
windowClass(None,title="Our Window")

app.MainLoop()