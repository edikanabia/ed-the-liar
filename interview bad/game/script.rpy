# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#region Character
default bioName = "Biographer"

define ed = Character("ed_dn", image="ed", dynamic=True) #dynamically change name from Immortal Wizard to Ed
define bio = Character("You", image="bio")
define boss = Character("Boss")
define umi = Character("Umi")
define yetu = Character("Dr. Olu")
define devil = Character("The Devil")
define petya = Character("petya_dn", dynamic=True)
#endregion

#region Ending Flags

define totalPhds = "7"
define totalDoctorals = "8"
define factstotal = 8

#endregion

#region Points and Counters
default yourFacts = 0 
default nameroute = False
default endearing = False
default secretending = False

default factscollect = [] #named facts that are picked at random at the end to go over

#endregion


#region Story Flags and Game Mechanics
default affection = 0
default favorlost = False
default e_firsttime = True
default o_firsttime = True

default stareflag = 0
default greeting = ""

default ed_observation = False

default homophobic = False
default homophobicbeliefs = []
default starsign = False
default finesse = False
default vampireevilseen = False

default ed_dn = "The Agent of Chaos"
default petya_dn = "Петя"
default commonality = False

default earlyend = False
#endregion

#region Resources

#em dash: —

#endregion

#region Images
image ed = "../charasprites/ed neutral.png"
image ed angry = "../charasprites/ed annoyed.png"
image ed blush = "../charasprites/ed bashful.png"
image ed lying = "../charasprites/ed lie.png"
image ed fakeout = "../charasprites/ed liefake.png"
image ed thinking = "../charasprites/ed thinking.png"
image ed smug = "../charasprites/ed smug.png"
image ed lookup = "../charasprites/ed sidelook.png"
image ed shock1 = "../charasprites/ed horror.png"
image ed shock2 = "../charasprites/ed horrorside.png"

image side bio = "../charasprites/bio neutral.png"
image side bio angry = "../charasprites/bio doubt.png"
image side bio sad = "../charasprites/bio concern.png"
image side bio blush = "../charasprites/bio flustered.png"
image side bio happy = "../charasprites/bio happy.png"
image side bio shocked = "../charasprites/bio shocked.png"

#Minor Characters
image devil = "../charasprites/devil_normal.png"
image devil glow = "../charasprites/devil_glow.png"
image layla = "../charasprites/layla_the_terrible.png"
image petya = "../charasprites/petya_bloody.png"
image colleague = "../charasprites/colleague.png"
image microwave = "../charasprites/microwave.png"

#BGs
image bg coffeeshop = "/backgrounds/coffeeshop.png"
image bg ship = "/backgrounds/ship.png"
image bg movieset = "/backgrounds/movieset.png"
image bg castle = "/backgrounds/vampire.png"
image bg library = "/backgrounds/library.png"

image bg black = Solid("000")
image bg white = Solid("fff")
#CGs
image cg csection = "/cgs/cg_csection.png"



#endregion

#region Transforms and Screen Variables
transform person_a:
    xalign 0.15
    yalign 1.0

transform person_b:
    xalign 0.3
    yalign 1.0

transform person_c:
    xalign 0.5
    yalign 1.0

transform person_d:
    xalign 0.7
    yalign 1.0

transform person_e:
    xalign 0.82
    yalign 1.0



transform move_to_right:
    linear 0.8 xalign 0.85
    yalign 1.0
    
transform move_to_center:
    linear 0.8 xalign 0.5 
    yalign 1.0

transform move_to_left:
    linear 0.8 xalign 0.1
    yalign 1.0

#endregion

#region Audio
#SFX

#Music


#endregion


# The game starts here.

label start:
    jump intro

    return

label intro:
    # play music officejob
    "You are a biographer of the magical,{w=0.2} mystical,{w=0.2} miraculous,{w=0.2} marvelous,{w=0.2} mythical,{w=0.2} and{cps=*.5}... {w=0.3}mmmm{/cps}{i}spellbinding{/i} people of this world."
    "Even though you fancy yourself rather credentialed,{w=0.2} what with the seventeen biographies under your belt,"
    "you are repeatedly upstaged by the charlatans in your field who insist upon filling their \"books\" with falsehoods and lies."
    "If there's anything you despise with every fiber of your being,{w=0.2} it's lies,{w=0.2} and liars,{w=0.2} and also people who tell lies."
    "There's a lot of that in the magical community, and you find it nauseating."
    "You would rather die than take part!"

    show bg coffeeshop with dissolve
    "But today is different.{w=0.1} Today, you're meeting with one of the most notorious magicians in the magical world."
    "No, not the dusty one...{w=0.1} The other one.{w=0.1} Your paper is doing a profile on the Immortal Agent of Chaos."
    "It's nearly complete,{w=0.1} except for the fact that it's nowhere near finished."
    "You aren't worried,{w=0.1} though."
    "Okay,{w=0.1} the deadline is this weekend and you're a {cps=*0.7}{i}little{/i}{/cps} worried."
    "But after a few weeks of phone calls,{w=0.1} dead-ends,{w=0.1} and couple of desperate summoning circles,{w=0.1} your boss finally arranged an interview with him."
    "You're finally going to get the truth from the man himself.{w=0.1} So there's nothing to worry about!" 

    "Of course,{w=0.1} you also brought the most factual encyclopedia known to magickind as supplementary material{w=0.1}—just in case." 
    "It's the Valkyrie Order's Compendium of Known Agitators."
    show screen bookbutton with dissolve
    "But you're sure you won't need it." #show the valkyrie reference button  

    jump icebreaker
    return

label icebreaker:
    show ed with dissolve
    "He sits in front of you expectantly."
    menu greeting:
        "You decide to greet him..."
        "Cordially":
            $ greeting = "cordial"
            bio happy"Thank you for taking the time to meet with me today."
            "He casually waves you off."
            ed "I didn't have anything better to do."
            bio -happy "Really?"
            ed "Nope.{w=0.1} Take as much time as you need.{w=0.1} As much time as you need..." 
            #play sound wink
            "!?" #wink
            "You feel a lot more confident now!{w=0.1} But..."
            "It seems unlikely that someone as busy as he is has \"nothing better to do.\"{w=0.1} He's not messing with you,{w=0.1} {cps=*0.5}or...?{/cps}"
            
        "Excitedly":
            $ greeting = "excited"
            bio "It's an honor to meet you,{w=0.1} sir."
            ed "Really.{w=0.1} An honor?{w=0.3} \"Sir?\""
            bio "Yes!{w=0.1} Actually..." 
            bio "I'm a little starstruck,{w=0.1} I have to admit..."
            ed "Huh.{w=0.1} I didn't realize I had a... {w=0.3}following."
            "Your face runs hot and you absentmindedly start fanning yourself."
            "You start to wonder how his lashes are so long...{w=0.1} and supple...{w=0.1} when it hits you:"
            "He \"didn't realize\" he had a following?{w=0.1} How could he not know?"

    "Is he...{nw=0.1}" 
    #play sound ominous
    extend "lying?"

    "You pay it no mind."

    "You clear your throat and shake your head.{w=0.1} Now is not the time to get distracted.{w=0.1} You have a job to do!" 
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
    
    "The magician leans back in his chair and crosses one leg over another,{w=0.1} resting his hands on one knee."
    "...Seeing him relax makes you relax,{w=0.1} as well."

    jump demography
    return

label demography:
    bio "Let's just start with a basic background..."
    bio "As we both know,{w=0.1} you are an immortal warlock,{w=0.1} the Agent of Chaos-{nw=0.1}"
    ed "You can call me Ed."
    $ ed_dn = "Ed"
    bio "Ed."
    ed "Yes."
    bio "Just{cps=*0.5}...{/cps} Ed?"
    ed "{cps=*0.5}Mm-hm.{/cps}"
    "You are thinking about something already..."
    menu:
        "Is that really your real name?":
            $ renpy.block_rollback()
            ed "No. {w=0.1}Obviously."
            bio "You're joking,{w=0.1} right?"
            ed lookup "Madam."
            ed thinking "I think if you stick around you will find that I am a very funny guy..."
            ed lookup "But I don't joke about my name."
            bio "Well...{w=0.1} what is your real name?"
            ed -lookup "We can...{nw=0.3}" 
            #play sound wink
            show ed smug
            extend "save that one for later, can we?" 
            # so you've initiated the impress him route 
            # what with him lowkey flirting with you and all, he'll tell you his real name if you charm him
            # but of course, out of respect, you won't publish it.
            bio "Oh,{w=0.1} all right..."
            show ed -smug
            $ nameroute = True
        "Keep it to yourself":
            $ renpy.block_rollback()
            "\"Ed\" cannot possibly be his real name.{w=0.1} But you're sure he has his reasons..."
    
    "You think about your deadline again and realize you need to cut back on some of your questions."
    bio "I need to cut back on some of these questions."
    "Right,{w=0.1} that's...{w=0.1} what I said?"
    "See,{w=0.1} now he's looking at you funny."
    "Don't bite your lip!"
    "He's reciprocating.{w=0.1} {cps=*0.5}Unbelievable.{/cps}"
    "Anyway."
    menu:
        "You figure you don't need to spend so much time on his background,{w=0.1} so you ask him about..."
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
    ed thinking "Harrowing."
    bio "Oh..."
    menu:
        "I'm so sorry":
            
            ed smug "Don't be.{w=0.1} I'm evil."
            "You furrow your brow in concern,{w=0.1} or is it fear?"
            "You're not sure why it would be either because you already knew he was a warlock."
            ed -smug "That was supposed to be a joke."
            bio shocked "Oh."
            bio "Well."
        "I'm not surprised":
            
            "He chuckles at your blasé response."
            bio "At our paper,{w=0.1} we call warlocks with good childhoods priests."
            "He snorts,{w=0.1} then covers his mouth to keep the giggles at bay."
            ed "I mean,{w=0.1} it's true.{w=0.1} And they certainly aren't immortal."
            call endeared
    $ renpy.fix_rollback()
    jump interviewintro
    return

label endeared:
    $ affection += 1
    if e_firsttime == True and affection >=1:
        "..."
        "You feel like you've endeared yourself to him."
        $ e_firsttime = False

    elif favorlost == True and affection >= 1:
        "..."
        "You feel like you've regained his favor."
        $ favorlost = False
    
    else:
        pass
    

    return

label offended:
    $ affection -= 1
    if affection <= 0:
        $ endearing = False
        $ affection = 0
    
    if affection <= 0 and e_firsttime == False:
        "You've definitely lost your favor with him."
        $ endearing = False
        $ favorlost = True
        
    elif o_firsttime == True:
        "..."
        "He seems offended."
        if affection > 0:
            "Let's try to avoid that."
    elif affection == 1:
        "He's starting to get testy.{w=0.1} Try not to offend him again..."
        
    else:
        pass
    return

label takenote(factoid, factuality):
    menu:
        "You consider noting that [factoid]."
        "Jot that down":
            if factuality==True:
                $ yourFacts += 1
                
            else:
                pass
            pass
        "Leave it be":
            pass
    $ factscollect.append(factoid)
    return

