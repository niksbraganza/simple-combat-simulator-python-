# simple-combat-simulator--python-
Your task is to implement a simple battle simulator that pits one army against another.
At the start of the game, each commander is given a starting total of $10. Units are purchased and stored in their army. The commanders may spend as much or as little of their money as they desire. After the armies are assembled, the units are then made to ﬁght each other in the order they were purchased in. Each unit in the standard game costs $1.
There are three types of units available:
• Archer • Soldier • Knight
Each unit has a weakness and a strength. Archers are good against Soldiers but are terrible against Knights. Soldiers are good against Knights but can’t win against Archers. Knights beat Archers, but fall short against Soldiers. If a unit comes up against a unit of the same type, both lose. Table 1 indicates who wins in any encounter.

After each ﬁght, the winner is left on the battleﬁeld to ﬁght the next combatant. If both units lose, then two new units are taken from the army and begin their ﬁght.
