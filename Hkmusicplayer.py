
def unmutemusic():
    global currentvol
    root.unmutebutton.grid_remove()
    root.mutebutton.grid()
    mixer.music.set_volume(currentvol)

def mutemusic():
    global currentvol
    root.mutebutton.grid_remove()
    root.unmutebutton.grid()
    currentvol=mixer.music.get_volume()
    mixer.music.set_volume(0)
def resumemusic():
    root.resumebutton.grid_remove()
    root.pausebutton.grid()
    mixer.music.unpause()
    audiostatuslabel.configure(text='Resume...')
def volumeup():
    vol = mixer.music.get_volume()
    mixer.music.set_volume(vol + 0.05)
    ProgressbarVolumeLabel.configure(text='{}%'.format(int(mixer.music.get_volume()*100)))
    Progressbarvolume['value']=mixer.music.get_volume()*100
def volumedown():
    vol = mixer.music.get_volume()
    mixer.music.set_volume(vol - 0.05)
    ProgressbarVolumeLabel.configure(text='{}%'.format(int(mixer.music.get_volume() * 100)))
    Progressbarvolume['value'] = mixer.music.get_volume() * 100
def stopmusic():
    mixer.music.stop()
    audiostatuslabel.configure(text='Stop...')
def pausemusic():
    mixer.music.pause()
    root.pausebutton.grid_remove()
    root.resumebutton.grid()
    audiostatuslabel.configure(text='Pause...')
def playmusic():
    ad=audiotrack.get()
    mixer.music.load(ad)
    ProgressbarLabel.grid()
    root.mutebutton.grid()
    Progressbarmusiclabel.grid( )
    mixer.music.set_volume(0.4)
    Progressbarvolume['value'] = 40
    ProgressbarVolumeLabel['text'] = '40%'
    mixer.music.play()
    audiostatuslabel.configure(text='Playing...')

    song=MP3(ad)
    totalsonglength=int(song.info.length)
    Progressbarmusic['maximum']=totalsonglength
    Progressbarmusicendtimelabel.configure(text='{}'.format(str(datetime.timedelta(seconds=totalsonglength))))
    def Progressbarmusictick():
        CurrentSongLength=mixer.music.get_pos()//1000
        Progressbarmusic['value']=CurrentSongLength
        Progressbarmusicstarttimelabel.configure(text='{}'.format(str(datetime.timedelta(seconds=CurrentSongLength))))
        Progressbarmusic.after(2,Progressbarmusictick)
    Progressbarmusictick()
def musical():
    try:
        dd=filedialog.askopenfilename(title='Select audio file',
                                  filetype=(('MP3','.mp3'),('WAV','.wav')))
    except:
        dd=filedialog.askopenfilename(title='Select audio file',
                                  filetype=(('MP3','.mp3'),('WAV','.wav')))

    audiotrack.set(dd)
def createwidthes():
    global imbrowse,imresume,impause, imvolumeup, imvolumedown, imstop,immute,imunmute,implay
    global audiostatuslabel,ProgressbarVolumeLabel,Progressbarvolume,ProgressbarLabel,Progressbarmusiclabel,Progressbarmusic,Progressbarmusicendtimelabel,Progressbarmusicstarttimelabel
    #####################################Image Regitser
    implay = PhotoImage(file='play-button.png')
    impause = PhotoImage(file='pause.png')
    imbrowse = PhotoImage(file='browse.png')
    imstop = PhotoImage(file='stop.png')
    imvolumeup = PhotoImage(file='volume.png')
    imvolumedown = PhotoImage(file='volume-down.png')
    imresume = PhotoImage(file='play-button.png')
    immute = PhotoImage(file='mute.png')
    imunmute = PhotoImage(file='volume.png')
    ##########################################change size of images
    imbrowse=imbrowse.subsample(2,2)
    implay = implay.subsample(2, 2)
    impause = impause.subsample(2, 2)
    imstop = imstop.subsample(2, 2)
    imvolumeup = imvolumeup.subsample(2, 2)
    imvolumedown = imvolumedown.subsample(2, 2)
    imresume = imresume.subsample(2, 2)
    immute = immute.subsample(2, 2)
    imunmute = imunmute.subsample(2, 2)
    ################################################################################ labelsssss
    tracklabel = Label(root, text='Song location', background='pink', font=('arial', 15, 'bold'))
    tracklabel.grid(row=0, column=0, padx=20, pady=20)

    audiostatuslabel=Label(root, text='',background='pink',font=('arial', 15, 'bold'),width=20)
    audiostatuslabel.grid(row=2,column=1)

    ProgressbarLabel=Label(root,text='',bg='deeppink')
    ProgressbarLabel.grid(row=0,column=3,rowspan=3,padx=20,pady=20)
    ProgressbarLabel.grid_remove()
    Progressbarvolume=Progressbar(ProgressbarLabel,orient=VERTICAL,mode='determinate',
                              value=0,length=190)
    Progressbarvolume.grid(row=0,column=0,ipadx=5)

    ProgressbarVolumeLabel=Label(ProgressbarLabel,text='01',bg='pink',width=3)
    ProgressbarVolumeLabel.grid(row=0,column=0)