label selecttrue(truth, lie):
    menu:
        "You decide to write down..."
        "[truth]":
            $ yourFacts +=1
            $ factscollect.append(truth)
        "[lie]":
            $ factscollect.append(lie)
            pass
    return

label starsign:
    bio "Would you say your nature as a Virgo started you down the path of dark magic?"
    ed "Hold up.{w=0.1} I'm not a Virgo."
    bio "Your entry on the Valkyrie Compendium of Known Agitators has your star sign listed as Virgo."
    ed "Well it's wrong."
    ed "What are you gonna do,{w=0.1} argue with me? {w=0.1}It's wrong."
    ed "I wasn't born in freaking September."
    menu:
        "The Valkyrie Compendium is the most factual encyclopedia on magic ever written,{w=0.1} so..."
        "Insist he's a Virgo":
            "He acts like one, anyhow."
            bio "I would rather not contradict the Order of the Valkyries."
            ed "That's fine.{w=0.1} But I'm not no damn Virgo."
            jump interviewintro
        "Ask him his sign":
            pass

    bio "When were you born,{w=0.1} then?"
    ed "October 9. {w=0.2}Write that down." 
    "You scratched out Virgo and wrote Libra."
    $ starsign = True
    
    bio "Now that that's out of the way- {nw}"
    ed "A September birthday...{w=0.2} \"Virgo.\"{w=0.2} {cps=*0.3}Tchhhhhhhh... {/cps}{w=0.2}A September birthday?"
    ed "I'm sorry,{w=0.1} you can continue."
    "He reaches out,{w=0.1} as if to put his hand on yours,{w=0.1} but your chairs are too far apart.{w=0.1} You nod and smile."
    call endeared
    bio "Okay."

    jump interviewintro
    return

label jacket:
    $ jacket = True
    $ stareflag += 1
    bio "Where did you get that sleek,{w=0.1} luxurious jacket?"
    ed "Oh,{w=0.1} this?{w=0.1} It's designer."
    "You stare at him.{w=0.1} He stares at you."
    "You stare at him...{w=0.1} He stares at you."
    bio "Which...{w=0.1} designer?"
    ed "Rick...{w=0.1} Owens...?" # annoyed
    "You stare at him some more.{w=0.1} He cocks his head."
    "You narrow your eyes..."
    menu firstlie:
        ed "What?"
        "Tell him he's lying":
            ed "Seriously?{w=0.1} We just started."
            bio "Right.{w=0.1} Sorry."
            jump interviewintro
            # jumps to the main story block
        "Move on":
            "It probably is designer."
    "You look back down at your notes and shake your head."
    bio "Nothing.{w=0.1} Nevermind."
    "..."
    "He's looking directly at you."
    menu:
        ed "What,{w=0.1} you like it or something?"
        "I might":
            ed "You might?"
            ed "Okay,{w=0.1} I mess with it." #he's flirting
            call endeared
        "Just curious":
            ed "Ooookay."
    jump interviewintro
    return

label interviewintro:
    "You let out a breath."
    bio "Well."
    bio "Now that that's out of the way,{w=0.1} I wanted to get into the big discussion."
    bio "You know,{w=0.1} the question I'm sure everyone's always wanted to ask you-{nw=0.1}"
    ed "What my involvement was with all those divorces in the 1920s?"
    bio "E-excuse me?{nw=0.1}"
    ed "Oh,{w=0.1} you want to know how many Ph.Ds I have." #"silly me, I can't believe I didn't think of that first!"
    menu:
        "What? No!":
            bio "I mean,{w=0.1} no.{w=0.1} Sorry."
            bio "I didn't mean to yell."
            ed "You can yell.{w=0.1} If you want to."
            bio "Like...{w=0.1} like,{w=0.1} at you?"
            ed "At anyone.{w=0.1} At me,{w=0.1} too.{w=0.1} If I'm being a bonehead.{w=0.1} You can."
            "His nonchalance was charming before,{w=0.1} but now it's starting to throw you off your game." 
            bio "It's time to tap in."
            ed "Okay."
            bio "I mean,{w=0.1} that's not what I meant to ask you."
            ed "Go on."

        "You have multiple??":
            ed "I might."
            "You stare at him.{w=0.1} He stares you."
            "You stare at him...{w=0.3} He stares at you."
            if stareflag >= 1:
                "You...{w=0.3} are starting to get tired of this."
                $ stareflag +=1
            else:
                pass
            ed "Hey."
            ed "Stop starin' at me with those big old eyes."
            "You try batting your eyelashes with what you think is a coquettish expression."
            "You're not sure if it came off as such or if it was more of a drunken hand-eye coordination exercise." 
            "You decide to move on."
    bio "My question{w=0.1}—it's fairly straightforward{w=0.1}—I want to know just how you became an immortal wizard!"
    ed "Mm."
    bio "It's one of my favorite questions."
    bio "Of all the fine,{w=0.1} magically-inclined folks I've interviewed,{w=0.1} I've always asked the same question,{w=0.1} but I've never gotten the same answer!"
    ed "Well, if you wanna hear about that..."
    # stop music with fadeout 1.0
    "He uncrosses his legs,{w=0.1} leaning forward with his elbows now resting on his knees." 
    "You find yourself leaning forward as well,{w=0.1} pulled into his vortex,{w=0.1} his magnetic field." 
    "You are about to hear A Story."
    jump portugal
    return

label portugal:
    show ed at move_to_left
    show bg ship with dissolve
    #queue music ed
    ed "I had just gotten my first Ph.D{w=0.1}—theology.{w=0.1} I wasn't religious,{w=0.1}but there weren't many options back in those days."
    bio "Which days?"
    menu:
        ed "It was when I turned thirty in 1430.{w=0.1} Pretty easy to remember,{w=0.1} right?"
        "I suppose so":
            pass
        "You're how old, again?":
            ed "Thirty."
            bio "Right.{w=0.1} Of course."
            bio "And just how {i}long{/i} have you been thirty,{w=0.1} hm?"
            ed "{cps=*0.8}Since...{w=0.1} {w=0.1}14...{w=0.1}30.{/cps}"
            bio "Oh.{w=0.1} Oh yeah."
            bio "Carry on."

    $ renpy.fix_rollback()
    ed "My girlfriend at the time wanted to try out some different waters,{w=0.1} and especially different fish." 
    ed "So with my studies finished,{w=0.1} we figured it would be the perfect time to try somewhere new,{w=0.1} and we swam up to Portugal."
    bio "That sounds so romantic!"
    bio "Wait...{w=0.1} what do you mean you {i}swam{/i} to Portugal?"
    ed "Well, you see,{w=0.1} swimming is when you place your legs in the water and-{nw}"
    bio "I know what swimming is."
    ed "You do?{w=0.1} So why did you ask?"
    if stareflag >= 1:
        "You don't want to enter another staring contest with him,{w=0.1} so you carefully consider how you're going to phrase this."
        pass
    else:
        "You carefully consider how you're going to phrase this."
        pass
    "Magical types can be such volatile personalities,{w=0.1} and if you happen to offend the most important interview of your career,{w=0.1} you're boned."
    "You CANNOT under any circumstances imply he is insane for alleging that he swam to Portugal from literally anywhere."

    menu:
        "Isn't that... kind of far?":
            ed "I mean...{w=0.1} It's a coastal nation with pretty easy access to the sea."
            bio "That's not what I meant."
            ed "Then what did you mean?"
            bio "That's...{w=0.1} well...{w=0.1} you swam by yourself?"
            ed "{w=0.1}...Did I not say I was with my girlfriend?"
            bio "You {i}and{/i} your girlfriend swam??"
            ed "Well yeah it's not like she could walk."

        "You're insane for alleging that you swam to Portugal from anywhere.":
            ed "Lawyer says what?"
            bio "What?"
            ed "Heh.{w=0.1} Gottem."
            "Sigh.{w=0.1} He freaking got you."
    $ renpy.fix_rollback()

    ed "So are we clear on how I got to the Kingdom of Portugal or are we still working out the mechanics of swimming?"
    bio "I'm done.{w=0.1} Let's get back on track."
    "You're not done."
    bio "It's just,{w=0.1} I'm a bit confused."
    ed "By what?{w=0.1} My ex-girlfriend and I swam to Portugal." 
    ed "She's a mermaid,{w=0.1} so it wasn't particularly difficult."
    menu:
        "Ohhhh. She's a mermaid!":
            ed "Exactly."
            
        "You do not have a mermaid girlfriend":
            ed "Correct.{w=0.1} I {i}had{/i} a mermaid girlfriend.{w=0.1} There's a difference."
            ed "Who would lie about having a mermaid ex?"
            bio "Many a fisherman have lied about mermaids."
            ed "No fisherman this century would lie about having a mermaid girlfriend,{w=0.1} let alone a mermaid {i}ex.{/i}"
            ed "These days that's just plain embarrassing."
            bio "Point taken."
    $ renpy.fix_rollback()

    ed "Once we landed,{w=0.1} we split up." 
    ed "I wasn't in the market to fish shop,{w=0.1} and besides,{w=0.1} I had heard that if you aren't at least a {cps=*0.7}little{/cps} bit bisexual in Lisbon,{w=0.1} 
    they straight up kill you."
    menu:
        "In the 1400s...?":
            $ homophobic = True
            ed "Oh.{w=0.1} I see.{w=0.1}" 
            ed "You think being bisexual wasn't invented yet."
            bio "No,{w=0.2} I don't-{w=0.2} I wasn't-{w=0.2} I mean-{w=0.2}"
            $ renpy.notify("Trait earned: homophobic!")
            ed "Wowwwwww."
            $ homophobicbeliefs.append("bisexuals existed before David Bowie")
            "He shakes his head disapprovingly." #shit eating grin. fucking hater
        "Oh!":
            bio "You're bisexual!"
            ed "Is it a surprise?"
            bio "I thought you were just...{w=0.1} a really sensitive guy."
            ed "I can be both."
            ed "After all, I'm bi, aren't I...?"
            call endeared
            call takenote("Ed is bisexual", True)
    
    bio "So you're wandering the streets of Lisbon,{w=0.1} waiting for your mermaid girlfriend to get fish." 
    bio "And you come across some kind of powerful being,{w=0.1} right?{w=0.1} Another warlock,{w=0.1} or maybe an old alchemy book?"
    ed "Not quite..."

    show devil at person_d with dissolve

    devil "I'm the Devil."
    ed "Now me,{w=0.1} I'm an industrious guy.{w=0.1}" 
    ed "I see The Devil and I think,{w=0.3} \"how can I profit off of such a one in a lifetime chance encounter?\""
    ed "There was this new economic system emerging called \"capitalism\" and I was dying to test it out."
    devil "I love taking advantage of emerging economic systems!"
    bio "But didn't capitalism emerge in the 16th century?"
    ed "Oh,{w=0.1} you're gonna argue with the guy who was there?{w=0.1} Is that it?"

    menu:
        "Remind him of the year":
            $ finesse = True
            bio "It was 1430."
            ed "And I was about to be rolling in it the way I finessed the #!*% outta that devil."
            ed "You're gonna love this.{w=0.1} I promise."
            "You make a note to yourself to edit that out of the transcript."
            
            
        "Ask him about the year":
            bio "What year was it again?"
            ed "Like,{w=0.1} 1420-something.{w=0.1} Why?"
            bio "Just checking."
            call selecttrue("Ed turned 30 in the 1420s", "Ed turned 30 in 1430")
            
        "Let him have it":
            "You mutter something under your breath about historical revisionism."

    ed "So I see The Devil standing there on the street curb,{w=0.1} and I know it's him because he's got these eyes like a husky." 
    ed "Piercing doesn't even begin to describe it{w=0.1}—they were glowing!"
    show devil glow
    ed "So I see him standing there with his freaky{w=0.1}and I mean STRANGE bright blue glowing eyes and I say,"

    ed "\"How about we make a deal...{w=0.1} a business deal.\"" 
    ed "Also I had the slickest braids on at the time where are my braids. You gotta include the braids."
    bio "Please continue."
    ed "Right,{w=0.1} so he's like,"
    devil "I'm glad you noticed my eyes,{w=0.1} they don't call me Big Dog for nothing bark bark am I right."
    bio "I don't think he said that...{w=0.1} no one would respect a man called Big Dog."
    ed "How do you know the Devil wasn't a woman,{w=0.1} by the way?"
    menu:
        "Because you said \"he\" earlier.":
            ed "Women can't be he/hims?"
            if homophobic == True:
                "You don't even bother this time and just let him have it."
            else:
                bio "No, I- {w=0.1}"
                ed "No? They {i}can't{/i}!?"
                bio "They can, I just- {w=0.3}"
                ed "You don't believe in gender-nonconforming women."
                $ renpy.notify("Trait earned: homophobic!")
                ed "Wowwwwwwww."
                "You stop sputtering and compose yourself."
                bio "I'm asserting myself as the interviewer and taking back control.{w=0.1} Please continue."
            $ homophobicbeliefs.append("women can use he/him pronouns")
        "Because men are the devil and you're the misogynist if you disagree.":
            ed "Hm."
            "He shut up real quick."
            "You can't believe that worked."
    
    ed "So one long series of contracts and spells later,{w=0.1} I made a deal with the devil.{w=0.1} I got to be thirty{w=0.1}—forever!"
    bio "What did he get?"
    ed "One of my Ph.Ds{w=0.1}—the one in fisherman's science." 
    ed "I worked really hard on it, but education comes and goes when you never age."
    ed "What's wrong?{w=0.1} You look disappointed."
    bio "I have to admit that was a bit anticlimactic."
    ed "I never claimed it was climactic.{w=0.1} That was all you." 
    bio "Some of the stories about you claim to be climactic.{w=0.1} There's about one or two for every year you've been alive."
    ed "Oh yeah?{w=0.1} You know they're all fake,{w=0.1} right?"
    
    menu exploits:
        "What about the time you stopped what would have been \"the next Pompeii?\"":
            ed "How could I do that?"
            ed "I don't speak Italian." #lying
        "What about the one where you had two religions founded after you?":
            ed "Both were started by ex-boyfriends.{w=0.1} I guess I just inspire that in people."
            if endearing:
                ed "Want to make the third?"
                bio "Ah,{w=0.1} well,{w=0.1} I.{w=0.1} Have.{w=0.1} To be professional,{w=0.1} you know!{w=0.1} I can't answer that on the clock."
                "He leans in."
                ed "How about off the record?"
                "Your face is getting hot again...." 
                "No.....{w=0.1} his sweet tambour...{w=0.1}" 
                "You must focus....."
        "What about the time you trapped an entire town in an endless fog?":
            ed "Really?{w=0.1} {i}That{/i} story?"
            ed "What are you,{w=0.1} an authoritarian?"
            bio "You just admitted to being a capitalist."
            ed "Game recognizes game."
            "Touché."
            bio "Not touché!{w=0.1} I'm not an authoritarian!"
            ed "Then don't quote authoritarians at me.{w=0.1} That tale is Valkyrie slander."
            call offended

    "You tap your notepad with your pen. It was...{w=0.1} a lot."
    "But the specifics of the deal itself seem to be a bit thin."
    "You wonder if you could get him to elaborate on this later..."
    
    ed "Do you need a moment to take that all in?"
    ed "Because there's more."

    "To get a clearer picture of your subject, you decide to let him continue."

    jump renaissance
    return

