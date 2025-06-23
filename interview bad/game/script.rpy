# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

default bioName = "Biographer"

define ed = Character("Ed")
define bio = Character("You")
define boss = Character("Boss")
define umi = Character("Umi")

default yourFacts = 0

define totalPhds = "7"
define totalDoctorals = "8"


# The game starts here.

label start:
    jump intro
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "heheheheh ."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return

label intro:
    "You are a biographer of the magical, mystical, miraculous, marvelous, mythical, and{cps=*.5}... {w=0.3}mmmm{/cps}{i}spellbinding{/i} people of this world."
    "You have seventeen biographies under your belt already, and you fancy yourself rather credentialed---"
    "far more than the "

    "Today is different. Your paper is doing a profile on one of the most notorious magicians in the magical world."
    "It's nearly complete, except for the fact that it's nowhere near finished. "

    jump demography
    return

label icebreaker:

    return

label demography:
    bio "So I wanted to start with a basic background..."
    jump starsign
    return

label starsign:
    bio "You were born in 1394, which would make you a little over 600 years old."
    ed "That's right."
    bio "Would you say your nature as a Virgo started you down the path of dark magic?"
    ed "Hold up. I'm not a Virgo."
    bio "Your entry on the Valkyrie Compendium of Known Agitators has your star sign listed as Virgo."
    ed "Well it's wrong."
    ed "What are you gonna do, argue with me? {w=0.2}It's wrong."
    ed "I wasn't born in freaking September."
    bio "When were you born, then?"
    ed "My date of birth: October 9, 1394." 
    ed "Write that down."

    menu birthday:
        "Correct this in your notes":
            "You scratched out Virgo and wrote Libra."
            $ yourFacts += 1
        "Do not":
            bio "I would rather not contradict the order of the Valkyries."
            ed "That's fine. But I'm not no damn Virgo."
    
    bio "Now that that's out of the way- {nw}"
    ed "A September birthday...{w=0.2} \"Virgo.\"{w=0.2} {cps=*0.3}Tchhhhhhhh... {/cps}{w=0.2}A September birthday?{nw=0.6}"
    ed "I'm sorry, you can continue."
    bio "Now that that's out of the way, I wanted to ask..."
    bio "Where did you get that sleek, luxurious jacket?"
    jump jacket
        
    return

label jacket:
    ed "Oh, this? It's designer."
    "You stare at him. He stares at you."
    "You stare at him... He stares at you."
    bio "Which... designer?"
    ed "Rick... Owens...?" # annoyed
    "You stare at him some more. He cocks his head."
    menu firstlie:
        ed "What?"
        "Tell him he's lying":
            ed "Seriously? We just started."
            bio "Right. Sorry."
        "Move on":
            "It probably is designer."

    jump interviewconclusion
    return

label interviewconclusion:
    bio "But... I think in all your stories, you've never told me the \"why.\" You've gone on about the how..."
    bio "Why did you do it?"
    ed "Why did I do it?"
    ed "...for love."

    jump finaltest



    return

label finaltest:
    "Pleased with your findings, you returned to the office with your head held high. You had a brilliant idea for the profile."
    "You could even picture the final line of the article:"
    "Even a life full of tall tales can keep at its core a simple truth."
    boss "There you are, you silly goosey goo! So what did you find out? Is he really the world's most credentialed man?"

    boss "I don't gaf. How many Ph.Ds"
    bio "..."
    bio "what"
    boss "How many Ph.Ds did he earn?"
    bio "Are you serious?"
    boss "Very"
    bio "Well... umm..."
    $ finalanswer = renpy.input(prompt="How many Ph.Ds did Ed earn in his lifetime? (Enter numbers only.)", allow="1234567890")

    if finalanswer==totalPhds:
        jump goodend
    elif finalanswer == totalDoctorals:
        boss "Eight? He shouldn't have more than- aw no, did you go and count the MD!?"
        boss "an MD isn't a Ph.D, it's an MD! It's in the name!"
        jump badend
    else:
        jump badend
    return


label goodend:
    "You wrote the profile for the New York Crimes."
    "You got the good ending!"
    return

label badend:
    "Some weeks after the profile went live, you got a call from your boss."
    boss "Hey. Don't check Glitter."
    "Glitter is Magic Twitter."
    "Unfortunately for you, it also has a significantly higher proportion of vicious gay stans. The highest on the Internet."
    "When your boss told you not to check Glitter, it's because he knew they were eviscerating you on there. So you go"

    "You, too, were a talentless hack."
    "You got the bad ending."
    return