#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 18/02/2017

@author: augusto
'''
import wx
from views.main_window import MainWindow 
from views.add_folder_dialog import AddFolderDialog
from controller.validators import TextObjectValidator, NumberValidator 

class MainWindowControl:
    """ Controller for the Application """
    def __init__(self):
        self.initView()
    
    def initView(self):
        # Create main Window
        self.frame = MainWindow(None)
        self.frame.Maximize(True)
        self.frame.Show(True)
        
        # Adjust Panel Size 
        frame_width, frame_height = self.frame.GetSize()
        self.frame.panel_initial.setSplitterPanelSize((frame_width*2)/3)
        self.frame.panel_initial.setSplitterImageSize(frame_width/6)
        
        # Create local references to components
        self.imageTree = self.frame.panel_initial.image.list_files
        self.textOutput = self.frame.panel_initial.parameters.outputBrowser.fileText
        
        # --------------------------------------------------------
        # -----------------  Set Binds To Frame ------------------
        # --------------------------------------------------------
        
        # Close Frame Bind
        self.frame.Bind(wx.EVT_CLOSE, self.onExit)

        # --------------------------------------------------------
        # -----------------  Set Binds To MenuBar ----------------
        # -------------------------------------------------------- 
        
        # Open Bind
        self.frame.Bind(wx.EVT_MENU, self.onOpen, self.frame.fMenuOpen) 
        # Quit Bind  
        self.frame.Bind(wx.EVT_MENU, self.onExit, self.frame.fMenuExit)
        # Copy Bind 
        self.frame.Bind(wx.EVT_MENU, self.onCopy, self.frame.eMenuCopy) 
        # Cut Bind
        self.frame.Bind(wx.EVT_MENU, self.onCut, self.frame.eMenuCut)
        # Paste Bind 
        self.frame.Bind(wx.EVT_MENU, self.onPaste, self.frame.eMenuPaste)
        # Help Bind
        self.frame.Bind(wx.EVT_MENU, self.onHelp, self.frame.hMenuHelp)
        # About Bind 
        self.frame.Bind(wx.EVT_MENU, self.onAbout, self.frame.hMenuAbout)  
        
        # --------------------------------------------------------
        # -----------------  Set Binds To Toolbar ----------------
        # -------------------------------------------------------- 
        
        # open Bind
        self.frame.Bind(wx.EVT_TOOL, self.onOpen, self.frame.tool_open)
        # Save Bind
        self.frame.Bind(wx.EVT_TOOL, self.onSave, self.frame.tool_save) 
        # Start Bind
        self.frame.Bind(wx.EVT_TOOL, self.onStart, self.frame.tool_start) 
        # Stop Bind
        self.frame.Bind(wx.EVT_TOOL, self.onStop, self.frame.tool_stop) 
        # Exit Bind
        self.frame.Bind(wx.EVT_TOOL, self.onExit, self.frame.tool_exit) 
        
        # --------------------------------------------------------
        # ------  Set Binds To Parameters Panel Buttons ----------
        # -------------------------------------------------------- 
        
        # Start Bind
        self.frame.Bind(wx.EVT_BUTTON, self.onOutput, self.frame.panel_initial.getOutputButton())
        # Stop Bind
        self.frame.Bind(wx.EVT_BUTTON, self.onStart, self.frame.panel_initial.getStartButton())
        
        # --------------------------------------------------------
        # ----------  Set Binds To Image Panel Buttons -----------
        # --------------------------------------------------------
        
        # Add Folder Bind
        self.frame.Bind(wx.EVT_BUTTON, self.onAddFolder, self.frame.panel_initial.getAddFolderButton())
        # Add File Bind
        self.frame.Bind(wx.EVT_BUTTON, self.onAddFile, self.frame.panel_initial.getAddFileButton())
        # Remove Bind
        self.frame.Bind(wx.EVT_BUTTON, self.onRemove, self.frame.panel_initial.getRemoveButton())
        
        # --------------------------------------------------------
        # --------------  Set Binds To Image Tree ----------------
        # --------------------------------------------------------
        self.frame.Bind(wx.EVT_TREE_SEL_CHANGED, self.onSelChanged, self.imageTree)
    # --------------------------------------------------------
    # -----------------  Set Binds Functions -----------------
    # -------------------------------------------------------- 
    
    def onOpen(self, event):
        wx.MessageBox('Open Information', 'Info', 
            wx.OK | wx.ICON_INFORMATION)  
    # Exit Function (Load Question Message to Confirm Close Application)
    def onExit(self, event):
        self.frame.Destroy()
        #dialog_exit = wx.MessageDialog(self.frame, u'Desea salir de la aplicación', 'Salir')
        #if dialog_exit.ShowModal() == wx.ID_OK:
        #    self.frame.Destroy()
    
    def onCopy(self, evente):
        wx.MessageBox('Copy Information', 'Info', 
            wx.OK | wx.ICON_INFORMATION)  
    
    def onCut(self, event):
        wx.MessageBox('Cut Information', 'Info', 
            wx.OK | wx.ICON_INFORMATION)
        
    def onPaste(self, event):
        wx.MessageBox('Paste Information', 'Info', 
            wx.OK | wx.ICON_INFORMATION)
    
    def onHelp(self, event):
        wx.MessageBox('Help Information', 'Info', 
            wx.OK | wx.ICON_INFORMATION)
    
    def onAbout(self, event):
        wx.MessageBox('About Information', 'Info', 
            wx.OK | wx.ICON_INFORMATION)
    
    def onSave(self, event):
        wx.MessageBox('Save Information', 'Info', 
            wx.OK | wx.ICON_INFORMATION)
         
    def onStart(self, event):
        message = self.frame.panel_initial.parameters.ValidateInputs()
        if  message == "":
            imageList = self.frame.panel_initial.image.traverseTree()
            if not imageList:
                wx.MessageBox(u'No hay Imágenes para Procesar', 'Error', 
                wx.OK | wx.ICON_ERROR)
            else:
                for imagePath in imageList:
                    print (imagePath)
                wx.MessageBox('Start Information', 'Info', 
                wx.OK | wx.ICON_INFORMATION)
        else:
            wx.MessageBox(message, u'Error en Parámetros Iniciales', 
            wx.OK | wx.ICON_ERROR)
        
    def onStop(self, event):
        wx.MessageBox('Stop Information', 'Info', 
            wx.OK | wx.ICON_INFORMATION)     
        
    # Output Browser Function (Open Folder Dialog to set output folder)
    def onOutput(self, event):
        self.openFolderDialog = wx.DirDialog(self.frame,"Abrir", style = wx.DD_DEFAULT_STYLE| wx.DD_DIR_MUST_EXIST)
        if self.openFolderDialog.ShowModal() == wx.ID_OK:
            self.textOutput.SetValue(self.openFolderDialog.GetPath())
        self.openFolderDialog.Destroy() 
        
    def onAddFolder(self, event):
        dialog_add = AddFolderDialog(None)
        dialog_add.Centre()
        if dialog_add.ShowModal() == wx.ID_OK:
            self.imageTree.AppendItem(self.imageTree.GetRootItem(), 'Tiempo = ' + str(dialog_add.text_time.GetValue()) + ' min')
        dialog_add.Destroy()
        
        
    def onAddFile(self, event):
        self.openFileDialog = wx.FileDialog(self.frame,"Abrir", wildcard = 
                                            "PNG files (*.png)|*.png|TIFF files (*.tif)|*.tif", 
                                      style = wx.FD_OPEN | wx.FD_FILE_MUST_EXIST|wx.FD_MULTIPLE)
        if self.openFileDialog.ShowModal() == wx.ID_OK:
            item = self.imageTree.GetSelection()
            if self.imageTree.GetRootItem() == self.imageTree.GetItemParent(item):
                item_new = self.frame.panel_initial.image.addItem(item, self.openFileDialog.GetPaths())
                self.imageTree.Expand(item)
            else:
                self.frame.panel_initial.image.addItem(self.imageTree.GetItemParent(item), self.openFileDialog.GetPaths())
                self.imageTree.Expand(self.imageTree.GetItemParent(item))
        self.openFileDialog.Destroy()
    
    def onRemove(self, event):
        item = self.imageTree.GetSelection()
        dialog_remove = wx.MessageDialog(self.frame, u'Desea eliminar "' + self.imageTree.GetItemText(item) +'"', 'Eliminar')
        if dialog_remove.ShowModal() == wx.ID_OK:
            self.imageTree.Delete(item)
        if not self.frame.panel_initial.image.list_files.GetSelection():
            self.frame.panel_initial.image.button_addFile.Disable()
            self.frame.panel_initial.image.button_remove.Disable()
        else: 
            self.frame.panel_initial.image.button_addFile.Enable()
            self.frame.panel_initial.image.button_remove.Enable()
        self.frame.panel_initial.image.removeImage()
        
    def onSelChanged(self, event):
        item =  event.GetItem()
        if not self.frame.panel_initial.image.list_files.GetSelection():
            self.frame.panel_initial.image.button_addFile.Disable()
            self.frame.panel_initial.image.button_remove.Disable()
        else: 
            self.frame.panel_initial.image.button_addFile.Enable()
            self.frame.panel_initial.image.button_remove.Enable()
       
        if self.imageTree.GetRootItem() == self.imageTree.GetItemParent(item):
            pass
        else:
            self.frame.panel_initial.image.onView((event.GetEventObject().GetItemText(item)))