label renaissance:
    #scene

    ed "When you become immortal,{w=0.1} kicking around eating fish and talking to Portuguese mermaids starts to get real old after a while,{w=0.1} and my girlfriend could tell. "
    ed "She suggested we could swim down south,{w=0.1} stop by Rafat or Algiers on our way to Palermo..."
    ed "You know, make a vacation of it."
    bio "Aww, how sweet!"
    ed "Plus The Devil kept stopping me in the street asking when our business investments were going to pay off, and I just couldn't be bothered with all that anymore."
    devil "Capital dividends stock marketing economics investiture let's circle on back stakeholders sunk cost corporate consultant-{nw=0.3}"
    ed "Listen,{w=0.1} Mr. The Devil?"
    devil "Yes?"
    ed "I just feel like we need to rethink our strategy."
    devil "How do you mean?"
    ed "Some of these projections,{w=0.1} they're just not synergistic."
    devil "Not synergistic? ¡Dios mío!"
    "Dios mío, you say."
    menu:
        "Interrupt":
            bio "He said dios mío?"
            ed "Yeah."
            menu:
                "But he's Portuguese?":
                    ed "Okay, he was like, \"Meu Deus.\""
                "But he's the Devil?":
                    ed "Okay he was like... \"Diablo mío???\""
            pass
        "Do not":
            "Eh. He's paraphrasing."

    ed "Anyway I was like."
    ed "\"We gotta do some corporate restructuring,{w=0.1}\" and stuff.{w=0.1} \"So you just sit tight...{w=0.1}maybe do some networking???\""
    bio "Eugh."
    "Even hearing corpo speak like that is making your mouth sticky."
    ed "He nodded along like a dog-{nw=0.2}"
    bio "Right, like a husky."
    ed "And after he ran off I sold our assets and liquidated the company."
    if finesse:
        "You let out an \"ooooh\" under your breath."
        ed "Right? I told you you'd love it."
    
    menu:
        "Compliment":
            bio "You must have made a lot of cash from that."
            ed "I made a lot of {i}gold...!{/i}"
            pass
        "Move on":
            pass

    call selecttrue("Ed dabbled in mercantilism", "Ed dabbled in capitalism")

    if jacket:
        "That must be how he can afford designer clothes..."

    ed "So! I hop in my boat and we set sail. Eventually, I get to Sicily."
    bio "Just you, or you and your girlfriend?"

    ed "Uh...{w=0.2} just me."

    bio "What happened?"

    ed thinking "We got separated."
    menu:
        "You mean she dumped you?":
            ed "No.{w=0.1} We got physically separated."
        "You mean you left her for another mermaid?":
            ed angry "{w=0.1}...Who do you think I am?"
            call offended
        "Separated how?":
            ed "We got into a really bad shipwreck."
            ed "It was...{w=0.1} ugly."
            bio "But you managed to survive,{w=0.1} right?"
            "He scoffs."
            ed "Evidently."
    ed "Anyway."
    ed "Once I arrived in Sicily, everything changed." 
    ed "I couldn't find my girlfriend,the Italian mermaids wouldn't talk to me, my ship was destroyed..." 
    ed "I was alone and effectively homeless."

    $ mermaidmafia = False
    menu:
        "That's terrible!":
            pass
        "Why wouldn't the Italian mermaids talk to you?":
            $ mermaidmafia = True
            ed "The mafia."
            bio "Really?"
            ed "Those women are stone cold."
            "He stares past you,{w=0.1} into the distance."
            "But...{w=0.1} there was only wall behind you."

    ed "Once I managed to calm down and take a better look at my situation, I took the money I had liberated from The Devil."
    ed "I knew I needed to reinvent myself, so I decided I would do what I do best:"
    menu:
        "Seduce beautiful women":
            ed "Now I don't like your use of the word \"seduce,\" but I'm flattered you think I'm good at it."
            ed "But not quite."
            pass
        "Usurp the powers of other mages":
            ed "FOR THE RECORD, there exists no evidence of me ever having done that."
            ed "Even your book suspiciously leaves it off because they know that it's a rumor."
            bio "You seem to know a lot about what's in my book. Have you read it?"
            "...He doesn't seem to want to keep talking about it."
            call offended
        "Clout chase":
            ed "That's right."
            pass
    ed "I needed to get an education."
    ed "See, there was some sickness going around Europe at the time—something to do with rats?"
    ed "Others called it a plague."
    bio "Some would even call it... the Bubonic Plague?{nw=0.1}"
    ed "Eh! Maybe. {i}I{/i} called it{w=0.2} an opportunity."
    ed "Soon enough I had that MD under my belt. But while my academic life flourished, my romantic life flatlined."

    menu:
        "I had no idea you were such a romantic...!":
            "When he looks up to make eye contact with you, you don't catch a whiff of humor or wit or perhaps even whimsy."
            "He looks depressed."
        "Say nothing":
            pass

    ed "With the mermaid mafia having ruined any of my attempts to fraternize with both the mermaids and mermen, and the townspeople not wanting to hang around somebody who just treated their neighbor for the plague, 
    I headed up to the big city where all the magic was happening:" 
    ed "Florence."

    ed "The thing they don't tell you about Florence is that absolutely nobody GAF about doctors in that city."
    ed "I walked right in and those people were partying it UP, music, art, messy lesbian drama out on the streets."
    ed "Let me give you an example." 
    ed "I meet this one guy. And his wife was going through labor, but the baby wouldn't come out, right?"
    ed "So I offered to perform a C-section on her, and he was all like,"
    show cg csection with dissolve
    "Boyfriend" "What's that,{w=0.1} that's stupid."
    "Boyfriend" "What do you mean you cut the baby out of the womb."
    "Boyfriend" "Hell no."
    ed "I'm like,{w=0.1} \"But this could be the baby that kills Macbeth.{w=0.1} {i}Trust{/i} me.\"{nw=0.2}"
    ed "And he was like,{nw=0.2}"
    "Boyfriend" "Nooooo hahaha nooooo no one can kill Macbeth!"
    ed "Anyway she died of sepsis."
    hide cg with dissolve
    bio "How is-{nw}"
    ed "And I thought to myself,{w=0.1} wow.{w=0.1} These guys have nothing on the Ottomans."
    ed "Whatever the people thought the plague was, they were convinced it wasn't in Florence." 
    ed "It was The Decameron in there."

    menu:
        "Move on":
            pass
        "The whole point of the Decameron was that they {i}left{/i} Florence.":
            ed "Hm. You say this, and yet you did not meet and talk with Giovanni Boccaccio."
            menu:
                "You met and talked with Giovanni Boccaccio!?":
                    ed "No. I did not."
                "Who???":
                    ed "Exactly."
    
    ed "Sure, I could have opened my own practice, or even found a clinic to work for, but I was lonely, and enough time had passed." 
    ed "I was ready to be desirable again."
    ed "As I said before, doctors were out. What was in was inventing. So naturally I knew I needed to invent." 
    ed "I decided to take my studies to the engineering school, where I earned my next Ph.D."
    ed "It was a lot of hard work, sleepless nights...! And the mathematics and the prototypes...{nw=0.1}"
    "You cannot let him get distracted by his postgraduate studies, so you decide to prompt him a bit."
    bio "Well, surely the access to engineering gave you social clout, right? How did that work out for you?"
    ed "Oh, very well. People had the expectation when you met that you would eventually start inventing for them." 
    ed "And who am I if not someone who delivers?"
    bio happy "I don't know. You tell me!"

    ed "Well!"
    ed "First I caught the attention of a tailor Lenù. We had fun together."
    ed "She often complained about the knives tailors used because they snagged the fabric and I thought: \"what if I combined two knives together?\""
    ed "And the scissors were born."

    bio "I thought Da Vinci invented those?"
    ed "Leonardo owed me money, so I let him have the patent." 
    call takenote("scissors were invented by the Dark Mage Ed", False)

    bio "What did your tailor girlfriend think of the scissors?"
    ed "Oh, she {i}loved{/i} them; her work flowed so much faster, she was the pride of tailors everywhere. But..." 
    ed "The problem with dating in Florence is that once you make the invention they've been waiting for, the relationship is pretty much over."
    bio sad "What? That's so sad..."
    ed "That's just the way it was."
    ed "From Lenù, I had a lot of contacts in the textile industry. Once they saw my scissors, they were practically jumping on top of me to get their own invention."
    ed "I eventually wound up dating Lila, who owned a fabric workshop." 
    ed "She was sweet, and her dream was to make cloth of intricate patterns that could rival even the paintings of the city." 
    ed "After thinking long and hard about it, I invented a loom that could weave any image into cloth."
    ed "Got that one from Anansi at a trickster convention. Funny guy, but you do {i}not{/i} want to get into a drinking competition with him."
    ed "In a way, you could say I brought the gift of weaving to mankind."
    bio "Where have I heard that before...?"

    call takenote("Ed invented the modern power loom", False)

    label microwaver:
        ed "Now, my greatest invention was not made for love or to impress someone." 
    ed "My greatest invention was made for self-satisfaction." 
    ed "I wanted to see if I could even do it."
    ed "A box that could heat anything inside it using electromagnetic radiation."
    bio "The microwave?"
    ed "The one and only."
    $ microwaveseen = False
    menu:
        "That's so cool":
            pass
        "Don't buy it for a second":
            if not endearing:
                ed "That's fine. You don't have to."
                jump aftermicrowave
            ed "Behold my most prized possession."
            show microwave:
                xalign 0.8
                yalign 0.5
            #play sound thunk
            bio shocked "..."
            bio "You're kidding."
            "You reluctantly credit Ed with the invention of the microwave."
            $ microwaveseen = True
            hide microwave

    $ yourFacts += 1
    $ factscollect.append("Ed invented the microwave just because he could")

    label aftermicrowave:
        ed "It took a lot of trial and error, but I'd made a working prototype." 
    ed "I was ready to show it off to the world when disaster struck."
    menu disaster:
        "Fire?":
            pass
        "Volcano?":
            pass
        "Political instability?":
            pass

    ed "No... the mermaid mafia."
    $ issueraised = False
    menu:
        "Interrupt":
            $ issueraised = True
            bio "How did the mermaid mafia get-{nw}"
            ed "Hold on, hold on, I'm explaining."
        "Do not":
            pass    
    
    label afterdisaster:
        ed "They were jealous of my inventions, of the good I was bringing to humanity."
    ed "So one night they snuck into my house and raided of all my inventions... my beautiful inventions..."
    ed "This was worse than the Library of Alexandria getting burned... they stole my prototypes and threw them in the sea."
    
    if not issueraised:
        menu:
            "Interrupt":
                $ issueraised = True
                bio "But there's no-{nw}"
                ed "Hey, hey, hey, I'm having a moment here."
            "Not yet":
                pass

    ed "If that wasn't enough, they also pulled out their grubby little claws and ripped everything to shreds." 
    ed "Except for the bottles of nail polish, which I also invented by the way. They kept those for themselves."

    if microwaveseen:
        bio "If they tore apart everything, how did you manage to rescue the microwave?"
        ed "At the time, I was workshopping a new magic... They call it void-hopping now, but I mainly used it for storage."
        ed "This is how I've been able to keep my lifeforce safe from fatal accidents, but it's also where I kept my microwave."
        ed blush "His name is Michael."
        ed -blush "Unfortunately, at the time, my void dimension was only big enough to fit a few things."
        ed thinking "I couldn't rescue the other inventions."
        "Seems awfully convenient."
        "But the proof is in the microwave."

    ed "I was furious, but what was I supposed to do?" 
    ed "I couldn't drag them out of the water, and I knew if I fell in, they'd tear me apart like they did the prototypes..."

    if not issueraised:
        menu:
            "Interrupt":
                $ issueraised = True
                bio "I just don't know if-{nw}"
                ed "Hang on, I gotta finish this thought."
            "Keep holding it in":
                pass

    ed "I started chucking rocks into the ocean, hoping to hit some of them." 
    ed "I was yelling at the beach, grabbing whatever stones I could find and launching them at the mermaids."

    if not issueraised:
        menu:
            "Interrupt":
                $ issueraised = True
                bio "But there's no-{nw}"
                ed "Wait wait wait, I'm almost done."
            "Just a little longer":
                pass

    ed "The city guard didn't like that. I was causing a public disturbance, and the mermaids were lining their pockets anyway." 
    ed "Corruption everywhere... mermaids at my back... my exes had no use for me..." 
    ed "It was time to get the hell out of Italy."
    ed "There. I'm done."
    
    if not issueraised:
        ed "...Are you all right?"
        ed "You look like you have a burning question."
        menu:
            "Just one small problem":
                $ issueraised = True
                bio "Florence is landlocked."
                ed "..."
                bio "They couldn't throw your inventions into the sea."
                bio "Because there was no sea."
                ed "It was..." 
                ed "It was a river."
                ed lookup "I swear it happened.{nw=0.1}"
                ed -lookup "It happened, I swear.{nw=0.1}"
                ed lookup "I tell a lot of tall tales, but that was real!{nw=0.1}"
                ed fakeout "It was real, I promise!{nw=0.1}"
                ed angry "I just got it mixed up!{nw=0.1}"
                ed lookup "I can't help it, I'm old!{nw=0.1}"
                ed thinking "I'm sorry!{w=0.1} I'm sorry.{nw=0.5}"
                bio "It's no big d{nw}"
                ed -thinking "I'm sorry."
                bio "It's no big deal."
    
            "Not at all":
                pass
    # hide the florence bg

    ed "Do you want me to keep going? I could talk about something else."
    "You're starting to get a feel for the kind of person Ed is." 
    "Scrappy, resourceful, and in constant pursuit of knowledge."
    "And a bit of a flirt."

    bio "Go ahead."

    jump vampirecastle
    return

