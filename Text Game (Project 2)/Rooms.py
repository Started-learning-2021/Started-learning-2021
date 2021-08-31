#Game map (i.e. rooms)

from Objects import Boss, Nowhere, Ivanhoe, Thornbury, Brunswick, Heidelberg, Coburg, Macleod, Resivoir, Fawkner

rooms = {
    'Nowhere': {
        'name': 'the middle of nowhere',
        'function': Nowhere,  
        'north': 'Reservoir',
        'north east': 'Macleod', 
        'east': 'Heidelberg',
        'south east': 'Ivanhoe', 
        'south': 'Thornbury',
        'south west': 'Brunswick', 
        'west': 'Coburg', 
        'north west': 'Fawkner',     
        'contents': 'There are stone walls and floors around you, and an open door behind you. \n'\
        'You may travel in any compass direction considering you are in the middle of nowhere.', 
        'item': 'None'},
    'Fawkner': {
        'name': 'Fawkner', 
        'function': Fawkner,         
        'east': 'Resivoir',
        'south east': 'Nowhere', 
        'south': 'Coburg',
        'contents': 'There are children playing near Merri Creek and hobos taking meth. Everyone is having a good time \n'\
        'You may travel East, South East or South.',
        'item': 'None'},
    'Resivoir': {
        'name': 'Resivoir',
        'function': Resivoir,  
        'east': 'Macleod', 
        'south east': 'Heidelberg', 
        'south': 'Nowhere',
        'south west': 'Coburg', 
        'west': 'Fawkner', 
        'contents': 'There is a Magical Stick in the area. However, you will need to fight for it. \n'\
        'You may travel East, South East, South, South West or West.',
        'item': 'None'},
    'Macleod': {
        'name': 'Macleod', 
        'function': Macleod, 
        'south': 'Heidelberg',
        'south west': 'nowhere',
        'west': 'Resivoir',
        'contents': 'You started in the middle of nowhere, but maybe this is the middle of nowhere. You should move on. \n'\
        'You may travel South, South West or West.', 
        'item': 'None'}, 
    'Coburg': {
        'name': 'Coburg', 
        'function': Coburg, 
        'north': 'Fawkner', 
        'north east': 'Resivoir',
        'east': 'Nowhere',
        'south east': 'Thornbury',
        'south': 'Brunswick',
        'contents': 'There are some hipsters and a magical wizard around. The wizard is holding a magical stick, but it is fake. \n'\
        'What a stupid stupid motherfucker. You should move on. \n'\
        'You may travel North, North East, East, South East or South.', 
        'item': 'None'},
    'Heidelberg': {
        'name': 'Heidelberg',
        'function': Heidelberg,  
        'north': 'torture',
        'north west': 'Resivoir', 
        'south': 'Ivanhoe',
        'south west': 'Thornbury',
        'west': 'Nowhere',
        'contents': 'There are some shady looking characters around here. The hoodlums are weilding knives. \n'\
        'You may travel North, North West, South, South West or West.', 
        'item': 'None'},
    'Brunswick': {
        'name': 'Brunswick',
        'function': Brunswick,  
        'north': 'Coburg',
        'north east': 'Nowhere',
        'east': 'Thornbury',
        'contents': 'There are many hipsters around. Some of these fuckers are holding joints which look appealing. \n'\
        'Others are carrying Magical Sticks which will help you complete your quest. \n'\
        'You may travel North, North East or East.', 
        'item': 'None'},
    'Thornbury': {
        'name': 'Thornbury',
        'function': Thornbury,  
        'north': 'Nowhere',
        'north east': 'Heidelberg', 
        'east': 'Ivanhoe', 
        'west': 'Brunswick', 
        'north west': 'Coburg', 
        'contents': 'There are some nice playgrounds around the place, but you look like a preditor and should move on. \n'\
        'You may travel North, North East, East, West or North West.', 
        'item': 'None'},
    'Ivanhoe': {
        'name': 'Ivanhoe',
        'function': Ivanhoe,  
        'north': 'Heidelberg',
        'west': 'Thornbury', 
        'north west': 'Coburg',
        'contents': 'There are magical sticks throughout the land. \n'\
        'You may travel North, West or Northwest.', 
        'item': 'None'},
    'Boss': {
        'name': "the Boss' Base",
        'function': Boss, 
        'teleport': "Boss' Base",
        'contents': 'It stinks in here.', 
        'item': 'None'},
    }