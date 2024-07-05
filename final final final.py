import wikipedia
from PIL import Image

###     getting info from wikipedia       ###

def summary(topic, maxsentences):
    try:
        summary = wikipedia.summary(topic, sentences=15)  
        sentences = summary.split('. ')[:maxsentences]  
        limited_summary = ". ".join(sentences) 
        return limited_summary
    except wikipedia.exceptions.DisambiguationError as e:
        options = e.options[:10]
        print("Sorry, the topic", topic , "is ambiguous. You can choose from following topics:")
        for a in range (0,len(options)):
            print(a,':',options[a])
    except wikipedia.exceptions.PageError:
        print( "Sorry, Couldn't find information on that topic.")

##########################################################################

###   function for storing correct file in filename according to user inputs   #######

f=open("dummy.txt",'r')
default=f.read()

def savefile(filename, text):
    with open(filename, "w") as file:
        if not text:
            file.write(default)
        else:
            file.write(text)

##############################################################################
## user inputs

choice1=input("Do you want to save the image ? (y/n) : ")
choice2=input("Do you want to convert text provided by you in 'usertext.txt' or convert summary from wikipidea? (y/n) : ")
choice3=input("Whose handwriting do you want? (d/a) : ")
if choice2=='n':
    userinput = input("You: ")
    summary = summary(userinput, maxsentences=15)
    print(summary)
    savefile("response.txt", summary)
    filename="response.txt"
else:
    filename="usertext.txt"


#############################################################

###   placing alphabet images using ASCII codes   ###

txt=open(filename, "r")   
text=txt.read().replace("\n","")


BG=Image.open("bg.png") 
sheetwidth=BG.width
gap, ht = 50, 50 #margins
oggap=50 #margins
for i in text:
        if choice3=='a':
            cases = Image.open("myfontankush/{}.png".format(str(ord(i))))
            BG.paste(cases, (gap, ht))
            size = cases.width
            height=cases.height
            gap+=size
        elif choice3=='d':
            cases = Image.open("myfontdivyam/{}.png".format(str(ord(i))))
            BG.paste(cases, (gap, ht))
            size = cases.width
            height=cases.height
            gap+=size

        if sheetwidth < gap or len(i)*115 >(sheetwidth-gap) :  ## making a new line when reaching edge
            gap,ht=oggap,ht+140

##################################################################

###  saving the image   ######
if choice1=="y":
    outfolder = "pics" 
    if choice2=="y":
        outfile="usertext.jpg"
    elif choice2=="n":
        outfile = userinput+".jpg" 
    outpath = f"{outfolder}/{outfile}"
    BG.save(outpath)
    print("Image saved successfully in the specified folder!")
    
BG.show()

