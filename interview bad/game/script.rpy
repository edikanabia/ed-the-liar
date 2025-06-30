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
define factstotal = 10

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
define affectionthreshold = 2
default misogynyaccusation = False


default stareflag = 0
default greeting = ""
default whatyouget = False


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
default yearcontradiction = False
default italian = 0
#endregion

#region Resources

#em dash: —

#endregion

#region Persistent Data
default persistent.good_ending_reached = False
default persistent.bad_ending_reached = False
default persistent.secret_ending_reached = False
default persistent.completed_playthroughs = 0


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
image ed wink = "../charasprites/ed wink.png"

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
image bg workshop = "/backgrounds/workshop.png"

image bg black = Solid("000")
image bg white = Solid("fff")
#CGs
image cg csection = "/cgs/cg_csection.png"
image cg filmset = "/cgs/cg_film.png"
image cg slaughter = "/cgs/cg_vampire_hunting.png"
image cg framed = "cgs/cg_frame.png"

#endregion

#region Transforms, Transitions, and Screen Variables
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

define circlewipe = ImageDissolve("/transitions/circle_wipe.png", 1.0,2)

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
            show ed wink
            "!?" #wink
            show ed -wink
            "You feel a lot more confident now!{w=0.1} But..."
            "It seems unlikely that someone as busy as he is has \"nothing better to do.\"{w=0.1} He's not messing with you,{w=0.1} {cps=*0.5}or...?{/cps}"
            
        "Excitedly":
            $ greeting = "excited"
            bio "It's an honor to meet you,{w=0.1} sir."
            ed lookup "Really.{w=0.1} An honor?{w=0.3} \"Sir?\""
            bio happy "Yes!{w=0.1} Actually..." 
            bio -happy "I'm a little starstruck,{w=0.1} I have to admit..."
            ed thinking "Huh.{w=0.1} I didn't realize I had a... {w=0.3}following."
            "Your face runs hot and you absentmindedly start fanning yourself."
            "You start to wonder how his lashes are so long...{w=0.1} and supple...{w=0.1} when it hits you:"
            "He \"didn't realize\" he had a following?{w=0.1} How could he not know?"

    show bg black with dissolve
    "Is he...{nw=0.1}" 
    #play sound ominous
    extend "lying?"
    show bg coffeeshop with dissolve

    "You pay it no mind."

    "You clear your throat and shake your head.{w=0.1} Now is not the time to get distracted.{w=0.1} You have a job to do!" 
    "You might be the first person to ever get the full story out of such a slippery and elusive figure."
    
    menu:
        "Time to lock in!":
            "You said that out loud."
            ed lookup "Hm?"
            menu:
                "Sorry that wasn't meant for you I think":
                    "He doesn't react."
                "Clear your throat":
                    "You clear your throat (again)."
    show ed -lookup
    "The magician leans back in his chair and crosses one leg over another,{w=0.1} resting his hands on one knee."
    "...Seeing him relax makes you relax,{w=0.1} as well."

    jump demography
    return

label demography:
    bio "Let's just start with a basic background..."
    bio "As we both know,{w=0.1} you are an immortal warlock,{w=0.1} the Agent of Chaos-{nw=0.1}"
    ed thinking "You can call me Ed."
    $ ed_dn = "Ed"
    bio "Ed."
    ed "Yes."
    bio "Just{cps=*0.5}...{/cps} Ed?"
    ed -thinking "{cps=*0.5}Mm-hm.{/cps}"
    "You are thinking about something already..."
    menu:
        "Is that really your real name?":
            $ renpy.block_rollback()
            ed "No. {w=0.1}Obviously."
            bio "You're joking,{w=0.1} right?"
            ed lookup "Madam."
            ed -lookup "I think if you stick around you will find that I am a very funny guy..."
            ed lookup "But I don't joke about my name."
            bio "Well...{w=0.1} what is your real name?"
            ed -lookup "We can...{nw=0.3}" 
            #play sound wink
            show ed blush
            extend "save that one for later, can we?" 
            # so you've initiated the impress him route 
            # what with him lowkey flirting with you and all, he'll tell you his real name if you charm him
            # but of course, out of respect, you won't publish it.
            bio "Oh,{w=0.1} all right..."
            show ed -blush
            $ nameroute = True
        "Keep it to yourself":
            $ renpy.block_rollback()
            "\"Ed\" cannot possibly be his real name.{w=0.1} But you're sure he has his reasons..."
    
    "You think about your deadline again and realize you need to cut back on some of your questions."
    bio "I need to cut back on some of these questions."
    "Right,{w=0.1} that's...{w=0.1} what I said?"
    show ed lookup
    "See,{w=0.1} now he's looking at you funny."
    "Don't bite your lip!"
    show ed smug
    "He's reciprocating.{w=0.1} {cps=*0.5}Unbelievable.{/cps}"
    show ed -smug
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
            ed "Don't be. {nw=0.5}"
            show ed smug with None
            extend "I'm evil."
            "You furrow your brow in concern,{w=0.1} or is it fear?"
            "You're not sure why it would be either because you already knew he was a warlock."
            ed -smug "That was supposed to be a joke."
            bio shocked "Oh."
        "I'm not surprised":
            
            "He chuckles at your blasé response."
            bio "At our paper,{w=0.1} we call warlocks with good childhoods priests."
            "He snorts,{w=0.1} then covers his mouth to keep the giggles at bay."
            ed blush "I mean,{w=0.1} it's true.{w=0.1} And they certainly aren't immortal."
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
    
    if affection > affectionthreshold:
        $ endearing = True

    return

label offended:
    $ affection -= 1
    if affection <= 0:
        $ affection = 0
    
    if affection <= affectionthreshold and e_firsttime == False:
        "You've definitely lost your favor with him."
        $ endearing = False
        $ favorlost = True
        
    elif o_firsttime == True:
        "..."
        "He seems offended."
        if affection > 0:
            "Let's try to avoid that."
    elif affection == affectionthreshold+1:
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
    ed lookup "Hold up.{w=0.1} I'm not a Virgo."
    bio "Your entry on the Valkyrie Compendium of Known Agitators has your star sign listed as Virgo."
    ed "Well it's wrong."
    ed "What are you gonna do,{w=0.1} argue with me? {w=0.1}It's wrong."
    ed fakeout "I wasn't born in freaking September."
    menu:
        "The Valkyrie Compendium is the most factual encyclopedia on magic ever written,{w=0.1} so..."
        "Insist he's a Virgo":
            "He acts like one, anyhow."
            bio sad "I would rather not contradict the Order of the Valkyries."
            ed angry "That's fine.{w=0.1} But I'm not no damn Virgo."
            jump interviewintro
        "Ask him his sign":
            pass

    bio "When were you born,{w=0.1} then?"
    ed lookup "October 9. {w=0.2}Write that down." 
    "You scratched out Virgo and wrote Libra."
    $ starsign = True
    
    bio "Now that that's out of the way- {nw}"
    ed angry "A September birthday...{w=0.2} \"Virgo.\"{w=0.2} {cps=*0.3}Tchhhhhhhh... {/cps}{w=0.2}A September birthday?"
    ed lookup "I'm sorry,{w=0.1} you can continue."
    "He reaches out,{w=0.1} as if to put his hand on yours,{w=0.1} but your chairs are too far apart.{w=0.1} You nod and smile."
    bio "Okay."
    call endeared
    jump interviewintro
    return

label jacket:
    $ jacket = True
    $ stareflag += 1
    bio happy "Where did you get that sleek,{w=0.1} luxurious jacket?"
    ed blush "Oh,{w=0.1} this?{w=0.1} It's designer."
    "You stare at him.{w=0.1} He stares at you."
    "You stare at him...{w=0.1} He stares at you."
    bio -happy "Which...{w=0.1} designer?"
    ed -blush "Rick...{w=0.1} Owens...?"
    "You stare at him some more.{w=0.1} He cocks his head."
    "You narrow your eyes..."
    menu firstlie:
        ed lookup"What?"
        "Tell him he's lying":
            ed angry "Seriously?{w=0.1} We just started."
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
        ed smug "What,{w=0.1} you like it or something?"
        "I might":
            ed lookup "You might?"
            ed smug "Okay,{w=0.1} I mess with it." #he's flirting
            show ed -smug
            call endeared
        "Just curious":
            ed -smug "Ooookay."
    jump interviewintro
    return

