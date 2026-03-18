import traci
import time


class TrafficEnv:
    def __init__(self, use_gui=False):
        self.use_gui = use_gui
        binary = "sumo-gui" if use_gui else "sumo"
        self.gui_delay = 0.2
        self.sumoCmd = [
            binary,
            "-c",
            "configs/sim.sumocfg",
            "--quit-on-end",
        ]

        # SUMO green phases for B1
        self.green_phases = [0, 2]

        # yellow phases between green phases
        self.yellow_phase = {
            (0, 2): 1,
            (2, 0): 3,
        }

        self.green_duration = 10
        self.yellow_duration = 3
        self.max_steps = 100

        self.current_step = 0
        self.current_green = 0

    def reset(self):
        try:
            traci.close()
        except:
            pass

        traci.start(self.sumoCmd)

        self.current_step = 0
        self.current_green = 0

        # start with phase 0 green
        traci.trafficlight.setPhase("B1", self.green_phases[self.current_green])

        return self._get_state()

    def step(self, action):

        # action is logical: 0 or 1
        target_green = action
        current_phase = self.green_phases[self.current_green]
        target_phase = self.green_phases[target_green]

        # if switching, go through yellow first
        if self.current_green != target_green:
            yellow = self.yellow_phase[(current_phase, target_phase)]
            traci.trafficlight.setPhase("B1", yellow)

            for _ in range(self.yellow_duration):
                traci.simulationStep()
                if self.use_gui:
                    time.sleep(self.gui_delay)

            traci.trafficlight.setPhase("B1", target_phase)
            self.current_green = target_green

        # hold green
        for _ in range(self.green_duration):
            traci.simulationStep()
            if self.use_gui:
                time.sleep(self.gui_delay)

        state = self._get_state()

        total_waiting = sum(state)
        imbalance = max(state) - min(state)

        # better reward: reduce total queue and balance traffic
        reward = -total_waiting - imbalance

        self.current_step += 1
        done = self.current_step >= self.max_steps

        return state, reward, done

    def _get_state(self):
        lanes = list(dict.fromkeys(traci.trafficlight.getControlledLanes("B1")))
        lane_counts = []

        for lane in lanes:
            lane_counts.append(traci.lane.getLastStepHaltingNumber(lane))

        direction1 = lane_counts[0] + lane_counts[1]
        direction2 = lane_counts[2] + lane_counts[3]

        def bucket(x):
            if x < 3:
                return 0
            elif x < 7:
                return 1
            else:
                return 2

        time_bucket = min(self.current_step // 10, 2)

        return (bucket(direction1), bucket(direction2), time_bucket)

    def close(self):
        try:
            traci.close()
        except:
            pass
