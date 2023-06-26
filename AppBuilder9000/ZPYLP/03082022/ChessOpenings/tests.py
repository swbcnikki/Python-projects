from django.test import TestCase
import string
import json
# Create your tests here.
from django.test import TestCase

# Create your tests here.
lst = [{'id': 'boLujJkB', 'rated': False, 'variant': 'standard', 'speed': 'correspondence', 'perf': 'correspondence', 'status': 'resign', 'players': {'white': {'name': 'Caruana, F. (2818)'}, 'black': {'name': 'Carlsen, M. (2882)'}}, 'winner': 'white', 'opening': {'eco': 'B30',
 'name': 'Sicilian Defense: Nyezhmetdinov-Rossolimo Attack', 'ply': 5}, 'moves': """e4 c5 Nf3 Nc6 Bb5 e6 Bxc6 bxc6 d3 Ne7 b3 Ng6 h4 h5 e5 f6 Nbd2 d6 exd6 e5 Bb2 Bg4 Q
e2 Qxd6 g3 Be7 O-O-O Nf8 Rde1 Ne6 Qe4 Qd5 Nxe5 Qxe4 dxe4 fxe5 f3 Nd4 fxg4 hxg4 Nc4 O-O Kb1 Rf2 Nxe5 Nxc2 Nxg4 Rg2 Reg1 Re2 h5 c4 h6 c3 h7+ Kf7 Rf1+ Bf6 Bc1 Nb4 e5 R
xa2 Ne3 Rh8 exf6 g5 Rd1 a5 Rd4 c2+ Nxc2 Rxc2 Rxb4 Rxc1+ Kxc1 axb4 Rh6"""}]

print(lst[0]['players']['black']['name'])






