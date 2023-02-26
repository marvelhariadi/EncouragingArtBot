# EncouragingArtBot
A discord bot that sends uplifting messages (and occasionally: Bob Ross gifs) for artists. Created for discord art communities.

To use in your server: https://discord.com/api/oauth2/authorize?client_id=1078574197506322492&permissions=534723947584&scope=bot

## Features
All commands are case insensitive. type without quotations. Commands are designed to be written in natural language, being flexible to punctuation and capitalization. (note that ML model is not used to detect the command. We just used flexible keywords)

Commands:
- "hi/hello ... art bot" - introduction function. The EncouragingArtBot says hi back.

        Acceptable example phrasings:
        hi there, art bot.
        hello art bot
        art bot!!! hi!!!!

- "art bot...be nice" - gives the user encourging messages on their art. 

        Acceptable example phrasings:
        art bot, be nice.
        Be nice to me art bot
        art bot be nice!

- "art bot...vent" -  will automatically delete your message right after you write it. Used to vent out all of the user's hard - feelings. Since the message will be deleted immediately after, nobody will be able to see it. 

        Acceptable example phrasings:
        art bot, I need to vent.
        I have stuff I need to vent art bot
        art bot....vent time:

- "art bot...bob ross..." - sends a gif of bob ross with a lovely bob ross quote

        Acceptable example phrasings:
        bob ross time art bot
        bob ross me up art bot
        art bot, i would like to see a bob ross gif please

- sad detector - detects user mentioning of "sad"
- negative self talk mitigator - detects negative self talk based on keywords and automatically outputs a rebutting message to encourage high self-esteem and confidence in users' art

## Demo
![ezgif-3-77e1921f0f](https://user-images.githubusercontent.com/77342694/221417565-f32beb74-69f0-4075-ab94-9590a4b969a8.gif)
![ezgif-3-6b0e4006c3](https://user-images.githubusercontent.com/77342694/221417567-f58d9a59-bc6f-45ac-a8d7-3d44b4f63a87.gif)


## Tech Stack
- Hosted live using Repl.it & UptimeRobot
- Uses Giphy API & Discord API

## Special Thanks
Inspired by and created for my dear friend, Thalia. 

## Notes
Future scaleability plans:
- we can improve the venting feature so that the venting occurs in two parts, first the user asks if they can vent. art bot says "sure.". The next text box is then automatically deleted. Requires "next message" detection mechanism?
- purge() does not work for within bot DMs. Maybe requires change in permissions
- use an AI model so you can converse with the bot as if a real person?

Good overall lesson into python! Had a lot of fun making this bot. 
