#timer.py

class Timer:
    def __init__(self, initial_time=1):
        self.current_time = initial_time

    def update(self, elapsed_seconds):
        self.current_time -= elapsed_seconds
        if self.current_time <= 0:
            self.reset()

    def reset(self):
        # Set the initial time for the timer
        pass  # You can implement the logic here based on your requirements

    def get_current_time(self):
        return self.current_time
