# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#region Character
default bioName = "Biographer"

define ed = Character("Ed") #dynamically change name from Immortal Wizard to Ed
define bio = Character("You")
define boss = Character("Boss")
define umi = Character("Umi")
define yetu = Character("Dr. Olu")
define devil = Character("The Devil")
#endregion

#region Ending Flags

define totalPhds = "7"
define totalDoctorals = "8"
#factstotal

#endregion

#region Points and Counters
default yourFacts = 0 
default nameroute = False
default endearing = False
default secretending = False

#endregion


#region Story Flags

default stareflag = 0

default ed_observation = False
#endregion

#region Resources

#em dash: —

#endregion

#

# The game starts here.

label start:
    jump finaltest


    return

label intro:
    "You are a biographer of the magical, mystical, miraculous, marvelous, mythical, and{cps=*.5}... {w=0.3}mmmm{/cps}{i}spellbinding{/i} people of this world."
    "Even though you fancy yourself rather credentialed, what with the seventeen biographies under your belt,"
    "you are repeatedly upstaged by the charlatans in your field who insist upon filling their \"books\" with falsehoods and lies."
    "If there's anything you despise with every fiber of your being, it's lies, and liars, and also people who tell lies."
    "There's a lot of that in the magical community, and you would rather die than take part."

    "But today is different. Today, you're meeting with one of the most notorious magicians in the magical world."
    "No, not the dusty one... The other one. Your paper is doing a profile on the Immortal Agent of Chaos."
    "It's nearly complete, except for the fact that it's nowhere near finished."
    "You aren't worried, though."
    "Okay, the deadline is this weekend and you're a {i}little{/i} worried."
    "But after a few weeks of phone calls, dead leads, and couple of desperate summoning circles, your boss finally arranged an interview with him."
    "You're finally going to get the truth from the man himself. So there's nothing to worry about!" 
    #lines below this (cut if I run out of time)
    "Of course, you also brought the most factual encyclopedia known to magickind as supplementary material---just in case." 
    "It's the Valkyrie Order's Compendium of Known Agitators---{w=0.2}but you're sure you won't need it." #show the valkyrie reference button  

    jump icebreaker
    return

label icebreaker:
    menu greeting:
        "You decide to greet him..."
        "Cordially":
            bio "Thank you for taking the time to meet with me today."
            "He casually waves you off."
            ed "I didn't have anything better to do."
            bio "Really?"
            ed "Nope. Take as much time as you need. As much time as you need..." 
            "!?" #wink
            "You feel a lot more confident now! But..."
            "It seems unlikely that someone as busy as he is has \"nothing better to do.\" He's not messing with you, or...?"
            
        "Excitedly":
            bio "It's an honor to meet you, sir."
            ed "Really. An honor? \"Sir?\""
            bio "Yes! Actually..." 
            bio "I'm a little starstruck, I have to admit..."
            ed "Huh. I didn't realize I had... following."
            "Your face runs hot and you absentmindedly start fanning yourself."
            "You start to wonder how his lashes are so long... and supple... when it hits you:"
            "He \"didn't realize\" he had a following? How could he not know?"

    "Is he... lying?" # ominous tone

    "You pay it no mind."

    "You clear your throat and shake your head. Now is not the time to get distracted, you have a job to do!" 
    "You might be the first person to ever get the full story out of such a slippery and elusive figure."
    
    menu:
        "Time to lock in!":
            "You said that out loud."
            ed "Hm?"
            menu:
                "Sorry that wasn't meant for you I think":
                    "He doesn't react."
                "Clear your throat":
                    "You clear your throat (again)."
    
    "The magician leans back in his chair and crosses one leg over another, resting his hands on one knee."
    "...Seeing him relax makes you relax, as well."

    jump demography
    return

