f = open('valid-wordle-words.txt', 'r')
import random

f = list(f)


word_list = []
for i in f:
    i.upper()
    word_list.append(f'{i[0]}{i[1]}{i[2]}{i[3]}{i[4]}')

common_list = [
    "About", "After", "Again", "Below", "Could", "Every", "First", "Great", "House", "Large",
    "Never", "Other", "Place", "Right", "Small", "Sound", "Still", "Think", "Three", "Where",
    "World", "Youth", "Alone", "Early", "Human", "Known", "Light", "Maybe", "Night", "Quite",
    "Sense", "Voice", "Whole", "Above", "Black", "Carry", "Close", "Drive", "Enter", "Fight",
    "Green", "Heart", "Learn", "Month", "Power", "Ready", "Table", "Union", "Water", "Woman",
    "Angry", "Blood", "Break", "Check", "Death", "Earth", "Floor", "Force", "Frank", "Front",
    "Grass", "Happy", "Heavy", "Horse", "Level", "Major", "March", "Music", "Party", "Peace",
    "Press", "Reach", "Scene", "Solid", "South", "Speak", "Speed", "Sport", "Stand", "Start",
    "State", "Study", "Teach", "Thank", "Touch", "Train", "Trust", "Truth", "Voice", "Waste",
    "Watch", "Whole", "World", "Young", "Apple", "Beach", "Brown", "Clock", "Cross", "Dance",
    "Dream", "Drink", "Dress", "Earth", "Field", "Fight", "Flash", "Fruit", "Glass", "Golds",
    "Greet", "Group", "Guide", "Horse", "Hotel", "House", "Image", "Index", "Inner", "Joint",
    "Light", "Lower", "Magic", "Match", "Medal", "Metal", "Money", "Music", "Night", "Offer",
    "Order", "Party", "Peace", "Phone", "Plane", "Plant", "Power", "Press", "Price", "Prime",
    "Radio", "Raise", "Reach", "Ready", "Relax", "River", "Round", "Scale", "Scene", "Sense",
    "Serve", "Shape", "Share", "Shift", "Shirt", "Shore", "Short", "Smart", "Smile", "Smoke",
    "Sound", "Space", "Speak", "Speed", "Spend", "Sport", "Stand", "Start", "State", "Stone",
    "Story", "Study", "Table", "Teach", "Thank", "Think", "Throw", "Touch", "Train", "Trust",
    "Union", "Value", "Visit", "Voice", "Waste", "Water", "Whole", "Woman", "World", "Write",
    "Young", "Adult", "Alarm", "Angle", "Arrow", "Badge", "Bench", "Block", "Bread", "Brick",
    "Brush", "Carve", "Chain", "Chair", "Chart", "Cheat", "Cheer", "Child", "Climb", "Clock",
    "Cloud", "Coach", "Coast", "Color", "Crown", "Dance", "Draft", "Earth", "Edge", "Equip",
    "False", "Flash", "Frame", "Giant", "Guide", "Heart", "House", "Human", "Image", "Judge",
    "Knife", "Light", "Limit", "Magic", "Metal", "Money", "Mount", "Night", "Noise", "North",
    "Ocean", "Paint", "Paper", "Peace", "Piece", "Pilot", "Place", "Plant", "Point", "Power",
    "Press", "Prize", "Queen", "Radio", "Reach", "Relax", "River", "Scale", "Scene", "Score",
    "Sense", "Serve", "Share", "Shirt", "Shore", "Short", "Sight", "Slice", "Smile", "Sound",
    "Space", "Speak", "Speed", "Sport", "Stand", "Start", "State", "Stone", "Story", "Study",
    "Sweet", "Table", "Teach", "Thank", "Theme", "Thick", "Think", "Throw", "Title", "Touch",
    "Tower", "Train", "Trust", "Union", "Value", "Visit", "Voice", "Waste", "Watch", "Whole"
]
new_list = []
for i in common_list:
    new_list.append(i.lower())



def string(x):
    y = ''
    for i in x:
        y += i
    return y


