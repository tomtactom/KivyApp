# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 12:13:56 2022

@author: Luca, Tom
"""
import kivy
kivy.require('2.1.0')

from kivy.app import App
from kivy.uix.label import Label


class MyApp(App):

    def build(self):
        return Label(text='Hello world')


if __name__ == '__main__':
    MyApp().run()
