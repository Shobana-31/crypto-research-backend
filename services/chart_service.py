# Chart Data

import random
import time


def generate_mock_chart(days: int = 7):
    """Generate mock price data for specific number of days"""
    prices = []
    
    if days == 1:
        value = 65234.50
        points = 24
        change_range = 100
    elif days == 7:
        value = 65000
        points = 168
        change_range = 200
    elif days == 30:
        value = 64000
        points = 720
        change_range = 300
    elif days == 90:
        value = 62000
        points = 2160
        change_range = 400
    elif days == 365:
        value = 58000
        points = 8760
        change_range = 500
    else:
        value = 65000
        points = 168
        change_range = 200
    
    for i in range(points):
        change = random.uniform(-change_range, change_range)
        value += change
        
        if days == 1:
            if value < 64000: value = 64000
            if value > 66000: value = 66000
        elif days == 7:
            if value < 60000: value = 60000
            if value > 70000: value = 70000
        elif days == 30:
            if value < 55000: value = 55000
            if value > 75000: value = 75000
        elif days == 90:
            if value < 50000: value = 50000
            if value > 80000: value = 80000
        elif days == 365:
            if value < 40000: value = 40000
            if value > 90000: value = 90000
        
        timestamp = int(time.time()) - (points - i) * 3600
        prices.append([timestamp, value])
    
    return prices