label vampirecastle:
    ed "I moved around Europe for a while, kept up to date with my medical knowledge in areas that cared about the plague."
    ed "Had some fun with Ottoman mermaids (way chiller than the Italian ones), and wizards in Saxony."
    ed "I had been wandering for some time in the Eastern or Central or perhaps even Northern regions of the continent—who's to say." 
    ed "It had been years since I had any time for quiet or study, and I had heard rumblings about a very quiet castle out in the middle of nowhere."
    ed "I thought perhaps I could get a job and live a few peaceful years in the countryside."
    ed "Some guy named Napoleon was taking over half of Europe and frankly, I didn't want to get involved." 
    ed "When I arrived it was a cold and chilly night, a little eerie. When I knocked on the entrance to the castle, only one person answered."
    show layla at person_d
    "Layla the Terrible" "Oh, hello why aren't you a tall drink of water."
    bio "Did she really say that???"
    ed "Would you rather she say something like, {nw=0.1}"
    "Layla" "Come (wink wink) into my castle sexy warlock I will feed you grapes while I suck your blood."
    "Ew."
    bio "I really wouldn't."
    ed "Okay. Th{nw}"
    bio "Wait, {i}blood?{/i}"
    ed "What?"
    ed "Oh, yeah. She was a vampire."
    ed "When I arrived, Layla had just bought that castle."
    ed "She had big plans for it: a massive library, elaborate dining room, giant vat of blood in the kitchen."
    ed "Yeah she had vampires all over the place, but it wasn't {i}too{/i} bad in the beginning..."
    ed  "During the day I'd sit in the library and read, and at night the vampires ran around doing whatever it is vampires do I really don't give a f**k."
    
    menu:
        "They suck blood.":
            ed "Okay well some vampires suck ass."
            if endearing:
                ed smug "Don't ask me how I know."
        "I think they suck blood.":
            ed "You think, huh?"
            ed "What else do you think in that pretty little head of yours...?"
            bio blush "..."
            call endeared
    
    ed "Anyway, she was about to start ramping things up around there."
    "Layla" "Edward I have a proposal for you."
    ed "Not what I'm called."
    "Layla" "You're always going on about all those Ph.D.s you have..." 
    "Layla" "Surely a man with a big strong brain such as yours pines for another one, yes?"
    ed blush "Darn... I can't say no to another Ph.D..."
    ed -blush "The hot new science of the times was chemistry and Layla was willing to pay out." 
    ed "All I had to do was \"donate\" some of my blood from time to time." 
    ed "Otherwise, I had the best books, highest quality equipment, and some of the best teachers at my disposal."
    bio "So this is another story about your Ph.D.s?"
    ed "Is-{nw=0.1}"
    ed "Is this not an interview about my Ph.D.s?"
    "No."
    "It is not."
    bio "You can continue."
    ed "While I studied, the vampires continued to come and go." 
    ed "Many of them visited from all around the world and had traveled great lengths." 
    ed "Some brought me treats or candies from their homelands. Others would quietly stare before shuffling off."
    ed "For a period there was even one, Eskender, who would come all the way from Abyssinia." 
    ed "He would pop into my study for a chat each time he visited, ask about my research. "
    ed "We would sometimes have philosphical conversations that went on well into the night."
    ed blush "I liked him a lot."

    ed "When I completed my studies, everyone seemed a little {i}too{/i} excited." 
    ed "I was hoping to apply the knowledge to my backgrounds in medicine or engineering. But Layla had other plans."
    "Layla" "Darling Edmund how was chemistry."
    ed "It was great. Unlike alchemy. Which was wrong."
    "Layla" "Yeah okay whatever."
    "Layla" "As you know, I have clientele that visits this castle from quite afar." 
    "Layla" "They come in search of a very particular product."
    "Layla" "One they can usually only get from beyond the seas, which we've been importing for some time..."
    "Layla" "...but which would be not just more economical but hugely lucrative to synthesize in-house."
    ed "You mean they don't have to pillage Afghanistan to mine lapis lazuli?"
    "Layla" "What? No. It's drugs. I'm talking about drugs."
    "Layla" "Idiot."
    #she slides off screen to the right
    bio "Drugs for vampires, huh?"
    menu:
        "Are they different from regular drugs":
            ed "Look. This German guy came up with this cutting edge wacky stimulant class called amphetamines."
            ed angry "But these vampires were so old, they didn't even know what heroin was."
            ed "So I mainly made that."
            
        "Why did you agree to make drugs":
            ed "I already had an active warrant out for my arrest."
            ed smug "It's not like my record could get any worse."
            menu:
                "For vampire hunting without a license?":
                    ed angry "I'm licensed, and I had been licensed since before I went to the castle."
                    ed "Don't let anyone tell you otherwise."
                    call offended
                    pass
                "For aiding and abetting a vampire?":
                    $ vampireevilseen = True
                    "He sighs."
                    ed thinking "You know, they're not all bad..."
            $ renpy.fix_rollback()
            ed "Also I'll do anything for a paycheck."
    $ renpy.fix_rollback()

    ed "The more drugs I made, the more vampires came. The more vampires came, the rowdier they got."
    ed "And after certain crowd came in, Eskender stopped visiting."
    ed "Now, this new group didn't just stare." 
    ed "They were obsessed with asking me when I was going to become a vampire so it would \"fix\" my complexion."
    menu:
        "Yikes":
            pass
        "Yikes on bikes":
            call endeared
    ed "It was becoming unbearable, and I had started drafting up plans to leave it all." 
    ed "Until one day."
    "Layla" "What if we rounded up all of the humans and started breeding them like cattle?"
    "Layla" "That would keep me fed for an eternity!"
    ed shock1 "..."
    ed shock2 "..."
    ed "Okay that's enough."
    ed -shock2 "What Layla didn't know was when I wasn't in the lab, I was building and collecting weapons."
    if endearing:
        ed "And working out. I was also working out a lot."
        bio blush "Wow..."
    ed "All of the schmucks in Layla's castle were just too drunk, high, or both to notice."
    ed "So when the time came for me to show my hand, I made quick work of that frat house."
    bio "You defeated them all?"
    ed "Every last one of them was either staked, silvered, or garlicked."
    ed "I swiped her valuables too. Since she wasn't gonna be using them anymore."
    menu:
        "Stealing from a vampire castle?":
            ed angry "Technically it was ALSO MINE. WE made that money. TOGETHER."
            "Is he... sulking?"
        "What did you take?":
            ed "She loved jewels and precious stones and things. Had a lot of art in there, too." 
            ed "I took those to repatriate."
            ed "Other than money, I had to take my research."
            ed lying "There was a little recipe I was working on that produced a brilliant blue pigment..."
            ed smug "You might know her."
            call takenote("Ed discovered ultramarine blue", False)
            pass
    $ renpy.fix_rollback()

    show bg coffeeshop with dissolve
    show ed at move_to_center
    #move ed back to center
    "You take diligent notes of his vampire exploits."

    ed "Hey."
    "You look up from your notebook."
    ed lookup "Do your job. You've been letting me yap too much with no direction."
    show ed -lookup with dissolve
    "He's right. He's ready for your next question."
    "...only, you spent your best question already. And his answer kind of sucked."
    "You reach back into the recesses of your mind for an interview question that could inspire a tale as riveting as the one he just told..."
    bio happy "Tell about a time you struggled."
    "What was that!?"
    "You want to press your fists into your forehead, but you've got to keep your composure."
    "Luckily, it looks like something in his brain is turning..."
    ed lookup "You want to hear about my English Literature degree."
    bio "I don't want to hear about the degree at all. But the setting sounds primed for adventures."
    bio "You could talk about that."
    ed thinking "All right, no problem..."

    jump classiclit
    return

