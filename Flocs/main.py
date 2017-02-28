#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 21/02/2017

@author: augusto
'''

import wx

from controller.main_window_control import MainWindowControl

if __name__ == '__main__':
    app = wx.App(False)
    initApp = MainWindowControl()
    app.MainLoop()