label demography:
    bio "Let's just start with a basic background..."
    bio "As we both know, you are an immortal warlock, the Agent of Chaos-{w=0.4}"
    ed "You can call me Ed."
    bio "Ed."
    ed "Yes."
    bio "Just{cps=*0.2}...{/cps} Ed?"
    ed "{cps=*0.2}Mm-hm.{/cps}"
    "You are thinking about something already..."
    menu:
        "Is that really your real name?":
            ed "No. Obviously."
            bio "You're joking, right?"
            ed "Madam."
            ed "I think if you stick around you will find that I am a very funny guy."
            ed "But I don't joke about my name."
            bio "Well... what is your real name?"
            ed "We can... save that one for later, can we?" 
            # so you've initiated the impress him route 
            # what with him lowkey flirting with you and all, he'll tell you his real name if you charm him
            # but of course, out of respect, you won't publish it.
            bio "Oh, all right..."
            $ nameroute = True
        "Keep it to yourself":
            "\"Ed\" cannot possibly be his real name. But you're sure he has his reasons..."
    
    "You think about your deadline again and realize you need to cut back on some of your questions."
    bio "I need to cut back on some of these questions."
    "Right, that's... what I said?"
    "See, now he's looking at you funny."
    "Don't bite your lip!"
    "He's reciprocating. Unbelievable."
    "Anyway."
    menu:
        "You figure you don't need to spend so much time on his background, so you ask him about..."
        "His childhood":
            jump upbringing
        "His zodiac sign":
            jump starsign
        "The leather jacket he's wearing right now":
            jump jacket
    
    return


label upbringing:
    $ upbringing = True
    bio "What was your upbringing like?"
    ed "Harrowing."
    bio "Oh."
    menu:
        "I'm so sorry":
            ed "Don't be."
        "I'm not surprised":
            bio "As most warlocks' are, I'm sure."
            "He seems to chuckle at your blase attitude."
            call endeared
            
    
    jump interviewintro
    return

label endeared:
    $ endearing = True
    "You feel like you've endeared yourself to him."
    return

label starsign:
    $ starsign = True
    bio "Would you say your nature as a Virgo started you down the path of dark magic?"
    ed "Hold up. I'm not a Virgo."
    bio "Your entry on the Valkyrie Compendium of Known Agitators has your star sign listed as Virgo."
    ed "Well it's wrong."
    ed "What are you gonna do, argue with me? {w=0.2}It's wrong."
    ed "I wasn't born in freaking September."
    menu:
        "The Valkyrie Compendium is the most factual encyclopedia on magic ever written, so..."
        "Insist he's a Virgo":
            "He acts like one."
            bio "I would rather not contradict the Order of the Valkyries."
            ed "That's fine. But I'm not no damn Virgo."
            jump interviewintro
            pass
        "Ask him his sign":
            
            pass

    bio "When were you born, then?"
    ed "October 9. {w=0.2}Write that down." 
    "You scratched out Virgo and wrote Libra."
    $ yourFacts += 1
    
    bio "Now that that's out of the way- {nw}"
    ed "A September birthday...{w=0.2} \"Virgo.\"{w=0.2} {cps=*0.3}Tchhhhhhhh... {/cps}{w=0.2}A September birthday?"
    ed "I'm sorry, you can continue."
    "He reaches out, as if to put his hands on yours, but your chairs are too far apart. You nod and smile."
    call endeared
    bio "Okay."

    jump interviewintro
    return

label jacket:
    $ jacket = True
    $ stareflag += 1
    bio "Where did you get that sleek, luxurious jacket?"
    ed "Oh, this? It's designer."
    "You stare at him. He stares at you."
    "You stare at him... He stares at you."
    bio "Which... designer?"
    ed "Rick... Owens...?" # annoyed
    "You stare at him some more. He cocks his head."
    "You narrow your eyes..."
    menu firstlie:
        ed "What?"
        "Tell him he's lying":
            ed "Seriously? We just started."
            bio "Right. Sorry."
            jump interviewintro
            # jumps to the main story block
        "Move on":
            "It probably is designer."
    "..."
    "..."
    "He's looking directly at you."
    menu:
        ed "What, you like it or something?"
        "I might":
            ed "You might?"
            ed "Okay, I mess with it." #he's flirting
            call endeared
        "Just curious":
            pass
    
    
    return