label interviewintro:
    "You let out a breath."
    bio "Well."
    bio "Now that that's out of the way,{w=0.1} I wanted to get into the big discussion."
    bio happy "You know,{w=0.1} the question I'm sure everyone's always wanted to ask you-{nw=0.1}"
    ed fakeout "What my involvement was with all those divorces in the 1920s?"
    bio shocked "E-excuse me?{nw=0.1}"
    ed -fakeout "Oh,{w=0.1} you want to know how many Ph.Ds I have." #"silly me, I can't believe I didn't think of that first!"
    menu:
        "What? No!":
            bio -shocked"I mean,{w=0.1} no.{w=0.1} Sorry."
            bio "I didn't mean to yell."
            ed thinking "You can yell.{w=0.1} If you want to."
            bio shocked "Like...{w=0.1} like,{w=0.1} at you?"
            ed "At anyone.{w=0.1} At me,{w=0.1} too.{w=0.1} If I'm being a bonehead." 
            ed -thinking "You can."
            "His nonchalance was charming before,{w=0.1} but now it's starting to throw you off your game." 
            bio -shocked "It's time to tap in."
            ed "Okay."
            bio sad "I mean,{w=0.1} that's not what I meant to ask you."
            ed thinking "Go on."

        "You have multiple??":
            ed lookup "I might."
            "You stare at him.{w=0.1} He stares you."
            "You stare at him...{w=0.3} He stares at you."
            if stareflag >= 1:
                "You...{w=0.3} are starting to get tired of this."
                $ stareflag +=1
            else:
                pass
            ed -lookup "Hey."
            ed lookup "Stop starin' at me with those big old eyes."
            "You try batting your eyelashes with what you think is a coquettish expression."
            "You're not sure if it came off as such or if it was more of a drunken hand-eye coordination exercise." 
            "You decide to move on."
    bio happy "My question{w=0.1}—it's fairly straightforward{w=0.1}—I want to know just how you became an immortal wizard!"
    ed thinking "Mm."
    bio "It's one of my favorite questions."
    bio "Of all the fine,{w=0.1} magically-inclined folks I've interviewed,{w=0.1} I've always asked the same question,{w=0.1} but I've never gotten the same answer!"
    ed -thinking "Well, if you wanna hear about that..."
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
        ed lying "It was when I turned thirty in 1430.{w=0.1} Pretty easy to remember,{w=0.1} right?"
        "I suppose so":
            show ed -lying
            pass
        "You're how old, again?":
            ed lookup "Thirty."
            bio "Right.{w=0.1} Of course."
            bio angry "And just how {i}long{/i} have you been thirty,{w=0.1} hm?"
            ed -lookup "{cps=*0.8}Since...{w=0.1} {w=0.1}14...{w=0.1}30.{/cps}"
            bio -angry "Oh.{w=0.1} Oh yeah."
            bio sad "Carry on."

    $ renpy.fix_rollback()
    ed "My girlfriend at the time wanted to try out some different waters,{w=0.1} and especially different fish." 
    ed "So with my studies finished,{w=0.1} we figured it would be the perfect time to try somewhere new,{w=0.1} and we swam up to Portugal."
    bio happy "That sounds so romantic!"
    bio shocked "Wait...{w=0.1} what do you mean you {i}swam{/i} to Portugal?"
    ed lookup "Well, you see,{w=0.1} swimming is when you place your legs in the water and-{nw}"
    bio sad "I know what swimming is."
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
            ed -lookup "I mean...{w=0.1} It's a coastal nation with pretty easy access to the sea."
            bio "That's not what I meant."
            ed "Then what did you mean?"
            bio "That's...{w=0.1} well..."
            bio shocked "You swam by yourself?"
            ed fakeout "{w=0.1}...Did I not say I was with my girlfriend?"
            bio "You {i}and{/i} your girlfriend swam??"
            ed smug "Well yeah it's not like she could walk."

        "You're insane for alleging that you swam to Portugal from anywhere.":
            ed "Lawyer says what?"
            bio shocked "What?"
            ed smug "Heh.{w=0.1} Gottem."
            "Sigh.{w=0.1} He freaking got you."
    $ renpy.fix_rollback()

    ed -smug "So are we clear on how I got to the Kingdom of Portugal or are we still working out the mechanics of swimming?"
    bio -shocked "I'm done.{w=0.1} Let's get back on track."
    "You're not done!"
    bio sad "It's just,{w=0.1} I'm a bit confused."
    ed lookup "By what?{w=0.1} My ex-girlfriend and I swam to Portugal." 
    ed -lookup "She's a mermaid,{w=0.1} so it wasn't particularly difficult."
    menu:
        "Ohhhh. She's a mermaid!":
            ed thinking "Exactly."
            
        "You do not have a mermaid girlfriend":
            ed lookup "Correct.{w=0.1} I {i}had{/i} a mermaid girlfriend.{w=0.1} There's a difference."
            ed "Who would lie about having a mermaid ex?"
            bio angry "Many a fisherman have lied about mermaids."
            ed -lookup "No fisherman this century would lie about having a mermaid girlfriend,{w=0.1} let alone a mermaid {i}ex.{/i}"
            ed thinking "These days that's just plain embarrassing."
            bio -angry"Point taken."
    $ renpy.fix_rollback()

    ed -thinking "Once we landed,{w=0.1} we split up." 
    ed "I wasn't in the market to fish shop,{w=0.1} and besides,{w=0.1} I had heard that if you aren't at least a {cps=*0.7}little{/cps} bit bisexual in Lisbon,{w=0.1} 
    they straight up kill you."
    menu:
        "In the 1400s...?":
            $ homophobic = True
            ed lookup "Oh.{w=0.1} I see.{w=0.1}" 
            ed thinking "You think being bisexual wasn't invented yet."
            bio shocked "No,{w=0.2} I don't-{w=0.2} I wasn't-{w=0.2} I mean-{nw=0.2}"
            $ renpy.notify("Trait earned: homophobic!")
            ed  "Wowwwwww."
            $ homophobicbeliefs.append("bisexuals existed before David Bowie")
            "He shakes his head disapprovingly." #shit eating grin. fucking hater
        "Oh!":
            bio happy "You're bisexual!"
            ed lookup "Is it a surprise?"
            bio "I thought you were just...{w=0.1} a really sensitive guy."
            ed blush "I can be both."
            ed "After all, I'm bi, aren't I...?"
            call endeared
            call takenote("Ed is bisexual", True)
    
    bio happy "So you're wandering the streets of Lisbon,{w=0.1} waiting for your mermaid girlfriend to get fish." 
    bio -happy "And you come across some kind of powerful being,{w=0.1} right?{w=0.1} Another warlock,{w=0.1} or maybe an old alchemy book?"
    ed thinking "Not quite..."

    show devil at right with dissolve

    devil "I'm the Devil."
    ed "Now me,{w=0.1} I'm an industrious guy.{w=0.1}" 
    ed -thinking "I see The Devil and I think,{w=0.3} \"how can I profit off of such a one in a lifetime chance encounter?\""
    ed lying "There was this new economic system emerging called \"capitalism\" and I was dying to test it out."
    devil "I love taking advantage of emerging economic systems!"
    bio angry "But didn't capitalism emerge in the 16th century?"
    ed fakeout "Oh,{w=0.1} you're gonna argue with the guy who was there?{w=0.1} Is that it?"

    menu:
        "Remind him of the year":
            $ finesse = True
            bio "It was 1430."
            ed "And I was about to be rolling in it the way I finessed the #!*% outta that devil."
            ed "You're gonna love this.{w=0.1} I promise."
            "You make a note to yourself to edit that out of the transcript."
            
            
        "Ask him about the year":
            bio "What year was it again?"
            ed lookup "Like,{w=0.1} 1420-something.{w=0.1} Why?"
            bio happy "Just checking."
            call selecttrue("Ed turned 30 in the 1420s", "Ed turned 30 in 1430")
            $ yearcontradiction = True
            
        "Let him have it":
            "You mutter something under your breath about historical revisionism."

    ed "So I see The Devil standing there on the street curb,{w=0.1} and I know it's him because he's got these eyes like a husky." 
    ed "Piercing doesn't even begin to describe it{w=0.1}—they were glowing."
    show devil glow with dissolve
    ed thinking "So I see him standing there with his freaky{w=0.1}and I mean STRANGE bright blue glowing eyes and I say,"

    ed -thinking "\"How about we make a deal...{w=0.1} a business deal.\"" 
    ed lookup "Also I had the slickest braids on at the time where are my braids. You gotta include the braids."
    "Please, sir. We didn't have the time."
    bio sad "Please continue."
    ed -lookup "Right,{w=0.1} so he's like,"
    devil "I'm glad you noticed my eyes,{w=0.1} they don't call me Big Dog for nothing bark bark am I right."
    bio "I don't think he said that...{w=0.1} no one would respect a man called Big Dog."
    ed lookup "How do you know the Devil wasn't a woman,{w=0.1} by the way?"
    menu:
        "Because you said \"he\" earlier.":
            ed smug "Women can't be he/hims?"
            if homophobic == True:
                "You don't even bother this time and just let him have it."
            else:
                bio shocked "No, I- {w=0.1}"
                ed "No? They {i}can't{/i}!?"
                bio "They can, I just- {w=0.3}"
                ed thinking "You don't believe in gender-nonconforming women."
                $ renpy.notify("Trait earned: homophobic!")
                ed "Wowwwwwwww."
                "You stop sputtering and compose yourself."
                bio angry "I'm asserting myself as the interviewer and taking back control.{w=0.1} Please continue."
            $ homophobicbeliefs.append("women can use he/him pronouns")
        "Because men are the devil and you're the misogynist if you disagree.":
            $ misogynyaccusation = True
            ed thinking "Hm."
            "He shut up real quick."
            "You can't believe that worked..."
    
    ed -thinking "So one long series of contracts and spells later,{w=0.1} I made a deal with the devil.{w=0.1} I got to be thirty{w=0.1}—forever!"
    bio "What did he get?"
    ed lying "One of my Ph.Ds{w=0.1}—the one in fisherman's science." 
    ed thinking "I worked really hard on it, but education comes and goes when you never age."
    hide devil
    ed lookup "What's wrong?{w=0.1} You look disappointed."
    bio sad "I have to admit that was a bit anticlimactic."
    ed thinking "I never claimed it was climactic.{w=0.1} That was all you." 
    bio happy "Some of the stories about you claim to be climactic.{w=0.1} There's about one or two for every year you've been alive."
    ed lookup "Oh yeah?{w=0.1} You know they're all fake,{w=0.1} right?"
    
    menu exploits:
        "What about the time you stopped what would have been \"the next Pompeii?\"":
            ed "How could I do that?"
            ed lying "I don't speak Italian."
            $ italian += 1
            show ed -lying
        "What about the one where you had two religions founded after you?":
            ed thinking "Both were started by ex-boyfriends.{w=0.1} I guess I just inspire that in people."
            if endearing:
                ed lookup "Want to make the third?"
                bio blush "Ah,{w=0.1} well,{w=0.1} I.{w=0.1} Have.{w=0.1} To be professional,{w=0.1} you know!{w=0.1} I can't answer that on the clock."
                "He leans in."
                ed wink "How about off the record?"
                show ed smug
                "Your face is getting hot again...." 
                "No.....{w=0.1} his sweet tambour...{w=0.1}" 
                "You must focus....."
                show ed -smug

        "What about the time you trapped an entire town in an endless fog?":
            ed angry "Really?{w=0.1} {i}That{/i} story?"
            ed "What are you,{w=0.1} an authoritarian?"
            bio angry "You just admitted to being a capitalist."
            ed thinking "Game recognizes game."
            "Touché."
            bio shocked "Not touché!{w=0.1} I'm not an authoritarian!"
            ed angry "Then don't quote authoritarians at me.{w=0.1} That tale is Valkyrie slander."
            call offended
            show ed -angry
    show bg coffeeshop with dissolve
    show ed at move_to_center
    "You tap your notepad with your pen. That was...{w=0.1} a lot."
    "But the specifics of the deal itself seem to be a bit thin."
    "You wonder if you could get him to elaborate on this later..."
    
    ed lookup "Do you need a moment to take that all in?"
    ed -lookup "Because there's more."

    "To get a clearer picture of your subject, you decide to let him continue."

    jump renaissance
    return

