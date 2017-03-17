#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 18/02/2017

@author: augusto
'''
import wx
from views.main_window import MainWindow 
from views.add_folder_dialog import AddFolderDialog
from model.Image import Image

class MainWindowControl:
    """ Controller for the Application """
    def __init__(self):
        self.initView()
    
    def initView(self):
        # Create main Window
        self.frame = MainWindow(None)
        self.frame.Maximize(True)
        self.frame.Show(True)
        
        # Create Image
        self.image = Image()
        
        # Adjust Panel Size 
        frame_width = self.frame.GetSize().GetWidth()
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
    
    # Init images processing     
    def onStart(self, event):
        message = self.frame.panel_initial.parameters.ValidateInputs()
        if  message == "":
            imageList = self.frame.panel_initial.image.traverseTree(True)
            emptyItems = self.frame.panel_initial.image.verifyEmptySamples()
            if not self.frame.panel_initial.image.traverseTree(False):
                wx.MessageBox(u'No hay Imágenes para Procesar', 'Error', 
                wx.OK | wx.ICON_ERROR)
            else:
                if emptyItems:
                    message_empty = u'Las siguientes muestras no tienen imágenes \n'
                    for empty in emptyItems:
                        message_empty = message_empty +  u"\u2022" + u' Tiempo = ' + str(empty) + u' min \n'
                    wx.MessageBox(message_empty, u'Información', 
                                  wx.OK | wx.ICON_INFORMATION)
                else:
                    for imagePath in imageList:
                        if isinstance(imagePath, int):
                            pass
                        else:
                            self.processImage(imagePath)
                                           
                    #wx.MessageBox('Start Information', 'Info', wx.OK | wx.ICON_INFORMATION)
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
    
    # Add sample Time in TreeCtrl
    def onAddFolder(self, event):
        dialog_add = AddFolderDialog(None)
        dialog_add.Centre()
        if dialog_add.ShowModal() == wx.ID_OK:
            value = dialog_add.text_time.GetValue()
            # Get List of all First Level items in Tree 
            imageList = self.frame.panel_initial.image.traverseTree(True)
            
            # If TreeCtrl of images is empty, then add a sample time to tree
            if not imageList:
                self.imageTree.AppendItem(self.imageTree.GetRootItem(), 'Tiempo = ' + str(value) + ' min')
                dialog_add.Destroy()
            # If TreeCtrl of images is not empty, then to verify if value exist else add sample time to tree
            else:  
                sampleList = False
                for sample in imageList:
                    if sample == value:
                        sampleList = True
                        break
                if not sampleList:
                    self.imageTree.AppendItem(self.imageTree.GetRootItem(), 'Tiempo = ' + str(value) + ' min')
                    dialog_add.Destroy()
                else:
                    wx.MessageBox('El tiempo de la muestra ya existe', u'Información', wx.OK | wx.ICON_INFORMATION)  
                    
    # Add Image paths to TreeCtrl      
    def onAddFile(self, event):
        # open File Dialog (PNG, TIFF)
        self.openFileDialog = wx.FileDialog(self.frame,"Abrir", wildcard = 
                                            "TIFF files (*.tif)|*.tif|PNG files (*.png)|*.png", 
                                      style = wx.FD_OPEN | wx.FD_FILE_MUST_EXIST|wx.FD_MULTIPLE)
        if self.openFileDialog.ShowModal() == wx.ID_OK:
            # Verify if the parent of selected Item is the root or a level 1 item
            imageList = self.frame.panel_initial.image.traverseTree(False)
            imagePaths = self.openFileDialog.GetPaths()
            duplicatePaths = [] 
            newPaths = []
            exist = False
            
            # Verify if paths exits in the TreeCtrl 
            for path in imagePaths:
                for image in imageList:
                    if image == path:
                        duplicatePaths.append(path)
                        exist = True
                if not exist:
                    newPaths.append(path)
            
            # verify if Path are not duplicate, else show info message
            if not duplicatePaths:
                pass
            else:
                message = 'Los siguientes archivos ya existen:\n'
                for path in duplicatePaths:
                    message = message + u"\u2022 " + path + '\n'
                wx.MessageBox(message, 'Archivos duplicados', wx.OK | wx.ICON_ERROR)
 
            # Add Not duplicate path to TreCtrl, first verify the parent Item                
            item = self.imageTree.GetSelections()
            # If have multiple item selected show information message
            if len(item) == 1:
                if self.imageTree.GetRootItem() == self.imageTree.GetItemParent(item[0]):
                    self.frame.panel_initial.image.addItem(item[0], newPaths)
                    self.imageTree.Expand(item[0])
                else:
                    self.frame.panel_initial.image.addItem(self.imageTree.GetItemParent(item[0]), newPaths)
                    self.imageTree.Expand(self.imageTree.GetItemParent(item[0]))
            else:
                wx.MessageBox(u'Seleccione un solo elemento', 'Agregar', wx.OK | wx.ICON_INFORMATION)
        self.openFileDialog.Destroy()
    
    # Remove Selected items of TreeCtrl 
    def onRemove(self, event):
        items = self.imageTree.GetSelections()
        message = u'Desea eliminar los siguientes archivos: \n'
        for path in items:
            message = message + u"\u2022 " + self.imageTree.GetItemText(path) + "\n"
        dialog_remove = wx.MessageDialog(self.frame, message, 'Eliminar')
        if dialog_remove.ShowModal() == wx.ID_OK:
            for item in items:
                self.imageTree.Delete(item)
        # Verify if TreeCtrl is empty and disable add_file button
        if not self.frame.panel_initial.image.list_files.GetSelections():
            self.frame.panel_initial.image.button_addFile.Disable()
            self.frame.panel_initial.image.button_remove.Disable()
        else: 
            self.frame.panel_initial.image.button_addFile.Enable()
            self.frame.panel_initial.image.button_remove.Enable()
        self.frame.panel_initial.image.removeImage()
    
    # Show selected path on the image panel
    def onSelChanged(self, event):
        # If any item is selected disable add_file and remove buttons
        item =  event.GetItem()
        if not self.frame.panel_initial.image.list_files.GetSelections():
            self.frame.panel_initial.image.button_addFile.Disable()
            self.frame.panel_initial.image.button_remove.Disable()
        else: 
            self.frame.panel_initial.image.button_addFile.Enable()
            self.frame.panel_initial.image.button_remove.Enable()
       
        # If selected item is a Parent Item don't performs anything
        if self.imageTree.GetRootItem() == self.imageTree.GetItemParent(item):
            pass
        else:
            self.frame.panel_initial.image.onView((event.GetEventObject().GetItemText(item)))

    
    def disableInitialPanel(self):
        self.frame.panel
        
    def processImage(self, path):
        self.image.loadImage(path)
        self.image.getBinaryImage()
        self.image.showImage()
        