label interviewintro:
    bio "Now that that's out of the way, I wanted to get into the big discussion."
    bio "You know, the question I'm sure everyone's always wanted to ask you-"
    ed "What my involvement was with all those divorces in the 1920s?"
    bio "E-excuse me?"
    ed "Oh, you want to know how many Ph.Ds I have." #gesturing like "silly me, I can't believe I didn't think of that first!"
    menu:
        "What? No!":
            bio "I mean, no. Sorry."
            bio "I didn't mean to yell."
            ed "You can yell. If you want to."
            bio "Like... like, at you?"
            ed "At anyone. At me, too. If I'm being a bonehead. You can."
            "His nonchalance was charming before, but now it's starting to throw you off your game." 
            bio "It's time to tap in."
            ed "Okay."
            bio "I mean that's not what I meant to ask you."
            ed "Go on."

        "You have multiple??":
            ed "I might."
            "You stare at him. He stares you."
            "You stare at him... He stares at you."
            if stareflag >= 1:
                "You... are starting to get tired of this."
                $ stareflag +=1
            else:
                pass
            ed "Hey."
            ed "Stop starin' at me with those big old eyes."
            "You try batting your eyelashes with what you think is a coquettish expression."
            "You're not sure if it came off as such or if it was more of a drunken hand-eye coordination exercise. You decide to move on."
    bio "My question---it's fairly straightforward---I want to know just how you became an immortal wizard!"
    ed "Mm."
    bio "It's one of my favorite questions."
    bio "Of all the fine, magically inclined folks I've interviewed, I've always asked the same question, and I've never gotten the same answer!"
    ed "Well, if you wanna hear about that..."
    jump portugal
    return

label portugal:
    "He uncrosses his legs, leaning forward with his elbows now resting on his knees." 
    "You find yourself leaning forward as well, pulled into his vortex, his magnetic field." 
    "You are about to hear A Story."

    return



label interviewconclusion:
    bio "But... I think in all your stories, you've never told me the \"why.\" You've gone on about the how..."
    bio "Why did you do it?"
    ed "Why did I do it?"
    ed "...for love."

    jump finaltest



    return

label sneakdevildeal:
    #criteria for reaching the deal:
    # you've asked him about his name
    # you've flirted with him a lot
    # you've dodged all of his falsehoods
    $ dealtriggered = True
    #stop the music
    ed "Listen here."
    ed "I like you. How come I've never heard of you before?"
    bio "I suppose... it's just by chance. I mean, I've never had a lot of eyes on much of my work."
    ed "But you're clearly good at what you do. You want people to know that about you, right?"
    "That would be nice..."
    ed "Wouldn't it?"
    bio "I... wouldn't have to answer to my good-for-nothing boss."
    ed "Exactly!"
    ed "Look, I'll cut to the chase. I want to help you."

    menu:
        "Accept his help":
            jump accept
        "Reject his help":
            jump reject
        "Ask a question":
            pass

    bio "Oh! Really? I mean, I don't know... help me how?"
    ed "Well... let me put it this way."
    ed "I think that... this profile your paper is doing..."
    ed "I think it's going to make a killing. I think it's gonna make waves."
    ed "How do the kids say it? It's gonna do numbers?"
    bio "Well, what makes you say that?"
    ed "Just by the sheer quality. You're keen. Observant."
    ed "Honest."
    "He's right, you know."
    menu:
        "Accept his help":
            jump accept
        "Reject his help":
            jump reject
        "Ask another question":
            pass
    
    bio "But... why me? There are far more prolific writers doing way worse than I am."
    ed "There are far {i}worse{/i} writers doing much better than you are, too."
    bio "I never said anything about worse writers."
    ed "It's not what you said. It's what you didn't say."
    ed "\"Prolific.\" Not learned, not talented. Prolific." 
    ed "In other words: just talk. They talk too much."
    ed "Not you, though."
    ed "I like you, so I'll help you. Simple as that."

    menu:
        "Accept his help":
            jump accept
        "Reject his help":
            jump reject
        "Ask another question":
            pass

    bio "And what do you get out of helping me?"
    ed "Hm..."
    ed "The satisfaction, I guess. A bit of comfort?"
    "Wow. How selfless..."
    "I don't like the way he's whispering."

    menu:
        "Accept his help":
            jump accept
        "Reject his help":
            jump reject
        "Ask another question":
            pass

    bio "How can I be sure I can trust you?"
    ed "Of course. That's very important. You hate lies. And I've proven I love lying."
    "You laugh idly. But it's not very funny."
    ed "I'll give you my name. My real name."

    bio "And what do I give you?"
    ed "Your word that you will keep it a secret."

    menu:
        "That seems fair":
            jump accept
        "No way, Jose":
            "You don't call him Jose, by the way."
            jump reject
    

    return