label classiclit:

    show bg library with dissolve
    #move ed to the left again
    ed "When I enrolled at the university, they gave me the option to have an apartment out by myself." 
    ed "But I was tired of living in countryside inns and small hostels after leaving the vampire castle, so I instead took the option to get a roommate."

    ed "Oh my roommate... Пётр Александрович Соколов." 
    ed "He really thought he was going to be somebody important and would make everyone call him by his full name."
    ed blush "...but he let me call him [petya_dn]."
    menu:
        "How did you say that with your mouth":
            $ renpy.notify("Trait gained: monolingual!")
            ed "What, [petya_dn]?"
            bio "Seriously, how do you do that?"
            ed "I open my mouth and say the sounds using the tongue God gave me."
            bio "I thought you weren't religious."
            ed "And I thought I wouldn't have to explain speaking to person with a communications degree?"

        "I'm guessing you were close":
            $ petya_dn = "Petya"
            ed -blush "Close is certainly a way you could describe me and [petya_dn]."
            menu:
                "How close are you thinkin' girl"
                "I mean they were roommates":
                    if homophobic:
                        ed "Sure."
                    else:
                        ed "It was closer than that."
                "Probably best friends?":
                    if homophobic:
                        ed "Sure."
                    else:
                        ed "It was closer than that."
                    pass
                "Oh they were doin' it":
                    if endearing:
                        bio happy "You liked him {i}a lot{/i}, didn't you?"
                        ed blush "Yeah. I did."
                    else:
                        "You bite your lip a little too hard."
                        "To make it feel better (and to cover it up), you lick it with your tongue..."
                        $ renpy.notify("Trait gained: fujoshi!")
                        "But to Ed, it looks like you're salivating over the thought of him and his roommate."
                    pass
    $ renpy.fix_rollback()

    ed "Anyhow..."
    ed "To call [petya_dn] obsessive and paranoid was an understatement."
    ed "He thought the students in his classics program were out to get him." 
    ed "That people were writing magic spells in the library books, or leaving secrets only for him to find."
    bio "So why did you stick with him?"
    ed "We were the only non-Anglo students in the school, so we just connected with each other, I guess. And he really seemed to like me." 
    ed "He was always asking me to help him study or cook. He confided in me a lot about the insane beef he had with his classmates and professors."
    bio "Let me guess: it was asinine and petty?"
    ed "Absolutely. There was an endless stream of names for people whose many slights against him I couldn't keep track of." 
    ed "This person looked at him and gave him the evil eye, that person chose to study an author he didn't think had any merit, so on and so forth."
    ed " Still, he was affectionate to me...{w=0.3} he had nice hands..." 
    ed "I fed him info and insights into the magical world while he lay with his back on my legs..."
    bio "Info or lies?"
    ed "Perfectly legitimate information."
    $ itwasinfo = False
    menu:
        "It was info":
            $ itwasinfo = True
            pass
        "It was lies":
            $ itwasinfo = False
            pass
    ed "Plus, I found his personality charming in a pathetic kind of way." 
    ed "He was kind of like a really jittery dog that finally stopped shaking every time you pick it up."
    bio "But he was always barking at people."
    ed blush "Yes, you get it!"
    ed "But soon, [petya_dn] started getting worse. He wasn't sleeping, he barely ate anything, and he stopped coming to our dinner nights." 
    ed "One of his classmates had plagiarized a section from one of his papers, and that was a breaking point." 
    ed "He completely and utterly lost his marbles."
    show petya at person_d
    petya "Ed, you gotta help me man. I messed up."
    ed angry "What in the world!?"
    petya "I don't even know what happened... I lost control of myself..."
    petya "Y-you told me I should stand up for myself, but I... I went too far... he's..."
    ed "{size=+20}[petya_dn].{/size}"
    ed "{size=+20}I never told you to kill anybody.{/size}"
    petya "I know, I know, but..."
    petya "You gotta help me. Please? It'll be just like old times!"
    ed "I couldn't say no to that, mainly because I was worried that if I didn't do anything, he was going to find a way to rope me in anyway." 
    ed "So I figured it was better to take control of the situation myself."
    bio sad "What did you end up doing???"
    ed smug "We framed the murder on someone else."
    bio shocked "WHAT."
    ed fakeout "Some goofball studying this newfangled thing called computer science?"
    ed smug "He didn't know what hit him."
    bio "WHEN WAS THIS."
    ed -lookup "Later that night, we packed up and fled the country."
    bio "OH MY GOD?"
    ed "What's the problem? You didn't seem to have a problem with all those vampires I slaughtered."
    menu:
        "This is different":
            ed "How so?"
            menu:
                "Vampires are evil":
                    ed "Well,"
                    ed blush "not all of them are."
                    if vampireevilseen:
                        ed -blush "Didn't I say that?"

                "You have a license to hunt vampires":
                    ed "Ooh, good point."
                    ed smug "You're clever."
                    call endeared
                    pass
            pass
        "I guess you're right":
            pass

    bio "Okay, fine. What happened afterwards? A relationship tested through the flames should be able to survive, right?"
    ed "Not really. I guess we could only relate to each other through that brief period." 
    ed "We were on the run together for a litle while, but we decided to split up." 
    ed "I tried to keep in contact with him, but after a few letters, I never heard from him again."

    if itwasinfo:
        bio "I can hardly imagine why. You helped him through so much."
        ed "If I'm being honest, I'm not too proud of what I helped him with!"
        "He's laughing like it's a joke, but..."
        pass
    else:
        bio "I can see why. You basically drove him to madness."
        ed lookup "Huh? What makes you say that?"
        bio sad "If I can be frank for a bit, he was already a nervous wreck."
        bio "He didn't need you filling his head with magic and sweet nothings."
        ed angry "E... excuse me...?"
        call offended

    ed "Anyway, if I had to relate it back to the question, {nw=0.3}"
    "You had nearly forgotten about the question (probably because it sucked).{nw=0.3}"
    ed "the degree itself wasn't too tough since I had already seen Shakespeare's plays in person."
    ed "What I really struggled with was..."
    ed "I don't know..."
    ed "Sometimes I close my eyes and I see [petya_dn]'s sad wet little eyes."
    ed "And his hands and face covered in blood."
    bio "In like a creepy way?"
    ed "No, it's definitely attractive."
    menu:
        "So you were struggling with your sexuality" if homophobic:
            ed angry "No, what the-{nw=0.3}"
            ed "What's your damage?"
            call offended
            pass
        "It sounds like your recent partners weren't very nice":
            ed "They weren't."
            if endearing:
                ed "They were kind of awful..."
                ed "But every time they left I felt like..."
                ed "I felt like I had a gaping hole in my heart."
                "You tilt your head in interest."
                "You wish you could fill that hole..."
                ed "Don't go getting ideas about filling any holes."
                bio blush "ED!"
            pass
    ed "Anyway. That's what comes to mind..."
    bio "All right."
    "You start to notice a theme emerging in the tales he's spinning."
    #conditional that checks for the amount of facts
    "Though you're having trouble telling fact from fiction."
    "It could be a mere fluke, so you decide to prompt one last time, just in case it doesn't show."
    "But you're sure it will."
    bio "What moment would you say is emblematic of your biggest fear?"
    ed "What?"
    ed "Why not just ask me my biggest fear?"
    bio happy "Because I have a feeling I already know what it is!"
    bio -happy "Also, you wouldn't answer a question like that."
    ed "True."
    ed "Okay, here goes."

    jump film
    return


