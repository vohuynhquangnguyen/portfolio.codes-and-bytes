\ Model ProductionPlanning
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  10 units_produced-rt[1] + 10 units_produced-rt[2]
   + 10 units_produced-rt[3] + 10 units_produced-rt[4]
   + 10 units_produced-rt[5] + 10 units_produced-rt[6]
   + 15 units_produced_ot[1] + 15 units_produced_ot[2]
   + 15 units_produced_ot[3] + 15 units_produced_ot[4]
   + 15 units_produced_ot[5] + 15 units_produced_ot[6] + 2 units_carried[1]
   + 2 units_carried[2] + 2 units_carried[3] + 2 units_carried[4]
   + 2 units_carried[5] + 2 units_carried[6] + 5 back_order_units[1]
   + 5 back_order_units[2] + 5 back_order_units[3] + 5 back_order_units[4]
   + 5 back_order_units[5] + 5 back_order_units[6]
Subject To
 R0: units_carried[1] = 0
 R1: back_order_units[1] = 0
 R2: units_carried[6] = 0
 R3: back_order_units[6] = 0
 R4: units_produced-rt[1] + units_produced_ot[1] - units_carried[1]
   + back_order_units[1] = 1055
 R5: units_produced-rt[2] + units_produced_ot[2] + units_carried[1]
   - units_carried[2] - back_order_units[1] + back_order_units[2] = 700
 R6: units_produced-rt[3] + units_produced_ot[3] + units_carried[2]
   - units_carried[3] - back_order_units[2] + back_order_units[3] = 1645
 R7: units_produced-rt[4] + units_produced_ot[4] + units_carried[3]
   - units_carried[4] - back_order_units[3] + back_order_units[4] = 1600
 R8: units_produced-rt[5] + units_produced_ot[5] + units_carried[4]
   - units_carried[5] - back_order_units[4] + back_order_units[5] = 1095
 R9: units_produced-rt[6] + units_produced_ot[6] + units_carried[5]
   - units_carried[6] - back_order_units[5] + back_order_units[6] = 845
 R10: units_produced-rt[1] <= 1000
 R11: units_produced_ot[1] <= 300
 R12: units_produced-rt[2] <= 1000
 R13: units_produced_ot[2] <= 300
 R14: units_produced-rt[3] <= 1000
 R15: units_produced_ot[3] <= 300
 R16: units_produced-rt[4] <= 1000
 R17: units_produced_ot[4] <= 300
 R18: units_produced-rt[5] <= 1000
 R19: units_produced_ot[5] <= 300
 R20: units_produced-rt[6] <= 1000
 R21: units_produced_ot[6] <= 300
Bounds
Generals
 units_produced-rt[1] units_produced-rt[2] units_produced-rt[3]
 units_produced-rt[4] units_produced-rt[5] units_produced-rt[6]
 units_produced_ot[1] units_produced_ot[2] units_produced_ot[3]
 units_produced_ot[4] units_produced_ot[5] units_produced_ot[6]
 units_carried[1] units_carried[2] units_carried[3] units_carried[4]
 units_carried[5] units_carried[6] back_order_units[1] back_order_units[2]
 back_order_units[3] back_order_units[4] back_order_units[5]
 back_order_units[6]
End