label accept:

    "You let out the breath you've been holding."
    bio "Sure! Why not."
    ed "Good! Good. That means I can trust you with this."
    call realname
    bio "So... what do I do now?"
    ed "You lock it in."
    menu:
        "Lock it in with a handshake":
            "You stretched out your right hand for Ed to grab. He gives you a firm hanshake." 
            "You felt your palm tingle."
        "Lock it in with a fistbump":
            "You raised your fist to chest height. He raises his to meet yours. You bump fists."
            "You felt a slight gust wind brush past your face and through your hair."
        "Lock it in with a kiss":
            "You had to stand on the tips of your toes to reach his face."
            "He holds you steady by your waist as you lean into him. You close your eyes and feel his warm lips on yours."
            "...you feel them again."
            "You felt your heart flutter."
    "As you leave the studio, something starts to nag at you from the back of your mind." # his house (the vampire castle)? a cafe? a hotel? wherever
    "He agreed when you said it would be nice..."
    "But you were sure you never said that aloud."
    jump finaltest
    return

label reject:
    $ ed_observation = True
    bio "Sorry. I don't think I can accept your help."
    ed "That's all right... that's all right."
    #the music and background return.
    ed "I hope you remember how many Ph.Ds I have, though. Cuz if you don't, tuh? Well."
    ed "You'll never work in this field again."
    bio "How- how can you be so sure?"
    ed "Oh I'm sure. Of this, I am{w=0.2} {i}very{/i} certain."
    
    jump finaltest

    return

label realname:
    ed "My name is Aniedi Akpan."
    ed "My mother got it from a friend of hers..."
    ed "\"Akpan\" just means \"first-born son.\""
    bio "Wow..."
    bio "What does \"Aniedi\" mean?"
    ed "..."
    ed "\"Who knows?\""
    bio "Ah..."
    return

label finaltest:
    #scene
    if secretending == True:

        "You wander into the office, almost in a trance."
        "You don't even notice your boss calling out for your attention. He seems perplexed as you saunter to your desk."
        call endoftest
        jump dealend
        pass
    elif ed_observation == True:
        "You mull on the last conversation you had before you left."
        pass
    else:
        "Pleased with your findings, you returned to the office with your head held high. You had a brilliant idea for the profile."
        "You could even picture the final line of the article:"
        "Even in a life full of tall tales, he kept a simple truth in his heart."
        pass

    boss "There you are, you silly goosey goo! So what did you find out? Is he really the world's most credentialed man?"
    bio "Well he's... " #fact or falsehood

    #fun lil randomness segment (my specialty) -- it's three random facts you rattle off each time?
    #if statement shows boss's response to each fact
    bio "And he also..."
    #boss response
    
    # if you have the virgo thing she says:
    bio "Did you know he's actually a Libra and not a Virgo?"

    boss "Kid."
    boss "You're tellin' me stuff we already heard!"
    bio "Um... I was under the impression that we hadn't written the profile yet because of the sheer amount of misinformation surrounding the individual."
    boss "No, no, we hadn't written the profile because we were waiting for the new keyboard to come in! Keep up!"
    bio "Well, he sent me off with a tidbit I thought was really beautiful and true."
    boss "Really? Let's hear it."
    bio "He told me he had never forgotten the reason he became immortal." 
    bio "He told me he'd done it for love. And that the one thing he desired most was forgiveness."
    boss "YAWNNNNNNNNNNNNNNNNNNNNN. Boring!"
    bio "I thought it was nice..."
    if dealtriggered == True:
        boss "I thought it was CORNY!"
        bio "I have something else that...happened...if you'd rather hear about that?"

    boss "Nope! {w=0.2}Don't gaf. {w=0.3}SO! {w=0.3}How many Ph.Ds did he earn?"
    bio "um{w=0.1}"
    bio "what?"
    "Your boss sighs."
    boss "{cps=*.8}How many Ph.Ds did he earn?{/cps}"
    bio "Are you serious?"
    boss "Very."
    bio "Well- {nw}"
    boss "Your job depends on it. Just so you know."
    $ finalanswer = renpy.input(prompt="How many Ph.Ds did Ed earn in his lifetime? (Enter numbers only.)", allow="1234567890")
    boss "Okay, don't forget to write that in. I'm counting on you!"
    boss "Don't embarrass the paper!"

    call endoftest

    if finalanswer==totalPhds:
        jump goodend
    else:
        jump badend
    return