label film:

    ed "I moved to Los Angeles."
    menu:
        "I've heard enough":
            $ renpy.block_rollback()
            $ earlyend = True
            ed "Really? Okay."
            "You look at him, expecting him to continue after chuckling along with you. But he doesn't laugh."
            "In fact, he seems to have taken you quite literally and refuses to speak more about his time in L.A."
            "You stare at him."
            "He stares at you."
            "You stare at him..."
            "He stares at you."
            if stareflag >=1:
                "You don't care if you've done this song and dance before."
            "This is really the end of the interview."
            "You thank him for his time, and you leave the coffee shop."
            jump gooseygoo

        "Oh the inhumanity":
            ed "Where was I supposed to go? Ohio?"
            "You nod your head in concession."

        "Go on":
            pass

    ed "I had spent decades in countries with rotten weather when I decided I'd finally had enough." 
    ed "I {i}needed{/i} to go somewhere with warm winters." 
    ed "Besides, the talkies had just come out and I wanted to have some fun."
    bio "At the movies."
    ed "Yeah."
    bio "So what got you interested in film?"
    ed "In truth, I became interested in film when I realized someone had brought one back in time to scare and confuse me."
    menu:
        "Are you joking kidding me":
            ed "About what?"
            bio angry "The time travel."
            ed fakeout "Is it that hard to believe?"
            bio "It's pretty freaking hard to believe."
            ed -fakeout "Really?{w=0.1} Cuz I haven't even told you about the Trickster God Wars." 
            ed lookup "Do you wanna hear about the Trickster God Wars?"
            bio "I'll pass."
            if endearing:
                ed "That's okay.{w=0.1} Some other time, then."
                ed smug "Maybe over dinner."

                
        "Was it a good movie though":
            ed "It probably changed my life forever."
            ed blush "So I would say it's pretty good."
            bio "What was the movie?"
            ed fakeout "1986's {i}Blue Velvet{/i} (dir. David Lynch)."

    call takenote("Ed was shown a movie before they ever existed", True)     

    ed "So my first day in the city, I was approached by someone on my walk to the grocery store."
    ed "I had just the look Hollywood was going for. Handsome but approachable, charming and soft."
    ed "I'd compliment the ladies and the men on screen. I had the potential to be a star and I figured—yeah, why not."
    ed "My first role was as a man in a ballroom who is sitting at a table waiting for his date." 
    ed "The lead actress comes up to me and asks if my seat is free. I prop my arm around my chair and smile at her and say,"
    ed "\"Not right now, darling, but I might have some space later.\""

    ed "I delivered that line and my fate was sealed." 
    ed "Critics raved, \"Who is that background actor with a single voiced line? Really pulls the whole film together,\" and audiences couldn't get enough of me."
    ed "Suddenly I was the hottest guy anyone had seen or heard of in the motion picture business."
    ed "The best friend in a screwball comedy, the uncle in a serious play adaptation, the romantic lead—{nw=0.1}"
    ed "the roles just kept on coming. And I was killing it with all of them!"
    ed "Everyone praised my ability to command a scene, the ease of which I held myself,{nw=0.1}" 
    ed "the casual and charming way that I talked about the 1700s like I had been there for it." 
    ed "Everyone {i}loved{/i} me."
    bio "They all {i}loved{/i} you, you say?"
    ed "Yeah, they loved me a bit too much, because here's where it starts to cause problems."

    ed "I lived in a modestly-sized house tucked away in the Hollywood Hills, with a view of the ocean." 
    ed "I mostly kept out of the public eye and hardly engaged with my fans." 
    ed "In a way, you could say I played hard to get. I thought it added to my gentlemanly charm."
    ed "Then come the after work drinks and cast wrap-up parties."
    ed "Day in and day out, I am surrounded by beautiful women and handsome men as far as the eye could see."
    ed "So I cave. And I buy people a few drinks here and there, and invite some of them over to my house..."
    bio angry "Some people?"
    menu:
        "He was throwing modestly-sized informal gatherings in his humble abode":
            "Methinks you trust this man a tad too much!"
            pass
        "He was throwing some crazy parties in that mansion, yo":
            $ yourFacts += 1
            pass
    "He shifts in his seat a little bit. You get the feeling he may have undersold some details..."
    "You brace yourself for what's about to come next."
    bio "So who were these people who had you in their favor? Anyone I know?"
    ed "Hm, well..."
    ed "Rock Hudson, Anna May Wong, Katherine Hepburn, Eartha Kitt, James Dean,{nw=0.2}"
    bio "Wow,{w=0.1} that's-{nw}"
    ed "Josephine Baker, Rita Hayworth, Paul Robeson, Anthony Perkins, Paul Newman...{nw=0.3}"
    ed lying "...Zendaya{nw=0.2}"

    "Zendaya? Seriously?"
    menu:
        "You did not sleep with freaking Zendaya":
            ed "ok maybe not zendaya maybe like {w=0.4} pedro pascal{nw}"
            bio angry "Ed.{nw=0.3}"
            ed "Okay."
            ed blush "The other ones were real.{nw}"
            bio "I know."
            ed "Okay."
            ed "Just making sure."
            $ yourFacts +=1

        "I believe it":
            pass
    
    ed "I was having so much fun loving{w=0.1}—and being loved{w=0.1}—that I nearly forgot about the fact that it was the early 20th century in North America, and actions like that have Consequences." 
    ed "You see, the first divorce you cause is kind of funny. By the third, you start getting invited to the courthouse..."
    ed "It's pretty hard to be the cause of over fifteen divorces and not get the attention of your boss."
    bio "{i}Fifteen!?{/i}"
    ed "The studio heads were pissed." 
    ed "If I hadn't been with their wives, I had been with their wives sisters,{w=0.1} or their wives sisters' husbands."
    ed "Or perhaps all of them at once."
    bio "No s**t they were pissed. I would be, too!"
    ed "Yeah, but they couldn't fire me because I was loved by the public too much, and no one was worried about communists infiltrating Hollywood yet."
    ed "So it's not like I was going to be blacklisted."
    ed "Besides, if I got banned from a set I could just get one of my many lovers to sneak me back in."
    bio "In spite of it all, you still wound up on top."
    ed "That is until the suits decided enough was enough." 
    ed "Thirty eight divorces strong, I had to be stopped."
    ed "If they couldn't fire me, and they couldn't ban me from the studios, they decided to take drastic measures: {p=0.1}they had to go to the United States government." 
    ed "Movies were going too far and a governing body had to be put in place to stop them."
    bio "You mean you caused the creation of the Hays Code!?"
    ed "Well? Joke's on them. I retired with my millions and spent the rest of the 20th century unburdened and unbothered."
    bio "And alone."
    ed thinking "..."

    jump currentday
    return


label currentday:
    ed "Much later,{w=0.1} I went and got a Ph.D in film studies."
    ed "It was pretty easy since I was there for all of it."
    bio "So you just collect degrees, just because?"
    ed "What? No. No one does that."
    bio "No one? I don't know how true that is."
    ed "You know what...? You could be right."
    ed "Maybe there's someone out there who wants a doctorate to affirm their gender."
    bio "So you got your Ph.D. Again."
    ed "Yes there's more I got more Ph.Ds."
    $ degreeskip = False
    menu:
        "Sigh. Again with the Ph.Ds?"
        "Tell him to hurry it up":
            $ renpy.block_rollback()
            bio "Ed, I don't know if we have this much time to dedicate to all of your postgraduate degrees."
            ed "Really? Because I've been blowing a lot of hot air on s**t that really doesn't matter." #id we could alter the style on "stuff" to look like a censor
            ed "The Ph.Ds are the most important part."
            "You decide to be frank."
            bio "Ed."
            bio "No one cares how many Ph.Ds you have."
            ed "Damn, okay." 
            ed smug "Famous last words though." #looks at the camera. 
            $ degreeskip = True
            jump afterPhd
            
        "Let him get them out of his system":
            $ renpy.block_rollback()
            pass

    ed "It was the late 90s, a while after I got my Ph.D. in clinical psychology."
    ed "I had just become a board-certified physician at the time, too, and my private practice was doing pretty well."
    ed "Since I had a bit of extra cash, I figured I could go back and do another program. One that was less sciencey."
    ed "Like I said, I was there, so it wasn't suuuper difficult. But, my god, the papers, and the records?"
    ed "I was like, \"Is this film studies or archaeology?\""
    show colleague at person_d
    "Colleague" "It's called, \"doing research,\" Ed."
    hide colleague
    ed "But, you know, spending time in and out of libraries,"
    ed "seeing patients,"
    ed "robbing banks to pay for my girlfriend's HRT..."
    menu:
        "E-excuse me!?":
            ed "Oh, so now it's weird to want to support your girlfriend's transition."
            bio "I- {nw}"
            if homophobic:
                $ homophobicbelief = renpy.random.choice(homophobicbeliefs)
                ed "I know what you're gonna say."
                ed "\"But Ed, I was talking about the bank robbing part!\""
                bio "I was! And I don't sound like that!"
                ed "Likely story from someone who doesn't believe [homophobicbelief]."
                "Come on, girl, get it together. He cannot keep baiting you like this!"
            else:
                ed "Are you transphobic?"
                bio "I'm not!"
                $ renpy.notify("Trait earned: transphobic!")
                ed "Wowwwwwwwww."

        "You mean like...?" if endearing:
            bio "Like Al Pacino in {i}Dog Day Afternoon?{/i}" (multiple=2)
            ed "Like Al Pacino in {i}Dog Day Afternoon.{/i}" (multiple=2)
            "He leans back in his chair and points at you."
            ed "Oh, I {i}like{/i} this one."  #smile 
            call endeared

    label afterPhd:
        ed "Long story short, I had an {i}amazing{/i} time in New York City."
    ed "Until I had to leave."
    bio "You {i}had{/i} to leave? Why?"
    ed "7/11."
    bio "Oooh, when that psychic girl collapsed that building, huh?"
    ed "Yep."
    bio "So this is like,{w=0.1} the 2000s era."
    bio "You know she still doesn't feel bad about that."
    ed "Oh I know."
    ed "Believe you me...{w=0.1} I know."
    ed "Anyway,{w=0.1} I knew it was about to get crazy over here,{w=0.1} so I moved to London."
    
    if not degreeskip:
        ed "I got my most recent Ph.D. a few years later,{w=0.1} in Africana Studies."
        ed "And I thought it was a very illuminating experience,{w=0.1} but now I don't know how I feel about gynecology?"
        menu:
            "Gynecology?":
                bio "What exactly is the thought process behind that...?"
                ed "That's beyond the scope of this conversation,{w=0.1} don't you think?"
                ed "You're a smart woman.{w=0.1} I'm sure you can figure it out."
            "I get what you mean":
                pass
    ed "I taught there for the better part of two decades, and ended up working very closely with another professor who was also a witch."
    ed "She was deep in ghost research, which was a field of magic I had barely touched for a number of reasons."
    ed "...Reasons I would hope are obvious."
    ed "Early on in our stint together, keeping the magic a secret got to be really quite difficult."
    ed "You know, it's a university, so people ask questions."
    ed "\"Can I have the key to the printing closet.\" \"Why do you need library access after hours.\" \"Aren't you the guy from Star War.\"" 
    ed "Things like that."
    ed "So we put on fake wedding bands. That made them mainly ask when we got married."
    bio "But you wouldn't pretend to marry someone you didn't like."
    ed "Oh boy. Don't even joke about that."
    "It took a while, but the theme finally re-emerged..."
    ed "I floated the idea around, but I wasn't anywhere close to her level."
    ed "She said I was too immature for her."
    ed "She's a regular 30-something!"
    bio "She's a 30-something, right now?"
    ed "Yes."
    bio "So young!"
    ed "Yes, it's embarrassing."
    bio "When did that happen?"
    ed "Only a few years ago."
    bio happy "You're taking it like a champ."
    ed "I- {nw=0.1}"
    ed "Thank you."

    bio "What made you decide to come back from England?"
    ed "Oh,{w=0.1} you know..."
    ed "{size=-10}...philandering.{/size}"
    menu:
        "Tell him to speak up":
            bio "Excuse me,{w=0.1} can you say that again?"
            ed "That again."
            "Sigh.{w=0.1} Of course."
            bio happy "Of horse."
            "He stares at you."
            "You stare at him."
            if stareflag >=2:
                "He stares at-{nw}"
                "ENOUGH!" 
                $ renpy.notify("Trait gained: the lookerrrrrrrrr")
                "NO MORE STARING!"
                $ stareflag += 1
            else:
                "He stares at you."
            "You move on."
        "He can keep his secrets":
            "You nod along even though you didn't really hear what he muttered."
            "You have a feeling it was something embarassing like,{w=0.1} \"philandering,\"{nw=0.3}"
            "which is a funny word for \"womanizing\" because it sort of implies he's attracted to men."
            "Not that that's bad or anything.{w=0.1}" 
            if homophobic:
                $ renpy.notify("Trait gained: in denial!")
            "It's not like you're homophobic."

    
    ed "So."
    ed "Based on that."
    ed "What would you say my biggest fear is?"
    menu:
        "Commitment":
            pass
        "Abandonment":
            pass
        "Insincerity":
            pass
        "All of the above":
            pass
    $ renpy.fix_rollback()
    ed "You seem really sure about that."
    bio "Mm-hm."         
    jump review
    return

