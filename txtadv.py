# this is a text adventure game set in Himoto
# the player chooses to play as priest, gryphon, or dragon
# the setup differs, the middle is the same, and the end is choose your own adventure
setup = """Welcome to Himoto: Choose Your Own Adventure!
In the land of Himoto, there are three types of people: humans, dragons, and gryphons.
Among the humans, the dragons and gryphons are known as 'tenshi' and are considered the messengers of the gods. They're revered and feared because of their role in punishing humanity for crimes against each other and against the divine. A special kind of human, who takes the role of priest, has the strength to stand up to the tenshi, and use their power to protect the innocent from harm. Their power is costly and limited: it drains away their life when it's active, and can only be used once every 24 hours. However, it gives them strength, stamina, resilience, and senses far beyond that of a normal human being. Enough to stand up to the tenshi when it counts.
Tenshi have a different way of communicating from humans: they mostly speak telepathically, with verbal sounds conveying only tone. Because of this, humans can't understand the tenshi, and the 'tenshi' believe that humans are relatively smart and accomplished animals, but non-sentient nevertheless because they can't imagine a language that's entirely verbal.
Dragons have many different types, but the ones that live on land in Himoto are fire dragons, with special glands that create venom in the throat. When the venom is expelled, contact with open air ignites it, making them breathe fire that's similar to napalm. Dragons are about the size of elephants, capable of powered flight, and have functioning thumbs with retractable, cat-like claws on their fingertips. 
Gryphons have an affinity for nature, and so are capable of more efficiently working with natural elements, like stone and wood. As such, they make excellent miners, and they 'build' homes by coaxing trees to grow in specific ways, such as very large, hollow trunks big enough to live inside of, or by weaving their branches together to create nests above the ground. Gryphons can be any mix of raptor and feline, are around the size of horses, and capable of powered flight.
"""
player = None
class Dragon:
     starter = "You're flying with your friends. The elders have all told you about how dangerous human settlements are, but you're all young and none of you really believe it. So, when you spot one nearby, you decide to have a little fun. It's too easy! You don't have to get too close because of your auto-igniting venom, and the town begins to burn. None of the weapons the humans have reach high enough or move fast enough to hit any of you. On your way home, while your friends are laughing, you spot something down below. No one notices you dip below them, so you're left behind."
     part2 = "You don't see anything after getting below the forest canopy, but you smell blood. Do you: stalk the smell to ambush potential prey or search for the source to help? If you don't care, you can also leave. Enter 1, 2, or 3: "
     part3 = "You hunker down in the brush and move as quietly as possible. After a few minutes, you come upon a gryphon with a badly wounded shoulder, rendered unable to fly. Dragons and gryphons aren't on the friendliest terms at the moment. It might decide you're a threat and attack once you reveal yourself. You're behind it and have the drop. Do you: pounce and finish the job, step out and ask if you can help, or leave because you don't care?"    
     part3_choice = "Enter 1, 2, or 3: "
     part3_end_one = "You killed the gryphon. The End"
     part3_end_two = "The gryphon killed you. The End"
     part4 = "Coming soon."
     part4_choice = "Enter 1, 2, or 3: "
     game_over = "And then you went home because you don't care about any of this. Did anyone else live happily ever after? Who knows! The End"

class Gryphon:
     starter = "You're out hunting on your own. It's your first time: food is becoming scarce, so hunting parties have been split up into individuals, even those that aren't quite experienced enough, to cover more ground. You spot a huge stag and dive in for the kill, but you're spotted! The stag turns and gores you in the shoulder before bounding away."
     part2 = "The antlers pierced muscles in your shoulder, making it difficult to operate your wing effectively. Do you: call for help, look for shelter, or do nothing? Enter 1, 2, or 3: "
     one = "Help me!"
     two = "Hide me!"
     part3 = "Here's the next part of the gryphon story. Enter 1, 2, or 3: "
     three = "This is Gryphon Option 1 of Choice 2."
     four = "This is Gryphon Option 2 of Choice 2."
     game_over = "You died. The End"

class Priest:
     starter = "You live at Sakuraji. Your home has recently been attacked by dragons and is still recovering. Someone saw a dragon go down in the woods to the southeast. You're tasked with investigating. On horseback, it doesn't take long to reach the general area. There, you dismount to explore on foot so as to go unnoticed."
     part2 = "The forest is eerily silent, a sign that something is wrong. On a tree up ahead, you see a large splash of blood. It leads deeper into the forest, and in that direction, a sudden burst of wind announces the arrival of another tenshi or the exit of the injured one. Do you: follow the blood to render aid to a dangerous god, approach where the wind came from to see what happens, or leave because the matters of gods are not your problem? Enter 1, 2, or 3: "
     one = "What got hurt?"
     two = "What fresh hell is this?"
     part3 = "Here's the next part of the priest story. Enter 1, 2, or 3: "
     three = "This is Priest Option 1 of Choice 2."
     four = "This is Priest Option 2 of Choice 2."
     game_over = "It's probably safest for you and Sakuraji that way. You make it home safely and resume work rebuilding your home. The End"


print(setup)

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
    player = Dragon()
elif myrace == "gryphon":
    player = Gryphon()
else:
    player = Priest()


def get_choice1(player_type):
    global choice1
    print(player_type.starter)
    ans = int(input(player_type.part2))
    if ans == 1:
        choice1 = 1
        print(player_type.part3)
        return choice1
    elif ans == 2:
        choice1 = 2
        print(player_type.part4)
        return choice1
    else:
        print(player_type.game_over)
        quit()

get_choice1(player)

def get_choice2(player_type, choice):
     global choice2
     if choice == 1:
         ans = int(input(player_type.part3_choice))
         if ans == 1:
             print(player_type.part3_end_one)
         elif ans ==2 :
             print(player_type.part3_end_two)
         else: print(player_type.game_over)
     elif choice == 2:
         ans = int(input(player_type.part4_choice))
         if ans == 1:
             choice2 = 1
             print("This is choice 1!")
             return choice2
         elif ans == 2:
             choice2 = 2
             print("This is choice 2!")
             return choice2
     else:
         print(player_type.game_over)

get_choice2(player, choice1)

