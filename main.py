from appJar import gui 

#setups the Gui 
app=gui('Text Editor')
app.setSize(500,500)
app.setIcon('Icon.ico')

#Some basic variebals
Path=''
font=12
darkmode='Off' 
OpenText=''
FM=False

#the (New, Open, Save and Save as) menu function
def menuPress(fm1):
    global Path

    #Save menu
    if fm1 == 'Save':
        try:
            SaveText = app.getTextArea('text')
            with open(Path,'w') as fsa:
                fsa.write(SaveText)
                app.setTitle(Path)
                fsa.close()
        except:
            Path = app.saveBox('Save:',fileExt='.txt',fileTypes=[('Text files', '*.txt')])
            TextToSave = app.getTextArea('text')
            with open(Path,'a') as fs:
                fs.write(TextToSave)
                fs.close()

    #save as menu
    if fm1 == 'Save as':
        try:
            Path = app.saveBox('Save as:',fileExt='.txt',fileTypes=[('Text files', '*.txt')])
            TextToSave = app.getTextArea('text')
            with open(Path,'w') as fsa:
                fsa.write(TextToSave)
                app.setTitle(Path)
                fsa.close()
        except:
            pass
    
    #Open menu
    if fm1 == 'Open':
        try:
            Path = app.openBox('Open:')
            with open(Path,'r') as fo:
                OpenText=fo.read()
                app.clearAllTextAreas(callFunction=False)
                app.setTextArea('text',OpenText)
                app.setTitle(Path)
                fo.close()
        except:
            app.errorBox('Error! ',"Error You didn't select a supported file")

    #New menu
    if fm1 == 'New':
        if app.getTextArea('text') == '' or app.getTextArea('text') == ' ':
            app.clearTextArea('text')
        else:
            temp = app.yesNoBox('','do You wanna save?')
            if temp == True:
                menuPress('Save')
            else:
                app.clearTextArea('text')

#makes the font bigger function
def IncreaseFont():
    global font
    if font <= 999:
        font += 1
    else:
        app.soundWarning()
    app.setTextAreaFont('text',size=font)
#makes the font smaller function
def DecreaseFont():
    global font
    if font >= 6:
        font -= 1
    else:
        app.soundWarning()
    app.setTextAreaFont('text',size=font)

#the "Focus mode" function
def FocusMode():
    global FM
    if FM == False:
        app.setSize('Fullscreen')
        FM = True
    elif FM == True:
        app.exitFullscreen()
        FM = False

#Darkmode function
def DarkMode(OnOff):
    global darkmode
    if darkmode == 'On':
        darkmode = 'Off'
        app.setTextAreaFg('text','black')
        app.setTextAreaBg('text','white')
    elif darkmode == 'Off':
        darkmode = 'On'
        app.setTextAreaFg('text','white')
        app.setTextAreaBg('text','black')

# "The Hacker Mode"
def Hmode(OnOff):
    global darkmode
    if darkmode == 'On':
        darkmode = 'Off'
        app.setTextAreaFg('text','black')
        app.setTextAreaBg('text','white')
    elif darkmode == 'Off':
        darkmode = 'On'
        app.setTextAreaFg('text','green')
        app.setTextAreaBg('text','black')

def Apply():
    TS = app.getScale('Transparency')
    app.setTransparency(int(TS))

#Transparency window class
class tranWindow():
    app.startSubWindow('Transparency')
    app.addLabelScale('Transparency')
    app.setScaleRange('Transparency',100,5)
    app.setScaleIncrement('Transparency',1)
    app.showScaleValue('Transparency',show=True)
    app.addButton('Apply',Apply)
    app.stopSubWindow()

def transp():
    app.showSubWindow('Transparency')


#the Info and About function
def Other(IorA):

    if IorA == 'Info':
        app.infoBox('Info','KeyBinds:\n\nControl + S = Save\nControl + D = Save as\nControl + O = Open\nControl + N = New\nControl + Up = Icrease Font Size'
        +'\nControl + down Decrase Font Size\n\nAnd tab doesnt work')
    
    elif IorA == 'About':
        app.infoBox('About','Hi im kowal05. I have made this app just as a learning.\nSo dont expect updates maybe one or two a year and its prootly gonna be a bug fixs.\n'
        +'Anyways this is just a plain simple text editor like notepad\nLink to the project on github:\n{insert link here}')



#the menubar class
class menu_List():
    app.createMenu("File")
    app.addMenuItem("File", "New", func=menuPress, shortcut='Control-N')
    app.addMenuItem("File", "Open", func=menuPress, shortcut='Control-O')
    app.addMenuItem("File", "-")
    app.addMenuItem("File", "Save", func=menuPress, shortcut='Control-S')
    app.addMenuItem("File", "Save as", func=menuPress, shortcut='Control-D')


    app.createMenu("Config")
    app.addMenuItem("Config", "Increase Size", func=IncreaseFont, shortcut='Control-Up')
    app.addMenuItem("Config", "Decrease Size", func=DecreaseFont, shortcut='Control-Down')
    app.addMenuItem("Config", "-",)
    app.addMenuItem("Config",'Dark Mode', DarkMode)
    app.addMenuItem("Config",'THE HACKER MODE', Hmode)
    app.addMenuItem("Config",'Transparency', transp)
    app.addMenuItem("Config","Focus Mode", func=FocusMode,shortcut='Control-key-F')


    app.createMenu('Other')
    app.addMenuItem('Other','Info', Other)
    app.addMenuItem('Other','About', Other)


#the text area
app.addTextArea('text', text=None)

#starts the app
app.go()