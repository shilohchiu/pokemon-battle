import pandas as pd

MOVES = {
    'hydro_pump':{'type':'water','power':'120','accuracy':'100','side_effect':'none'},
    'dark_pulse':{'type':'water','power':'120','accuracy':'','side_effect':'flinch'}
}

STRENGTHS_AND_WEAKNESSES = {
    'normal':{'strengths':{},'weaknesses':{'rock', 'steel'}, 'immunities':{'ghost'}},
    'fire':{'strengths':{'grass', 'ice', 'bug', 'steel'},'weaknesses':{'fire', 'water', 'rock', 'dragon'}, 'immunities':{}},
    'water':{'strengths':{'fire', 'ground', 'rock'},'weaknesses':{'water', 'grass', 'dragon'}, 'immunities':{}},
    'grass':{'strengths':{'water', 'ground', 'rock'},'weaknesses':{'fire', 'grass'}, 'immunities':{}},
    'electric':{'strengths':{},'weaknesses':{}, 'immunities':{}},
    'ice':{'strengths':{},'weaknesses':{}, 'immunities':{}},
    'fighting':{'strengths':{},'weaknesses':{}, 'immunities':{}},
    'poison':{'strengths':{},'weaknesses':{}, 'immunities':{}},
    'ground':{'strengths':{},'weaknesses':{}, 'immunities':{}},
    'flying':{'strengths':{},'weaknesses':{}, 'immunities':{}},
    'psychic':{'strengths':{},'weaknesses':{}, 'immunities':{}},
    'bug':{'strengths':{},'weaknesses':{}, 'immunities':{}},
    'rock':{'strengths':{},'weaknesses':{}, 'immunities':{}},
    'ghost':{'strengths':{},'weaknesses':{}, 'immunities':{}},
    'dragon':{'strengths':{},'weaknesses':{}, 'immunities':{}},
    'dark':{'strengths':{},'weaknesses':{}, 'immunities':{}},
    'steel':{'strengths':{},'weaknesses':{}, 'immunities':{}},
    'fairy':{'strengths':{},'weaknesses':{}, 'immunities':{}}
}

# access type and figure out multipliers