label renaissance:
    show bg ship with dissolve
    ed "When you become immortal,{w=0.1} kicking around eating fish and talking to Portuguese mermaids starts to get real old after a while,{w=0.1} and my girlfriend could tell. "
    ed "She suggested we could swim down south,{w=0.1} stop by Rafat or Algiers on our way to Palermo..."
    ed "You know, make a vacation of it."
    bio "Aww, how sweet!"
    ed angry "Plus The Devil kept stopping me in the street asking when our business investments were going to pay off, and I just couldn't be bothered with all that anymore."
    show ed:
        linear 0.3 xalign 0.2
    show devil glow:
        offscreenright
        linear 0.3 right
    devil "Capital dividends stock marketing economics investiture let's circle on back stakeholders sunk cost corporate consultant-{nw=0.3}"
    ed fakeout "Listen,{w=0.1} Mr. The Devil?"
    devil "Yes?"
    ed -fakeout "I just feel like we need to rethink our strategy."
    devil "How do you mean?"
    ed fakeout "Some of these projections,{w=0.1} they're just not synergistic."
    devil "Not synergistic? ¡Dios mío!"
    "Dios mío, you say."
    menu:
        "Interrupt":
            bio -happy "He said dios mío?"
            ed -fakeout "Yeah."
            menu:
                "But he's Portuguese?":
                    ed lookup "Okay, he was like, \"Meu Deus.\""
                "But he's the Devil?":
                    ed lookup "Okay he was like... \"Diablo mío???\""
            pass
        "Do not":
            "Eh. He's paraphrasing."

    ed thinking "Anyway I was like."
    ed fakeout "\"We gotta do some corporate restructuring,{w=0.1}\" and stuff.{w=0.1} \"So you just sit tight...{w=0.1}maybe do some networking???\""
    bio angry "Eugh."
    "Even hearing corpo speak like that is making your mouth sticky."
    ed -angry "He nodded along like a dog-{nw=0.2}"
    bio -angry "Right, like a husky."
    show devil:
        linear 0.8 offscreenright
    ed lookup "And after he ran off I sold our assets and liquidated the company."
    hide devil
    if finesse:
        "You let out an \"ooooh\" under your breath."
        ed smug "Right? I told you you'd love it."
        show ed -smug
    
    menu:
        "Compliment":
            bio happy "You must have made a lot of cash from that."
            ed smug "I made a lot of {i}gold...!{/i}"
            show ed -smug
            pass
        "Move on":
            pass

    call selecttrue("Ed dabbled in mercantilism", "Ed dabbled in capitalism")

    if jacket:
        "That must be how he can afford designer clothes..."

    ed lookup "So! I hop in my boat and we set sail. Eventually, I get to Sicily."
    bio happy "Just you, or you and your girlfriend?"
    show ed at move_to_center
    ed -lookup "Uh...{w=0.2} just me."

    bio -happy "What happened?"

    ed thinking "We got separated."
    menu:
        "You mean she dumped you?":
            ed "No.{w=0.1} We got physically separated."
        "You mean you left her for another mermaid?":
            ed angry "{w=0.1}...Who do you think I am?"
            call offended
        "Separated how?":
            ed "We got into a really bad shipwreck."
            ed angry "It was...{w=0.1} ugly."
            bio "But you managed to survive,{w=0.1} right?"
            "He scoffs."
            ed thinking "Evidently."
    ed "Anyway."
    ed -thinking "Once I arrived in Sicily, everything changed." 
    ed "I couldn't find my girlfriend,the Italian mermaids wouldn't talk to me, my ship was destroyed..." 
    ed thinking "I was alone and effectively homeless."
    $ italian += 1
    $ mermaidmafia = False
    menu:
        "That's terrible!":
            pass
        "Why wouldn't the Italian mermaids talk to you?":
            $ mermaidmafia = True
            ed "The mafia."
            bio angry "Really?"
            ed lookup "Those women are stone cold."
            show bg black with dissolve
            "He stares past you,{w=0.1} into the distance."
            show bg coffeeshop
            "But...{w=0.1} there was only wall behind you."
            show bg ship with dissolve

    ed thinking "Once I managed to calm down and take a better look at my situation, I took the money I had liberated from The Devil."
    ed "I knew I needed to reinvent myself, so I decided I would do what I do best:"
    menu:
        "Seduce beautiful women":
            ed fakeout "Now I don't like your use of the word \"seduce,\" but I'm flattered you think I'm good at it."
            call endeared
            ed "But not quite."
            pass
        "Usurp the powers of other mages":
            ed thinking "FOR THE RECORD, there exists no evidence of me ever having done that."
            ed angry "Even your book suspiciously leaves it off because they know that it's a rumor."
            bio happy "You seem to know a lot about what's in my book. Have you read it?"
            "...He doesn't seem to want to keep talking about it."
            call offended
        "Clout chase":
            ed smug "That's right."
            pass
    ed lookup "I needed to get an education."
    ed fakeout "See, there was some sickness going around Europe at the time—something to do with rats?"
    ed lookup "Others called it a plague."
    bio happy "Some would even call it... the Bubonic Plague."
    ed -lookup "Eh! Maybe. {i}I{/i} called it{w=0.2} an opportunity."
    show bg black with dissolve
    ed "Soon enough I had that MD under my belt. But while my academic life flourished, my romantic life flatlined."

    menu:
        "I had no idea you were such a romantic...!":
            show ed lookup with dissolve
            "When he looks up to make eye contact with you, you don't catch a whiff of humor or wit or perhaps even whimsy."
            "He looks depressed."
            show ed -lookup
        "Say nothing":
            pass

    ed "With the mermaid mafia having ruined any of my attempts to fraternize with both the mermaids and mermen, and the townspeople not wanting to hang around somebody who just treated their neighbor for the plague," 
    ed "I headed up to the big city where all the magic was happening:{p=0.4}Florence." 

    ed angry "The thing they don't tell you about Florence is that absolutely nobody GAF about doctors in that city."
    ed -angry "I walked right in and those people were partying it UP, music, art, messy lesbian drama out on the streets."
    ed lookup "Let me give you an example."
    show cg csection with dissolve 
    ed "I meet this one guy. And his wife was going through labor, but the baby wouldn't come out, right?"
    ed "So I offered to perform a C-section on her, and he was all like,{nw=0.2}"
    "Man" "What's that,{w=0.1} that's stupid."
    "Man" "What do you mean you cut the baby out of the womb."
    "Man" "Hell no."
    ed "I'm like,{w=0.1} \"But this could be the baby that kills Macbeth.{w=0.1} {i}Trust{/i} me.\""
    ed "And he was like,{nw=0.2}"
    "Man" "Nooooo hahaha nooooo no one can kill Macbeth!"
    ed "Anyway she died of sepsis."
    hide cg with dissolve
    ed "And I thought to myself,{w=0.1} wow." 
    ed smug "These guys have nothing on the Ottomans."
    ed -smug "Whatever the people thought the plague was, they were convinced it wasn't in Florence." 
    ed "It was The Decameron in there."

    menu:
        "The whole point of the Decameron was that they {i}left{/i} Florence.":
            ed thinking "Hm. You say this, and yet you did not meet and talk with Giovanni Boccaccio."
            menu:
                "You met and talked with Giovanni Boccaccio!?":
                    ed smug "No. I did not."
                    show ed -smug
                "Who???":
                    ed smug "Exactly."
                    show ed -smug
        "Move on":
            pass        
    
    ed "Sure, I could have opened my own practice, or even found a clinic to work for, but I was lonely, and enough time had passed." 
    ed lookup "I was ready to be desirable again."
    ed -lookup "As I said before, doctors were out. What was in was inventing."
    show bg workshop with dissolve
    ed "So naturally I knew I needed to invent." 
    ed "I decided to take my studies to the engineering school, where I earned my next Ph.D."
    ed blush "It was a lot of hard work, sleepless nights...! And the mathematics and the prototypes...{nw=0.1}"
    "You cannot let him get distracted by his postgraduate studies, so you decide to prompt him a bit."
    bio happy "Well, surely the access to engineering gave you social clout, right? How did that work out for you?"
    ed -blush "Oh, very well. People had the expectation when you met that you would eventually start inventing for them." 
    ed lookup "And who am I if not someone who delivers?"
    bio happy "I don't know. You tell me!"

    ed fakeout "Well!"
    ed lookup "First I caught the attention of a tailor Lenù. We had fun together."
    ed "She often complained about the knives tailors used because they snagged the fabric and I thought: \"what if I combined two knives together?\""
    ed lying "And the scissors were born."

    bio angry "I thought Da Vinci invented those?"
    ed lookup "Leonardo owed me money, so I let him have the patent." 
    call takenote("scissors were invented by the Dark Mage Ed", False)

    bio -angry "What did your tailor girlfriend think of the scissors?"
    ed blush "Oh, she {i}loved{/i} them; her work flowed so much faster, she was the pride of tailors everywhere. But..." 
    ed thinking "The problem with dating in Florence is that once you make the invention they've been waiting for, the relationship is pretty much over."
    bio sad "What? That's so sad..."
    ed lookup "That's just the way it was."
    ed -lookup "From Lenù, I had a lot of contacts in the textile industry. Once they saw my scissors, they were practically jumping on top of me to get their own invention."
    ed "I eventually wound up dating Lila, who owned a fabric workshop." 
    ed "She was sweet, and her dream was to make cloth of intricate patterns that could rival even the paintings of the city." 
    ed thinking "After thinking long and hard about it, I invented a loom that could weave any image into cloth."
    ed fakeout "Got that one from Anansi at a trickster convention. Funny guy, but you do {i}not{/i} want to get into a drinking competition with him."
    ed lookup "In a way, you could say I brought the gift of weaving to mankind."
    bio sad "Where have I heard that before...?"

    call takenote("Ed invented the modern power loom", True)

    label microwaver:
        ed thinking "Now, my greatest invention was not made for love or to impress someone." 
    ed "My greatest invention was made for self-satisfaction." 
    ed "I wanted to see if I could even do it."
    ed "A box that could heat anything inside it using electromagnetic radiation."
    bio shocked "The microwave?"
    ed lookup "The one and only."
    $ microwaveseen = False
    menu:
        "That's so cool":
            pass
        "Don't buy it for a second":
            if not endearing:
                ed -lookup "That's fine. You don't have to."
                jump aftermicrowave
            ed smug "Behold my most prized possession."
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
        ed thinking "It took a lot of trial and error, but I'd made a working prototype." 
    ed -thinking "I was ready to show it off to the world when disaster struck."
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
            bio -shocked "How did the mermaid mafia get-{nw}"
            ed "Hold on, hold on, I'm explaining."
        "Do not":
            pass    
    
    label afterdisaster:
        ed angry "They were jealous of my inventions, of the good I was bringing to humanity."
    ed "So one night they snuck into my house and raided of all my inventions... my beautiful inventions..."
    ed "This was worse than the Library of Alexandria getting burned... they stole my prototypes and threw them in the sea."
    
    if not issueraised:
        menu:
            "Interrupt":
                $ issueraised = True
                bio -shocked "But there's no-{nw}"
                ed -angry "Hey, hey, hey, I'm having a moment here."
            "Not yet":
                pass

    ed angry "If that wasn't enough, they also pulled out their grubby little claws and ripped everything to shreds." 
    ed lookup "Except for the bottles of nail polish, which I also invented by the way. They kept those for themselves."

    if microwaveseen:
        bio -shocked "If they tore apart everything, how did you manage to rescue the microwave?"
        ed -lookup "At the time, I was workshopping a new magic... They call it void-hopping now, but I mainly used it for storage."
        ed "This is how I've been able to keep my lifeforce safe from fatal accidents, but it's also where I kept my microwave."
        ed blush "His name is Michael."
        ed -blush "Unfortunately, at the time, my void dimension was only big enough to fit a few things."
        ed thinking "I couldn't rescue the other inventions."
        "Seems awfully convenient..."
        "But, y'know." 
        "The proof is in the microwave."

    ed angry "I was furious, but what was I supposed to do?" 
    ed thinking "I couldn't drag them out of the water, and I knew if I fell in, they'd tear me apart like they did the prototypes..."

    if not issueraised:
        menu:
            "Interrupt":
                $ issueraised = True
                bio sad "I just don't know if-{nw}"
                ed -thinking "Hang on, I gotta finish this thought."
            "Keep holding it in":
                pass

    ed thinking "I started chucking rocks into the ocean, hoping to hit some of them." 
    ed "I was yelling at the beach, grabbing whatever stones I could find and launching them at the mermaids."

    if not issueraised:
        menu:
            "Interrupt":
                $ issueraised = True
                bio sad "But there's no-{nw}"
                ed "Wait wait wait, I'm almost done."
            "Just a little longer":
                pass

    ed fakeout "The city guard didn't like that. I was causing a public disturbance, and the mermaids were lining their pockets anyway." 
    ed angry "Corruption everywhere... mermaids at my back... my exes had no use for me..." 
    ed thinking "It was time to get the hell out of Italy."
    ed -thinking "There. I'm done."
    
    if not issueraised:
        ed lookup "...Are you all right?"
        ed "You look like you have a burning question."
        menu:
            "Just one small problem":
                $ issueraised = True
                bio sad "Florence is landlocked."
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
                "You decided not to ask how the mermaid mafia got on land."
                pass
    else:
        ed "You were trying to say something earlier."
        bio "I..."
        "Don't tell me you forgot."
        bio sad "I forgot."
        ed "Wow. What a shame."
    show bg coffeeshop with dissolve

    ed lookup "Do you want me to keep going? I could talk about something else."
    "You're starting to get a feel for the kind of person Ed is." 
    "Scrappy, resourceful, in constant pursuit of knowledge..."
    "...and a bit of a flirt."

    if italian >=2:
        "Something is sticking out to you, though."
        menu:
            "Ed definitely speaks Italian":
                $ yourFacts += 1
                $ factscollect.append("Ed speaks Italian")
                "You quickly added it to your factoids."
            "Ed doesn't speak Italian":
                "You take him at his earlier word."
                "He was probably speaking to them in Latin... or something."
                pass

    bio happy "Go ahead."

    jump vampirecastle
    return

