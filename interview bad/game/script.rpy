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
default starsign = False
#endregion

#region Resources

#em dash: —

#endregion

#

# The game starts here.

label start:
    jump intro


    return

label intro:
    "You are a biographer of the magical,{w=0.2} mystical,{w=0.2} miraculous,{w=0.2} marvelous,{w=0.2} mythical,{w=0.2} and{cps=*.5}... {w=0.3}mmmm{/cps}{i}spellbinding{/i} people of this world."
    "Even though you fancy yourself rather credentialed,{w=0.2} what with the seventeen biographies under your belt,"
    "you are repeatedly upstaged by the charlatans in your field who insist upon filling their \"books\" with falsehoods and lies."
    "If there's anything you despise with every fiber of your being,{w=0.2} it's lies,{w=0.2} and liars,{w=0.2} and also people who tell lies."
    "There's a lot of that in the magical community, and you find it nauseating."
    "You would rather die than take part!"

    "But today is different.{w=0.1} Today, you're meeting with one of the most notorious magicians in the magical world."
    "No, not the dusty one...{w=0.1} The other one.{w=0.1} Your paper is doing a profile on the Immortal Agent of Chaos."
    "It's nearly complete,{w=0.1} except for the fact that it's nowhere near finished."
    "You aren't worried,{w=0.1} though."
    "Okay,{w=0.1} the deadline is this weekend and you're a {cps=*0.7}{i}little{/i}{/cps} worried."
    "But after a few weeks of phone calls,{w=0.1} dead-ends,{w=0.1} and couple of desperate summoning circles,{w=0.1} your boss finally arranged an interview with him."
    "You're finally going to get the truth from the man himself.{w=0.1} So there's nothing to worry about!" 
    #lines below this (cut if I run out of time)
    "Of course,{w=0.1} you also brought the most factual encyclopedia known to magickind as supplementary material{w=0.1}—just in case." 
    "It's the Valkyrie Order's Compendium of Known Agitators{w=0.1}—but you're sure you won't need it." #show the valkyrie reference button  

    jump icebreaker
    return

label icebreaker:
    #show ed and scene
    "He sits in front of you expectantly."
    menu greeting:
        "You decide to greet him..."
        "Cordially":
            $ greeting = "cordial"
            bio "Thank you for taking the time to meet with me today."
            "He casually waves you off."
            ed "I didn't have anything better to do."
            bio "Really?"
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
            ed "Madam."
            ed "I think if you stick around you will find that I am a very funny guy."
            ed "But I don't joke about my name."
            bio "Well...{w=0.1} what is your real name?"
            ed "We can...{nw=0.3}" 
            #play sound wink
            extend "save that one for later, can we?" 
            # so you've initiated the impress him route 
            # what with him lowkey flirting with you and all, he'll tell you his real name if you charm him
            # but of course, out of respect, you won't publish it.
            bio "Oh,{w=0.1} all right..."
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
    ed "Harrowing."
    bio "Oh..."
    menu:
        "I'm so sorry":
            # $ renpy.block_rollback()
            ed "Don't be.{w=0.1} I'm evil."
            "You furrow your brow in concern,{w=0.1} or is it fear?"
            "You're not sure why it would be either because you already knew he was a warlock."
            ed "That was supposed to be a joke."
            bio "Oh."
            bio "Well."
        "I'm not surprised":
            # renpy.block_rollback()
            "He chuckles at your blasé response."
            bio "At our paper,{w=0.1} we call warlocks with good childhoods priests."
            "He snorts,{w=0.1} then covers his mouth to keep the giggles at bay."
            ed "I mean,{w=0.1} it's true.{w=0.1} And they certainly aren't immortal."
            call endeared
            
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
    "He uncrosses his legs,{w=0.1} leaning forward with his elbows now resting on his knees." 
    "You find yourself leaning forward as well,{w=0.1} pulled into his vortex,{w=0.1} his magnetic field." 
    "You are about to hear A Story."
    jump portugal
    return

label portugal:
    #scene portugal
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
            ed "From North Africa?{w=0.1} No.{w=0.1} It's a coastal nation with pretty easy access to the sea."
            bio "That's not what I meant."
            ed "Then what did you mean?"
            bio "That's...{w=0.1} well...{w=0.1} you swam by yourself?"
            ed "{w=0.1}...Did I not say I was with my girlfriend?"
            bio "You {i}and{/i} your girlfriend swam??"
            ed "Well yeah it's not like she can walk."

        "You're insane for alleging that you swam to Portugal from anywhere.":
            ed "Lawyer says what?"
            bio "What?"
            ed "Heh.{w=0.1} Gottem."
            "Sigh.{w=0.1} He freaking got you."
    
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
            ed "Because I'm bisexual."
            call endeared
    
    bio "So you're wandering the streets of Lisbon,{w=0.1} waiting for your mermaid girlfriend to get fish." 
    bio "And you come across some kind of powerful being,{w=0.1} right?{w=0.1} Another warlock,{w=0.1} or maybe an old alchemy book?"
    ed "Not quite..."
    #show devil
    devil "I'm the Devil."
    ed "Now me,{w=0.1} I'm an industrious guy.{w=0.1}" 
    ed "I see The Devil and I think,{w=0.3} \"how can I profit off of such a one in a lifetime chance encounter?\""
    ed "There was this new economic system emerging called \"capitalism\" and I was dying to test it out."
    devil "I love taking advantage of emerging economic systems!"
    bio "But didn't capitalism emerge in the 16th century?"
    ed "Oh,{w=0.1} you're gonna argue with the guy who was there?{w=0.1} Is that it?"

    menu:
        "Remind him of the year":
            bio "It was 1430."
            ed "And I was about to be rolling in it the way I finessed the #!*% outta that devil."
            ed "You're gonna love this.{w=0.1} I promise."
            "You make a note to yourself to edit that out of the transcript."
            
        "Ask him about the year":
            bio "What year was it again?"
            ed "Like,{w=0.1} 1420-something.{w=0.1} Why?"
            bio "Just checking."
            
        "Let him have it":
            "You mutter something under your breath about historical revisionism."

    ed "So I see The Devil standing there on the street curb,{w=0.1} and I know it's him because he's got these eyes like a husky." 
    ed "Piercing doesn't even begin to describe it{w=0.1}—they were glowing!" 
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
            $ homophobicbeliefs.append("women can't use he/him pronouns")
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
            ed "Then don't quote authoritarians at me. That tale is Valkyrie slander."
            call offended
    return

