import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz
from skfuzzy import control as ctrl

Traffic_Flow = ctrl.Antecedent(np.arange(0, 1, 0.1), 'Traffic_Flow')
Traffic_Flow['Low'] = fuzz.trimf(Traffic_Flow.universe, [0,0, 0.4])
Traffic_Flow['moderate'] = fuzz.trimf(Traffic_Flow.universe, [0.2, 0.5,0.8])
Traffic_Flow['high'] = fuzz.trimf(Traffic_Flow.universe, [0.6, 1, 1])

Congestion_Level = ctrl.Antecedent(np.arange(0, 1, 0.1), 'Congestion_Level')
Congestion_Level['Low'] = fuzz.trimf(Congestion_Level.universe, [0,0, 0.4])
Congestion_Level['moderate'] = fuzz.trimf(Congestion_Level.universe, [0.2, 0.5, 0.7])
Congestion_Level['high'] = fuzz.trimf(Congestion_Level.universe, [0.6, 1, 1])

Green_Time = ctrl.Consequent(np.arange(0, 1, 0.1), 'Green_Time')
Green_Time['short'] = fuzz.trimf(Green_Time.universe, [0, 0, 0.3])
Green_Time['medium'] = fuzz.trimf(Green_Time.universe, [0.2, 0.5, 0.7])
Green_Time['long'] = fuzz.trimf(Green_Time.universe, [0.7, 1, 1])


rule1 = ctrl.Rule(Traffic_Flow['Low']&Congestion_Level['Low'],Green_Time['medium'])
rule2 = ctrl.Rule(Traffic_Flow['high']&Congestion_Level['high'],Green_Time['long'])
rule3 = ctrl.Rule(Traffic_Flow['moderate']&Congestion_Level['moderate'],Green_Time['short'])

Green_Time_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
Green_Time_simulation = ctrl.ControlSystemSimulation(Green_Time_ctrl)

Green_Time_simulation.input['Traffic_Flow'] = 0.5
Green_Time_simulation.input['Congestion_Level'] = 0.4
Green_Time_simulation.compute()

Traffic_Flow.view(sim=Green_Time_simulation)
Congestion_Level.view(sim=Green_Time_simulation)
Green_Time.view(sim=Green_Time_simulation)
plt.show()
