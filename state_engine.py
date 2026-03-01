import copy

class StateEngine:
    def __init__(self, node_id):
        self.node_id = node_id
        self.state = {}              # key -> {"value": int, "vector": {...}}
        self.vector_clock = {}       # global vector clock

    def increment(self):
        # Update own vector clock
        self.vector_clock[self.node_id] = self.vector_clock.get(self.node_id, 0) + 1

        # Update local state entry
        self.state[self.node_id] = {
            "value": self.vector_clock[self.node_id],
            "vector": copy.deepcopy(self.vector_clock)
        }

    def get_state(self):
        return copy.deepcopy(self.state)

    def get_summary(self):
        # Summary = only vector clocks
        return {
            key: entry["vector"]
            for key, entry in self.state.items()
        }

    def merge(self, incoming_state):
        updated = False

        for key, incoming_entry in incoming_state.items():
            if key not in self.state:
                self.state[key] = incoming_entry
                updated = True
                continue

            local_vector = self.state[key]["vector"]
            remote_vector = incoming_entry["vector"]

            comparison = self.compare_vectors(local_vector, remote_vector)

            if comparison == "remote_dominates":
                self.state[key] = incoming_entry
                updated = True

        if updated:
            print(" State merged:", self.state)

    def compare_vectors(self, v1, v2):
        """
        Compare two vector clocks
        """
        v1_bigger = False
        v2_bigger = False

        keys = set(v1.keys()).union(set(v2.keys()))

        for k in keys:
            val1 = v1.get(k, 0)
            val2 = v2.get(k, 0)

            if val1 > val2:
                v1_bigger = True
            elif val2 > val1:
                v2_bigger = True

        if v1_bigger and not v2_bigger:
            return "local_dominates"
        elif v2_bigger and not v1_bigger:
            return "remote_dominates"
        else:
            return "concurrent"

#for the disaster rescue application
def update_resource(self, resource_name, amount):
    self.vector_clock[self.node_id] = self.vector_clock.get(self.node_id, 0) + 1

    self.state[resource_name] = {
        "value": amount,
        "vector": self.vector_clock.copy()
    }

#for rural edge cluster mode by sensor update method
def update_sensor(self, sensor_id, reading):
    self.vector_clock[self.node_id] = self.vector_clock.get(self.node_id, 0) + 1

    self.state[sensor_id] = {
        "value": reading,
        "vector": self.vector_clock.copy()
    }
