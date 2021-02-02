"""
Hamza Hassan Khan

"""

from tkinter import *
import tkinter.font as font
import random
import time

class time_record:
    def __init__(self):
        self._time_capture = None
    def getTime(self):
        return self._time_capture

    def setTime(self):
        try:
            raise Exception (" Time Cannot be set")
        except Exception:
            print("Time cannot be set")

    # def __lt__(self, other):
    #     if self._time_capture < other + 2 :
    #         return True
    #     return False

    time_capture = property(getTime)





class Counter(object):
    def __init__(self):
        self._counter = 0

    def getCounter(self):
        return self._counter
    def setCounter(self):
        raise NotImplemented("Not Implemented")

    def increment(self):
        self._counter+=1
    def reset(self):
        self._counter = 0



    counter = property(getCounter)


#
# def counter(event):
#     counter = Counter()
#     counter.increment()
#     canvas.create_text(text = counter.getCounter)

tar_time = time_record()
counter = Counter()


def square():
    canvas.delete('all')
    play.pack_forget()
    stop.pack_forget()
    score.pack()
    score['font'] =font
    # global stop
    # stop = Button(frame, text="QUIT", command = lambda: quit() , padx=50, pady=20, bg='#014D6D', fg='orange')
    stop.pack()
    xpos = random.randint(1, 560)
    ypos = random.randint(1, 560)
    tar_time._time_capture = round(time.time())
    sqr = canvas.create_rectangle(xpos,ypos,xpos+40,ypos+40,fill='Orange')
    canvas.tag_bind(sqr,"<ButtonPress-1>",draw_sqr)


def boom(event):

    canvas.delete('all')
    stop.pack_forget()
    score.pack_forget()
    play.pack()
    stop.pack()
    play.config(text = "Play Again")
    stop.config(text = "Quit Game")
    canvas.create_text(100, 100, text="Score: "+ str(counter.counter), font=font, fill='orange')
    counter.reset()




def winning():
    canvas.delete('all')
    canvas.create_text(300, 200, text="YOU WON WELL DONE !", font=font, fill='orange')
    canvas.create_text(300, 300, text="Your Score: " + str(counter.counter), font=font, fill='orange')
    counter.reset()
    score.pack_forget()
    play.config(text="Play Again")
    play.pack()
    score.pack_forget()




def draw_sqr(event):
    canvas.delete('all')
    orange = "orange"
    red = "red"
    colc2 = "red"

    if counter.counter >= 60:
        winning()
        return
        # orange = "orange"
        # red = "red"

    elif counter.counter > 45:
        orange = "red"
        red = "red"
        colc2 = "orange"
        c1xpos = random.randint(281, 560)
        c1ypos = random.randint(1, 560)
        circle3 = canvas.create_oval(c1xpos, c1ypos, c1xpos + 40, c1ypos + 40, fill=colc2)
        canvas.tag_bind(circle3, "<ButtonPress-1>", boom)

    elif counter.counter > 33:
        orange = "orange"
        red = "orange"
        cxpos = random.randint(281, 560)
        cypos = random.randint(1, 560)
        circle2 = canvas.create_oval(cxpos, cypos, cxpos + 40, cypos + 40, fill=colc2)
        canvas.tag_bind(circle2, "<ButtonPress-1>", boom)
    elif counter.counter > 21:
        orange = "red"
        red = "orange"
    if counter.counter < 15:
        if round(time.time()) - tar_time._time_capture < 2:
            counter.increment()
    else:
        if round(time.time()) - tar_time._time_capture < 1.5:
            counter.increment()
    score.config(text = "Score: "+ str(counter.counter))
    global xpos
    global ypos
    xpos = random.randint(1, 280)
    ypos = random.randint(1, 560)
    tar_time._time_capture = round(time.time())
    newsqr =canvas.create_rectangle(xpos, ypos, xpos + 40, ypos + 40, fill=orange)
    if counter.counter >= 15:
        cxpos = random.randint(281,560)
        cypos  = random.randint(1,560)
        circle = canvas.create_oval(cxpos,cypos,cxpos+40,cypos+40,fill = red)
        canvas.tag_bind(circle, "<ButtonPress-1>",boom)
    canvas.tag_bind(newsqr, "<ButtonPress-1>", draw_sqr)


