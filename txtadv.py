# this is a text adventure game set in Himoto
# the player chooses to play as priest, gryphon, or dragon
# the setup differs, the middle is the same, and the end is choose your own adventure
setup = """Welcome to Himoto: Choose Your Own Adventure!
In the land of Himoto, there are three types of people: humans, dragons, and gryphons.
Among the humans, the dragons and gryphons are known as 'tenshi' and are considered the messengers of the gods. They're revered and feared because of their role in punishing humanity for crimes against each other and against the divine. A special kind of human, who takes the role of priest, has the strength to stand up to the tenshi, and use their power to protect the innocent from harm. Their power is costly and limited: it drains away their life when it's active, and can only be used once every 24 hours. However, it gives them strength, stamina, resilience, and senses far beyond that of a normal human being. Enough to stand up to the tenshi when it counts.
Dragons and gryphons have a different way of communicating from humans: they mostly speak telepathically, with verbal sounds conveying only tone. Because of this, humans can't understand the tenshi, and the 'tenshi' believe that humans are relatively smart and accomplished animals, but non-sentient nevertheless because they can't imagine a language that's entirely verbal.
Dragons have many different types, but the ones that live on land in Himoto are fire dragons, with special glands that create venom in the throat. When the venom is expelled, contact with open air ignites it, making them breathe fire that's similar to napalm. Dragons are about the size of elephants, capable of powered flight, and have functioning thumbs with retractable, cat-like claws on their fingertips. 
Gryphons have an affinity for nature, and so are capable of more efficiently working with natural elements, like stone and wood. As such, they make excellent miners, and they 'build' homes by coaxing trees to grow in specific ways, such as very large, hollow trunks big enough to live inside of, or by weaving their branches together to create nests above the ground. Gryphons can be any mix of raptor and feline, are around the size of horses, and capable of powered flight.
"""
priest_starter = "You live at Sakuraji. Your home has recently been attacked by dragons and is still recovering. Someone saw a dragon go down in the woods to the southeast. You're tasked with investigating. On horseback, it doesn't take long to reach the general area. There, you dismount to explore on foot so as to go unnoticed."
dragon_starter = "You're flying with your friends. The elders have all told you about how dangerous human settlements are, but you're all young and none of you really believe it. So, when you spot one nearby, you decide to have a little fun. It's too easy! You don't have to get too close because of your auto-igniting venom, and the town begins to burn. None of the weapons the humans have reach high enough or move fast enough to hit any of you. On your way home, while your friends are laughing, you spot something down below. No one notices you dip below them, so you're left behind."
gryphon_starter = "You're out hunting on your own. It's your first time: food is becoming scarce, so hunting parties have been split up into individuals, even those that aren't quite experienced enough, to cover more ground. You spot a huge stag and dive in for the kill, but you're spotted! The stag turns and gores you in the shoulder before bounding away."
#race = {"dragon", "priest", "gryphon"}

#print(setup)
#myrace = input("Welcome to Himoto: Choose Your Own Adventure! Are you a priest, a dragon, or a gryphon? ")
#while True:
#    if myrace not in race:
#        print("That's not what was asked.")
#        continue
#    else:
#        print(f"Okay, a {myrace.lower()}, then.")
#        break

name = input("What's your name? ")
print(f"Hello, {name.capitalize()}.")
def getRace(self=None):
        prompt = "Are you a priest, a dragon, or a gryphon? "
        races = "dragon", "priest", "gryphon"
        while (race := input(prompt).lower()) not in races:
            print("That's not what was asked.")
        return race

myrace = getRace()
if myrace == "dragon":
    print(dragon_starter)
elif myrace == "gryphon":
    print(gryphon_starter)
else:
    print(priest_starter)

