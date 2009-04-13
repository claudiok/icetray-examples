#!/usr/bin/env python

# capitals.py
 
import wx
import tables
from I3Hist import i3hist
from I3HistEnum import I3HistEnum
import pylab,numpy
import sys

class BrowserFrame(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, wx.DefaultPosition, wx.Size(640, 480))
        
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        vbox1 = wx.BoxSizer(wx.VERTICAL)
        vbox2 = wx.BoxSizer(wx.VERTICAL)
        panel1 = wx.Panel(self, -1)
        panel2 = wx.Panel(self, -1)
  
        self.tree = wx.TreeCtrl(panel1, 1, wx.DefaultPosition, (-1,-1), wx.TR_HIDE_ROOT|wx.TR_HAS_BUTTONS)

        self.tree.Bind(wx.EVT_TREE_SEL_CHANGED, self.OnSelChanged, id=1)
        self.lc = wx.ListCtrl(panel2, -1, style=wx.LC_REPORT)
        self.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.OnDoubleClick,self.lc)
        self.lc.InsertColumn(0,"Columns")
        vbox1.Add(self.tree, 1, wx.EXPAND)
        vbox2.Add(self.lc,   1, wx.EXPAND)
        hbox.Add(panel1, 1, wx.EXPAND)
        hbox.Add(panel2, 1, wx.EXPAND)
        panel1.SetSizer(vbox1)
        panel2.SetSizer(vbox2)
        self.SetSizer(hbox)
        self.Centre()

    def TraverseTree(self, obj, tree):
        for attr in dir(obj):
            if attr[0]=="_":
                continue
            a=getattr(obj,attr)
            if type(a)==tables.table.Table:
                self.TraverseTree(a.cols,self.tree.AppendItem(tree,attr))
            elif type(a)==tables.table.Cols:
                self.TraverseTree(a,self.tree.AppendItem(tree,attr))
                
    def ReadFile(self,filename):
        self.hdf5file=tables.openFile(sys.argv[1])
        self.root = self.tree.AddRoot(filename)        
        self.TraverseTree(self.hdf5file.root,self.root)       
        
    def OnSelChanged(self, event):
        item =  event.GetItem()

        tree_location=[]
        while not item==self.root:
            tree_location.append(self.tree.GetItemText(item))
            item=self.tree.GetItemParent(item)
        
        self.lc.DeleteAllItems()

        tree_location.reverse()   
        self.col=getattr(self.hdf5file.root,tree_location[0]).cols
        for s in tree_location[1:]:
            self.col=getattr(self.col,s)
            
        for attr in dir(self.col):
            column=getattr(self.col,attr)
            if type(column)==tables.table.Column:
                self.lc.InsertStringItem(0, attr)

    def OnDoubleClick(self, event):
        pylab.clf()
        col=getattr(self.col,event.Label)
        pylab.title(col.pathname)
        if col.type=='enum':
            I3HistEnum(col[:],col.table.getEnum(col.pathname)._values).draw(rotation=30)
        elif col.type=='bool':
            i3hist(col[:],bins=2).draw()
        elif col.type=='uint32' and max(col[:])-min(col[:]):
            a=i3hist(col[:],bins=max(col[:])-min(col[:])+1).draw()
            for n in range(max(col[:])+1):
                print n,sum(col[:]==n)
            print a.hist,a.le
        else:
            i3hist(col[:],bins=50).draw()
        pylab.show()
            
class BrowserApp(wx.App):
    def OnInit(self):
        self.frame = BrowserFrame(None, -1, 'HDF5 Browser')
        self.frame.Show(True)
        self.SetTopWindow(self.frame)
        return True
    
    def ReadFile(self,filename):
        self.frame.ReadFile(filename)
    
    
app = BrowserApp()
app.ReadFile(sys.argv[1])
app.MainLoop()
