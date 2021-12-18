#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
sys.path.append(os.getcwd())
import bot_base
from strategies import dumbest_strategy as strategy

if __name__ == "__main__":
    bot_base.main(strategy)
