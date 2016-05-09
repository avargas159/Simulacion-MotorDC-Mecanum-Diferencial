#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math as m;


class Mecanum:

    def __init__(self, lx, ly, r):
        self._lx = lx;
        self._ly = ly;
        self._r = r;
        self._vx = 0.0;
        self._vy = 0.0;
        self._w1 = 0.0;
        self._w2 = 0.0;
        self._w3 = 0.0;
        self._w4 = 0.0;
        self._w = 0.0;
        


    def set_wn(self, wn):
            self._w1 = wn[0];
            self._w2 = wn[1];
            self._w3 = wn[2];
            self._w4 = wn[3];

    
    def calculate_vx(self):
        self._vx = (self._w1 + self._w2 + self._w3 + self._w4) * (self._r / 4.0)
        return self._vx

    def calculate_vy(self):
        self._vy = (-self._w1 + self._w2 + self._w3 - self._w4) * (self._r / 4.0)
        return self._vy

    def calculate_w(self):
        self._w = (-self._w1 + self._w2 - self._w3 + self._w4) * (self._r / (4.0 * (self._lx + self._ly)))

    # El ángulo se da en grados se  hace la conversión
    def calculate_angle(self):
        ang = (m.atan2(self._vy, self._vx) * (180 / m.pi))
        if ang < 0:
            return ang + 360
        return ang

    def calculate_vr(self):
        return m.sqrt((m.pow(self._vx, 2) + m.pow(self._vy, 2)))

    def __str__(self):
        string = "[ Carro mecanum ] \n"
        string += "Lx: " + str(self._lx) + "\n"
        string += "Ly: " + str(self._ly) + "\n"
        string += "R: " + str(self._r) + "\n"
        string += "W: " + str(self._w) + "\n"
        string += "Vx: " + str(self._vx) + "\n"
        string += "Vy: " + str(self._vy) + "\n"
        string += "W1: " + str(self._w1) + "\n"
        string += "W2: " + str(self._w2) + "\n"
        string += "W3: " + str(self._w3) + "\n"
        string += "W4 " + str(self._w4) + "\n"
        return string

