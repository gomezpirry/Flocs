#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 24/02/2017

@author: augusto
'''
import wx, os


""" Class for validating text required """
class TextObjectValidator(wx.PyValidator):
    def __init__(self):
        wx.PyValidator.__init__(self)

    def Clone(self):
        return TextObjectValidator()


    def Validate(self, win):
        textCtrl = self.GetWindow()
        text = textCtrl.GetValue()

        if len(text) == 0:
            textCtrl.SetBackgroundColour("pink")
            textCtrl.SetFocus()
            textCtrl.Refresh()
            return False
        else:
            textCtrl.SetBackgroundColour( wx.SystemSettings_GetColour(wx.SYS_COLOUR_WINDOW))
            textCtrl.Refresh()
            return True
    
    def TransferToWindow(self):
        return True

    def TransferFromWindow(self):
        return True 
    
""" Class for validating number required and range value """
class NumberValidator():
    def __init__(self):
        self.message = ""
    
    def Validate(self, widget, min, max):
        value = widget.GetValue()
        if value == None:
            widget.SetBackgroundColour("pink")
            widget.SetFocus()
            widget.Refresh()
            return u"\u2022 " +  widget.GetName() + " es requerido \n"
        else:
            if value < min or value > max:
                widget.SetBackgroundColour("pink")
                widget.SetFocus()
                widget.Refresh()
                return u"\u2022 " +  widget.GetName() + " fuera de rango \n"
            else:
                widget.SetBackgroundColour( wx.SystemSettings_GetColour(wx.SYS_COLOUR_WINDOW))
                widget.Refresh()
                return ""
        

""" Class for validating text required """
class TextValidator():
    def __init__(self):
        self.message = ""
    
    def Validate(self, widget):
        value = widget.GetValue()
        if value == "":
            widget.SetBackgroundColour("pink")
            widget.SetFocus()
            widget.Refresh()
            return u"\u2022 " + widget.GetName() + " es requerido \n"
        else:
            widget.SetBackgroundColour( wx.SystemSettings_GetColour(wx.SYS_COLOUR_WINDOW))
            widget.Refresh()
            return ""

""" Class for validating output folder """       
class BrowserValidator():
    def __init__(self):
        self.message = ""
        
    def Validate(self, widget):
        value = widget.GetValue()
        if value == "":
            widget.SetBackgroundColour("pink")
            widget.SetFocus()
            widget.Refresh()
            return u"\u2022 " + widget.GetName() + " es requerido \n"
        else:
            if not os.path.isdir(value):
                widget.SetBackgroundColour("pink")
                widget.SetFocus()
                widget.Refresh()
                return u"\u2022 " + widget.GetName() + " no existe\n"
            else:
                widget.SetBackgroundColour( wx.SystemSettings_GetColour(wx.SYS_COLOUR_WINDOW))
                widget.Refresh()
                return ""
        
    