label review:

    bio "Well then. Let me just touch up my notes..."
    "You opened up your notepad and scribbled."
    menu vocation:
        "Though he is many things now, his original occupation was..."
        "A fisherman":
            $ yourFacts +=1
            pass
        "A scholar":
            pass
        "A sailor":
            pass
        "A pain in the ass":
            ed "Hey."
            pass

    menu travel:
        "Ed arrived in Portugal via..."
        "Boat":
            $ yourFacts += 1
            pass
        "Land":
            pass
        "Mermaid":
            pass
        "He swam using those strong arms and legs":
            "Chill out,{w=0.1} lil bro.{w=0.1} You can't even see them."

    $ pine = False
    menu year:
        "He met the Devil the year he turned thirty, which was..."
        "1418":
            pass
        "1422":
            $ yourFacts += 1
            pass
        "1430":
            pass
        "2023" if pine == False:
            "If only he were a regular 30-year-old man and not a 631-year-old warlock."
            "You might have been able to marry him."
            $ pine = True
            jump year

    #alignment q
    menu beliefs:
        "Ed is ideologically aligned with..."
        "The monarchy":
            pass
        "The owning class":
            pass
        "The proletariat":
            pass
        "Himself":
            $ yourFacts +=1
            pass
        "The girl reading this":
            $ yourFacts +=1
            ed "That includes you."
            bio blush "What!?"
            $ cuteanimal = renpy.random.choice(["fluffy kitties", "fat baby seals"])
            "You quickly scratch that out and write \"[cuteanimal]\" in its place."
            call endeared
        "Are you kidding!? Our paper isn't political!":
            "Yeah,{w=0.1} that's what your boss says,{w=0.1} but he knows how running cover for a warlock will reflect on it."
            "He's not an idiot.{w=0.1} He knows about...{nw=0.3}"
            # play sound ominous 
            extend "The Implication."

    menu crimes:
        "During your talk, Ed casually admits to..."
        "Framing someone for murder":
            $ yourFacts += 1
            ed "Hey, uh, don't write that in there."
            ed "I have enough problems as it stands."
            "Now it's your turn to be smug."
            bio happy "No promises."
        "Trapping a town in an endless fog":
            pass
        "Impersonating a vampire hunter":
            pass
        "Insider trading":
            pass

    ed "Hey, can you include a segment about my Ph.D.s?"
    "You sigh."
    bio "Fine."
    menu phds:
        "You decide you will offhandedly mention his Ph.D. in..."
        "Fishing Science":
            pass
        "Theology":
            $ yourFacts += 1
            pass
        "Screenwriting":
            pass
        "Library Science":
            pass

    "Finally..."
    menu thecost:
        "What did his immortality cost him?"
        "Two dollars":
            pass
        "A Ph.D.":
            pass
        "His lily-white reputation":
            pass
        "Human connection":
            "You look at the bags under his eyes."
            "You think to yourself, \"Eye{i}bags?{/i} More like eye luggage.\""
            "You snort, and then shake your head for laughing at your own joke."
            "Then you write, \"more than he could have ever imagined.\""
            $ yourFacts += 1

        
    $ renpy.fix_rollback()

    "You got the strange feeling that you and him were headed toward the same idea."
    menu commonthread:
        "The one thing all of his stories had in common was..."
        "Crazy-ass moments in world history":
            "At the moment, though, you were a bit distracted by the surface-level elements."
            pass
        "A romantic partner":
            $ commonality = True
            pass
        "A postgraduate degree":
            "Okay, like, yeah, but, like, not that."
            jump commonthread
        "A supernatural component":
            "At the moment, though, you were a bit distracted by the surface-level elements."
            pass
    $ renpy.fix_rollback()

    jump interviewconclusion

    return

label interviewconclusion:


    ed "Well?{w=0.1} That should be enough to write a pretty basic profile."
    bio "Basic? You don't mean to imply that there's more."
    ed "There {i}absolutely{/i} is,{w=0.1} but if I went into it,{w=0.1} I'm certain we'd be here all night."
    "Truthfully,{w=0.1} you wouldn't mind spending all night with him."
    if not endearing:
        ed "But you have a deadline,{w=0.1} so."
        pass
    ed "Was there anything else you needed from me?"
    bio "Yes,{w=0.1} well,{w=0.1} I just have one final question."
    bio "In all your stories,{w=0.1} you've gone on about the who, the what, the how..."
    bio "Why did you do it?{w=0.1} Why did you decide to become an immortal wizard?"
    ed "I was already a wizard before I became immortal."
    bio "Right,{w=0.1} of course.{w=0.1} But still. What motivates you?"
    bio "Is it all those fun adventures? Money?"
    bio "Were you trying to change the world?"
    bio "What's the reason?"
    bio "Or,{w=0.1} at least,{w=0.1} what's the reason you want the world to know?"

    ed "Why did I do it,{w=0.1} huh...?"
    ed "That's a great question."
    ed "I,{w=0.1} um..."
    ed "I did it for love."
    bio "Love...?"
    bio "Really?"
    ed "Yes."
    ed "That's not weird...{w=0.1} is it?"

    menu:
        "It's a little weird":
            ed "..."
            ed "I guess it is,{w=0.1} coming from someone like me."
            
        "It's not weird at all":
            ed "Good.{w=0.2} ...I was a little worried you would make fun of me."
    if commonality:
        bio "I noticed you had a partner for every story."
        bio "Or, at least someone you were very fond of, that you seem to miss, even now."
    else:
        bio "Why do you say you did it for love?"
    ed "It goes back to my first girlfriend."
    ed "...Actually, she was my fiancée."
    ed "When we shipwrecked, I actually died. {w=0.3} Well,{w=0.3} \"died.\""
    ed "I never told her about the immortality, so she never knew I was still alive."
    ed "I think that in the intervening years, I didn't want to replace her..."
    ed "So all of my relationships ended up being really short-lived."
    bio "Because you thought you would find her again?"
    ed "Right."
    bio "But you ended up never meeting her again."
    ed "No, that's not true."
    ed "When we reunited, she had married someone else."
    bio "Oh..."

    ed "Then she told me,\"You're like how I was when I met you.\""
    bio "That kind of makes sense. Mermaids live for much longer than humans do."
    bio "Ohhhh. I think I understand it now..."
    ed "Yeah."
    ed "I only see why she tried to talk me out of the deal after I'd done it."
    ed "But she wasn't upset with me or anything. She just kind of... laughed."
    ed "She told me that"

    if yourFacts >= factstotal:
        if endearing:
            if nameroute:
                $ secretending = True
            else:
                pass
        else:
            pass
    else:
        pass    

    if secretending:
        jump sneakdevildeal
    else:
        pass
    jump finaltest

    return


#endings
label sneakdevildeal:
    #criteria for reaching the deal:
    # you've asked him about his name
    # you've endeared yourself to him
    # you've dodged all of his falsehoods
    $ dealtriggered = True
    #stop the music
    ed "Listen here."
    ed "I like you.{w=0.1} How come I've never heard of you before?"
    bio "I suppose...{w=0.1} it's just by chance.{w=0.1} I mean,{w=0.1} I've never had a lot of eyes on much of my work."
    ed "But you're clearly good at what you do.{w=0.1} You want people to know that about you,{w=0.1} right?"
    "That would be nice..."
    ed "Wouldn't it?"
    bio "I...{w=0.1} wouldn't have to answer to my good-for-nothing boss."
    ed "Exactly!"
    ed "Look,{w=0.1} I'll cut to the chase.{w=0.1} I want to help you."

    menu:
        "Accept his help":
            jump accept
        "Reject his help":
            jump reject
        "Ask a question":
            pass

    bio "Oh!{w=0.1} Really?{w=0.1} I mean,{w=0.1} I don't know...{w=0.1} help me how?"
    ed "Well...{w=0.1} let me put it this way."
    ed "I think that...{w=0.1} this profile your paper is doing..."
    ed "I think it's going to make a killing.{w=0.1} I think it's gonna make waves."
    ed "How do the kids say it?{w=0.1} It's gonna do numbers?"
    bio "Well,{w=0.1} what makes you say that?"
    ed "Just by the sheer quality.{w=0.1} You're keen.{w=0.1} Observant."
    ed "Honest."
    "He's right,{w=0.1} you know."
    menu:
        "Accept his help":
            jump accept
        "Reject his help":
            jump reject
        "Ask another question":
            pass
    
    bio "But...{w=0.1} why me?{w=0.1} There are far more prolific writers doing way worse than I am."
    ed "There are far {i}worse{/i} writers doing much better than you are,{w=0.1} too."
    bio "{w=0.1}...I never said anything about worse writers."
    ed "It's not what you said.{w=0.1} It's what you didn't say."
    ed "\"Prolific.\"{w=0.1} Not learned,{w=0.1} not talented.{w=0.1} Prolific." 
    ed "In other words:{w=0.1} just talk.{w=0.1} They talk too much."
    ed "Not you,{w=0.1} though."
    ed "I like you,{w=0.1} so I'll help you.{w=0.1} Simple as that."

    menu:
        "Accept his help":
            jump accept
        "Reject his help":
            jump reject
        "Ask another question":
            pass

    bio "And what do you get out of helping me?"
    ed "Hm..."
    ed "The satisfaction,{w=0.1} I guess.{w=0.1} A bit of comfort?"
    "Wow.{w=0.1} How selfless..."

    menu:
        "Accept his help":
            jump accept
        "Reject his help":
            jump reject
        "Ask another question":
            pass

    bio "How can I be sure I can trust you?"
    ed "Of course.{w=0.1} That's very important.{w=0.1} You hate lies.{w=0.1} And I've proven I love lying."
    "You laugh idly."
    ed "I'll give you my name.{w=0.1} My real name."

    bio "And what do I give you?"
    ed "Your word that you will keep it a secret."

    menu:
        "That seems fair":
            jump accept
        "No way, José":
            "You don't call him José,{w=0.1} by the way."
            jump reject
    

    return

