import traci

sumoCmd = ["sumo-gui", "-c", "configs/sim.sumocfg"]
traci.start(sumoCmd)

logics = traci.trafficlight.getAllProgramLogics("B1")

for logic in logics:
    print("Program ID:", logic.programID)
    for i, phase in enumerate(logic.phases):
        print(f"Phase {i}: state={phase.state}, duration={phase.duration}")

traci.close()
