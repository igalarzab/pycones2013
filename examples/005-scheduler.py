#!/usr/bin/env python3
#
# PyCON ES 2013
# ---------------------
#
# Jose Ignacio Galarza
# @igalarzab
#

from collections import deque
from helpers import list_dir, echo_text


class Task:

    ID = 0

    def __init__(self, runner):
        Task.ID += 1
        self.id = Task.ID
        self.runner = runner

    def __str__(self):
        return str(self.id)

    def run(self):
        result = next(self.runner)
        print('\033[32m[%d]\033[0m %s' % (self.id, result))


class Scheduler:

    def __init__(self):
        self.tasks = deque()

    def schedule(self, task):
        self.tasks.append(task)

    def run(self):
        while self.tasks:
            task = self.tasks.popleft()

            try:
                task.run()
            except StopIteration:
                print('Task %s has finished' % task)
            else:
                self.tasks.append(task)



if __name__ == '__main__':
    s = Scheduler()

    s.schedule(Task(list_dir('.')))
    s.schedule(Task(echo_text(5)))
    s.schedule(Task(echo_text(3)))

    s.run()
