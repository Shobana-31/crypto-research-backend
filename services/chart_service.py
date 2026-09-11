# services/chart_service.py

import random
import time


def generate_mock_chart(days: int = 7):
    """Generate 7-day mock price data"""
    prices = []
    value = 65000
    points = 30 
    change_range = 200
    
    for i in range(points):
        change = random.uniform(-change_range, change_range)
        value += change
        
        if value < 60000:
            value = 60000
        if value > 70000:
            value = 70000
        
        timestamp = int(time.time()) - (points - i) * 3600
        prices.append([timestamp, value])
    
    return prices