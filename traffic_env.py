import traci


class TrafficEnv:
    def __init__(self, use_gui=False):
        binary = "sumo-gui" if use_gui else "sumo"

        self.sumoCmd = [
            binary,
            "-c",
            "configs/sim.sumocfg",
            "--quit-on-end",
        ]
        self.green_phases = [0, 2]
        self.phase_duration = 10
        self.max_steps = 100
        self.current_green_index = 0

    def reset(self):
        try:
            traci.close()
        except:
            pass

        traci.start(self.sumoCmd)
        self.current_step = 0
        self.current_green_index = 0

        traci.trafficlight.setPhase("B1", self.green_phases[self.current_green_index])

        return self._get_state()

    def step(self, action):
        target_green_index = action
        target_phase = self.green_phases[target_green_index]

        current_phase = traci.trafficlight.getPhase("B1")

        # if switching from one green to the other, first allow yellow transition
        if current_phase != target_phase:
            traci.trafficlight.setPhase("B1", target_phase)

        for _ in range(self.phase_duration):
            traci.simulationStep()

        self.current_green_index = target_green_index

        state = self._get_state()
        total_waiting = sum(state)

        reward = -total_waiting

        self.current_step += 1
        done = self.current_step >= self.max_steps

        return state, reward, done

    def _get_state(self):
        lanes = list(dict.fromkeys(traci.trafficlight.getControlledLanes("B1")))
        lane_counts = []

        for lane in lanes:
            lane_counts.append(traci.lane.getLastStepHaltingNumber(lane))

        return tuple(lane_counts)

    def close(self):
        traci.close()