label accept:

    "You let out the breath you've been holding."
    bio "Sure!{w=0.1} Why not."
    ed "Good! Good. That means I can trust you with this."
    call realname
    bio "So...{w=0.1} what do I do now?"
    ed "You lock it in."
    menu:
        "Lock it in with a handshake":
            "You stretched out your right hand for Ed to grab.{w=0.1} He gives you a firm hanshake." 
            "You felt your palm tingle."
        "Lock it in with a fistbump":
            "You raised your fist to chest height.{w=0.1} He raises his to meet yours.{w=0.1} You bump fists."
            "You felt a slight gust wind brush past your face and through your hair."
        "Lock it in with a kiss":
            "You had to stand on the tips of your toes to reach his face."
            "He holds you steady by your waist as you lean into him.{w=0.1} You close your eyes." 
            "Then, you feel his warm lips on yours."
            "...and once again."
            "You felt your heart flutter."
    "As you leave the studio,{w=0.1} something starts to nag at you from the back of your mind." # his house (the vampire castle)? a cafe? a hotel? wherever
    "He agreed when you said it would be nice..."
    "But you were sure you never said that aloud."
    jump finaltest
    return

label reject:
    $ ed_observation = True
    bio "Sorry.{w=0.1} I don't think I can accept your help."
    ed "That's all right...{w=0.1} that's all right."
    #the music and background return.
    ed "I hope you remember how many Ph.Ds I have,{w=0.1} though.{w=0.1} Cuz if you don't, tuh?{w=0.1}"
    ed "Well."
    ed "You'll never work in this field again."
    bio "How-{w=0.1} how can you be so sure?"
    ed "Oh I'm sure.{w=0.1} Of this, I am{w=0.2} {i}very{/i} certain."

    "And with that,{w=0.1} he shuffles off."
    "You should head back, too." #or if it takes place in the same office as yours you just don't
    
    jump finaltest

    return

label realname:
    ed "My name is Aniedi Akpan."
    ed "My mother got it from a friend of hers..."
    ed "\"Akpan\" just means \"first-born son.\""
    bio "Wow..."
    bio "What does \"Aniedi\" mean?"
    ed "I was told it meant..."
    ed "\"Who knows?\""
    bio "Hm..."
    return

label finaltest:
    #scene
    if secretending == True:

        "You wander into the office,{w=0.1} almost in a trance."
        "You don't even notice your boss calling out for your attention.{w=0.1} He seems perplexed as you saunter to your desk."
        call endoftest
        jump dealend
    elif ed_observation == True:
        "You mull on the last conversation you had before you left."
        "He was needlessly cryptic... wasn't he?"
        "But you're sure nothing will come of it."
        pass
    else:
        "Pleased with your findings,{w=0.1} you returned to the office with your head held high.{w=0.1} You had a brilliant idea for the profile."
        "You could even picture the final line of the article:"
        "{i}Even in a life full of tall tales,{w=0.1} he kept a simple truth in his heart.{/i}"
        pass
    label gooseygoo:
        boss "There you are,{w=0.1} you silly goosey goo!{w=0.1} So what did you find out?{w=0.1} Is he really the world's most credentialed man?"
    bio "Well... "
    $ rattle = False
    if yourFacts <=2:
        bio "I certainly talked to the man."
    elif yourFacts >2:
        $ rattle = True
        $ tidbit = renpy.random_choice(factscollect)
        bio "I found out that [tidbit]."
        $ factscollect.remove(tidbit)
        $ tidbit = renpy.random_choice(factscollect)
        bio "I also learned that [tidbit]..."  
        $ factscollect.remove(tidbit)
        $ tidbit = renpy.random_choice(factscollect)
        bio "And I'm pretty sure [tidbit]."       
    
    if starsign:
        bio "Did you know he's actually a Libra and not a Virgo?"

    if rattle:
        boss "Kid."
        boss "You're tellin' me stuff we already heard!"
    else:
        boss "What's that supposed to mean? So you were striking up friendly chatter instead of writing the article?"
    
    bio "Um...{w=0.1} I was under the impression that we hadn't written the profile yet because of the sheer amount of misinformation surrounding the individual."
    boss "No,{w=0.1} no,{w=0.1} we hadn't written the profile because we were waiting for the new keyboard to come in.{w=0.1} Keep up!"
    if not earlyend:
        bio "Well,{w=0.1} he sent me off with a tidbit I thought was really beautiful and true."
        boss "Really?{w=0.1} Let's hear it."
        bio "He told me he had never forgotten the reason he became immortal." 
        bio "He told me he'd done it for love.{w=0.1} That was the one thing he desired most."
        boss "YAWNNNNNNNNNNNNNNNNNNNNN.{w=0.1} Boring!"
        bio "I thought it was nice..."
        if dealtriggered == True:
            boss "I thought it was CORNY!"
            bio "I have something else that...{w=0.1}happened...{w=0.1}if you'd rather hear about that?"

        boss "Nope! {w=0.1}Don't gaf.{nw=0.1}"
    boss "SO! {w=0.1}How many Ph.Ds did he earn?"
    bio "um{nw=0.1}"
    bio "what?"
    "Your boss sighs."
    boss "{cps=*0.5}How many Ph.Ds did he earn?{/cps}"
    bio "Are you serious?"
    boss "Very."
    bio "Well- {nw}"
    boss "Your job depends on it. {w=0.1}Just so you know."
    $ finalanswer = renpy.input(prompt="How many Ph.Ds did Ed earn in his lifetime? (Enter numbers only.)", allow="1234567890")
    boss "Okay,{w=0.1} don't forget to write that in.{w=0.1} I'm counting on you!"
    boss "Don't embarrass the paper!"

    call endoftest

    if finalanswer==totalPhds:
        jump goodend
    else:
        jump badend
    return

label endoftest:
    "You sit down and write the article exactly as you envision it."
    "When you're done,{w=0.1} you submit it,{w=0.1} and you go home."
    return


label goodend:
    "Some weeks after the profile went live,{w=0.1} you got a call from your boss."
    boss "Hey,{w=0.1} um."
    boss "I wanted to say congratulations.{w=0.1} The article is doing pretty well."
    boss "People are saying some parts aren't true..."
    if yourFacts >= factstotal:
        boss "That's cuz I,{w=0.1} uh... {w=0.4}{i}embellished{/i}{w=0.4} your article a bit.{w=0.3} By the way." 
        boss "Just here and there!{w=0.1} To spruce things up a bit,{w=0.1} y'know?{w=0.1} Nothin' too crazy."
    else:
        boss "Which is,{w=0.1} y'know,{w=0.1} to be expected for a guy with such a history. {w=0.3}Misinformation,{w=0.1} like you said."
        boss "I'm sure it was tough to get the truth out of him."
    boss "I know how you feel about lying and inaccuracies.{w=0.1} How it makes you feel queasy and all that."
    boss "So,{w=0.1} to clear your conscience,{w=0.1} I went ahead and left your name off the byline."
    boss "Don't worry,{w=0.1} you'll get a bonus for the accurate reporting on the Ph.Ds."
    boss "You're welcome!"
    "He hangs up."
    
    "You reached the good ending...?"
    #persistent from reaching the secret ending
    "You realized this was as good an ending as you could get."
    return

label badend:
    "Some weeks after the profile went live,{w=0.1} you got a call from your boss."
    boss "Hey,{w=0.1} um."
    if finalanswer == totalDoctorals:
        boss "Did you go and count the number of doctoral degrees or the number of Ph.Ds?"
        boss "Cuz I asked for Ph.Ds...{w=0.1} and I get that he has an M.D..."
        boss "...but an M.D. isn't a Ph.D."
    boss "So,{w=0.1} you're fired.{w=0.1} Totally super mega ultra fired.{w=0.1} For embarrassing the paper."
    boss "Don't check Glitter."
    "Glitter is Magic Twitter."
    "It also has a significantly higher proportion of gay stans.{w=0.1} Vicious gay stans."
    "It's the highest on the Internet,{w=0.1} unfortunately for you."
    "When your boss told you not to check Glitter,{w=0.1} it's because he knew they were eviscerating you on there."
    "So you log on to check,{w=0.1} against your better judgement." 
    "You immediately find the post.{w=0.1} It's got one william likes.{w=0.1} The quote gleets are eating you up."
    "As it turns out,{w=0.1} a Dr. Yetunde Olu,{w=0.1} former colleague and ex-girlfriend of Ed,{w=0.1} wrote a response piece{nw=0.2}"
    "wherein she comments that she can excuse the occasional tall tale,{w=0.1} and even stops short of calling the piece laundering like many other critics have,{nw=0.2}"
    "but she draws the line at misrepresenting the nature of his involvement in academia."
    "Among other things,{w=0.1} she has revealed {i}exactly{/i} how many Ph.Ds he's earned." 
    "And it's not [finalanswer]."
    
    "In the end,{w=0.1} you,{w=0.1} too,{w=0.1} were a charlatan.{w=0.1} A grifter.{w=0.1} A hack.{w=0.1} A useful idiot{w=0.1}—at {i}best.{/i}" 
    if ed_observation == True:
        "It was just as Ed had predicted."
    "You can never work in this field again."
    "You reached the bad ending."
    return

label dealend:
    "Some weeks after the profile went live, you got a call from your boss."
    boss "Hey,{w=0.1} um."
    boss "I want to say I'm sorry."
    "Followed by an unusual pause."
    boss "I'm sorry for doubting you,{w=0.1} and-{nw=0.2}"
    "Another pause.{w=0.1} You hear shuffling on the other side of the line." 
    "You're sure you hear your boss say, \"okay\" over and over."
    boss "And I've been withholding tens of thousands of dollars in backpay which I-{w=0.5} which I will deposit in your checking account.{nw=0.3}" 
    boss "Immediately."
    "He hangs up." 
    "You've never heard him so stilted...{w=0.1} and so scared...?" 
    "Just one more thing to pile on to the weird couple of weeks you've been having..."
    "You thought back to the conversation you had with Ed,{w=0.1} right before you left."
    "It seems like he was right:{w=0.1} your article did incredibly well!"
    "But it also seems like no one who read it knows what it actually said." 
    "Everyone who talks to you about it says something wildly inaccurate."
    "And everyone says something different."
    "You've read it over and over every night since it was published.{w=0.1} It's exactly as you remember it—"
    "no tall tales,"
    "no editorializing from your boss,"
    "no inexplicable gaps in the narrative."
    "It should be a completely factual profile..."
    "You continue your career as a magical biographer."
    "But you can't shake the queasy feeling you get from telling a lie for as long as you live."

    "You reached the secret ending...!"
    return