label vampirecastle:
    show bg black with dissolve
    ed "I moved around Europe for a while, kept up to date with my medical knowledge in areas that cared about the plague."
    ed "Had some fun with Ottoman mermaids (way chiller than the Italian ones), and wizards in Saxony."
    ed thinking "I had been wandering for some time in the Eastern or Central or perhaps even Northern regions of the continent—who's to say." 
    show bg castle with dissolve
    ed "It had been years since I had any time for quiet or study, and I had heard rumblings about a very quiet castle out in the middle of nowhere."
    ed "I thought perhaps I could get a job and live a few peaceful years in the countryside."
    ed fakeout "Some guy named Napoleon was taking over half of Europe and frankly, I didn't want to get involved." 
    show ed at move_to_left
    ed -fakeout "When I arrived it was a cold and chilly night, a little eerie. When I knocked on the entrance to the castle, only one person answered."
    # play sound thunder
    # play music organ noloop
    show layla:
        offscreenright
        linear 1.5 person_d
    "Layla the Terrible" "Oh, hello why aren't you a tall drink of water."
    bio -happy "Did she really say that???"
    ed fakeout "Would you rather she say something like, {nw=0.5}"
    # play sound slidewhistle
    show layla:
        linear 0.5 offscreenright
        pause 1.0
        linear 1.5 person_d
    # play music organ noloop
    $ renpy.pause(3.0)
    "Layla" "Come (wink wink) into my castle sexy warlock I will feed you grapes while I suck your blood."
    "Ew."
    bio sad "I really wouldn't."
    ed thinking "Okay then. When I arr-{nw=0.2}"
    bio shocked "Wait, {i}blood?{/i}"
    ed lookup "What?"
    ed -lookup "Oh, yeah. She was a vampire."
    show layla:
        easeout 0.3 offscreenright
    show ed at move_to_center
    ed "When I arrived, Layla had just bought that castle."
    ed "She had big plans for it: a massive library, elaborate dining room, giant vat of blood in the kitchen."
    ed fakeout "Yeah she had vampires all over the place, but it wasn't {i}too{/i} bad in the beginning..."
    ed thinking "During the day I'd sit in the library and read,"
    ed -thinking "and at night the vampires ran around doing whatever it is vampires do I really don't give a f**k."
    
    menu:
        "They suck blood.":
            ed lookup "Okay well some vampires suck ass."
            if endearing:
                ed smug "Don't ask me how I know."
        "I think they suck blood.":
            ed lookup "You think, huh?"
            ed blush "What else do you think in that pretty little head of yours...?"
            bio blush "..."
            call endeared
    show ed at move_to_left
    ed lookup "Anyway, she was about to start ramping things up around there. Unfortunately for me."
    show layla:
        linear 0.5 person_d
    "Layla" "Edward I have a proposal for you."
    ed thinking "Not what I'm called."
    "Layla" "You're always going on about all those Ph.D.s you have..." 
    "Layla" "Surely a man with a big strong brain such as yours pines for another one, yes?"
    ed blush "Darn... I can't say no to another Ph.D..."
    hide layla with dissolve
    ed -blush "The hot new science of the times was chemistry, and Layla was willing to pay out." 
    ed fakeout "All I had to do was \"donate\" some of my blood from time to time." 
    ed -fakeout "Otherwise, I had the best books, highest quality equipment, and some of the best teachers at my disposal."
    bio angry "So this is another story about your Ph.D.s?"
    ed "Is-{nw=0.1}"
    ed lookup "Is this not an interview about my Ph.D.s?"
    "No."
    "It is not."
    bio sad "You can continue."
    ed -lookup "While I studied, the vampires continued to come and go." 
    ed "Many of them visited from all around the world and had traveled great lengths." 
    ed "Some brought me treats or candies from their homelands. Others would quietly stare before shuffling off."
    ed thinking "For a period there was even one, Eskender, who would come all the way from Abyssinia." 
    ed blush "He would pop into my study for a chat each time he visited and ask about my research. "
    ed "We would sometimes have philosphical conversations that went on well into the night."

    ed -blush "When I completed my studies, everyone seemed a little {i}too{/i} excited." 
    ed "I was hoping to apply the knowledge to my backgrounds in medicine or engineering. But Layla had other plans..."
    show layla at person_d with dissolve
    "Layla" "Darling Edmund how was chemistry."
    ed blush "It was great." 
    ed -blush "Unlike alchemy. Which was wrong."
    show ed lookup
    "Layla" "Yeah okay whatever."
    "Layla" "As you know, I have regular clientele that visit this castle from afar." 
    "Layla" "They come in search of a very particular product."
    show ed -lookup
    "Layla" "One they can usually only get from beyond the seas, which we've been importing for some time..."
    "Layla" "...but which would be not just more economical but hugely lucrative to synthesize in-house."
    ed blush "You mean they don't have to pillage Afghanistan to mine lapis lazuli anymore?"
    show ed lookup
    "Layla" "What? No. It's drugs. I'm talking about drugs."
    "Layla" "Idiot."
    show layla:
        linear 0.8 offscreenright
    #she slides off screen to the right
    bio -sad "Drugs for vampires, huh?"
    menu:
        "Are they different from regular drugs":
            ed lookup "Look. This German guy came up with this cutting edge wacky stimulant class called amphetamines."
            ed angry "But these vampires were so old, they didn't even know what heroin was."
            ed -angry "So I mainly made that."
            ed "So not really????"
            
        "Why did you agree to make drugs":
            ed "By this time I already had an active warrant out for my arrest."
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
            ed lookup "Also I'll do anything for a paycheck."
    $ renpy.fix_rollback()

    ed thinking "The more drugs I made, the more vampires came. The more vampires came, the rowdier they got."
    ed "And after certain crowd came in, Eskender stopped visiting."
    ed lookup "Now, this new group didn't just stare." 
    ed angry "They were obsessed with asking me when I was going to become a vampire so it would \"fix\" my complexion."
    menu:
        "Yikes":
            pass
        "Yikes on bikes":
            ed -angry "\"Yikes on bikes...\""
            ed blush "Adorable."
            call endeared
    ed thinking "It was becoming unbearable, and I had started drafting up plans to leave it all behind..." 
    ed "Until one day."
    show layla at person_d with dissolve
    "Layla" "What if we rounded up all of the humans and started breeding them like cattle?"
    "Layla" "That would keep me fed for an eternity!"
    ed shock1 "..."
    ed shock2 "..."
    ed "Okay that's enough."
    hide layla with dissolve
    show bg black
    show ed at move_to_center
    ed thinking "What Layla didn't know was when I wasn't in the lab, I was building and collecting weapons."
    if endearing:
        ed lookup "And working out. I was also working out a lot."
        bio blush "Wow..."
    ed thinking "All of the schmucks in Layla's castle were just too drunk, high, or both to notice."
    hide ed with dissolve
    ed "So when the time came for me to show my hand..."
    #play sound alert
    $ renpy.pause(0.5)
    show cg slaughter
    ed "I made quick work of that frat house."
    bio -blush "You defeated them all?"
    ed lookup "Every last one of them was either staked, silvered, or garlicked."
    hide cg with dissolve
    show ed with dissolve
    ed "I swiped her valuables too. Since she wasn't gonna need them anymore..."
    menu:
        "Stealing from a vampire castle?":
            ed angry "Technically it was ALSO MINE. WE made that money." 
            ed "TOGETHER."
            "Is he... sulking?"
        "What did you take?":
            ed thinking "She loved jewels and precious stones and things. Had a lot of art in there, too." 
            ed "I took those to repatriate."
            ed "Other than money, I had to take my research."
            ed -thinking "There was a little recipe I was working on that produced a brilliant blue pigment..."
            ed wink "You might know her."
            show ed -wink
            call takenote("Ed discovered ultramarine blue", True)
            pass
    $ renpy.fix_rollback()

    show bg coffeeshop with dissolve
    #move ed back to center
    "You take diligent notes of his vampire exploits."
    "You're particularly in awe of the way he stood up to Layla the Terrible..."
    "Although it sounded like his feelings toward that time were more complex than he let on."
    "What was up with that?"

    ed "Hey."
    "You look up from your notebook."
    ed lookup "Do your job." 
    ed "You've been letting me yap too much with no direction."
    show ed -lookup with dissolve
    "He's right. He's ready for your next question."
    "...only, you spent your best question already. It was the one about the immortality deal." 
    "And his answer kind of sucked."
    "You reach back into the recesses of your mind for an interview question that could inspire a tale as riveting as the one he just told..."
    bio happy "Tell about a time you struggled."
    "What was that!?"
    "You want to press your fists into your forehead, but you've got to keep your composure."
    "Luckily, it looks like something in his brain is turning..."
    ed lookup "You want to hear about my English Literature degree."
    bio "I don't want to hear about the degree."
    bio angry "At all."
    bio happy "But the setting sounds primed for adventures."
    bio -happy "You could talk about that."
    ed thinking "All right, no problem..."

    jump classiclit
    return

