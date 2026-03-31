import copy
import uuid


class Memento:
    def __init__(self, state):
        self.state = copy.deepcopy(state)


class TrackedObject:
    def __init__(self, name):
        self.name = name
        self.data = {}

    def update(self, key, value):
        self.data[key] = value

    def __str__(self):
        return f"{self.name} State: {self.data}"


class Timeline:
    def __init__(self):
        self.id = str(uuid.uuid4())[:8]
        self.history = []
        self.current_index = -1

    def save(self, memento):
        self.history = self.history[:self.current_index + 1]
        self.history.append(memento)
        self.current_index += 1

    def undo(self):
        if self.current_index > 0:
            self.current_index -= 1
            return self.history[self.current_index]
        return None

    def redo(self):
        if self.current_index < len(self.history) - 1:
            self.current_index += 1
            return self.history[self.current_index]
        return None

    def current_state(self):
        if self.current_index >= 0:
            return self.history[self.current_index]
        return None


class TimelineManager:
    def __init__(self, obj):
        self.obj = obj
        self.timelines = {}
        self.current_timeline = self._create_new_timeline()

    def _create_new_timeline(self):
        timeline = Timeline()
        self.timelines[timeline.id] = timeline
        return timeline

    def save_state(self):
        memento = Memento(self.obj.data)
        self.current_timeline.save(memento)

    def undo(self):
        memento = self.current_timeline.undo()
        if memento:
            self.obj.data = copy.deepcopy(memento.state)

    def redo(self):
        memento = self.current_timeline.redo()
        if memento:
            self.obj.data = copy.deepcopy(memento.state)

    def branch(self):
        new_timeline = self._create_new_timeline()
        new_timeline.history = copy.deepcopy(self.current_timeline.history)
        new_timeline.current_index = self.current_timeline.current_index
        self.current_timeline = new_timeline
        print(f"Switched to new timeline: {new_timeline.id}")

    def switch_timeline(self, timeline_id):
        if timeline_id in self.timelines:
            self.current_timeline = self.timelines[timeline_id]
            memento = self.current_timeline.current_state()
            if memento:
                self.obj.data = copy.deepcopy(memento.state)
            print(f"Switched to timeline: {timeline_id}")
        else:
            print("Timeline not found")

    def show_timelines(self):
        print("\nAvailable Timelines:")
        for tid in self.timelines:
            current = "(Current)" if self.current_timeline.id == tid else ""
            print(f"{tid} {current}")


if __name__ == "__main__":
    obj = TrackedObject("MyObject")
    manager = TimelineManager(obj)

    obj.update("x", 10)
    manager.save_state()

    obj.update("y", 20)
    manager.save_state()

    print(obj)

    manager.undo()
    print("After Undo:", obj)

    manager.redo()
    print("After Redo:", obj)

    manager.branch()
    branch_id = manager.current_timeline.id

    obj.update("z", 999)
    manager.save_state()

    print("After Branch Change:", obj)

    original_id = list(manager.timelines.keys())[0]
    manager.switch_timeline(original_id)

    print("Back to Original:", obj)

    manager.show_timelines()