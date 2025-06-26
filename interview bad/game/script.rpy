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
define factstotal = 0

#endregion

#region Points and Counters
default yourFacts = 0 
default nameroute = False
default endearing = False
default secretending = False

default factscollect = [] #named facts that are picked at random at the end to go over

#endregion


#region Story Flags
default affection = 0
default favorlost = False
default e_firsttime = True
default o_firsttime = True

default stareflag = 0
default greeting = ""

default ed_observation = False

default homophobic = False
default homophobicbeliefs = []
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
    "There's a lot of that in the magical community, and you find it nauseating."
    "You would rather die than take part!"

    "But today is different. Today, you're meeting with one of the most notorious magicians in the magical world."
    "No, not the dusty one... The other one. Your paper is doing a profile on the Immortal Agent of Chaos."
    "It's nearly complete, except for the fact that it's nowhere near finished."
    "You aren't worried, though."
    "Okay, the deadline is this weekend and you're a {i}little{/i} worried."
    "But after a few weeks of phone calls, dead-ends, and couple of desperate summoning circles, your boss finally arranged an interview with him."
    "You're finally going to get the truth from the man himself. So there's nothing to worry about!" 
    #lines below this (cut if I run out of time)
    "Of course, you also brought the most factual encyclopedia known to magickind as supplementary material---just in case." 
    "It's the Valkyrie Order's Compendium of Known Agitators---{w=0.2}but you're sure you won't need it." #show the valkyrie reference button  

    jump icebreaker
    return

label icebreaker:
    #show ed and scene
    menu greeting:
        "You decide to greet him..."
        "Cordially":
            $ greeting = "cordial"
            bio "Thank you for taking the time to meet with me today."
            "He casually waves you off."
            ed "I didn't have anything better to do."
            bio "Really?"
            ed "Nope. Take as much time as you need. As much time as you need..." 
            "!?" #wink
            "You feel a lot more confident now! But..."
            "It seems unlikely that someone as busy as he is has \"nothing better to do.\" He's not messing with you, or...?"
            
        "Excitedly":
            $ greeting = "excited"
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
            ed "We can...{w=0.3}" 
            #play sound ding
            extend ed "save that one for later, can we?" 
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
    bio "Oh..."
    menu:
        "I'm so sorry":
            ed "Don't be. I'm evil."
            "You furrow your brow in concern, though you're not sure why, because you already knew he was a warlock...?"
            ed "That was supposed to be a joke."
            bio "Oh."
            bio "Well."
        "I'm not surprised":
            "He chuckles at your blasé response."
            bio "At our paper, we call warlocks with good childhoods priests."
            "He snorts, then covers his mouth to keep the giggles at bay."
            ed "I mean, it's true. And they certainly aren't immortal."
            call endeared
            
    jump interviewintro
    return

label endeared:
    $ affection += 1
    if e_firsttime == True and affection >=1:
        "..."
        "You feel like you've endeared yourself to him."

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
    
    if affection <= 0 and e_firsttime == False:
        "You've definitely lost your favor with him."
        $ endearing = False
        $ favorlost = True
        
    elif o_firsttime == True:
        "..."
        "He seems offended."
    elif affection == 1:
        "He's starting to get testy. Try not to offend him again..."
        
    else:
        pass
    return

label starsign:
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
        "Ask him his sign":
            pass

    bio "When were you born, then?"
    ed "October 9. {w=0.2}Write that down." 
    "You scratched out Virgo and wrote Libra."
    $ starsign = True
    
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
    "You look back down at your notes and shake your head."
    bio "Nothing. Nevermind."
    "..."
    "He's looking directly at you."
    menu:
        ed "What, you like it or something?"
        "I might":
            ed "You might?"
            ed "Okay, I mess with it." #he's flirting
            call endeared
        "Just curious":
            ed "Ooookay."
            pass
    jump interviewintro
    
    return

