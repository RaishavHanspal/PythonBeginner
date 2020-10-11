import cat_talk
talk = "Default"
while talk!="":
    talk = input('What you want the cat to say?')
    if talk!="":
        cat_talk.greeting(talk)
    
