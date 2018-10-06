from turtle import *
from main import *
setup(600,600)
p=Pen()
p.ht()
p.speed(0)

class hole:
    size=25
    pos=[0,0]
    mode='e'
    row=0
    hole_number=0
    colos={'red':'#FF0000',
                'blue':'#0097FF',
                'green':'#0E7A1C',
                'yellow':'#FFF300',
                'white':'#FFFFFF',
                'black':'#000000'
               }
    def __init__(self,row,pos,hn):
        self.row=row
        self.pos=pos
        self.hole_number=hn
        
    
    def mod(self,mo):
        p.pu()
        p.goto(self.pos)
        p.pd()
           
        if mo=='e':
            p.dot(self.size,'#000000')
            self.mode=mo
        elif mo=='s':
            p.dot(self.size,self.colos['black'])
            p.dot(self.size-5,self.colos['white'])
            self.mode=mo
        elif mo=='r':
            p.dot(self.size,self.colos['red'])
            self.mode=mo
        elif mo=='b':
            p.dot(self.size,self.colos['blue'])
            self.mode=mo
        elif mo=='g':
            p.dot(self.size,self.colos['green'])
            self.mode=mo
        elif mo=='y':
            p.dot(self.size,self.colos['yellow'])
            self.mode=mo
        elif mo=='w':
            p.dot(self.size,self.colos['white'])
            self.mode=mo

        return


    
class roww:
    rp=[0,0]
    rn=0
    
    l=[]
    def __init__(self,r,n):                                                                    #r is the rows initial position and n is row number just for reference.
        self.rp=r
        self.rn=n
        
        self.l=[hole(n,[r[0]+x*40,r[1]],x) for x in range(4)]
    def editrow(self,newl):
        for i in range(4):                                                                      #newl is the new row info
            self.l[i].mode=newl[i]
    def pri(self):
       for i in self.l:
            i.mod(i.mode)



answer_table=[roww([-200,200-x*50],x) for x in range(10)]                 #contains the answer plot
reporte_table=[roww([70,200-x*50],x) for x in range(10)]                    #contains the report plot

def prians():                                                                                    #prints the answer_table                                   
    global answer_table                     
    for i in answer_table:
        i.pri()
    p.pu()
    p.goto(0,0)
    p.pd()
    p.dot(30,hole.colos['red'])

def prirep():                                                                                    #print the report table
    global reporte_table
    for i in reporte_table:
        i.pri()


prians()
patt=pattern_generator()
prirep()

r=[]
i=0

def turnSetup():
    global r
    global i
    r=answer_table[i]
    t=Pen()
    t.speed(5)
    t.pu()
    t.width(10)
    t.goto(r.rp[0]-30,r.rp[1]+30)
    t.pd()
    t.forward(180)
    t.right(90)
    t.forward(60)
    t.right(90)
    t.forward(180)
    t.right(90)
    t.forward(60)
    t.pu()  
    
def clickAnalyzer(x,y):
    if -30<x and x<30 and -30<y and y<30:
        submitter()
    elif 270-30<x and x<300 and -30-270<y and y<30-270:
        terminator()
    else:
            for i in r.l:
                if x>i.pos[0]-i.size and x<i.pos[0]+i.size and y>i.pos[1]-i.size and y<i.pos[1]+i.size:
                    if i.mode=='e':
                        i.mod('r')
                        print('r')
                    else:
                        c=['r','g','b','y']
                        print(i.mode)
                        i.mod(c[(c.index(i.mode)+1)%4])

def submitter():
    global i
    report=check_compare([r.l[t].mode for t in range(4)],patt)
    report.sort(reverse=1)
    
    t=Pen()
    
    t.color(hole.colos['white'])
    t.speed(5)
    t.pu()
    t.width(10)


    t.goto(r.rp[0]-30,r.rp[1]+30)
    t.pd()
    t.right(90)
    t.forward(60)
    t.left(90)
    t.forward(180)
    t.left(90)
    t.forward(60)
    t.left(90)
    t.forward(180)
    if report.count('r')==4:
        terminator()
        print("YOU HAVE WON!!!!!!!\nYOU WIN!!!!\nCONGRATULATIONS!!!!!!!!!!!!!!!!!!!!!!!!!")
    for p in range(4):
        reporte_table[i].l[p].mod(report[p])
    i+=1
    if i==10:
        terminator()
        print("YOU RAN OUT OF TRIES!!!!!!!\nYOU ARE A LOSER\n")
        exit()
    
    
    turnSetup()


def terminator():
    bye()

##def input_setup(i):                                                                              #sets row to input mode
##    global answer_table
##    global r
##    r=answer_table[i]
##    
##    for n in r.l:
##        n.size=30
##        n.pos=[n.pos[0]+(n.hole_number-1.5)*10,n.pos[1]]
##        n.mode='s'
##    r.pri()


 
##def take_input(i):
##    global answer_table
##    global r
##    r=answer_table[i]
##    onscreenclick(ho_ident)
    
    
##def ho_ident(x,y):
##    global r
##    print(x,y)
##    if -30<x and x<30 and -30<y and y<30:
##        #####
##        print('submit')
##    else:
##        for i in r.l:
##            if x>i.pos[0]-i.size and x<i.pos[0]+i.size and y>i.pos[1]-i.size and y<i.pos[1]+i.size:
##                if i.mode=='s':
##                    i.mod('r')
##                    print('r')
##                else:
##                    c=['r','g','b','y']
##                    print(i.mode)
##                    i.mod(c[(c.index(i.mode)+1)%4])

##def finish_input(i):
##    global r
##    modes=[i.mode for i in r.l]
##    print(modes)
##    p.goto(r.rp[0]-30,r.rp[1]+30)
##    p.pd()
##    p.forward(200)
##    p.right(90)
##    p.forward(50)
##    p.right(90)
##    p.forward(200)
##    p.right(90)
##    p.forward(50)
##    p.pu()  
##    return modes
##    r.pri()
##input_setup(0)
##take_input(0)
##finish_input(0)


turnSetup()

def clicker():
    onscreenclick(clickAnalyzer,1)

clicker()

print('n',p.speed())