label classiclit:

    show bg library with dissolve
    show ed at move_to_left
    #move ed to the left again
    ed "When I enrolled at the university, they gave me the option to have an apartment out by myself." #it's never named but my guess is it's cambridge
    ed "But I was tired of living in countryside inns and small hostels after leaving the vampire castle, so I instead took the option to get a roommate."
    #play music roommate
    ed "My roommate... Пётр Александрович Соколов." 
    ed angry "He really thought he was going to be somebody important and would make everyone call him by his full name."
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
                ed lookup "How close we talkin'?"
                "I mean they were roommates":
                    if homophobic:
                        ed "Sure."
                    else:
                        ed "It was closer than that."
                "Probably best friends?":
                    if homophobic:
                        ed "Sure."
                    else:
                        ed "...It was closer than that."
                    pass
                "Oh they were doin' it":
                    if endearing:
                        bio "I'm just curious if you two... were ever..."
                        bio happy "You know, if it wasn't just books you were studying."
                        ed blush "..."
                        show ed -blush
                    else:
                        "You bite your lip a little too hard. It starts to hurt...!"
                        "To make it feel better (and to cover it up), you lick it with your tongue..."
                        $ renpy.notify("Trait gained: fujoshi!")
                        "But to Ed, it looks like you're salivating over the thought of him and his roommate."
                        "To your credit, he doesn't seem to care."
                    "You make a note of Ed's pretentious Russian boyfriend."
    $ renpy.fix_rollback()

    ed "Anyhow..."
    ed thinking "To call [petya_dn] obsessive and paranoid was an understatement."
    ed "He thought the students in his classics program were out to get him." 
    ed "That people were writing magic spells in the library books, or leaving secrets only for him to find."
    bio -happy "So why did you stick with him?"
    ed -thinking "We were the only non-Anglo students in the school, so we just connected with each other, I guess." 
    ed blush "And he really seemed to like me." 
    ed -blush "He was always asking me to help him study or cook. He confided in me a lot about the insane beef he had with his classmates and professors."
    bio "Let me guess: it was asinine and petty?"
    ed angry "Absolutely. There was an endless stream of names for people whose many slights against him I couldn't keep track of." 
    ed "This person looked at him and gave him the evil eye, that person chose to study an author he didn't think had any merit, so on and so forth."
    ed blush " Still, he was affectionate to me...{w=0.3}and he had nice hands..." 
    ed "I would feed him info and insights into the magical world while he lay with his back on my legs..."
    bio "Info or lies?"
    ed lookup "Perfectly legitimate information."
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
    if endearing:
        bio happy "But he was always barking at people."
        ed blush "Yes, you get it!"
    ed fakeout "But soon, [petya_dn] started getting worse. He wasn't sleeping, he barely ate anything, and he stopped coming to our dinner nights." 
    ed "One of his classmates had plagiarized a section from one of his papers, and that was a breaking point." 
    ed thinking "He completely and utterly lost his marbles."
    show petya at person_d
    petya "Ed, you gotta help me man. I messed up."
    ed shock2 "What in the world!?"
    petya "I don't even know what happened... I lost control of myself..."
    petya "Y-you told me I should stand up for myself, but I... I went too far... he's..."
    ed thinking "{size=+20}[petya_dn].{/size}"
    ed "{size=+20}I never told you to kill anybody.{/size}"
    petya "I know, I know, but..."
    petya "You gotta help me. Please? It'll be just like old times!"
    ed -thinking "I couldn't say no to that, mainly because I was worried that if I didn't do anything, he was going to find a way to rope me in anyway." 
    ed thinking "So I figured it was better to take control of the situation myself..."
    bio sad "What did you end up doing???"
    show cg framed
    $ renpy.pause(0.5)
    ed smug "We framed the murder on someone else."
    hide petya
    hide ed
    bio shocked "WHAT."
    ed fakeout "Some goofball studying this newfangled thing called computer science?"
    show ed smug at person_a with dissolve
    ed smug "He didn't know what hit him."
    hide cg with dissolve
    bio "WHEN WAS THIS."
    ed thinking "Later that night, we packed up and fled the country."
    bio "OH MY GOD?"
    ed lookup "What's the problem? You didn't seem to have a problem with all those vampires I slaughtered."
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
                    show ed -smug
                    pass
            pass
        "I guess you're right":
            pass

    show ed at move_to_center
    bio sad "Okay, fine. What happened afterwards?"
    bio happy "A relationship tested through the flames should be able to survive, right?"
    ed "Not really. I guess we could only relate to each other through that brief period."
    show bg black with dissolve
    ed "We were on the run together for a little while, but we decided to split up." 
    ed thinking "I tried to keep in contact with him, but after a few letters, I never heard from him again."

    if itwasinfo:
        bio sad "I can hardly imagine why. You helped him through so much."
        ed fakeout "If I'm being honest, I'm not too proud of what I helped him with!"
        "He's laughing like it's a joke, but..."
        show ed -fakeout
    else:
        bio -happy "I can see why. You basically drove him to madness."
        ed lookup "Huh? What makes you say that?"
        bio angry "If I can be frank for a bit, he was already a nervous wreck."
        bio "He didn't need you filling his head with magic and sweet nothings."
        ed angry "E... excuse me...?"
        call offended
        show ed -angry

    ed "Anyway, if I had to relate it back to the question, {nw=0.3}"
    bio happy "Oh! Right."
    bio sad "That."
    "You had nearly forgotten about the question (probably because it sucked)."
    ed "the degree itself wasn't too tough since I had already seen Shakespeare's plays in person."
    ed "What I really struggled with was..."
    ed "I don't know..."
    ed thinking "Sometimes I close my eyes and I see [petya_dn]'s sad wet little eyes."
    ed "And his hands and face covered in blood."
    bio "In like a creepy way?"
    ed smug "No, it's really really attractive."
    menu:
        "So you were struggling with your sexuality" if homophobic:
            ed angry "No, what the-{nw=0.3}"
            ed lookup "What's your damage?"
            call offended
            pass
        "It sounds like your recent partners weren't very nice":
            ed -smug "They weren't."
            if endearing:
                ed thinking "They were kind of awful..."
                ed "But every time they left I felt like..."
                ed -thinking "I felt like I had a gaping hole in my heart."
                "You tilt your head in interest."
                "You wish you could fill that hole..."
                ed smug "Don't go getting ideas about filling any holes."
                bio blush "ED!"
            pass

    show bg coffeeshop with dissolve
    show ed at move_to_center
    ed thinking "Anyway. That's what comes to mind..."
    bio happy "All right."
    "You start to notice a theme emerging in the tales he's spinning."
    if yourFacts < 4:
        "Although, you're having trouble telling fact from fiction."
    "It could be a mere fluke, so you decide to prompt him one last time, just in case it doesn't show..."
    "But you're sure it will."
    $ bodycountcount = 0
    menu fear:
        "What is your body count" if bodycountcount <=0:
            $ bodycountcount += 1
            ed shock1 "I,{nw=0.5}"
            show ed shock2
            extend "like,{nw=0.5}"
            show ed shock1
            extend "feel really objectified by that question."
            call offended
            bio happy "I was being facetious."
            ed thinking "Even still."
            bio sad "Sorry. Let me try that again..."
            jump fear
        
        "Why are you afraid of being single" if bodycountcount< 0:
            ed angry "You're two-for-two on jackass behavior in the same in-game menu."
            bio sad "I'm trying to hint at something."
            ed -angry "You could be a little more subtle."
            call offended
            "That didn't net you an answer."
            "You try to reword your prompt so that it's less confrontational."
            pass

        "You don't spend a lot of time by yourself":
            ed lookup "Well of course not!"
            ed "The only reason anyone would become immortal is to spend more time around other people."
            bio happy "Or take over the world."
            ed angry "No one who wanted to take over the world would waste time doing interviews for a publication as dubious and unreliable as yours."
            ed "They'd be too busy taking over the world. And your s**t-for-brains boss would glaze them for free."
            ed lookup "No offense to you."
            bio "None taken."
            bio -happy "The paper has a slant."
            ed -lookup "Yeah, a big one. It's harming your credibility."
            if yourFacts >= 4:
                ed "Your writing is waste on that joint."
            bio happy "You said something interesting just now, though..."
            "You return to the big gap you left for the immortality deal. You're starting to recontextualize it in your head..."
            "You add \"wants to be around other people\" to the comically short list of bullet points{w=0.2}—right underneath the part where he ran the scam."
            "But he talked about it so briefly..."
            "You try to reword your prompt so that it's more specific."
            pass
    
    bio happy "Is there a moment would you say is emblematic of your biggest fear?"
    ed fakeout "What?"
    show bg black with dissolve
    ed lookup "Why not just ask me my biggest fear?"
    bio happy "Because I have a feeling I already know what it is!"
    bio -happy "Also, if I've got you pegged correctly, you wouldn't answer a question like that, now would you?"
    ed thinking "True."
    if endearing:
        "You thought you saw him light up for a fraction of a second."
    ed -thinking "Okay, here goes."

    jump film
    return


