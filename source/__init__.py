from appJar import gui 
from collections import Counter
from time import sleep
from datetime import datetime

#setups the Gui 
app=gui('T-Editor')
app.setSize(500,500)
app.setIcon('Icon.ico')
app.loadSettings(fileName="settings.ini", useSettings=True)
app.setSetting('darkmode','Off' )
app.setSetting('TS',100)
app.setSetting('hmode','Off')

#Some basic variebals
Path=''
font=12
hmode='Off'
darkmode='Off' 
OpenText=''
FM=False
TS=''
words=0


def openw(filename):
    try:
        with open(filename,'r') as fo:
            OpenText=fo.read()
            app.clearAllTextAreas(callFunction=False)
            app.setTextArea('text',OpenText)
            app.setTitle(Path)
            fo.close()
    except:
        app.errorBox('Error! ',"Error You didn't select a supported file")
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

#changes the font(not working)
def Font(font):
    app.setTextAreaFont('text',family="Comic Sans")

# add the log function
def Log():
    temp = str(datetime.now())
    app.setTextArea('text','['+temp[:-7]+']')

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
def DarkMode():
    global darkmode, hmode
    if darkmode == 'On':
        darkmode = 'Off'
        app.setTextAreaFg('text','black')
        app.setTextAreaBg('text','white')
        app.setStatusbarBg("white", 0)
        app.setStatusbarFg("black", 0)
        app.setSetting('darkmode','Off' )
    elif darkmode == 'Off':
        darkmode = 'On'
        hmode = 'Off'
        app.setTextAreaFg('text','white')
        app.setTextAreaBg('text','black')
        app.setStatusbarBg("black", 0)
        app.setStatusbarFg("white", 0)
        app.setSetting('darkmode','On' )
        app.setSetting('hmode','Off')

# "The Hacker Mode"
def Hmode():

    global hmode, darkmode
    if hmode == 'On':
        hmode = 'Off'
        app.setTextAreaFg('text','black')
        app.setTextAreaBg('text','white')
        app.setStatusbarBg("white", 0)
        app.setStatusbarFg("black", 0)
        app.setSetting('hmode','Off')
        
    elif hmode == 'Off':
        hmode = 'On'
        darkmode='Off'
        app.setTextAreaFg('text','green')
        app.setTextAreaBg('text','black')
        app.setStatusbarBg("black", 0)
        app.setStatusbarFg("green", 0)
        app.setSetting('darkmode','Off' )
        app.setSetting('hmode','On')

#apply's tranparency to the window 
def Apply():
    global TS
    TS = app.getScale('Transparency')
    app.setSetting('TS',int(TS))
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


# the transparency menu
def transp():
    app.showSubWindow('Transparency')


#the Info and About function
def Other(IorA):

    if IorA == 'Info':
        app.infoBox('Info','KeyBinds:\n\nControl + S = Save\nControl + D = Save as\nControl + O = Open\nControl + N = New\nControl + Up = Icrease Font Size'
        +'\nControl + down Decrase Font Size\n\nAnd tab doesnt work')
    
    elif IorA == 'About':
        app.infoBox('About','Hi im kowal05. I have made this app just as a learning.\nSo dont expect updates maybe one or two a year and its prootly gonna be a bug fixs.\n'
        +'Anyways this is just a plain simple text editor like notepad\nLink to the project on github:\nhttps://github.com/kowal05/T-Editor')

        
#confirmation to exit function
def checkStop():
    app.saveSettings(fileName="settings.ini")
    return app.yesNoBox("Confirm Exit", "Are you sure you want to exit the application?")

#counts the words and displays them in statusbar
def wordcount():
    words = len(app.getTextArea('text').split())
    app.setStatusbar("words: " + str(words), 0)

def Tab():
    app.setTextArea('text','    ')
#the menubar class
class menu_List():
    #File menu
    app.createMenu("File")
    app.addMenuItem("File", "New", func=menuPress, shortcut='Control-N')
    app.addMenuItem("File", "Open", func=menuPress, shortcut='Control-O')
    app.addMenuItem("File", "-")
    app.addMenuItem("File", "Save", func=menuPress, shortcut='Control-S')
    app.addMenuItem("File", "Save as", func=menuPress, shortcut='Shift-Control-key-S')

    #Utility menu
    app.createMenu("Utility")
    app.addMenuItem("Utility", "Increase Size", func=IncreaseFont, shortcut='Control-Up')
    app.addMenuItem("Utility", "Decrease Size", func=DecreaseFont, shortcut='Control-Down')
    app.addMenuItem("Utility", "Log", func=Log, shortcut='Control-key-L')
    app.addMenuItem("Utility", "Tab", func=Tab, shortcut='key-Tab')
    app.addSubMenu("Utility", "Fonts")
    app.addMenuItem("Fonts","Arial", func=Font)
    app.addMenuItem("Fonts","Courier", func=Font)
    app.addMenuItem("Fonts","Comic sans", func=Font)
    app.addMenuItem("Fonts","Sans Serif", func=Font)
    app.addMenuItem("Fonts","Times", func=Font)
    app.addMenuItem("Fonts","Verdana", func=Font)
    app.addMenuItem("Utility", "-",)
    app.addMenuItem("Utility",'Dark Mode', DarkMode)
    app.addMenuItem("Utility",'THE HACKER MODE', Hmode)
    app.addMenuItem("Utility",'Transparency', transp)
    app.addMenuItem("Utility","Focus Mode", func=FocusMode,shortcut='Control-key-F')


    #Other menu
    app.createMenu('Other')
    app.addMenuItem('Other','Info', Other)
    app.addMenuItem('Other','About', Other)

#setup's the widgets
#the text area
app.addTextArea('text', text=None)
#setup's the statusbar   
app.addStatusbar(fields=1)
app.setStatusbar("words: " + str(words), 0)
#setup's stop function
app.setStopFunction(checkStop)
#counts words
app.registerEvent(wordcount)

#start function loads settings.ini
def start():
    global darkmode, hmode
    sleep(0.01)
    temp3=app.getSetting('TS')
    if app.getSetting('darkmode') == 'On':
        darkmode = 'Off'
        DarkMode()
    elif app.getSetting('hmode') == 'On':
        hmode = 'Off'
        Hmode()
    else:
        pass
    app.setTransparency(int(temp3))
#starts the app
app.setStartFunction(start)

if __name__ == '__main__':
    from context_menu import menus

    fc = menus.FastCommand('Open With T-Editor', type='*.txt', python=openw)
    fc.compile()
    app.go()