####################################################################################Progress bar music
    Progressbarmusiclabel=Label(root,text='',bg='pink')
    Progressbarmusiclabel.grid(row=7, column=0,columnspan=3, padx=20, pady=20)
    Progressbarmusiclabel.grid_remove()
    Progressbarmusicstarttimelabel = Label(Progressbarmusiclabel, text='0:00:0', bg='white',width=10)
    Progressbarmusicstarttimelabel.grid(row=0, column=0,)

    Progressbarmusic=Progressbar(Progressbarmusiclabel,orient=HORIZONTAL,mode='determinate',value=0)
    Progressbarmusic.grid(row=0,column=1,ipadx=300)


    Progressbarmusicendtimelabel = Label(Progressbarmusiclabel, text='0:00:0', bg='white')
    Progressbarmusicendtimelabel.grid(row=0, column=2)
    ################################################################################Entry box
    tracklabelentry = Entry(root, font=('arial', 15, 'italic bold'), width=35,textvariable=audiotrack)
    tracklabelentry.grid(row=0, column=1, padx=20, pady=20)
    #################################################################################buttons
    browsebutton = Button(root, text='', font=('arial', 13, 'italic bold'), width=35, bd=5,border='0',
                          activebackground='purple4', image=imbrowse, compound=RIGHT,command=musical)
    browsebutton.grid(row=0, column=2, pady=20, padx=20)

    playbutton = Button(root, text='',font=('arial', 13, 'italic bold'), width=47, bd=5,border='0',
                        activebackground='purple4', image=implay, compound=RIGHT,command=playmusic)
    playbutton.grid(row=8, column=0, pady=20, padx=20)

    root.pausebutton = Button(root, text='', font=('arial', 13, 'italic bold'), width=47, bd=5,border='0',
                        activebackground='purple4', image=impause, compound=RIGHT,command=pausemusic)
    root.pausebutton.grid(row=8, column=1, pady=20, padx=20)


    root.resumebutton = Button(root, text='', width=47, bd=5,border='0',
                         activebackground='purple4', image=imresume, compound=RIGHT,command=resumemusic)
    root.resumebutton.grid(row=8, column=1, pady=20, padx=20)
    root.resumebutton.grid_remove()

    root.mutebutton=Button(root,text='',width=35,border='0',activebackground='purple4',bd=0,
                           image=immute,compound=RIGHT,command=mutemusic)
    root.mutebutton.grid(row=3,column=3)
    root.mutebutton.grid_remove()
    root.unmutebutton = Button(root, text='', width=35,border='0', activebackground='purple4', bd=0,
                             image=imunmute, compound=RIGHT,command=unmutemusic)
    root.unmutebutton.grid(row=3, column=3)
    root.unmutebutton.grid_remove()

    volumeupbutton = Button(root, text='', font=('arial', 13, 'italic bold'), width=35, bd=0,border=0,
                            activebackground='purple4', image=imvolumeup, compound=RIGHT,command=volumeup)
    volumeupbutton.grid(row=1, column=2, pady=20, padx=20)

    stopbutton = Button(root, text='', font=('arial', 13, 'italic bold'), width=47, bd=5,border='0',
                        activebackground='purple4', image=imstop, compound=RIGHT,command=stopmusic)
    stopbutton.grid(row=8, column=2, pady=20, padx=20)

    volumedownbutton = Button(root, text='', font=('arial', 13, 'italic bold'),width=35,bd=5,border='0',
                                activebackground='purple4', image=imvolumedown, compound=RIGHT,command=volumedown)
    volumedownbutton.grid(row=2, column=2, pady=20, padx=20)
##################################################################################Progressbar
#ProgressbarLabel=Label(root,text='',background='pink',font=('arial', 15, 'italic bold'),width=20)
#ProgressbarLabel.grid(row=0,column=3)

#ProgressbarVolume=Progressbar(ProgressbarLabel,orient=VERTICAL,mode='determinate',
    #                          value=0,length=190)
#ProgressbarVolume.grid(row=0,column=0,ipadx=5)
#traclabel = Label(root, text='Select audio track', background='lightskyblue', font=('arial', 15, 'italic bold'))
#traclabel.grid(row=0, column=3, padx=20, pady=20)

from tkinter import *
from tkinter import filedialog
from pygame import mixer
from tkinter.ttk import Progressbar
from PIL import ImageTk,Image
import datetime
from mutagen.mp3 import MP3
root = Tk()
root.geometry('1100x500+200+50')
root.title('harry music player')
root.iconbitmap('d.ico')
root.resizable(False, False)
root.configure(bg='pink')
######################################## Global variable
audiotrack=StringVar()
currentvol=0
totalsonglength=0
count=0
text=''
################    ######################### Craete Slider
ss = 'DEVELOPED BY HARSH KUMRAWAT SOFTWARES'
count = 0
text = ''
#################################SLIDER
SliderLabel = Label(root, text=ss,background='pink', font=('arial', 20, 'italic bold'))
SliderLabel.grid(row=9, column=0, padx=20, pady=20, columnspan=3)



mixer.init()
createwidthes()
root.mainloop()