label interviewintro:
    "You let out a breath."
    bio "Well."
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
    bio "My question—{w=0.2}it's fairly straightforward—{w=0.2}I want to know just how you became an immortal wizard!"
    ed "Mm."
    bio "It's one of my favorite questions."
    bio "Of all the fine, magically inclined folks I've interviewed, I've always asked the same question, and I've never gotten the same answer!"
    ed "Well, if you wanna hear about that..."
    "He uncrosses his legs, leaning forward with his elbows now resting on his knees." 
    "You find yourself leaning forward as well, pulled into his vortex, his magnetic field." 
    "You are about to hear A Story."
    jump portugal
    return

label portugal:
    #scene portugal
    ed "I had just gotten my first Ph.D—theology. I wasn't religious, but there weren't many options back in those days."
    bio "Which days?"
    menu:
        ed "It was when I turned thirty in 1430. Pretty easy to remember, right?"
        "I suppose so":
            pass
        "You're how old, again?":
            ed "Thirty."
            bio "Right. Of course."
            bio "And just how {i}long{/i} have you been thirty, hm?"
            ed "Since... 14...30."
            bio "Oh. Oh yeah."
            bio "Carry on."

    ed "My girlfriend at the time wanted to try out some different waters, and especially different fish." 
    ed "So with my studies finished, we figured it would be the perfect time to try somewhere new, and we swam up to Portugal."
    bio "That sounds so romantic! Wait... what do you mean you {i}swam{/i} to Portugal?"
    ed "Well you see, swimming is when you place your legs in the water and kic-{nw}"
    bio "I know what swimming is."
    ed "You do? So why did you ask?"
    if stareflag >= 1:
        "You don't want to enter another staring contest with him, so you carefully consider how you're going to phrase this."
        pass
    else:
        "You carefully consider how you're going to phrase this."
        pass
    "Magical types can be such volatile personalities, and if you happen to offend the most important interview of your career, you're boned"
    "You CANNOT under any circumstances imply he is insane for alleging that he swam to Portugal from literally anywhere."

    menu:
        "Isn't that... kind of far?":
            ed "From North Africa? No. It's a coastal nation with pretty easy access to the sea."
            bio "That's not what I meant."
            ed "Then what did you mean?"
            bio "That's... well... you swam by yourself?"
            ed "...Did I not say I was with my girlfriend?"
            bio "You {i}and{/i} your girlfriend swam??"
            ed "Well, yeah, it's not like she can walk."

        "You're insane for alleging that you swam to Portugal from anywhere.":
            ed "Lawyer says what?"
            bio "What?"
            ed "Heh. Gottem."
            "Sigh. He freaking got you."
    
    ed "So are we clear on how I got to the Kingdom of Portugal or are we still working out the mechanics of swimming?"
    bio "I'm done. Let's get back on track."
    "You're not done."
    bio "It's just, I'm a bit confused."
    ed "By what? My ex-girlfriend and I swam to Portugal." 
    ed "She's a mermaid, so it wasn't particularly difficult."
    menu:
        "Ohhhh. She's a mermaid!":
            ed "Exactly."
            
        "You do not have a mermaid girlfriend":
            ed "Correct. I {i}had{/i} a mermaid girlfriend. There's a difference."
            ed "Who would lie about having a mermaid ex?"
            bio "Many a sailor have lied about mermaids."
            ed "No sailor this century would lie about having a mermaid girlfriend. Let alone a mermaid ex."
            ed "That's just embarrassing."
            bio "Point taken."
    
    ed "Once we landed, we split up." 
    ed "I wasn't in the market to fish shop, and besides, I had heard that if you aren't at least a {cps=*0.7}little{/cps} bit bisexual in Lisbon, 
    they would straight up kill you."
    menu:
        "In the 1400s...?":
            $ homophobic = True
            ed "Oh. I see. You think being bisexual wasn't invented yet."
            bio "No,{w=0.2} I don't-{w=0.2} I wasn't-{w=0.2} I mean-{w=0.2}"
            ed "Wowwwwww."
            $ renpy.notify("Trait earned: homophobic!")
            $ homophobicbeliefs.append("bisexuals existed before David Bowie")
            "He shakes his head disapprovingly." #shit eating grin. fucking hater
        "Oh!":
            bio "You're bisexual!"
            ed "Is it a surprise?"
            bio "I thought you were just... a really sensitive guy."
            ed "Yeah. We call those \"bisexuals.\""
    
    bio "So you're wandering the streets of Lisbon, waiting for your mermaid girlfriend to get fish." 
    bio "And you come across some kind of powerful being, right? Another warlock, or maybe an old alchemy book?"
    ed "Not quite..."
    #show devil
    devil "I'm the Devil."
    ed "Now me, I'm an industrious guy. I see The Devil and I think, \"how can I profit off of such a one in a lifetime chance encounter?\""
    ed "There was this new economic system emerging called \"capitalism\" and I was dying to test it out."
    devil "I love taking advantage of emerging economic systems!"
    bio "But didn't capitalism emerge in the 16th century?"
    ed "Oh, you're gonna argue with the guy who was there? Is that it?"

    menu:
        "Remind him of the year":
            bio "It was 1430."
            ed "And I was about to be rolling in it the way I finessed the f**k outta that devil."
            ed "You're gonna love this. I promise."
            "You make a note to yourself to edit that out."
            
        "Ask him about the year":
            bio "What year was it again?"
            ed "Like, 1420-something. Why?"
            bio "Just checking."
            
        "Let him have it":
            "You mutter something under your breath about historical revisionism."

    ed "So I see The Devil standing there on the street curb, and I know it's him because he's got these eyes like a husky." 
    ed "Piercing doesn't even begin to describe it. They glowed." 
    ed "So I see him standing there with his freaky and I mean STRANGE bright blue glowing eyes and I say,"

    ed "\"How about we make a deal... a business deal.\"" 
    ed "Also I had the slickest braids on at the time where are my braids. You gotta include the braids."
    bio "Please continue."
    ed "Right, so he's like,"
    devil "I'm glad you noticed my eyes, they don't call me Big Dog for nothing bark bark am I right."
    bio "I don't think he said that... no one would respect a man called Big Dog."
    ed "How do you know the Devil wasn't a woman, by the way?"
    menu:
        "Because you said \"he\" earlier.":
            ed "Women can't be he/hims?"
            if homophobic == True:
                "You don't even bother this time and just let him have it."
            else:
                bio "No, I- {w=0.1}"
                ed "So they {i}can't{/i} be he/hims!?"
                bio "They can, I just- {w=0.3}"
                ed "You don't believe in gender-nonconforming women."
                ed "Wowwwwwwww."
                $ renpy.notify("Trait gained: homophobic!")
                "You stop sputtering and compose yourself."
                bio "I'm asserting myself as the interviewer and taking back control. Please continue."
            $ homophobicbeliefs.append("women can't use he/him pronouns")
        "Because men are the devil and you're the misogynist if you disagree.":
            ed "Hm."
            "He shut up real quick..."
    
    ed "So one long series of contracts and spells later, I made a deal with the devil. I got to be thirty forever."
    bio "What did he get?"
    ed "One of my PhDs, the one in fisherman's science. I worked really hard on it, but education comes and goes when you never age."
    ed "What's wrong? You look disappointed."
    bio "I have to admit that was a bit anticlimactic."
    ed "I never claimed it was climactic. That was all you." 
    bio "Some of the stories about you claim to be climactic. There's about one or two for every year you've been alive."
    ed "Oh yeah? You know they're all fake, right?"
    
    menu exploits:
        "What about the time you stopped what would have been \"the next Pompeii?\"":
            ed "How could I do that?"
            ed "I don't speak Italian." #lying
        "What about the one where you had two religions founded after you?":
            ed "Both were started by ex-boyfriends. I guess I just inspire that in people."
            if endearing:
                ed "Want to make the third?"
                bio "Ah, well, I. Have. To be professional, you know! I can't answer that on the clock."
                ed "How about off the record?"
                "Your face is getting hot again...." 
                "No..... his sweet tambour..." 
                "You must focus....."
        "What about the time you trapped an entire town in an endless fog?":
            ed "Really? That story?"
            ed "What are you, an authoritarian!?"
            bio "You just admitted to being a capitalist."
            ed "And game recognizes game."
            "Touché."
            bio "Not touché! I'm not an authoritarian!"
            ed "Then don't quote those Valkyries at me again."
            call offended

    return

