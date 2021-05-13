#Type in Terminal-  pip install python-telegram-bot

import random

import constants as keys
from telegram.ext import *
# from telegram import *
import responses as R

print("Bot Started...")


def start_command(update, context):
    update.message.reply_text('Yeah It is Working Bro, type something like /truthclean to begin.')


def help_command(update, context):
    update.message.reply_text('Bruh... @inclinedadarsh put so much effort in it, what are you not understanding?! It '
                              'is the simplest bot ever, what do you want help in! Still, you can message '
                              '@inclinedadarsh if you want help.')


def generate_truth_clean():
    replies = """
              Have you ever eaten or been tempted to eat your dog’s treats?
              Have you ever farted in an elevator?
              Have you ever had a wardrobe malfunction?
              Have you ever peed in a pool?
              Have you ever picked your nose and eaten it?
              Have you ever promised to quit beer,smoking,cake,chocolate etc., but then broke the promise?
              Have you ever used an inappropriate word in front of your parents?
              How many days have you ever gone without taking a shower?
              If you could suddenly become invisible, what more naughty things would you like to do?
              What is one thing that gets you hot and bothered every time?
              What is that one thing you would never do even if someone offered you all of the money in the world?
              What is the most stupid thing you’ve done in front of a crowd?
              What is the worst rumor or gossip you repeated which ended up costing you big time?
              What was the most disgusting joke ever played with someone?
              What’s something stupid you’ve done that you’re most proud of?
              What’s the best thing you wanted to become but now consider the worst thing ever?
              What’s the most embarrassing thing that turns you on?
              Which celebrity do you think is overrated and why?
              Who here are you most jealous of?
              What is your biggest regret?
              What are you most self-conscious about?
              What is the biggest lie you have ever told?
              What is your worst habit?
              What is the strangest thing you have ever bought?
              Have you ever lied on your resume to get a job?
              What is your guilty pleasure?
              What is your favorite thing to do with your leisure time?
              What is your biggest pet peeve?
              If you could choose a different career, what would it be and why?
              If you could live anywhere in the world, where would it be?
              If you were given a million dollars, what would you do with it?
              What makes you the happiest?
              If you were invisible what is something you would do?
              Is there any movie that always makes you cry?
              """.splitlines()
    ct = random.choice(replies).strip()
    return ct


def generate_dare_clean():
    replies = """
              I dare you to order me $10 worth of food for delivery.
              Shave your arms and send me a pic.
              Record yourself singing a song and post it on YouTube.
              Mix a drop of every condiment in your house and drink/eat it.
              Message someone you haven’t talked to in at least 1 year on Facebook or Instagram and take a screenshot.
              Try to lick your own foot!
              Do a three-way prank call to somebody so I can listen.
              Text your crush and ask them out on a date.
              Fill up the bath and get in with your current outfit still on.
              Pick the third number on your contacts list and message them a silly poem.
              Open up all your windows and sing an entire song as loud as you can.
              Cut a piece of your hair.
              Put ice cubes down your pants and try to shake them out and send me a video.
              Take a video of yourself doing a crazy dance and post it to social media.
              Ask a neighbor if they have fifty cents.
              Walk around the block and talk to yourself the entire time, even when people are around.
              Drink or eat a teaspoon of soap.
              Close your eyes and reach into your fridge or food pantry – the first thing you touch, you have to eat.
              Send me a screenshot of your messages with the last person besides me you texted.
              Brush your teeth with peanut butter or another condiment and send me a pic.
              Take a really unflattering picture and make it your profile picture for one full day.
              Send me a screenshot of your selfies gallery.
              Watch five minutes of an adult movie I’ll send you.
              Go up to your biggest window and dance really badly until someone walks past.
              Text a random number and write “I see dead people”.
              Text a random number a selfie.
              Shave a part of your body you wouldn’t usually shave.
              Pretend to be a cat for five minutes and send me a video.
              Find the spiciest thing in your house and eat an entire spoonful of it.
              Make a video of yourself doing your weirdest habit!
              Put on clothes of the opposite gender and take a video of yourself trying to act like a guy/girl.
              Create a really bad, five-minute make-up tutorial and post it to YouTube.
              Walk to the nearest store and ask for the smallest available change for five dollars.
              Wait until a dog walks past your house and bark at it!
              Knock on someone’s door and try to run away before they answer!
              """.splitlines()
    cd = random.choice(replies).strip()
    return cd


