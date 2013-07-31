#Usage: python fropi.py <frequency> <morse_letter>

import os;
import sys;
import cmd;
import time;

frequency = float(sys.argv[1]);
ditlength = (1/frequency)/2;

letter = ord(sys.argv[2][0].upper()) - 65;

def on():
	return;
	
def off():
	return;
	
dit = "1"
dah = "111"
p = "0"
ch_p = "000"

#appended character pause for ease
morse_letter = [
					dit+ p+ dah+ ch_p,#A
					dah+ p+ dit+ p+ dit+ p+ dit+ ch_p,#B
					dah+ p+ dit+ p+ dah+ p+ dit+ ch_p,#C
					dah+ p+ dit+ p+ dit+ ch_p,#D
					dit+ ch_p,#E
					dit+ p+ dit+ p+ dah+ p+ dit+ ch_p,#F
					dah+ p+ dah+ p+ dit+ ch_p,#G
					dit+ p+ dit+ p+ dit+ p+ dit+ ch_p,#H
					dit+ p+ dit+ ch_p,#I
					dit+ p+ dah+ p+ dah+ p+ dah+ ch_p,#J
					dah+ p+ dit+ p+ dah+ ch_p,#K
					dit+ p+ dah+ p+ dit+ p+ dit+ ch_p,#L
					dah+ p+ dah+ ch_p,#M
					dah+ p+ dit+ ch_p,#N
					dah+ p+ dah+ p+ dah+ ch_p,#O
					dit+ p+ dah+ p+ dah+ p+ dit+ ch_p,#P
					dah+ p+ dah+ p+ dit+ p+ dah+ ch_p,#Q
					dit+ p+ dah+ p+ dit+ ch_p,#R
					dit+ p+ dit+ p+ dit+ ch_p,#S
					dah+ ch_p,#T
					dit+ p+ dit+ p+ dah+ ch_p,#U
					dit+ p+ dit+ p+ dit+ p+ dah+ ch_p,#V
					dit+ p+ dah+ p+ dah+ ch_p,#W
					dah+ p+ dit+ p+ dit+ p+ dah+ ch_p,#X
					dah+ p+ dit+ p+ dah+ p+ dah+ ch_p,#Y
					dah+ p+ dah+ p+ dit+ p+ dit+ ch_p#Z
]

def main():
	while 1:
		for unit in morse_letter[c]:
			if unit == 1:
				on();
				time.sleep(ditlength);
			else:
				off();
				time.sleep(ditlength);
	return;

main()