label film:

    ed lookup "I moved to Los Angeles."
    menu:
        "I've heard enough":
            $ renpy.block_rollback()
            $ earlyend = True
            ed lookup "Really? Okay."
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
            hide ed with dissolve
            hide screen bookbutton with dissolve
            show bg black with dissolve
            jump gooseygoo

        "Oh the inhumanity":
            ed -lookup "Where was I supposed to go?"
            ed smug "Ohio?"
            "You nod your head in concession."

        "Go on":
            pass

    # play music smartwomen
    ed thinking "I had spent decades in countries with rotten weather when I decided I'd finally had enough."
    show ed at move_to_right
    ed lookup "I {i}needed{/i} to go somewhere with warm winters." 
    show bg movieset with dissolve
    ed blush "Besides, the talkies had just come out and I wanted to have some fun."
    bio "At the movies."
    ed "Yeah."
    bio happy "So what got you interested in film?"
    ed -blush "In truth, I became interested in film when I realized someone had brought one back in time to scare and confuse me."
    menu:
        "Are you joking kidding me":
            ed lookup "About what?"
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
            bio "Oh, wow!"
            bio "I'd love to watch it with you some day."
            if endearing:
                ed lookup "Don't take this the wrong way, but I wouldn't watch that movie with you."
                ed thinking "...not yet, at least."
                ed -thinking "Maybe {nw=0.5}"
                show ed wink
                extend "{i}Challengers{/i} would be more your speed."
                show ed -wink
                
            else:
                ed lookup "Oh."
                ed fakeout "(Does she know...?)"

    call takenote("Ed was shown a movie before they ever existed", True)     

    ed lookup "So my first day in the city, I was approached by someone on my walk to the grocery store."
    ed -lookup "I had just the look Hollywood was going for. Handsome but approachable, charming, and soft."
    $ moviedoubt = False
    menu:
        "As you do":
            pass
        "Are you sure":
            $ moviedoubt = True
            bio "Ed, if I'm to believe you, that means that you were playing the black gentleman some 20 years before Sidney Poitier ever started acting."
            ed lying "He got it from me."
            bio angry "Did he now?"
            ed lookup "Yeah, he was quoted as once having said,{nw=0.1}"
            show ed wink 
            extend "\"That man Ed is probably greatest to ever do it.\""
            bio "That is not what he said."
            ed lookup "Yeah."
            ed -lookup "Maybe not."
            pass
    ed -lookup "I'd compliment the ladies and the men on screen. I had the potential to be a star and I figured—yeah, why not."
    show cg filmset with dissolve
    ed "My first role was as a man in a ballroom who is sitting at a table waiting for his date." 
    ed "The lead actress comes up to me and asks if my seat is free. I prop my arm around my chair and smile at her and say,"
    ed "\"Not right now, darling, but I might have some space later.\""
    ed "I delivered that line and my fate was sealed." 
    ed "Critics raved, \"Who is that background actor with a single voiced line? Really pulls the whole film together.\""
    ed "Audiences couldn't get enough of me."
    if moviedoubt:
        bio happy "Now that you mention it, I remember seeing this movie."
        bio -happy "I had to watch it for an elective I took in college."
        ed "So how much of this story do you already know?"
        bio happy "Not much. You can continue."
    hide cg filmset with dissolve
    ed thinking "Suddenly I was the hottest guy anyone had seen or heard of in the motion picture business."
    ed "The best friend in a screwball comedy, the uncle in a serious play adaptation, the romantic lead—"
    ed "the roles just kept on coming." 
    ed smug "Not to brag, but I was absolutely killing it in all of them."
    ed -smug "Everyone praised my ability to command a scene, the ease with which I held myself," 
    ed "the casual and charming way that I talked about the 1700s like I had been there for it." 
    ed blush "Everyone {i}loved{/i} me."
    bio happy "They all {i}loved{/i} you, you say?"
    ed angry "Yeah, they loved me a bit too much, because here's where it starts to get wacky."

    ed thinking "I lived in a modestly-sized house tucked away in the Hollywood Hills, with a view of the ocean." 
    ed -thinking "I mostly kept out of the public eye and hardly engaged with my fans." 
    ed lookup "In a way, you could say I played hard to get. I thought it added to my gentlemanly charm."
    ed -lookup "Bit in retrospect, it may have ended up compounding the problem..."
    ed thinking "It all started with the after work drinks and cast wrap-up parties."
    ed "Day in and day out, I am surrounded by beautiful women and handsome men as far as the eye can see..."
    ed -thinking "So I cave. And I buy people a few drinks here and there, and invite some of them over to my house..."
    bio angry "Just some of them?"
    menu:
        "He was throwing modestly-sized informal gatherings in his humble abode":
            "You wonder if you trust this man a tad too much."
            pass
        "He was throwing some crazy parties in that mansion, yo":
            "No doubt."
            $ yourFacts += 1
            pass
    $ renpy.fix_rollback()
    "He shifts in his seat a little bit. You get the feeling he may have undersold some details..."
    "You brace yourself for what's about to come next."
    bio -angry "So who were these people who had you in their favor? Anyone I know?"
    ed fakeout "Well..."
    ed "Rock Hudson, Anna May Wong, Katherine Hepburn, Eartha Kitt, James Dean,{nw=0.2}"
    bio "Wow,{w=0.1} that's-{nw}"
    ed -fakeout "Josephine Baker, Rita Hayworth, Paul Robeson, Anthony Perkins, Paul Newman...{nw=0.3}"
    ed lying "...Zendaya{nw=0.5}"

    "Zendaya? Seriously?"
    menu:
        "You did not sleep with freaking Zendaya":
            # pause music
            ed -lying "ok maybe not zendaya maybe like {w=0.4} pedro pascal{nw}"
            bio angry "Ed.{nw=0.3}"
            ed thinking "Okay."
            ed blush "The other ones were real.{nw}"
            bio "I know."
            ed -blush "Okay."
            ed thinking "Just making sure."
            $ yourFacts +=1
            # play music fadein 1.0

        "I believe it":
            pass
    
    ed thinking "I was having so much fun loving{w=0.1}—and being loved{w=0.1}—that I nearly forgot about the fact that it was the early 20th century in North America,{nw=0.5}" 
    ed "and actions like that have Consequences." 
    ed "You see, the first divorce you cause is kind of funny." 
    ed lookup "By the third, you start getting invited to the courthouse..."
    ed -lookup "It's pretty hard to be the cause of over fifteen divorces and not get the attention of your boss."
    bio shocked "{i}Fifteen!?{/i}"
    ed "The studio heads were pissed." 
    ed fakeout "If I hadn't been with their wives, I had been with their wives sisters,{w=0.1} or their wives sisters' husbands."
    ed wink "Or perhaps all of them at once."
    bio shocked "No s**t they were pissed. I would be, too!"
    ed -wink "Yeah, but they couldn't fire me because I was loved by the public too much, and no one was worried about communists infiltrating Hollywood yet."
    ed thinking "So it's not like I was going to be blacklisted."
    ed -thinking "Besides, if I got banned from a set I could just get one of my many lovers to sneak me back in."
    bio -shocked "In spite of it all, you still wound up on top."
    show bg black with dissolve
    show ed at move_to_center
    ed lookup "That is until the suits decided enough was enough." 
    ed thinking "Thirty eight divorces strong, I had to be stopped."
    ed "If they couldn't fire me, and they couldn't ban me from the studios, they decided to take drastic measures:"
    ed lookup "they had to go to the United States government." 
    ed -lookup "Movies were going too far, and a governing body had to be put in place to stop them."
    bio shocked "{size=+20}You mean you caused the creation of the Hays Code!?{/size}"
    ed smug "Well? Joke's on them. I retired with my millions and spent the rest of the 20th century unburdened and unbothered."
    show ed lookup
    bio sad "And alone."
    ed thinking "..."
    ed "Yeah. And alone."

    jump currentday
    return


label currentday:
    show bg library with dissolve
    ed "Much later,{w=0.1} I went and got a Ph.D in film studies."
    ed -thinking "It was pretty easy since I was there for all of it."
    bio "So you just collect degrees, just because?"
    ed lookup "What? No. No one does that."
    bio "No one? I don't know how true that is."
    ed -lookup "You know what...? You could be right."
    ed thinking "Maybe there's someone out there who wants a doctorate to affirm their gender."
    bio "So you got your Ph.D.{w=0.5} Again."
    ed smug "Yes there's more I got more Ph.Ds."
    show ed -smug with dissolve
    "Sigh.{w=0.5} Again with the Ph.Ds?"
    "This is getting out of hand."
    $ degreeskip = False
    menu:
        "Tell him to hurry it up":
            $ renpy.block_rollback()
            bio "Ed, I don't know if we have this much time to dedicate to all of your postgraduate degrees."
            ed lookup "Really? Because I've been blowing a lot of hot air on s**t that really doesn't matter."
            ed "The Ph.Ds are the most important part."
            "You decide to be frank."
            bio "Ed."
            bio angry "No one cares how many Ph.Ds you have."
            ed thinking "Damn, okay." 
            ed -thinking "Famous last words though."
            $ degreeskip = True
            #play sound slidewhistledownup
            show bg coffeeshop with circlewipe
            jump afterPhd
            
        "Let him get them out of his system":
            $ renpy.block_rollback()
            "You throw your hands up (in your head, so he can't see you doing it)."
            "Whatever. More material is more material..."
            pass

    ed "It was the late 90s, a while after I got my Ph.D. in clinical psychology."
    ed lookup "I had just become a board-certified physician at the time, too, and my private practice was doing pretty well."
    ed -lookup "Since I had a bit of extra cash, I figured I could go back and do another program. One that was less sciencey."
    ed "Like I said, I was there, so it wasn't suuuper difficult."
    ed angry "But, my god, the papers, and the records?"
    ed "I was like, \"Is this film studies or archaeology?\""
    show ed at move_to_left
    show colleague:
        offscreenright
        linear 0.8 person_d
    show ed fakeout
    "Colleague" "It's called, \"doing research,\" Ed."
    show colleague:
        linear 0.8 offscreenright
    show ed at move_to_center
    ed thinking "But, you know, spending time in and out of libraries,"
    hide colleague
    ed "seeing patients,"
    ed -thinking "robbing banks to pay for my girlfriend's HRT..."
    menu:
        "E-excuse me!?":
            ed lookup "Oh, so now it's weird to want to support your girlfriend's transition."
            bio shocked "I- {nw}"
            if homophobic:
                $ homophobicbelief = renpy.random.choice(homophobicbeliefs)
                ed thinking "I know what you're gonna say."
                ed lookup "\"But Ed, I was talking about the bank robbing part!\""
                bio angry "I was! And I don't sound like that!"
                ed smug "Likely story from someone who doesn't believe [homophobicbelief]."
                if misogynyaccusation:
                    $ everywoman = renpy.random.choice(["Chaka Khan", "Whitney Houston"])
                    "You're about to let the moment pass when you remember your trump card:"
                    bio angry "Look, if you're not a misogynist, name every woman."
                    ed thinking "..."
                    "See? It worked again!{nw=0.3}"
                    #pause music
                    #play sound explosion
                    ed smug "[everywoman]."
                    bio shocked "..."
                    "..."
                    hide ed with dissolve
                    show bg black with dissolve
                    "You tried to close your eyes so you wouldn't have to look at his smug, irritating grin."
                    "But when you did, all you could see was him hitting the most ridiculous victory dance you could imagine."
                    show ed with dissolve at center
                    "You can't beat this guy."

            else:
                ed "Are you transphobic?"
                bio angry "I'm not!"
                $ renpy.notify("Trait earned: transphobic!")
                ed thinking "Wowwwwwwwww."
            if endearing:
                "He notices you pouting..."
                ed lookup "Hey."
                ed -lookup "I'm just kidding."

        "You mean like...?" if endearing:
            ed lookup "Like Al Pacino in {i}Dog Day Afternoon.{/i}" (multiple=2)
            bio happy "Like Al Pacino in {i}Dog Day Afternoon?{/i}" (multiple=2)
            "He leans back in his chair and points at you."
            ed smug "Oh, I {i}like{/i} this one." 
            bio blush "Oh...!"
            show ed -smug
            call endeared
    show bg coffeeshop with dissolve
    label afterPhd:
        ed lookup "To make a long story short, I had an {i}amazing{/i} time in New York City."
    ed fakeout "Until I had to leave."
    bio angry "You {i}had{/i} to leave? Why?"
    #pause music
    ed thinking "7/11."
    bio -angry "Oooh, when that psychic girl collapsed that building, huh?"
    ed "Yep."
    bio happy "So this is like,{w=0.1} the 2000s era."
    bio -happy "You know she still doesn't feel bad about that."
    ed lookup "Oh I know."
    ed angry "Believe you me...{w=0.1} I know."
    #play music
    ed lookup "Anyway,{w=0.1} I knew it was about to get crazy over here,{w=0.1} so I moved to London."
    
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
    ed angry "...Reasons I would hope are obvious."
    ed -angry "Early on in our stint together, keeping the magic a secret got to be really quite difficult."
    ed lookup "You know, it's a university, so people ask questions."
    ed "\"Can I have the key to the printing closet.\"{w=0.1} \"Why do you need library access after hours.\"{w=0.1} \"Aren't you the guy from Star War.\"" 
    ed -lookup "Things like that."
    ed "So we put on fake wedding bands. That made them mainly ask when we got married."
    bio "I see."
    bio happy "But you wouldn't pretend to marry someone you didn't like."
    ed thinking "Oh boy. Don't even joke about that..."
    "It took a while, but the theme finally re-emerged..."
    ed -thinking "I floated the idea around, but I wasn't anywhere close to her level."
    ed "She said I was too immature for her."
    ed angry "She's a regular 30-something."
    bio "She's a 30-something, right now?"
    ed "Yes."
    bio "So young!"
    ed "Yes, it's embarrassing."
    show ed thinking with dissolve
    bio "When did that happen?"
    ed "Only a few years ago."
    bio happy "You're taking it like a champ."
    ed lookup "I- {nw=0.1}"
    ed blush "Thank you."
    show ed lookup with dissolve
    bio "What made you decide to come back from England?"
    ed -lookup "Oh,{w=0.1} you know..."
    ed fakeout "{size=-25}philandering{/size}"
    menu:
        "Tell him to speak up":
            bio "Excuse me,{w=0.1} can you say that again?"
            ed smug "That again."
            "Sigh.{w=0.1} Of course."
            bio happy "Of horse."
            show ed lookup with dissolve
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
            show ed -lookup
        "He can keep his secrets":
            show ed -fakeout with dissolve
            "You nod along even though you didn't really hear what he muttered."
            "You have a feeling it was something embarassing like,{w=0.1} \"philandering,\""
            "which is a funny word for \"womanizing\" because it sort of implies he's attracted to men."
            "Not that that's bad or anything." 
            if homophobic:
                $ renpy.notify("Trait gained: in denial!")
            "It's not like you're homophobic."

    
    ed "So."
    ed "Based on that."
    ed lookup "What would you say my biggest fear is?"
    menu:
        "Commitment":
            pass
        "Abandonment":
            pass
        "Insincerity":
            pass
        "All of the above":
            ed blush "Ouch."
            pass
    $ renpy.fix_rollback()
    ed lookup "You seem really sure about that."
    bio happy "Mm-hm."         
    jump review
    return

