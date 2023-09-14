\ Model Production_Planning_with_Backorders
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  10 units_produced_regular[1] + 10 units_produced_regular[2]
   + 10 units_produced_regular[3] + 10 units_produced_regular[4]
   + 10 units_produced_regular[5] + 10 units_produced_regular[6]
   + 15 units_produced_overtime[1] + 15 units_produced_overtime[2]
   + 15 units_produced_overtime[3] + 15 units_produced_overtime[4]
   + 15 units_produced_overtime[5] + 15 units_produced_overtime[6]
   + 2 units_carriedover_invetories[1] + 2 units_carriedover_invetories[2]
   + 2 units_carriedover_invetories[3] + 2 units_carriedover_invetories[4]
   + 2 units_carriedover_invetories[5] + 2 units_carriedover_invetories[6]
   + 5 units_backordered[1] + 5 units_backordered[2]
   + 5 units_backordered[3] + 5 units_backordered[4]
   + 5 units_backordered[5] + 5 units_backordered[6]
Subject To
 R0: units_carriedover_invetories[1] = 0
 R1: units_backordered[1] = 0
 R2: units_carriedover_invetories[6] = 0
 R3: units_backordered[6] = 0
 R4: units_produced_regular[1] + units_produced_overtime[1]
   - units_carriedover_invetories[1] + units_backordered[1] = 1055
 R5: units_produced_regular[2] + units_produced_overtime[2]
   + units_carriedover_invetories[1] - units_carriedover_invetories[2]
   - units_backordered[1] + units_backordered[2] = 700
 R6: units_produced_regular[3] + units_produced_overtime[3]
   + units_carriedover_invetories[2] - units_carriedover_invetories[3]
   - units_backordered[2] + units_backordered[3] = 1645
 R7: units_produced_regular[4] + units_produced_overtime[4]
   + units_carriedover_invetories[3] - units_carriedover_invetories[4]
   - units_backordered[3] + units_backordered[4] = 1600
 R8: units_produced_regular[5] + units_produced_overtime[5]
   + units_carriedover_invetories[4] - units_carriedover_invetories[5]
   - units_backordered[4] + units_backordered[5] = 1095
 R9: units_produced_regular[6] + units_produced_overtime[6]
   + units_carriedover_invetories[5] - units_carriedover_invetories[6]
   - units_backordered[5] + units_backordered[6] = 845
 R10: units_produced_regular[1] <= 10
 R11: units_produced_overtime[1] <= 15
 R12: units_produced_regular[2] <= 10
 R13: units_produced_overtime[2] <= 15
 R14: units_produced_regular[3] <= 10
 R15: units_produced_overtime[3] <= 15
 R16: units_produced_regular[4] <= 10
 R17: units_produced_overtime[4] <= 15
 R18: units_produced_regular[5] <= 10
 R19: units_produced_overtime[5] <= 15
 R20: units_produced_regular[6] <= 10
 R21: units_produced_overtime[6] <= 15
Bounds
Generals
 units_produced_regular[1] units_produced_regular[2]
 units_produced_regular[3] units_produced_regular[4]
 units_produced_regular[5] units_produced_regular[6]
 units_produced_overtime[1] units_produced_overtime[2]
 units_produced_overtime[3] units_produced_overtime[4]
 units_produced_overtime[5] units_produced_overtime[6]
 units_carriedover_invetories[1] units_carriedover_invetories[2]
 units_carriedover_invetories[3] units_carriedover_invetories[4]
 units_carriedover_invetories[5] units_carriedover_invetories[6]
 units_backordered[1] units_backordered[2] units_backordered[3]
 units_backordered[4] units_backordered[5] units_backordered[6]
End