label endoftest:
    "You sit down and write the article exactly as you envision it."
    "When you're done, you submit it, and you go home."
    return


label goodend:
    "Some weeks after the profile went live, you got a call from your boss."
    boss "Hey, um."
    boss "I wanted to say congratulations. The article is doing pretty well."
    boss "People are saying some parts aren't true..."
    boss "Which is, y'know, to be expected for a guy with such a history. {w=0.3}Misinformation, like you said."
    boss "I, uh... {w=0.4}{i}embellished{/i}{w=0.4} your article a bit. By the way." 
    boss "Just here and there! To spruce things up a bit, y'know? But I gotcha."
    boss "You know that, right? I'm your boss, I take of ya'!"
    boss "I know how you feel about lying and inaccuracies. How it makes you feel queasy and all that."
    boss "So, to clear your conscience, I went ahead and left your name off the byline."
    boss "Don't worry, you'll get a bonus for the accurate reporting on the Ph.Ds."
    boss "You're welcome!"
    "He hangs up."
    
    "You reached the good ending...?"
    #persistent from reaching the secret ending
    "You realized this was as good an ending as you could get."
    return

label badend:
    "Some weeks after the profile went live, you got a call from your boss."
    boss "Hey, um."
    if finalanswer == totalDoctorals:
        boss "Did you go and count the number of doctoral degrees or the number of Ph.Ds?"
        boss "Cuz I asked for Ph.Ds... and I get that he has an M.D..."
        boss "...but an M.D. isn't a Ph.D."
    boss "So, you're fired. Totally super mega ultra fired. For embarrassing the paper."
    boss "Don't check Glitter."
    "Glitter is Magic Twitter."
    "It also has a significantly higher proportion of gay stans. Vicious gay stans."
    "It's the highest on the Internet, unfortunately for you."
    "When your boss told you not to check Glitter, it's because he knew they were eviscerating you on there."
    "So you log on to check, against your better judgement."
    "As it turns out, a Dr. Yetunde Olu, former colleague and ex-girlfriend of Ed, has revealed {i}exactly{/i} how many Ph.Ds he's earned." 
    "And it's not [finalanswer]."
    "In the end, you, too, were a charlatan. A grifter. A hack. A useful idiot—at {i}best.{/i}" 
    if ed_observation == True:
        "It was just as Ed had predicted."
    "You can never work in this field again."
    "You reached the bad ending."
    return

label dealend:
    "Some weeks after the profile went live, you got a call from your boss."
    boss "Hey, um."
    boss "I want to say I'm sorry."
    "Followed by an unusual pause."
    boss "I'm sorry for doubting you, and-"
    "Another pause. You hear shuffling on the other side of the line." 
    "You're sure you hear your boss say, \"okay\" over and over."
    boss "And I've been withholding tens of thousands of dollars in backpay which I-{w=0.5} which I will deposit in your checking account." 
    boss "Immediately."
    "He hangs up." 
    "You've never heard him so stilted... and so scared...?" 
    "Just one more thing to pile on to the weird couple of weeks you've been having..."
    "You thought back to the conversation you had with Ed, right before you left."
    "It seems like he was right: your article did incredibly well!"
    "But it also seems like no one who read it knows what it actually said." 
    "Everyone who talks to you about it says something wildly inaccurate."
    "And everyone says something different."
    "You've read it over and over every night since it was published. It's exactly as you remember it—"
    "no tall tales,"
    "no editorializing from your boss,"
    "no inexplicable gaps in the narrative."
    "It should be a completely factual profile..."
    "You continue your career as a magical biographer."
    "But you can't shake the queasy feeling you get from telling a lie for as long as you live."

    "You reached the secret ending...!"
    return