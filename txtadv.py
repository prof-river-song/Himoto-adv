# this is a text adventure game set in Himoto
# the player chooses to play as priest, gryphon, or dragon
# the setup differs, the middle is the same, and the end is choose your own adventure

class Game:
    def __init__(self) -> None:
        self.setup = """Welcome to Himoto: Choose Your Own Adventure!
In the land of Himoto, there are three types of people: humans, dragons, and gryphons.
Among the humans, the dragons and gryphons are known as 'tenshi' and are considered the messengers of the gods. They're revered and feared because of their role in punishing humanity for crimes against each other and against the divine. A special kind of human, who takes the role of priest, has the strength to stand up to the tenshi, and use their power to protect the innocent from harm. Their power is costly and limited: it drains away their life when it's active, and can only be used once every 24 hours. However, it gives them strength, stamina, resilience, and senses far beyond that of a normal human being. Enough to stand up to the tenshi when it counts.
Tenshi have a different way of communicating from humans: they mostly speak telepathically, with verbal sounds conveying only tone. Because of this, humans can't understand the tenshi, and the 'tenshi' believe that humans are relatively smart and accomplished animals, but non-sentient nevertheless because they can't imagine a language that's entirely verbal.
Dragons have many different types, but the ones that live on land in Himoto are fire dragons, with special glands that create venom in the throat. When the venom is expelled, contact with open air ignites it, making them breathe fire that's similar to napalm. Dragons are about the size of elephants, capable of powered flight, and have functioning thumbs with retractable, cat-like claws on their fingertips. 
Gryphons have an affinity for nature, and so are capable of more efficiently working with natural elements, like stone and wood. As such, they make excellent miners, and they 'build' homes by coaxing trees to grow in specific ways, such as very large, hollow trunks big enough to live inside of, or by weaving their branches together to create nests above the ground. Gryphons can be any mix of raptor and feline, are around the size of horses, and capable of powered flight.
"""
        self.player=None
        self.last_choice=None

class Dragon:
    def __init__(self) -> None:
        self.choices = {
            "starter":"You're flying with your friends. The elders have all told you about how dangerous human settlements are, but you're all young and none of you really believe it. So, when you spot one nearby, you decide to have a little fun. It's too easy! You don't have to get too close because of your auto-igniting venom, and the town begins to burn. None of the weapons the humans have reach high enough or move fast enough to hit any of you. On your way home, while your friends are laughing, you spot something down below. No one notices you dip below them, so you're left behind.",       
            "part2" : "You don't see anything after getting below the forest canopy, but you smell blood. Do you: stalk the smell to ambush potential prey or search for the source to help? If you don't care, you can also leave. Enter 1, 2, or 3: ",
            "part3" : "You hunker down in the brush and move as quietly as possible. After a few minutes, you come upon a gryphon with a badly wounded shoulder, rendered unable to fly. Dragons and gryphons aren't on the friendliest terms at the moment. It might decide you're a threat and attack once you reveal yourself. You're behind it and have the drop. Do you: pounce and finish the job, step out and ask if you can help, or leave because you don't care?",
            "make_a_choice" : "Enter 1, 2, or 3: ",
            "end_one" : "You killed the gryphon. The End",
            "end_two" : "The gryphon killed you. The End",
            "part4" : "You follow the scent to a trail of blood. Large smears of it lead the way deeper into the woods until you see a small cave opening. A gryphon with a wounded shoulder lies inside. Do you: attack it while it's cornered, reveal yourself, or leave because the mystery is solved?",
            "part5" : "Do you spray your fire venom into the cave from cover, leap into the cave to fight tooth and claw, or change your mind and leave?",
            "good_ending" : f"You introduce yourself and ask if you can help the gryphon recover. \nThe gryphon says, \"Thank you, {name.capitalize()}. My home is a grove twenty minutes to the east. Would you go let them know that Willow's been injured?\"\nYou agree, and Willow makes it home safely. You saved the gryphon! And everyone lived happily ever after. The End",
            "game_over" : "And then you went home because you don't care about any of this. Did anyone else live happily ever after? Who knows! The End",
        }

class Gryphon:
     def __init__(self) -> None:
         self.choices = {
            "starter" : "You're out hunting on your own. It's your first time: food is becoming scarce, so hunting parties have been split up into individuals, even those that aren't quite experienced enough, to cover more ground. You spot a huge stag and dive in for the kill, but you're spotted! The stag turns and gores you in the shoulder before bounding away.",
            "part2" : "The antlers pierced muscles in your shoulder, making it difficult to operate your wing effectively. Do you: call for help, look for shelter, or do nothing? Enter 1, 2, or 3: ",
            "part3" : "You let out a piercing cry that extends across the whole forest and up to the clouds.\n\"Can anyone hear me? I'm hurt and need help!\"\nNot long after that, a human appears through the trees. Oh great, humans can't talk but they're quite deadly in groups. Do you: try asking them for help even though they don't understand language, preemptively attack the wild creature, or wait to see what happens?",
            "make_a_choice" : "Enter 1, 2, or 3: ",
            "end_one" : "They killed you. The End",
            "end_two" : "You killed them, then bled out and died. The End",
            "part4" : "Though bleeding badly, you find a shallow cave not too far away to settle down in. There's now only one way in or out, which is a defensive advantage but also puts you in a corner. Next, a dragon appears from through the trees, apparently having followed the trail of your blood. It asks if you need help, but dragons and gryphons aren't on the best of terms right now. It could be a trap. Do you: tell it to fuck off, ask for help, or wait to see what happens?",
            "part5" : "The dragon says, \"Well, fuck you, too.\" Do you: apologize, preemptively attack the now probably hostile dragon, or wait to see what happens?",
            "good_ending" : f"You introduce yourself and ask if the dragon will help you contact your family.\nThe dragon says, \"Well met, {name.capitalize()}. I'm Sage. My friend Willow lives in the same grove. I'll be back soon with help.\"\nYou thank Sage, and they leave. Before you pass out from blood loss, they return with your whole family. You've been saved! And everyone lived happily ever after. The End",
            "game_over" : "No one helped you. You bled out and died. The End",
        }

