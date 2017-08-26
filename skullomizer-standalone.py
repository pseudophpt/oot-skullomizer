from random import randint
import random

# Set seed
seed = input('Seed: ')
random.seed(seed)

used_skulls = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
current_skulls = [0,0,0,0,0]
amt_skulls = 0
skulltxt="""
    (Child/Day or Night) Inside the Deku Tree - in an alcove with a chest in it, on floor 3F
    (Child/Day or Night) Inside the Deku Tree - on the vines that take you back to 1F (the gold skulltula is on floor B1)r
    (Child/Day or Night) Inside the Deku Tree - on the bars in the central room of floor B1
    (Child/Day or Night) Hyrule Castle Town Market - in a box in the guardhouse
    (Child/Day or Night) Path to Hyrule Castle - roll attack the tree by the entrance of the path to Hyrule Castle
    (Child/Day or Night) Lon Lon Ranch - roll attack the tree near the entrance to the field
    (Child/Day or Night) Kakariko Village - roll attack the tree in town
    (Child/Night) Kakariko Village - on the back wall of the house nearest the Death Mountain Trail entrance
    (Child/Night) Kakariko Village - on the ladder up to the lookout tower (use slingshot)
    (Child/Night) Kakariko Village - below the window of the House of Skulltula (there are non-gold skulltulas inside)
    (Child/Night) Kakariko Village - on the pile of bricks on the plot of land that's under construction
    (Child/Day or Night) Kakariko Graveyard - drop a bug in the soft soil
    (Child/Day or Night) Death Mountain Trail - drop a bug in the soft soil by the entrance to Dodongo's Cavern
    (Child/Day or Night) Dodongo's Cavern - beyond the bombable wall in a room with baby dodongos, on floor 1F
    (Child/Day or Night) Dodongo's Cavern - at the top of the room with the stairs you bombed, on the vines (on floor 2F)
    (Child/Day or Night) Dodongo's Cavern - in the room accessible by pushing a block to a bombable wall, on floor 1F
    (Child/Day or Night) Death Mountain Crater - just inside the entrance in a crate
    (Child/Day or Night) Zora's River - roll attack the tree at the entrance to Zora's River
    (Child/Night) Zora's River - on the ladder at the base of the waterfall
    (Child/Day or Night) Lake Hylia - drop a bug in the soft soil in front of the Lakeside Laboratory
    (Child/Night) Lake Hylia - on a small square island near the middle of the lake
    (Child/Day or Night) Zora's Fountain - roll attack the tree by the bombable wall
    (Child/Day or Night) Inside Jabu-Jabu's Belly - on some vines in a room with rising water, on floor B1
    (Child/Day or Night) Inside Jabu-Jabu's Belly - in the room you reach by dropping down a hole, on a wall on floor B1
    (Child/Day or Night) Inside Jabu-Jabu's Belly - not far from the last one, on a wall on floor B1
    (Child/Day or Night) Inside Jabu-Jabu's Belly - on the vines leading up to a spiderweb wall, on floor 1F
    (Child/Night) Zora's Fountain - on the wall near the end of the log in the southeast area
    (Child/Night) Kakariko Graveyard - on the wall to the right of the second row of graves
    (Adult or Child/Night) Death Mountain Trail - bomb the wall just past the entrance to the trail
    (Child/Day or Night) Goron City - in a room reachable by bombing boulders, in a crate in the far right corner
    (Child/Night) Kokiri Forest - behind the Know-it-all-Brothers House
    (Child/Day or Night) Kokiri Forest - drop a bug in the soft soil next to the Kokiri shop.
    (Child/Day or Night) Inside the Deku Tree - in a room behind a bombable wall, on floor B1
    (Child/Day or Night) Lost Woods - in an area with two Business Scrubs, drop a bug in the soft soil
    (Child/Day or Night) Lost Woods - just beyond the area with the skull kid, drop a bug in the soft soil
    (Child/Night) Lake Hylia - on the back wall of the Lakeside Laboratory
    (Adult or Child/Night) Hyrule Field - bomb the circle of stones outside the path to Gerudo Valley
    (Child/Night) Gerudo Valley - on the water spout by the first bridge
    (Child/Day or Night) Gerudo Valley - drop a bug in the soft soil by the river below the second bridge
    (Child/Night) Lon Lon Ranch - on a window on the house next to the stable
    (Child/Night) Lon Lon Ranch - on the wall by the silo in the eastern part of the corral area
    (Child/Night) Lon Lon Ranch - behind the corral shed
    (Adult or Child/Day or Night) Hyrule Field - bomb the tree east of the entrance to Hyrule Castle Town to reveal a hole
    (Adult/Day or Night) Ice Cavern - in the room with the silver rupees, behind some icicles
    (Adult/Day or Night) Ice Cavern - in a room with falling icicles, the compass, and a piece of heart
    (Adult/Day or Night) Ice Cavern - in the block puzzle room
    (Adult/Day or Night) Lake Hylia - sink to the bottom of the lakeside laboratory with the iron boots and Zora's tunic, then roll attack the crate to find a gold skulltula
    (Adult/Night) Kokiri Forest - on top of the House of Twins
    (Adult/Night) Lost Woods - Plant a Magic Bean deep within the Lost Woods as a child. Then find the bean sprout as an adult and ride it to reach the Gold Skulltula.
    (Adult/Night) Sacred Forest Meadow - On the high wall above the maze. You have to be standing on top of a wall of the maze to reach it.
    (Adult/Day or Night) Forest Temple - on the vines in the first room, on floor 1F
    (Adult/Day or Night) Forest Temple - on the wall next to stairs in the central room, on floor 1F
    (Adult/Day or Night) Forest Temple - reached by using the hookshot on the front of a small chest on a ledge, in the East Courtyard, on floor 1F
    (Adult/Day or Night) Forest Temple - at the end of the stone walkway above the West Courtyard, on floor 1F
    (Adult/Day or Night) Forest Temple - in the room that can be rotated, on floor B2
    (Adult/Day or Night) Ganon's Castle - behind the arch near the edge of the lava pit
    (Adult/Day or Night) Goron City - On the back of the hanging platform on the top floor. Walk on the ropes to reach it.
    (Adult/Day or Night) Fire Temple - on a wall in a room with a Like Like and floating tiles, on floor 1F
    (Adult/Day or Night) Fire Temple - behind a bombable wall in the room with the rolling boulders, on floor 3F
    (Adult/Day or Night) Fire Temple - in the room reached by playing Scarecrow's Song in the boulder room, on floor 4F
    (Adult/Day or Night) Fire Temple - in the large circular room with 200 rupees in it, on floor 5F
    (Adult/Day or Night) Fire Temple - reached from the first room of the dungeon, in the rooms beyond the totem, on floor 1F
    (Adult/Night) Death Mountain - behind a rock in the area with eruptions
    (Adult/Night) Death Mountain - behind a rock on the ledge above Dodongo's Cavern
    (Adult/Day or Night) Water Temple - bomb the cracked floor on 1F, spin attack gate to reach it
    (Adult/Day or Night) Water Temple - in a corner of the vortex creek on 1F
    (Adult/Day or Night) Water Temple - on north wall of room with platforms that fall down waterfall, on 3F
    (Adult/Day or Night) Water Temple - on the wall behind where boulders come down on 1F
    (Adult/Day or Night) Water Temple - inside the tower, reached with the longshot on 3F
    (Adult/Night) Lake Hylia - on the tree atop the island of the Water Temple
    (Child/Day or Night) Under the Well - in a locked room reached from the center room on 1F
    (Child/Day or Night) Under the Well - in a locked room reached from the center room on 1F
    (Child/Day or Night) Under the Well - in a room with a Like Like on 1F
    (Adult/Day or Night) Shadow Temple - in a room with an invisible spinning blade on B4
    (Adult/Day or Night) Shadow Temple - in a cell in a room with falling spikes on B4
    (Adult/Day or Night) Shadow Temple - in a room with a single flaming skull on B4
    (Adult/Day or Night) Shadow Temple - in the room where the ghost ship is first seen on B4, reached with Scarecrow's song
    (Adult/Day or Night) Shadow Temple - in a room with three spinning flaming skulls on B4
    (Adult/Night) Gerudo Valley - behind the carpenter's tent
    (Adult/Night) Gerudo Valley - on the rock arch
    (Adult/Night) Gerudo Fortress - on a rock wall above the fortress
    (Adult/Night) Gerudo Fortress - on the far archery target in the archery range
    (Adult/Day or Night) Haunted Wasteland - inside the stone building
    (Child/Day or Night) Death Mountain Crater - play Bolero of Fire and drop a bug in the soft soil
    (Child/Day or Night) Hyrule Castle - Go to the area in front of Hyrule Castle where you woke up Talon the first time. Find the tree near the moat. Play the Song of Storms next to the tree to reveal a hole. Fall into the hole.
    (Child/Day or Night) Desert Colossus - drop a bug in the bean hole by the Spirit Temple entrance
    (Child/Day or Night) Spirit Temple - on a grating wall on 1F
    (Child/Day or Night) Spirit Temple - opposite a brick climbing wall on 1F
    (Child/Day or Night) Spirit Temple - above the door in the corridor just before Iron Knuckle
    (Adult/Night) Desert Colossus - on a tree by the empty pond
    (Adult/Night) Desert Colossus - on the second rocky mound reached with the beanstalk
    (Adult/Day or Night) Spirit Temple - in a niche in rolling boulder room, 1F
    (Adult/Day or Night) Spirit Temple - in the big statue room on 3F, reached by playing Scarecrow's Song
    (Adult/Night) Kakariko Village - on the roof of Impa's house (next to the Cucco pen)
    (Adult/Day or Night) Dodongo's Cavern - Set off all the bombs to lower the stairs. Use the Longshot to kill the Gold Skulltula in the alcove above the stairs.
    (Adult/Day or Night) Dodongo's Cavern - In the room with the baby Dodongos, play Scarecrow's Song to reach a ledge with a Gold Skulltula
    (Adult/Night) Zora's River - In the west side of Zora's River, there is a place where a narrow part of the river goes between two tall walls. Go to the east side of those walls to find a ledge that goes between them. Climb onto that ledge, then climb the ladder at the end of the ledge. At night, there is a Gold Skulltula on a wall near that ladder.
    (Adult/Night) Zora's River - At night, stand in front of the waterfall that goes to Zora's Domain, and turn around so your back is to the waterfall. You will see a Gold Skulltula on the wall up ahead.
    (Adult/Night) Zora's Domain - to the left of the top of the frozen waterfall
    (Adult/Night) Zora's Fountain - Make sure it's night. Go over to the entrance to the Great Fairy fountain, where there is a grey stone. You can only lift it if you have the silver gauntlets, so lift it, then hammer the small rock that was below it and drop into the hole. Turn on the Lens of Truth to see some hidden regular skulltulas. Kill them and go up the slope to the top, where the hundredth gold skulltula is waiting!
    """

for skull in range (0,5):
	# Choose 5 random numbers between 0 and 99
	skull_no = randint(0, 99)
	# Set them as used
	used_skulls[skull_no] = 1
	# And set the current skulls to those 5
	current_skulls[skull] = skull_no
for skull in range (0,5):
	# Print current skulls
	textline = skulltxt.split('\n')[current_skulls[skull]]
	print(str(skull + 1) + ". "+textline)

while 1:
	# Get input for which completed skull
	number = input('Skull no.:')
	number_int = int(number) - 1
	# Increment and display points
	amt_skulls += 1
	print("Points: " + str(amt_skulls))
	# Generate random numbers until a valid uncompleted skull is found
	x = 0
	while x == 0: 
		skull_no = randint(0, 99)
		if used_skulls[skull_no] == 0:
			x = 1
	# Set it as used and add it to the current 5 to replace the last gotten skull
	used_skulls[skull_no] = 1
	current_skulls[number_int] = skull_no
	# Print current skulls
	for skull in range (0,5):
		textline = skulltxt.split('\n')[current_skulls[skull]]
		print(str(skull+1) + ". "+textline)