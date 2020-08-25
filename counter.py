class Counter:
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value
        self.current_value = min_value

    def get_current_value(self):
        return self.current_value

    def do_step(self):
        if self.current_value < self.max_value:
            self.current_value += 1

    def do_reset(self):
        self.current_value = self.min_value


cnt = Counter(10, 15)
print(cnt.get_current_value())
cnt.do_step()
print(cnt.get_current_value())
cnt.do_step()
print(cnt.get_current_value())
cnt.do_step()
print(cnt.get_current_value())
cnt.do_step()
print(cnt.get_current_value())
cnt.do_step()
print(cnt.get_current_value())
cnt.do_step()
print(cnt.get_current_value())

cnt.do_reset()
print(cnt.get_current_value())
cnt.do_step()
print(cnt.get_current_value())
cnt.do_step()
print(cnt.get_current_value())
