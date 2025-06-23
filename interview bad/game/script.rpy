# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

default bioName = "Biographer"

define ed = Character("Ed")
define bio = Character("You")
define boss = Character("Boss")
define umi = Character("Umi")



# The game starts here.

label start:
    jump starsign
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
    ed "Date of birth: October 9, 1394." 
    ed "Write that down."

    menu birthday:
        "Correct this in your notes":
            "You scratched out Virgo and wrote Libra."
        "Do not":
            bio "I would rather not contradict the order of the Valkyries."
            ed "Suit yourself."
    
    bio "Now that that's out of the way- {nw}"
    ed "A September birthday... {cps=*0.3}Tchhhhhhhh... {/cps}A September birthday?{nw=0.5}"
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
    ed "Rick... Owens...?"
    "You stare at him some more. He cocks his head."
    menu firstlie:
        ed "What?"
        "Tell him he's lying":
            ed "Seriously? We just started."
            bio "Right. Sorry."
        "Move on":
            "It probably is designer."


    return

label end:
    "bio" "But... I think in all your stories, you've never told me the \"why.\" You've gone on about the how..."
    "bio" "Why did you do it?"
    "ed" "Why did I do it?"
    "ed" "...for love."

    menu love: 
        "I think I love you":
            ed ""



    return
