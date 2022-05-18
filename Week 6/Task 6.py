# Set initial state of l-system
initial = "AB"

# Rules for the l-system
rules = {
	"A": "AB",
	"B": "A"
}

def l_system(initial, rules, generation):
	current = initial									##### COPY INITIAL STATE INTO NEW STRING

	for _ in range(0, generation):						##### FOR LOOPED AS MANY TIMES AS GENERATIONS
		result = ""										##### RESET RESULT STRING

		for state in current:							##### NAVIGATE THROUGH THE INITIAL COPIED STRING
			result += rules.get(state, state)			##### ACCES RULES TO COPY INTO RESULT STRING 

		current = result								##### SAVE RESULT INTO CURRENT VAR BEFORE RESETING RESULT STRING WHEN WE GO BACK TO FOR LOOP

	return current										##### RETURN FINAL STRING

for i in range(0, 10):
	print( "{}: {}".format(i, l_system(initial, rules, i)) ) ##### PRINT THE FIRST 10 GENERATIONS OF INITIAL STRING