label portugalquiz:
    bio "Well then. Let me just finish up my notes..."
    "You opened up your notepad and scribbled."
    menu:
        "Ed arrived in Portugal via..."
        "Boat":
            $ yourFacts += 1
            pass
        "Land":
            pass
        "Mermaid":
            pass
        "He swam using those strong arms and legs":
            "Chill out, lil bro. You can't even see them."
    menu:
        "He met the Devil the year he turned thirty, which was..."
        "1418":
            pass
        "1422":
            $ yourFacts += 1
            pass
        "1430":
            pass
        "2023":
            "If only he were a regular 30-year-old man and not a 631-year-old warlock."
            "You might have been able to marry him."
            pass

    "You admit to yourself that this is a lot."
    jump renaissance
    return

label renaissance:

    jump renaissancequiz
    return

label renaissancequiz:
    "митя"

    menu:
        "Ed is ideologically aligned with..."
        "The monarchy":
            $ renpy.block_rollback()
            pass
        "The owning class":
            $ renpy.block_rollback()
            pass
        "The proletariat":
            $ renpy.block_rollback()
            pass
        "Himself":
            $ renpy.block_rollback()
            $ yourFacts +=1
            pass
        "Beautiful women everywhere":
            $ renpy.block_rollback()
            $ yourFacts +=1
            ed "That includes you."
            bio "What!?"
            $ cuteanimal = renpy.random.choice(["fluffy kitties", "fat baby seals"])
            "You quickly scratch that out and write [cuteanimal] in its place."
            pass
        "Are you kidding!? Our paper isn't political!":
            $ renpy.block_rollback()
            "Yeah, that's what your boss says, but he knows how running cover for a warlock will reflect on it."
            "He's not an idiot. He knows about...{w=0.3}"
            # play sound ominous 
            extend "The Implications."
            pass
    
    jump modernera
    return