label review:
    #stop music fadeout 1.0
    bio "Well then. Let me just touch up my notes..."
    show bg black with dissolve
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
            ed angry "Hey."
            show ed -angry
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
            "Chill out,{w=0.1} bro.{w=0.1} You can't even see them."

    $ pine = False
    menu year:
        "He met the Devil the year he turned thirty, which was..."
        "1422":
            pass
        "1430":
            pass
        "2023" if pine == False:
            "If only he were a regular 30-year-old man and not a 631-year-old warlock."
            "You might have been able to marry him."
            if not endearing:
                "But then again, maybe not."
            $ pine = True
            jump year
    if yearcontradiction:
        "You shake your head. This one might trip you up..."
    

    menu crimes:
        "During your talk, Ed casually admits to..."

        "Trapping a town in an endless fog":
            pass
        "Impersonating a vampire hunter":
            pass
        "Framing someone for murder":
            $ yourFacts += 1
            ed fakeout "Hey, uh, don't write that in there."
            ed "I have enough problems as it stands."
            "Now it's your turn to be smug."
            bio happy "No promises."
            show ed -fakeout
        "Insider trading":
            pass
    $ renpy.fix_rollback()

    menu beliefs:
        "Ed's allegiances lie with..."
        "The owning class":
            pass
        "The proletariat":
            pass
        "The Valkyrie theocracy":
            ed angry "Don't write that. Even as a joke."
            menu:
                "My mistake original gangsta":
                    bio sad "I must have gotten the wrong idea."
                "Don't tell me what to write":
                    "You think you see him roll his eyes."
                    call offended
            pass
        "Himself":
            $ yourFacts +=1
            pass
        "The girl reading this":
            $ yourFacts +=1
            ed "That includes you."
            bio blush "What!?"
            $ cuteanimal = renpy.random.choice(["fluffy kitties", "fat baby seals"])
            "You quickly scratch that out and write {w=0.3}\"[cuteanimal]\"{w=0.3} in its place."
            call endeared
        "Are you kidding!? Our paper isn't political!":
            "Yeah,{w=0.1} that's what your boss says,{w=0.1} but he knows how running cover for a warlock will reflect on it."
            "He's not an idiot.{w=0.1} He knows about...{nw=0.3}"
            # play sound ominous 
            extend "The Implication."
    $ renpy.fix_rollback()

    ed lookup "Hey, can you include a segment about my Ph.D.s?"
    "You sigh."
    bio sad "Fine."
    show ed -lookup
    menu phds:
        "You decide you will offhandedly mention his Ph.D. in..."
        "Fishing Science":
            show ed blush with dissolve
            bio angry "What!? What's so funny?"
            ed "That's not a real degree."
            bio shocked "What!?"
            show ed -blush
            pass
        "Theology":
            $ yourFacts += 1
            pass
        "English Literature":
            $ yourFacts += 1
            pass
        "Library Science":
            "Did he study in the library or work in the library...?"
            "You can't remember."
            pass
    $ renpy.fix_rollback()
    
    "Finally, after a long afternoon of..."
    bio sad "What would you even call your stories? Swashbuckling?"
    ed lookup "No I hate pirates."
    bio -sad "Oh, okay. I'm asking because my inner monologue needs a little help with her vocabulary."
    ed blush "Your inner monologue is very charming."
    "You share a laugh."
    bio happy "It's funny because you can't actually hear it."
    bio -happy "So what would you call your stories?"
    ed lookup "Try, \"After a long afternoon of conversation.\""
    bio happy "Oh, that's good. Nice and simple... Thank you!"


    "After a long afternoon of conversation, you arrived at the heart of your profile."
    menu thecost:
        "What did his immortality cost him?"
        "Two dollars":
            pass
        "A Ph.D.":
            bio happy "Nope! Not what I wrote."
            jump thecost
        "His lily-white reputation":
            "No. He has demonstrated in no uncertain terms that he had nothing of the sort."
            pass
        "Human connection":
            "You look at the bags under his eyes."
            "You think to yourself, \"Eye{i}bags?{/i} More like eye luggage.\""
            "You snort, and then shake your head for laughing at your own joke."
            "Then you write,"
            "\"More than he could have ever imagined.\""
            $ yourFacts += 1

    $ renpy.fix_rollback()

    "You uncovered your thesis through the one thing all of his tales had in common."
    menu commonthread:
        
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

    "You finished taking your notes."
    hide screen bookbutton with dissolve
    "You put your reference material away, too."
    show ed thinking with dissolve
    "...He looks relieved."
    show ed -thinking

    jump interviewconclusion

    return

