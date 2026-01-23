import enum
import time
import threading
import multiprocessing as mp

# ======================================================
# SYSTEM MODES
# ======================================================

class SystemMode(enum.Enum):

    DEFAULT = {
        "mode": "default",
        "camera": {
            "process": {"enabled": False},
            "thread": {}
        }
    }

    AUTO = {
        "mode": "auto",
        "camera": {
            "process": {"enabled": True},
            "thread": {"resolution": "480p"}
        }
    }

    NEW_MODE = {
        "mode": "new_mode",
        "camera": {
            "process": {"enabled": True},
            "thread": {"resolution": "720p"}
        }
    }

# ======================================================
# TRANSITION TABLE
# ======================================================

class TransitionTable:

    _TRANSITIONS = {
        SystemMode.DEFAULT: {
            "dashboard_auto_button": SystemMode.AUTO,
            "dashboard_new_button": SystemMode.NEW_MODE,
        },

        SystemMode.AUTO: {
            "dashboard_default_button": SystemMode.DEFAULT,
            "dashboard_new_button": SystemMode.NEW_MODE,
        },

        SystemMode.NEW_MODE: {
            "dashboard_default_button": SystemMode.DEFAULT,
            "dashboard_auto_button": SystemMode.AUTO,
        }
    }

    @classmethod
    def get_next_mode(cls, current_mode, transition_name):
        return cls._TRANSITIONS[current_mode].get(transition_name, None)

# ======================================================
# STATE MACHINE (SINGLETON)
# ======================================================

class StateMachine:

    _instance = None

    def __init__(self):
        self.current_mode = SystemMode.DEFAULT
        self.subscribers = []

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = StateMachine()
        return cls._instance

    def subscribe(self, callback):
        self.subscribers.append(callback)

    def request_mode(self, transition_name):
        next_mode = TransitionTable.get_next_mode(
            self.current_mode, transition_name
        )

        if next_mode:
            print(f"\n[StateMachine] {self.current_mode.name} → {next_mode.name}")
            self.current_mode = next_mode
            for cb in self.subscribers:
                cb(next_mode)
        else:
            print("[StateMachine] Invalid transition")

# ======================================================
# THREAD WITH STOP
# ======================================================

class ThreadWithStop(threading.Thread):
    def __init__(self):
        super().__init__(daemon=True)
        self._stop = threading.Event()

    def stop(self):
        self._stop.set()

    def stopped(self):
        return self._stop.is_set()

# ======================================================
# CAMERA THREAD
# ======================================================

class CameraThread(ThreadWithStop):

    def __init__(self):
        super().__init__()
        self.resolution = "unknown"

    def on_state_change(self, mode):
        cfg = mode.value["camera"]["thread"]
        if "resolution" in cfg:
            self.resolution = cfg["resolution"]
            print(f"[CameraThread] Resolution set to {self.resolution}")

    def run(self):
        while not self.stopped():
            print(f"[CameraThread] Running at {self.resolution}")
            time.sleep(1)

# ======================================================
# CAMERA PROCESS (SIMULATED)
# ======================================================

class CameraProcess:

    def __init__(self):
        self.thread = CameraThread()
        self.running = False

        sm = StateMachine.get_instance()
        sm.subscribe(self.on_state_change)
        sm.subscribe(self.thread.on_state_change)

    def on_state_change(self, mode):
        enabled = mode.value["camera"]["process"]["enabled"]

        if enabled and not self.running:
            print("[CameraProcess] Starting camera")
            self.thread.start()
            self.running = True

        elif not enabled and self.running:
            print("[CameraProcess] Stopping camera")
            self.thread.stop()
            self.running = False

# ======================================================
# DEMO (Dashboard Simulation)
# ======================================================

if __name__ == "__main__":

    sm = StateMachine.get_instance()
    camera = CameraProcess()

    time.sleep(2)
    sm.request_mode("dashboard_auto_button")

    time.sleep(3)
    sm.request_mode("dashboard_new_button")

    time.sleep(3)
    sm.request_mode("dashboard_default_button")