def col0(event):
    canvas.config(bg="#03254c")
    play.config(bg="#03254c")
    score.config(bg="#03254c")
    stop.config(bg="#03254c")


def col1(event):
    canvas.config(bg='#B9BBB6')
    play.config(bg='#B9BBB6')
    score.config(bg='#B9BBB6')
    stop.config(bg='#B9BBB6')


def col2(event):
    canvas.config(bg='#030200')
    play.config(bg='#030200')
    score.config(bg='#030200')
    stop.config(bg='#030200')

def col3(event):
    canvas.config(bg='#fff8e7')
    play.config(bg='#fff8e7')
    score.config(bg='#fff8e7')
    stop.config(bg='#fff8e7')

def col4(event):
    canvas.config(bg='#234F1E')
    play.config(bg='#234F1E')
    score.config(bg='#234F1E')
    stop.config(bg='#234F1E')

def org(event):
    canvas.config(bg="#014D6D")
    play.config(bg="#014D6D")
    score.config(bg="#014D6D")
    stop.config(bg="#014D6D")




def settings():
    canvas.delete('all')
    if stop:
        stop.pack_forget()
        score.pack_forget()
    canvas.create_text(200, 50, text="Change the Background colour: ", font=font, fill='orange')

    colour0 = canvas.create_oval(100,80,140,120, fill='#03254c' ,outline= "orange")
    colour1 = canvas.create_oval(150, 80, 190, 120, fill='#B9BBB6',outline= "orange")
    colour2 = canvas.create_oval(200, 80, 240, 120, fill='#030200',outline= "orange")
    colour3 = canvas.create_oval(250, 80, 290, 120, fill='#fff8e7',outline= "orange")
    colour4 = canvas.create_oval(300, 80, 340, 120, fill='#234F1E',outline= "orange")
    original = canvas.create_oval(350, 80, 390, 120, fill="#014D6D", outline="orange")

    canvas.tag_bind(colour0, "<ButtonPress-1>", col0)
    canvas.tag_bind(colour1, "<ButtonPress-1>", col1)
    canvas.tag_bind(colour2, "<ButtonPress-1>", col2)
    canvas.tag_bind(colour3, "<ButtonPress-1>", col3)
    canvas.tag_bind(colour4, "<ButtonPress-1>", col4)
    canvas.tag_bind(original, "<ButtonPress-1>", org)




    play.config(text="Continue")
    score.pack()
    play.pack()



def help():
    canvas.delete('all')
    canvas.create_text(300, 250, text=instructions, font=font, fill='orange')
    if stop:
        stop.pack_forget()
        score.pack_forget()
    play.config(text = "Continue")
    score.pack()
    play.pack()








root = Tk()
root.title("MY GAME")
canvas = Canvas(root, width = 600,height= 600,bg = "#014D6D")
canvas.pack(side = TOP)



frame  = Frame(root)
frame.pack(side = BOTTOM)







play = Button(root, text = "Play",command = square,padx = 50, pady = 20, bg= '#014D6D', fg = 'orange')
stop = Button(frame, text="QUIT", command=lambda: quit(), padx=50, pady=20, bg='#014D6D', fg='orange')
score = Label(frame, text="Score: " + str(counter.counter), fg="orange", bg="#014D6D")

font = font.Font(size= 15)
play['font'] = font
play.pack()
stop['font'] = font
instructions = """Instructions:\nYou will get 1 pt if you click the Square in less than 2 secs\n
Once your score reaches 15\nYou will see bombs and the time to click \n will be reduced to 1.5 seconds, Avoid bombs\n
Or It is game over\n 
\n IF YOU SCORE 60 YOU WIN \n
\nIt is not that simple ;)


"""




canvas.create_text(300,250,text = instructions,font = font,fill = 'orange')
# canvas.create_text(50,100,text = 'Hello Dude',font = font,fill = 'orange')






options = Menu(root)
root.config(menu = options)
options_nav = Menu(options)
help_nav = Menubutton(options)
options.add_cascade(label = "Options",menu = options_nav)
options_nav.add_command(label = "Settings",command = settings)
options_nav.add_command(label ="Exit",command = lambda: quit())
options.add_cascade(label = "Help",menu = help_nav,command = help)











root.mainloop()