label modernera:
    ed "I"
    if greeting == "excited":
        ed "You said you were honored to meet me."
        ed "Sir."
        "You did say that."
    
    bio "So what got you interested in film?"
    ed "You mean, \"interested enough to want to study it at a high level?\" Because no one gets degrees just because."
    bio "I don't know how true that is."
    ed "Well? You could be right."
    ed "Maybe there's someone out there who wants a doctorate to affirm their gender."
    ed "But for me, I became invested in film when I realized someone had brought one back in time to scare and confuse me."
    ed "I was 14, and the movie was {i}Blue Velvet.{/i}"
    menu:
        "Are you joking kidding me":
            ed "About what?"
            bio "The time travel."
            ed "Is it that hard to believe?"
            bio "It's pretty freaking hard to believe."
            ed "Really? I haven't even told you about the Trickster God Wars." 
            ed "Do you wanna hear about the Trickster God Wars?"
            if endearing:
                ed "I could tell you over dinner."

            bio "I'll pass."
                
        "Was it a good movie though":
            ed "It probably changed my life forever."
            ed "So I would say it's pretty good."
            pass

    ed "Much later, I went back and got a Ph.D in film studies."
    ed "It was pretty easy since I was there for all of it."
    bio "As we've established..."
    "Sigh. Again with the Ph.Ds!"
    $ degreeskip = False
    menu:
        "Tell him to hurry it up":
            $ renpy.block_rollback()
            bio "Ed, I don't know if we have this much time to dedicate to your postgraduate degrees."
            ed "Really? Because I've been blowing a lot of hot air on s#!t that really doesn't matter."
            ed "The Ph.Ds are the most important part."
            "You decide to be frank."
            bio "I'm pretty sure no one cares how many Ph.Ds you have."
            ed "Damn, okay. Famous last words though."
            $ degreeskip = True
            jump afterPhd
            
        "Let him get them out of his system":
            $ renpy.block_rollback()
            pass

    ed "It was the late 90s, a while after I got my Ph.D in clinical psychology."
    ed "I had just become board-certified at the time, too, and my private practice was doing pretty well."
    ed "Since I had a bit of extra cash, I figured I could go back and do another program. One that was less sciencey."
    ed "Like I said, I was there, so it wasn't suuuper difficult. But, my god, the papers, and the records?"
    ed "I was like, \"Is this film studies or archaeology?\""
    "Colleague" "It's called, \"doing research,\" Ed."
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
                bio "I wasn't! And I don't sound like that!"
                ed "Likely story from someone who doesn't believe [homophobicbelief]."
                "Come on, girl! Get it together. He cannot keep baiting you like this!"
                #achievement: women's wrongs
            else:
                ed "Are you transphobic?"
                bio "I'm not!"
                ed "Wowwwwwwwww."

        "You mean like...?":
            bio "Like Al Pacino in Dog Day Afternoon?" (multiple=2)
            ed "Like Al Pacino in Dog Day Afternoon." (multiple=2)
            ed "Oh. I {i}like{/i} you."  #smile
            ed "This one has taste."
            "SWOON..."

            #affection up

    label afterPhd:
        ed "Long story short, I had an {i}amazing{/i} time in New York City."
    ed "Until I had to leave."
    bio "You {i}had{/i} to leave? Why?"
    ed "7/11."
    bio "When that psychic girl collapsed that building, huh?"
    ed "Yep."
    bio "You know she still doesn't feel bad about that."
    ed "Oh I know."
    ed "Believe you me... I know."
    ed "Anyway, I knew it was about to get crazy over here, so I moved to London."
    
    if not degreeskip:
        ed "I got my most recent Ph.D a few years later, in Africana Studies."
        ed "And I thought it was a very illuminating experience, but now I don't know how I feel about gynecology?"
        bio "What do those two things have to do with each other...?"
        ed "...You're a smart woman. I'm sure you can figure out why."
   

    return