label interviewconclusion:

    show bg coffeeshop with dissolve
    ed "Well?{w=0.1} That should be enough to write a pretty basic profile."
    bio sad "Basic? You don't mean to imply that there's more."
    ed lookup "There {i}absolutely{/i} is,{w=0.1} but if I went into it,{w=0.1} I'm certain we'd be here all night."
    "Truthfully,{w=0.1} you wouldn't mind spending all night with him."
    if not endearing:
        ed -lookup "But you have a deadline,{w=0.1} so."
        pass
    ed lookup "Was there anything else you needed from me?"
    bio -sad "Yes,{w=0.1} well,{w=0.1} I just have one final question."
    bio "In all your stories,{w=0.1} you've gone on about the who, the what, the how..."
    bio "Why did you do it?{w=0.1} Why did you decide to become an immortal wizard?"
    ed -lookup "I was already a wizard before I became immortal."
    bio "Right,{w=0.1} of course.{w=0.1} But still. What motivates you?"
    bio happy "Is it all those fun adventures? Money?"
    bio "Were you trying to change the world?"
    bio -happy "What's the reason?"
    bio "Or,{w=0.1} at least,{w=0.1} what's the reason you want the world to know?"

    ed lookup "Why did I do it,{w=0.1} huh...?"
    ed -lookup "That's a great question."
    ed thinking "I,{w=0.1} um...{nw=0.5}"
    # play music lovesong
    ed blush "I did it for love."
    bio "Love...?"
    bio "Really?"
    ed "Yes."
    ed lookup "That's not weird...{w=0.1} is it?"

    $ weirdo = False
    menu:
        "It's a little weird":
            $ weirdo = True
            ed "..."
            ed "I guess it is,{w=0.1} coming from someone like me."
            
        "It's not weird at all":
            ed "I'm...{nw=0.2}"
            show ed thinking
            extend "You have no idea how relieved I am to hear that."
    if commonality:
        bio "I noticed you had a partner for every story."
        bio happy "Or, at least someone you were very fond of, that you seem to miss, even now."
    else:
        bio "Why do you say you did it for love?"
    show bg black with dissolve
    ed lookup "It goes back to my first girlfriend."
    ed "...Actually, she was my fiancée."
    ed "She had warned against it beforehand. She said it wouldn't make me happy."
    ed thinking "I went and did it anyway."
    ed -thinking "The way it works is that whenever I die, I come back in a few days or so..."
    ed angry "But I never told her. I was too ashamed."
    ed -lookup "The day of the shipwreck, I actually died.{w=0.3} Well,{w=0.3} \"died.\""
    ed "So she never knew I was still alive."
    ed thinking "I think that in the intervening years, I didn't want to replace her..."
    ed "So all of my relationships ended up being really short-lived."
    bio -happy "Because you thought you would find her again?"
    ed "Right."
    bio "But you never did."
    ed lookup "No, that's not true."
    ed -lookup "When we reunited, she had married someone else."
    bio sad "Oh..."

    ed blush "Then she told me,\"You're like how I was when I met you.\""
    bio "That kind of makes sense."
    bio happy "Mermaids live for much longer than humans do."
    ed thinking "...You're smarter than I am."
    bio blush "..."
    ed angry "I only see why she tried to talk me out of the deal some 200 years after I'd done it."
    ed -angry "But she wasn't upset with me or anything. She just kind of... laughed."
    ed thinking "She told me that if the connection is real, the love will be beautiful every time."
    ed "No matter how long or short the encounter is."
    ed "In the beginning, I thought did it for \"love...\""
    ed lookup "What's more important to me is that it's the reason I'm still here."
    ed thinking "When I think about it... even from before my life as... this..."
    ed blush "That's all I ever really wanted."

    show bg coffeeshop with dissolve
    ed lookup "So? What do you think?"
    menu:
        "That's so sweet":
            ed blush "Isn't it...?"
            ed "She saved my life."
        "I think I love you" if not weirdo:
            if endearing:
                ed blush "Haha..."
                ed "Is it strange to say..."
                ed "I don't think I want this day to end?"

            else:
                ed -lookup "Wow... you are forward."
                ed blush "I'll think about it."
        "Thank you for sharing":
            ed thinking "Of course."
    
    "And with that, you took the last of your notes."
    hide ed with dissolve
    "The two of you stand up to leave the coffee shop..."
    

    if yourFacts >= factstotal:
        if endearing:
            if nameroute:
                if persistent.completed_playthroughs >= 1:
                    $ secretending = True
                elif persistent.completed_playthroughs <=0:
                    show ed lookup with dissolve
                    ed "Hey."
                    ed "Do you think you could meet with me again?"
                    ed thinking "I have a proposal for you." # HINT TOWARD THE SECRET ENDING I HOPE YOU SAVED UR GAME.
                    bio blush "Yeah of course!"
                    "You accepted without thinking..."

                    pass
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
    show bg black with dissolve
    $ renpy.block_rollback()
    "As you turn around, you feel his hand on your shoulder."
    "You turn back to face him."
    show ed with dissolve
    ed "Listen here."
    ed lookup "I like you.{w=0.1} How come I've never heard of you before?"
    bio "I suppose...{w=0.1} it's just by chance.{w=0.1} I mean,{w=0.1} I've never had a lot of eyes on much of my work."
    ed "But you're clearly good at what you do.{w=0.1} You want people to know that about you,{w=0.1} right?"
    "That would be nice..."
    ed "Wouldn't it?"
    bio blush "I...{w=0.1} wouldn't have to answer to my good-for-nothing boss."
    ed "Exactly...!"
    ed -lookup "Look,{w=0.1} I'll cut to the chase."
    ed lookup "I want to help you."

    menu:
        "Accept his help":
            jump accept
        "Reject his help":
            jump reject
        "Ask a question":
            pass

    bio "Oh!{w=0.1} Really?"
    bio sad "I mean,{w=0.1} I don't know..."
    bio -sad "Help me... {w=0.1}how?"
    ed thinking "Well...{w=0.1} let me put it this way."
    ed "I think that...{w=0.1} this profile your paper is doing..."
    ed lookup "I think it's going to make a killing.{w=0.1} I think it's gonna make waves."
    ed -lookup "How do the kids say it?{w=0.1} It's gonna do numbers?"
    bio "Well,{w=0.1} what makes you say that?"
    ed "Just by the sheer quality.{w=0.1} You're keen.{w=0.1} Observant."
    ed thinking "Honest."
    "He's right,{w=0.1} you know."
    "Your talent is a waste at this stupid joint."
    menu:
        "Accept his help":
            jump accept
        "Reject his help":
            jump reject
        "Ask another question":
            pass
    
    bio "But...{w=0.1} why me?{w=0.1} There are far more prolific writers doing way worse than I am."
    ed lookup "There are far {i}worse{/i} writers doing much better than you are,{w=0.1} too."
    bio sad "{w=0.1}...I never said anything about worse writers."
    ed thinking "It's not what you said.{w=0.1} It's what you didn't say."
    ed "\"Prolific.\"{w=0.1} Not learned,{w=0.1} not talented.{w=0.1} Prolific." 
    ed -thinking "In other words:{w=0.1} just talk.{w=0.1} They talk too much."
    ed lookup "Not you,{w=0.1} though."
    ed blush "I like you,{w=0.1} so I'll help you.{w=0.1} Simple as that."

    menu:
        "Accept his help":
            jump accept
        "Reject his help":
            jump reject
        "Ask another question":
            pass

    bio -sad "And what do you get out of helping me?"
    ed thinking "Hm..."
    ed fakeout "The satisfaction,{w=0.1} I guess.{w=0.1} A bit of comfort?"
    "Wow.{w=0.1} How selfless..."

    menu:
        "Accept his help":
            jump accept
        "Reject his help":
            jump reject
        "Ask another question":
            pass

    bio angry "How can I be sure I can trust you?"
    ed thinking "Of course.{w=0.1} That's very important.{w=0.1} You hate lies.{w=0.1} And I've proven I love lying."
    "You laugh idly."
    ed lookup "I'll give you my name."
    ed "My real name."

    bio sad "And what do I give you?"
    ed "Your word that you will keep it a secret."
    ed fakeout "It's... a security thing for me."
    $ whatyouget = True

    menu:
        "That seems fair":
            jump accept
        "No way, José":
            "You don't call him José,{w=0.1} by the way."
            jump reject
    

    return

label accept:

    "You let out the breath you've been holding."
    bio happy "Sure!{w=0.1} Why not."
    ed thinking "Good! Good. That means I can trust you with this."
    call realname
    if not whatyouget:
        ed "Don't tell anybody that, by the way."
    bio -happy "So...{w=0.1} what do I do now?"
    ed lookup "You lock it in."
    menu:
        "Lock it in with a handshake":
            "You stretched out your right hand for Ed to grab.{w=0.1} He gives you a firm hanshake." 
            "You felt your palm tingle."
        "Lock it in with a fistbump":
            "You raised your fist to chest height.{w=0.1} He raises his to meet yours.{w=0.1} You bump fists."
            "You felt a slight gust wind brush past your face and through your hair."
        "Lock it in with a kiss" if persistent.secret_ending_reached:
            #triggers the true ending which I won't write because there's no time
            "You had to stand on the tips of your toes to reach his face."
            "He holds you steady by your waist as you lean into him.{w=0.1} You close your eyes."
            hide ed with dissolve
            "Then, you feel his warm lips on yours."
            "...and once again."
            show ed with dissolve
            "You felt your heart flutter."
    bio "Ed..."
    bio happy "Thanks for everything."
    ed thinking "Don't even mention it..."
    hide ed with dissolve
    "As you leave the studio,{w=0.1} something starts to nag at you from the back of your mind." # his house (the vampire castle)? a cafe? a hotel? wherever
    "He agreed when you said it would be nice if more people knew about your writing..."
    "But you were sure you never said that aloud."
    jump finaltest
    return

label reject:
    $ ed_observation = True
    show bg coffeeshop with dissolve
    bio sad "Sorry.{w=0.1} I don't think I can accept your help."
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
    ed thinking "My name is Aniedi Akpan."
    ed "My mother got it from a friend of hers..."
    ed "\"Akpan\" just means \"first-born son.\""
    bio -sad "Wow..."
    bio "What does \"Aniedi\" mean?"
    ed "I was told it meant..."
    ed blush "\"Who knows?\""
    show ed -blush
    bio "..."
    return

label finaltest:
    scene bg black
    # play music office
    if secretending == True:

        "You wander into the office,{w=0.1} almost in a trance."
        "You don't even notice your boss calling out for your attention.{w=0.1} He seems perplexed as you saunter to your desk."
        call endoftest
        jump dealend
    elif ed_observation == True:
        show bg black with dissolve
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
        $ tidbit = renpy.random.choice(factscollect)
        bio "I found out that [tidbit]."
        $ factscollect.remove(tidbit)
        $ tidbit = renpy.random.choice(factscollect)
        bio "I also learned that [tidbit]..."  
        $ factscollect.remove(tidbit)
        $ tidbit = renpy.random.choice(factscollect)
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
    bio "um{nw=0.5}"
    #stop music
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
    #play sound scribble
    "You sit down and write the article exactly as you envision it."
    "When you're done,{w=0.1} you submit it,{w=0.1} and you go home."
    return


label goodend:
    scene bg black
    $ all_endings_reached = False
    #play sound ringtone
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
    #play sound hangup
    "He hangs up."
    
    "You reached the good ending...?"
    $ persistent.good_ending_reached = True
    #persistent from reaching the secret ending

    if persistent.bad_ending_reached:
        if persistent.secret_ending_reached:
            $ all_endings_reached = True

    if all_endings_reached:
        "You realized this was as good an ending as you could get."
    $ persistent.completed_playthroughs += 1
    return

label badend:
    scene bg black
    #play sound ringtone
    "Some weeks after the profile went live,{w=0.1} you got a call from your boss."
    boss "Hey,{w=0.1} um."
    if finalanswer == totalDoctorals:
        boss "Did you go and count the number of doctoral degrees or the number of Ph.Ds?"
        boss "Cuz I asked for Ph.Ds...{w=0.1} and I get that he has an M.D..."
        boss "...but an M.D. isn't a Ph.D."
    boss "So,{w=0.1} you're fired.{w=0.1} Totally super mega ultra fired.{w=0.1} For embarrassing the paper."
    boss "Don't check Glitter."
    #play sound hangup
    "He hangs up."
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
    $ persistent.bad_ending_reached = True
    $ persistent.completed_playthroughs += 1
    return

label dealend:
    scene bg black
    #play sound ringtone
    "Some weeks after the profile went live, you got a call from your boss."
    boss "Hey,{w=0.1} um."
    boss "I want to say I'm sorry."
    "Followed by an unusual pause."
    boss "I'm sorry for doubting you,{w=0.1} and-{nw=0.2}"
    "Another pause.{w=0.1} You hear shuffling on the other side of the line." 
    "You're sure you hear your boss say, \"okay\" over and over."
    boss "And I've been withholding tens of thousands of dollars in backpay which I-{w=0.5} which I will deposit in your checking account.{nw=0.3}" 
    boss "Immediately."
    #play sound hangup
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
    #play sound ominous
    "You reached the secret ending...!"
    $ persistent.secret_ending_reached = True
    $ persistent.completed_playthroughs += 1
    return

