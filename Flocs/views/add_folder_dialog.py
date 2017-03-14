#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 12/03/2017

@author: augusto
'''

import wx
from numpy import integer

class AddFolderDialog(wx.Dialog):
    def __init__(self, *args, **kw):
        super(AddFolderDialog, self).__init__(*args, **kw) 
            
        self.initUI()
        self.SetSize((300, 150))
        self.SetTitle(u'Agregar Muestra')
    
    def initUI(self):
        panel = wx.Panel(self)
        dialogBox = wx.BoxSizer(wx.VERTICAL)

        panelBox = wx.StaticBox(panel, label = u'Agregar Muestra: ')
        panelBoxSizer = wx.StaticBoxSizer(panelBox, orient = wx.VERTICAL)        
        
        timeBox = wx.BoxSizer(wx.HORIZONTAL)   
        label_time = wx.StaticText(self,  wx.ID_ANY, u' &Tiempo (min):')
        self.text_time = wx.SpinCtrl(panel, wx.ID_ANY, style=wx.SP_ARROW_KEYS|wx.ALIGN_RIGHT, value="5", min = 0 , max = 10000, initial=5,  name = "Tiempo")     
        
        timeBox.Add(label_time, flag=wx.RIGHT)
        timeBox.Add(self.text_time)
        panelBoxSizer.Add(timeBox)
        
        panel.SetSizer(panelBoxSizer)
       
        buttonBox = wx.BoxSizer(wx.HORIZONTAL)
        self.button_ok = wx.Button(self, wx.ID_OK, label = u'Agregar')
        self.button_cancel = wx.Button(self, label = u'Close')
        buttonBox.Add(self.button_cancel, flag = wx.ALIGN_RIGHT, border=10)
        buttonBox.AddSpacer(10)
        buttonBox.Add(self.button_ok, flag = wx.ALIGN_LEFT , border=10)
        
        dialogBox.Add(panel, proportion=1, flag = wx.EXPAND, border=10)
        dialogBox.Add(buttonBox, flag=wx.ALIGN_CENTER, border=10)

        self.SetSizer(dialogBox)
        
        self.Bind(wx.EVT_BUTTON, self.onClose, self.button_cancel)
        
    def onClose(self, event):
        self.Destroy()
      