label interviewconclusion:


    ed "There. That should be enough to write a pretty basic profile."
    bio "Basic? You don't mean to imply that there's more."
    ed "There absolutely is, but if I went into it, I'm certain we'd be here all night."
    "You wouldn't mind spending all night with him."
    if not endearing:
        ed "But you have a deadline, so."
        pass
    ed "Was there anything else you needed from me?"
    bio "Yes, well, I just have one final question."
    bio "In all your stories, you've gone on about the what, the how..."
    bio "Why did you do it? Why did you decide to become an immortal wizard?"
    ed "I was already a wizard before I became immortal."
    bio "Right, of course. But still."
    bio "Was it for all those fun adventures? Money?"
    bio "You were trying to change the world?"
    bio "What was the reason?"
    bio "Or, at least, what's the reason you want the world to know?"

    ed "Why did I do it, huh...?"
    ed "Well, that's easy."
    ed "I, um..."
    ed "I did it for love."
    bio "Love...?"
    bio "Really?"
    ed "Yes."
    ed "That's not weird... is it?"

    menu:
        "It's a little weird":
            ed "..."
            ed "I guess it is, coming from a philanderer like me."
            
        "It's not weird at all":
            ed "Good. ...I was a little worried you would make fun of me."
            
    bio "Why do you say you did it for love?"
    ed "It goes back to my first girlfriend."
    ed "...Actually, she was my fiancée."
    ed "When we shipwrecked, I actually died. {w=0.3} Well,{w=0.3} \"died.\""
    ed "I never told her about the immortality thing."

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
            "He holds you steady by your waist as you lean into him. You close your eyes." 
            "Then, you feel his warm lips on yours."
            "...and once again."
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

    "And with that, he shuffles off."
    "You should head back, too."
    
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
    if yourFacts >= factstotal:
        boss "That's cuz I, uh... {w=0.4}{i}embellished{/i}{w=0.4} your article a bit.{w=0.3} By the way." 
        boss "Just here and there! To spruce things up a bit, y'know? Nothin' too crazy."
    else:
        boss "Which is, y'know, to be expected for a guy with such a history. {w=0.3}Misinformation, like you said."
        boss "I'm sure it was tough to get the truth out of him."
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
    "You immediately find the post. It's got one william likes. The quote gleets are eating you up."
    "As it turns out, a Dr. Yetunde Olu, former colleague and ex-girlfriend of Ed, wrote a response piece"
    "wherein she comments that she can excuse the occasional tall tale and even stops short of calling the piece laundering like many critics have,"
    "but she draws the line at misrepresenting the nature of his involvement in academia."
    "Among other things, she has revealed {i}exactly{/i} how many Ph.Ds he's earned." 
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

