import re


def process_message(message: object, response_array: object, response: object) -> object:
    # Splits the message and the punctuation into an array
    list_message = re.findall(r"[\w']+|[.,!?;]", message.lower())

    # Scores the amount of words in the message
    score = 0
    for word in list_message:
        if word in response_array:
            score = score + 1

    # Returns the response and the score of the response
    # print(score, response)
    return [score, response]


def get_response(message):
    # Add your custom responses here
    response_list = [
        process_message(message, ['hello', 'hi', 'hey'], 'Hi Whatup!'),
        process_message(message, ['bye', 'goodbye'], 'Goodbye!'),
        process_message(message, ['food', 'meal', 'calorie', 'provender', 'pabulum'], ':Shop: :1 မြန်မာထမင်းဟင်း: https://www.facebook.com/profile.php?id=100039740742359 :2 ဝတ်သားတုတ်ထိုး: https://www.facebook.com/pigking136/ :3 HotPot: https://www.facebook.com/%e1%80%a1%e1%80%85%e1%80%ac%e1%80%b8%e1%80%90%e1%80%9c%e1%80%ad%e1%80%af%e1%80%84%e1%80%ba%e1%80%b8-hot-pot-2185840031445516/ :4 Grilled Chicken: https://www.facebook.com/thehundredgrilledchicken/ :5 Raw Sea Food Shop: https://www.facebook.com/master-clam-seafood-distributor-1920931431489252/ :6 Sushi Bar Buffet: https://www.facebook.com/thesushibarmyanmar/'),
        process_message(message, ['how', 'are', 'you'], 'I\'m doing fine thanks!'),
        process_message(message, ['wtf'], 'Lee WTF!'),
        process_message(message, ['your', 'name'], 'My name is WaiYan-Bot, nice to meet you!'),
        process_message(message, ['help', 'me'], 'I will do my best to assist you!'),
        process_message(message, ['lee', 'asshole', 'motherfucker', 'lee', 'lar', 'tae', 'ma', 'aye', 'lo', 'ko', 'may', 'ko', 'lo'], 'What the fuck are you saying Idiot!👺👺'),
        process_message(message, ['lord', 'buddha'], 'He guide us True about Peace and Release All Human and Animals Disastrously Life cycle.'),
        process_message(message, ['google', 'google.com', 'www.google.com'], 'https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&ved=2ahUKEwiswp-9u7LzAhUwMlkFHXFBDMsQFnoECAgQAQ&url=https%3A%2F%2Fwww.google.com%2F&usg=AOvVaw1xDfJh-YduXzT4-Mrql0P3'),
        process_message(message, ['telegram', 'telegram.com', 'www.telegram.com'], 'https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjMoYeGvLLzAhVmFVkFHXX8D-wQFnoECAMQAQ&url=https%3A%2F%2Fweb.telegram.org%2F&usg=AOvVaw0lI4JHsSdBRCge6TQdJIip'),
        process_message(message, ['facebook', 'facebook.com'], 'https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwi0mPTSvLLzAhW7MVkFHVc6CK4QFnoECAYQAQ&url=https%3A%2F%2Fwww.facebook.com%2F&usg=AOvVaw2q27ov2cpCynr72DmuSqEz'),
        process_message(message, ['twitter'], 'https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwiqqcSFvbLzAhUnGFkFHSClD7gQFnoECAgQAQ&url=https%3A%2F%2Ftwitter.com%2F%3Flang%3Den&usg=AOvVaw1Sd3B-_cNZOLSmhw9z2lOm'),
        process_message(message, ['min', 'thant', 'zin'], ':Telegram: @MinThantZin'':Facebook: https://www.facebook.com/chhddghhfddggssfjijcxdddghhcdd'),
        process_message(message, ['kyaw', 'zayer', 'soe'], ':Facebook: https://www.facebook.com/pando.zuker.5 :Telegram: @kuro_zion  :GitHub:  github.com/kyaw-zayar-soe/'),
        process_message(message, ['minaunghlaing', 'mal', 'sakha'], 'The man Who know Fucking Brainless Junta.'),
        process_message(message, ['sexy', 'girl', 'loli', 'lolicom', 'littlegirl', 'hot'], 'FuckBoy!👌'),
        process_message(message, ['wrong', 'bad', 'stupid', 'false'], 'Yeach,You Are Fucker!'),
        process_message(message, ['ok', 'got', 'it', 'yeach', 'good', 'very well'], 'Welcome,My Fucking  Friend!'),
        process_message(message, ['fuck', 'son', 'bitch'], 'Fuck you Motherfucker!🖕'),
        process_message(message, ['find'], 'ဘာ find တာလဲဟ :🧐:'),
        process_message(message, ['label', 'jonnyWalker'], 'JWalker 2015 logo.png Type	Scotch whisky Manufacturer	Diageo Country of origin	Kilmarnock, East Ayrshire, Scotland Introduced	1820: Grocery store 1865: Whisky blending Related products	Ballantine, Buchanan Chivas Regal, Cutty Sark, Dewar Vat 69 Website	johnniewalker.com'),
        process_message(message, ['grand', 'royal'], 'International Beverages Trading Company Group  abbreviated IBTC is a major Myanmar-based beverage manufacturing company.1 IBTC possesses 80% of Myanmar domestic whiskey market with a revenue of US$100 million.1IBTC was founded in 1995 with 50 employees by Aung Moe Kyaw, the son-in-law of Thein Tun, chairman of the Myanmar Golden Star Group.[1] It is known for its alcohol brands, including Grand Royal Whiskey, Royal Dry Gin, Eagle Whiskey, Grand Royal Special Reserve Whiskey, Hero Whiskey, and Golden Island Whiskey.'),
        process_message(message, ['vodka'], 'Vodka is a clear distilled alcoholic beverage. Different varieties originated in Poland, Russia and Sweden. Vodka is composed mainly of water and ethanol, but sometimes with traces of impurities and flavourings. Traditionally it is made by distilling liquid from fermented cereal grains.'),
        process_message(message, ['peace'], 'Peace is a concept of societal friendship and harmony in the absence of hostility and violence. In a social sense, peace is commonly used to mean a lack of conflict and freedom from fear of violence between individuals or groups. Wikipedia'),
        process_message(message, ['photo', 'picture'], 'what photo or picture'),
        process_message(message, ['nug', 'pdf', 'crph'], ':Telegram: https://t.me/click2donate2'' :Facebook: :1: https://www.facebook.com/NUGmyanmar/, :2: https://www.facebook.com/PDF-Channel-106003028468709/'),
        process_message(message, ['channel' 'myanmar'], ':Website:http://www.channelmyanmar.org'':telegram:https://t.me/ChannelMyanmarTeam'),
        process_message(message, ['mmsubtitle'], ':Website:''http://MMSubtitles.co'':telegramlink:''https://t.me/MMSubtitlesOfficial'),
        process_message(message, ['movie', 'link'], ':Website: http://www.channelmyanmar.org :telegram: https://t.me/ChannelMyanmarTeam :Website:''http://MMSubtitles.co:telegramlink: https://t.me/MMSubtitlesOfficial'),
        process_message(message, ['udemy'], 'https://t.me/coursecouponclub'),
        process_message(message, ['anime'], ':Facebook: https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwi0mPTSvLLzAhW7MVkFHVc6CK4QFnoECAYQAQ&url=https%3A%2F%2Fwww.facebook.com%2F&usg=AOvVaw2q27ov2cpCynr72DmuSqEz :Telegram: https://t.me/Animewatching'),
        process_message(message, ['hentai'], ':1: https://t.me/hentaiNekofied :2: https://hentaidude.com/ :3: https://hentaidude.xxx/ :3 Nude Pics: https://beta.sankakucomplex.com/?tags=order%3apopularity'),
        process_message(message, ['what'], 'what!What?'),
        process_message(message, ['liquor', 'alcohol', 'cocktail'], 'Are You Alcoholic🤮'),
        process_message(message, ['မအလ', 'စခ', 'ကမကလ'], 'Fucking Brainless Junta🤯'),
        process_message(message, ['happy'], '😊'),
        process_message(message, ['sad'], '☹'),
        process_message(message, ['why'], '🤔'),
        process_message(message, ['bless'], '😇'),
        process_message(message, ['goodjob'], '👍'),
        process_message(message, ['evil'], '😈'),
        process_message(message, ['dead'], '☠'),
        process_message(message, ['corona'], ':Type: Beer :Manufacturer: Grupo Modelo, AB InBev :Country of origin:Mexico :Alcohol by volume:	4.5%[1] :Style: Pale lager :Website: corona.com'),
        process_message(message, ['cool'], '🤩'),
        process_message(message, ['money', 'cash', 'dollar'], '🤑'),
        process_message(message, ['though', 'thinker', 'mind'], 'The mind is about mental processes, thought and consciousness. ... Many theories have been put forward to explain the relationship between what we call your mind (defined as the conscious thinking :you: which experiences your thoughts) and your brain (i.e., part of your body).'),
        process_message(message, ['angry'], '🤬'),
        process_message(message, ['bot', 'automation'], 'https://www.kaspersky.com/resource-center/definitions/what-are-bots'),
        process_message(message, ['shit'], '💩'),
        process_message(message, ['sick'], '🤮'),
        process_message(message, ['tv', 'television'], 'Television, sometimes shortened to TV or telly, is a telecommunication medium used for transmitting moving images in monochrome (black and white), ...'),
        process_message(message, ['emoji'], '😂😘❤️😍😊😁👍☺️😄😔😭💋😒😉😳😃😜🙈😝😢😌😡😏😀😅😞🔇😚😌😋🙊👌😆😵♣️🖕📸👺😐🕒♠️😕🥲😇🔊🤣😛🤫😪🤮🤐🥴🤢😷🤧🤒🤕🤑🤠😈👿👹👺🤡💩😸👻😹💀😻☠👽😼👾😽🤖🙀👍🤝😿😾🤲🙌👐🤘👌👋✍👆🖖🦿🗣👨‍🦱🫁👃💄🦷👱‍♀👅👨‍🦰🧠👤🗣👩‍⚕👨‍🎤🧑‍🏫👮🧑‍⚕👩‍🍳🧚🧜‍♀🧟🐛🐣🐧🪲🦟🐥🐧🦄💐🍁🌍🐚🌗🌙🍫🍢🍚🍵🍿🎂🚙🪗🚜🕋🏥🏩🏙🌄⛩'),
        process_message(message, ['liar', 'bilk', 'cheat', 'con', 'cozen', 'crook', 'daub', 'deceit', 'diddle', 'dupe', 'faker'], '🤥'),
        process_message(message, ['wai', 'yan', 'tun'], ':Telegram: :1: @Creation0 :3: @badbloodboy_bot :4:https://t.me/barlarlardawn1 :Facebook: :1: https://www.facebook.com/new.gate.5036'),
        process_message(message, ['lol', 'olo', 'fucker', 'dick'], 'FuckYou.Dick Head!'),
        process_message(message, ['wikipedia'], ' https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwiHkIGK0r_zAhVQhHIEHbRjAnoQFnoECAYQAQ&url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FMain_Page&usg=AOvVaw1rzc4UVx4rSWqA-Z7DQ3um&cshid=1633862045143530'),
        process_message(message, ['porn'], ':1: https://adult.noodlemagazine.com/video/best+ever :2: https://www.pornhub.com/video/search?search=free+porn+hug :3: https://www.xnxx.com/search/porn :4: https://www.xvideos3.com/tags/porn'),
        process_message(message, ['book', 'study'], ':1: https://t.me/amazonebook :2: https://t.me/premium_ebooks :3: https://t.me/bookshub25 :4: https://t.me/NovelsRepositoryDiscussions :5: https://t.me/epubkindlebooksmm :6: https://t.me/joinchat/5_Dp81LY8DVjMjY1'),
        process_message(message, ['aquariam', 'fish', 'freshwater', 'fishtank'], ':https://t.me/gu_guandgi_gi_aquarium:')
        # Add more responses here
    ]

    # Checks all of the response scores and returns the best matching response
    response_scores = []
    for response in response_list:
        response_scores.append(response[0])

    # Get the max value for the best response and store it into a variable
    winning_response = max(response_scores)
    matching_response = response_list[response_scores.index(winning_response)]

    # Return the matching response to the user
    if winning_response == 0:
        bot_response = 'I didn\'t understand what you wrote.'
    else:
        bot_response = matching_response[1]

    print('Bot response:', bot_response)
    return bot_response


# Test your system
get_response('What is your name bro?')
get_response('Can you help me with something please?')
