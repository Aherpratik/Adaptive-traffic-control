import traci

sumoCmd = ["sumo-gui", "-c", "configs/sim.sumocfg"]
traci.start(sumoCmd)

step = 0

while step < 100:
    traci.simulationStep()

    lanes = list(set(traci.trafficlight.getControlledLanes("B1")))

    total_cars = 0

    for lane in lanes:
        num_cars = traci.lane.getLastStepVehicleNumber(lane)
        total_cars += num_cars

    reward = -total_cars

    print(f"Step {step}: Cars near B1 = {total_cars} | Reward: {reward}")

    step = step + 1

traci.close()