def generate_truth_dirty():
    replies = """
              Are second rounds exciting or exhausting?
              Do you fake orgasm while looking sideways or looking the person straight in the face?
              Do you have an “I’m getting laid tonight” outfit? What it is?
              Do you have any spicy pictures or videos saved on your phone?
              Have you ever been attracted to the same sex?
              Have you ever cheated/wanted to cheat?
              Have you ever done it in a car?
              Have you ever sexted anyone? If so, read one of the sexts in a fake British accent
              How many people have you slept with?
              How often do you watch something naughty?
              If you got to have a threesome with people in this room, who would you do it with and why?
              If you were into the same sex, which celebrity would you go for?
              It’s totally illegal to seduce my teachers but if it were.....
              What is the most sexually adventurous thing you’d want someone to do to you?
              What is the most you’ve done for sex in the past?
              What is the song that you get it on to the most?
              What panties are you wearing?
              What was the most embarrassing time you got turned on?
              What would be more thrilling: angry sex or make-up sex?
              What’s the most number of times you’ve done it in one day?
              What’s your favorite body part on a girl?
              What’s your favorite fantasy to pleasure yourself to?
              When did you lose your virginity?
              When was a time you were so turned on you couldn’t stand it?
              When was the first time you came?
              When was your first kiss?
              When was your sexual awakening?
              Where are you on the straight/queer spectrum?
              Who do you most want to sleep with, out of everyone here?
              Who was your best partner and why?
              """.splitlines()
    dt = random.choice(replies).strip()
    return dt


def generate_dare_dirty():
    replies = """
              Change your Facebook status to “Feeling horny . . .”
              Change your Facebook status to “I’m coming . . . I’m coming . . .” Then, one minute later, change it to “I just came.”
              Demonstrate to the room how to put a condom on using a banana.
              Do a sexy dance for your partner, but you can only use one leg.
              Feed someone almonds using just your mouth.
              Go hide somewhere in the house until the next round starts. No one is going to come find you, but you must remain hidden.
              Go to Cosmopolitan’s website’s love section and find a position you’ve never heard of. Then, try to act it out using whatever furniture and pillows you have at your disposal.
              Have someone blindfold you. Then, everyone in the group kisses you on the cheek, and you have to either say which one is your partner, and then kiss them on the lips. OR, you have to choose one person that you want to kiss on the lips.
              If there’s a pool, you have to go skinny dipping, and you have to choose one buddy to go with you.
              Lay down on the ground and have someone pretend like they’re using chalk to draw an outline of your body.
              Let someone go through your YouTube history and read it out to the group.
              Lightly trace your hands over someone else’s lips and whisper “I’m coming, I’m coming,” five times.
              Put a bra on your head and pretend you’re a DJ rocking it really hard for one minute.
              Put on a swimming suit and have someone rub sunscreen on your back. Wear the suit for the rest of the evening.
              Remove one piece of clothing every time you give the wrong answer to a series of questions.
              Remove your bra without taking off your shirt.
              Someone gives you a back massage for one minutes while you’re blindfolded. If you like their style, you can choose to kiss them afterwards, but without knowing their identity.
              Someone has to lick peanut butter, chocolate sauce, or whipped cream off your finger, cheek, or somewhere of their choice.
              Take a picture of your ‘O’ face. You have to use that as your lock screen for 48 hours.
              Take off your partner’s shirt with only your teeth.
              Talk to your hand like you’re making a game plan to sleep with someone else who is in the room.
              Turn out the lights and try to turn the other person on only using sounds.
              With your eyes closed and the other person or people standing across from you in the room, walk with your hands out. You have to kiss the first person you touch, where you touch them.
              You get to dress your partner up, using your clothes. Then take a picture.
              You have to hold a mouthful of water in your mouth until the round is over.
              You have to keep your hand on the very inner thigh of the person next to you for the next round.
              You have to leave an R-rated voicemail for an ex.
              You have to say “I’m just a silly boy” and slap yourself gently on the face 20 times.
              You have to undress down to your accessories and skivvies. If you want to keep any clothes on, you have to take a shot for every piece of clothing you want to keep.
              You leave the room. Everyone pours a shot. You come back into the room and take one of the shots that was poured. Whoever poured the drink, you have to sit on their lap for the rest of the round.

              """.splitlines()
    dd = random.choice(replies).strip()
    return dd


def truthclean_command(update, context):
    update.message.reply_text(generate_truth_clean())


def dareclean_command(update, context):
    update.message.reply_text(generate_dare_clean())


def truthdirty_command(update, context):
    update.message.reply_text(generate_truth_dirty())


def daredirty_command(update, context):
    update.message.reply_text(generate_dare_dirty())


def handle_message(update, context):
    text = str(update.message.text).lower()
    response = R.sample_responses(text)

    update.message.reply_text(response)


def error(update, context):
    print(f"Update {update} caused error {context.error}")


def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("truthclean", truthclean_command))
    dp.add_handler(CommandHandler("dareclean", dareclean_command))
    dp.add_handler(CommandHandler("truthdirty", truthdirty_command))
    dp.add_handler(CommandHandler("daredirty", daredirty_command))

    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


main()
