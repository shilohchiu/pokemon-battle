import pandas as pd

MOVES = {
    'hydro_pump':{'type':'water','power':'120','accuracy':'100','side_effect':'none'},
    'dark_pulse':{'type':'water','power':'120','accuracy':'','side_effect':'flinch'}
}

STRENGTHS_AND_WEAKNESSES = {
    'normal':{'strong_against':{},'weak_against':{},'resist':{},'vulnerable_to':{}},
    'water':{'strong_against':{},'weak_against':{},'resist':{},'vulnerable_to':{}},
    'grass':{'strong_against':{},'weak_against':{},'resist':{},'vulnerable_to':{}},
    'electric':{'strong_against':{},'weak_against':{},'resist':{},'vulnerable_to':{}},
    'ice':{'strong_against':{},'weak_against':{},'resist':{},'vulnerable_to':{}},
    'fighting':{'strong_against':{},'weak_against':{},'resist':{},'vulnerable_to':{}},
    'poison':{'strong_against':{},'weak_against':{},'resist':{},'vulnerable_to':{}},
    'ground':{'strong_against':{},'weak_against':{},'resist':{},'vulnerable_to':{}},
    'flying':{'strong_against':{},'weak_against':{},'resist':{},'vulnerable_to':{}},
    'psychic':{'strong_against':{},'weak_against':{},'resist':{},'vulnerable_to':{}},
    'bug':{'strong_against':{},'weak_against':{},'resist':{},'vulnerable_to':{}},
    'rock':{'strong_against':{},'weak_against':{},'resist':{},'vulnerable_to':{}},
    'ghost':{'strong_against':{},'weak_against':{},'resist':{},'vulnerable_to':{}},
    'dragon':{'strong_against':{},'weak_against':{},'resist':{},'vulnerable_to':{}},
    'dark':{'strong_against':{},'weak_against':{},'resist':{},'vulnerable_to':{}},
    'steel':{'strong_against':{},'weak_against':{},'resist':{},'vulnerable_to':{}},
    'fairy':{'strong_against':{},'weak_against':{},'resist':{},'vulnerable_to':{}}
}

# access type and figure out multipliers