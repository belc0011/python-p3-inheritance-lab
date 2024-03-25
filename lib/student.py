#!/usr/bin/env python

from user import User

class Student(User):
    knowledge = []
    def learn(self, string):
        self.knowledge.append(string)

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)