label portugalquiz:
    bio "Well then. Let me just touch up my notes..."
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

    "You admit to yourself that this is a lot."
    "Although,{w=0.1} it's to be expected from someone with over 600 years of adventures."
    "Still,{w=0.1} husky-looking devils...{w=0.1} mermaid girlfriends..."
    ed "Do you need a bit to take it all in?"
    ed "Because there's more."
    
    jump renaissance
    return

label renaissance:
    ed "When you become immortal,{w=0.1} kicking around eating fish and talking to Portuguese mermaids starts to get real old after a while,{w=0.1} and my girlfriend could tell. "
    ed "She suggested we could swim down south,{w=0.1} stop by Rafat or Algiers on our way to Palermo..."
    ed "You know, make a vacation of it."

    jump renaissancequiz
    return

label renaissancequiz:
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
            call endeared
        "Are you kidding!? Our paper isn't political!":
            $ renpy.block_rollback()
            "Yeah,{w=0.1} that's what your boss says,{w=0.1} but he knows how running cover for a warlock will reflect on it."
            "He's not an idiot.{w=0.1} He knows about...{w=0.3}"
            # play sound ominous 
            extend "The Implication."
    
    jump modernera
    return

label modernera:
    ed "I"
    if greeting == "excited":
        ed "You said you were honored to meet me."
        ed "Sir."
        "You did say that."
    
    bio "So what got you interested in film?"
    ed "I became interested in film when I realized someone had brought one back in time to scare and confuse me."
    menu:
        "Are you joking kidding me":
            ed "About what?"
            bio "The time travel."
            ed "Is it that hard to believe?"
            bio "It's pretty freaking hard to believe."
            ed "Really?{w=0.1} I haven't even told you about the Trickster God Wars." 
            ed "Do you wanna hear about the Trickster God Wars?"
            bio "I'll pass."
            if endearing:
                ed "That's okay.{w=0.1} Some other time, then."
                ed "Maybe over dinner."
                
        "Was it a good movie though":
            ed "It probably changed my life forever."
            ed "So I would say it's pretty good."
            bio "What was the movie?"
            ed "1985's {i}Blue Velvet,{/i} directed by David Lynch."

    ed "Much later,{w=0.1} I went back and got a Ph.D in film studies."
    ed "It was pretty easy since I was there for all of it."
    bio "So you just collect degrees, just because?"
    ed "What? No. No one does that."
    bio "No one? I don't know how true that is."
    ed "You know what...? You could be right."
    ed "Maybe there's someone out there who wants a doctorate to affirm their gender."
    bio "So you got your Ph.D."
    ed "Yes there's more I got more Ph.Ds."
    $ degreeskip = False
    menu:
        "Sigh. Again with the Ph.Ds!"
        "Tell him to hurry it up":
            $ renpy.block_rollback()
            bio "Ed, I don't know if we have this much time to dedicate to all of your postgraduate degrees."
            ed "Really? Because I've been blowing a lot of hot air on s#!t that really doesn't matter."
            ed "The Ph.Ds are the most important part."
            "You decide to be frank."
            bio "Ed."
            bio "No one cares how many Ph.Ds you have."
            ed "Damn, okay. Famous last words though." #looks at the camera. 
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
                "Come on, girl, get it together. He cannot keep baiting you like this!"
                #achievement: women's wrongs
            else:
                ed "Are you transphobic?"
                bio "I'm not!"
                $ renpy.notify("Trait earned: transphobic!")
                ed "Wowwwwwwwww."


        "You mean like...?" if endearing:
            bio "Like Al Pacino in Dog Day Afternoon?" (multiple=2)
            ed "Like Al Pacino in Dog Day Afternoon." (multiple=2)
            ed "Oh, I {i}like{/i} this one."  #smile
            
            call endeared

            #affection up

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
        ed "I got my most recent Ph.D a few years later,{w=0.1} in Africana Studies."
        ed "And I thought it was a very illuminating experience,{w=0.1} but now I don't know how I feel about gynecology?"
        bio "What do those two things have to do with each other...?"
        ed "...You're a smart woman.{w=0.1} I'm sure you can figure it out."
    ed "I taught there for the better part of two decades."
    bio "What made you decide to come back?"
    ed "Oh,{w=0.1} you know..."
    ed "{size=-10}...philandering.{/size}"
    menu:
        "Tell him to speak up":
            pass
        "He can keep his secrets":
            pass
    jump interviewconclusion
    return

label review:
    #questions
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
        "No way, José":
            "You don't call him José, by the way."
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
    
    if starsign:
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

