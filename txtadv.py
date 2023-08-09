# this is a text adventure game set in Himoto
# the player chooses to play as priest, gryphon, or dragon
# the setup differs, the middle is the same, and the end is choose your own adventure
race = input("Welcome to Himoto: Choose Your Own Adventure! Are you a priest (human), a dragon, or a gryphon? ")
print(f"Okay, a {race.lower()}, then.")
name = input("How about a name? ")
lets_go = input(f"Are you ready to get started, {name.capitalize()}? ")
if lets_go == True:
    print("Now we start the story.")
setup = """In the land of Himoto, there are three types of people: humans, dragons, and gryphons.
Among the humans, the dragons and gryphons are known as 'tenshi' and are considered the messengers of the gods. They're revered and feared because of their role in punishing humanity for crimes against each other and against the divine. A special kind of human, who takes the role of priest, has the strength to stand up to the tenshi, and use their power to protect the innocent from harm. Their power is costly and limited: it drains away their life when it's active, and can only be used once every 24 hours. However, it gives them strength, stamina, resilience, and senses far beyond that of a normal human being. Enough to stand up to the tenshi when it counts.
Dragons and gryphons have a different way of communicating from humans: they mostly speak telepathically, with verbal sounds conveying only tone. Because of this, humans can't understand the tenshi, and the 'tenshi' believe that humans are relatively smart and accomplished animals, but non-sentient nevertheless because they can't comprehend of language that's entirely verbal.
Dragons have many different 
"""
priest_starter = "{name}, you're a priest living at Sakuraji. Your home has recently been attacked by dragons and is still recovering. A report from a nearby farming village claims that a gryphon may have been injured and is hiding out in the woods to the southeast. You're tasked with investigating."
dragon_starter = "{name}, you're a dragon out flying with your friends. The elders have all told you about how dangerous human settlements are, but you're all young and none of you really believe it. So, when you spot one nearby, you decide to have a little fun. It's too easy! You don't have to get too close because of your auto-igniting venom, and the town begins to burn. None of the weapons the humans have reach high enough or move fast enough to hit any of you. On your way home, while your friends are laughing, you spot something down below. No one notices you dip below them, so you're left behind."
gryphon_starter = "{name}, you're a gryphon out hunting on your own. "