class Priest:
     def __init__(self) -> None:
         self.choices = {
            "starter" : "You live at Sakuraji. Your home has recently been attacked by dragons and is still recovering. Someone saw a dragon go down in the woods to the southeast. You're tasked with investigating. On horseback, it doesn't take long to reach the general area. There, you dismount to explore on foot so as to go unnoticed.",
            "part2" : "The forest is eerily silent, a sign that something is wrong. On a tree up ahead, you see a large splash of blood. It leads deeper into the forest, and after some tracking leads you to a dragon bleeding profusely from the shoulder. Though you don't see a weapon, it most likely was injured in the attack on your home. The others might be back any moment to help him. According to your beliefs, dragons only attack those who have sinned, and you've dedicated your life to helping others. It could be safe. Do you: watch and see what happens, reveal yourself, or leave because the matters of gods are not your problem? Enter 1, 2, or 3: ",
            "part3" : "The wind shifts and the dragon's nostrils flare. He looks right at you! With one spray of venom, he could light you on fire, but you might have an opening before he decides what to you. Do you: step out with your hands spread to show you're not a threat, use your power and finish the dragon off before he can attack you, or leave because you have a home to protect?",
            "make_a_choice" : "Enter 1, 2, or 3: ",
            "end_one" : "You were fried until only ash was left. The End",
            "end_two" : "You killed him and went home. The End",
            "part4" : "The dragon lifts his head and looks directly at you. The reptilian face is difficult to read, but it doesn't seem to have any hostile intent. For the moment. You're able to slowly approach to be within striking distance. The dragon growls, but otherwise his face doesn't change. It's unclear if dragons even have facial expressions to read. Do you: take your chances to finish off the dragon before he kills you, attempt to treat the bleeding wound, or back away slowly because growls are definitely warnings and you're not stupid?",
            "part5" : "Normally, you would absolutely need to use your power to fight one of the tenshi, but this one is quite badly injured already. Do you: draw your sword and lop his head off, use your power and kill him with your bare hands, or change your mind and back away slowly?",
            "good_ending" : "By using very slow, easy movements, you're able to approach and draw out your medical supplies. The dragon watches carefully but makes no move to stop you. As you apply a salve to stop the bleeding, he puts his head down. You have to rip up your shirt, but you manage to bandage it so it's protected from the elements. He sighs, perhaps in contentment. That's all you can do for him, so you slowly move away and head home. The next day, the tenshi alarm sounds, but it's the dragon from the woods, flying away. You saved his life! And everyone lived happily ever after. The End",
            "game_over" : "It's probably safest for you and Sakuraji that way. You make it home safely and resume work rebuilding your home. The End",
        }

game_state = Game()
print(game_state.setup)

name = input("What's your name? ")
print(f"Hello, {name.capitalize()}.")
def getRace(self=None):
        prompt = "Are you a priest, a dragon, or a gryphon? "
        races = "dragon", "priest", "gryphon"
        while (race := input(prompt).lower()) not in races:
            print("Invalid.")
        return race

myrace = getRace()

if myrace == "dragon":
    game_state.player = Dragon()
elif myrace == "gryphon":
    game_state.player = Gryphon()
else:
    game_state.player = Priest()


def get_choice1(player_type):
    print(player_type.choices["starter"])
    ans = int(input(player_type.choices["part2"]))
    if ans == 1:
        choice = 1
        print(player_type.choices["part3"])
        return choice
    elif ans == 2:
        choice = 2
        print(player_type.choices["part4"])
        return choice
    else:
        print(player_type.choices["game_over"])
        quit()

game_state.last_choice = get_choice1(game_state.player)

def get_choice2(player_type, choice):
     if choice == 1:
         #part 3 choice
         ans = int(input(player_type.choices["make_a_choice"]))
         if ans == 1:
             print(player_type.choices["end_one"])
         elif ans ==2 :
             print(player_type.choices["end_two"])
         else: 
             print(player_type.choices["game_over"])
             quit()
     elif choice == 2:
         #part 4 choice
         ans = int(input(player_type.choices["make_a_choice"]))
         if ans == 1:
             choice = 1
             print(player_type.choices["part5"])
             return choice
         elif ans == 2:
             choice = 2
             print(player_type.choices["good_ending"])
             return choice
         else:
             print(player_type.choices["game_over"])
             quit()
     else:
         print(player_type.game_over)
         quit()

game_state.last_choice = get_choice2(game_state.player, game_state.last_choice)

def get_choice3(player_type, choice):
    ans = int(input(player_type.choices["make_a_choice"]))
    if ans == 1:
        choice = 1
        print(player_type.choices["end_one"])
        return choice
    elif ans == 2:
        choice = 2
        print(player_type.choices["end_two"])
        return choice
    else:
        print(player_type.choices["game_over"])

if game_state.last_choice == 2:
    quit()

get_choice3(game_state.player, game_state.last_choice)