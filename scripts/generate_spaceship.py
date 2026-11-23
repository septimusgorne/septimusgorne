#!/usr/bin/env python3
"""Генерация анимации космического корабля SVG для GitHub профиля."""
import random
import datetime

# Seed based on date for consistent daily animation
today = datetime.date.today()
random.seed(today.toordinal())

WIDTH = 1000
HEIGHT = 200

# Generate stars
stars = []
for i in range(60):
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT - 40)
    size = random.choice([1, 1, 1, 2, 2, 3])
    opacity = round(random.uniform(0.4, 1.0), 2)
    color = random.choice(["white", "#00f2fe", "#ff9ff3", "#feca57"])
    stars.append(f'<circle cx="{x}" cy="{y}" r="{size}" fill="{color}" opacity="{opacity}"/>')

# Spaceship position (moves across screen over time)
day_of_year = today.toordinal() % 365
ship_x = int((day_of_year / 365) * (WIDTH + 150)) - 75  # Moves from left to right
ship_y = 100 + int(20 * __import__('math').sin(day_of_year / 10))

# Engine flame flicker
flame_flicker = random.randint(-5, 5)

svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="shipGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" style="stop-color:#ff6b6b;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#feca57;stop-opacity:1" />
    </linearGradient>
    <filter id="glow">
      <feGaussianBlur stdDeviation="2" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>
  
  <!-- Deep space background -->
  <rect width="{WIDTH}" height="{HEIGHT}" fill="#050510"/>
  
  <!-- Distant nebula -->
  <circle cx="200" cy="50" r="80" fill="#4facfe" opacity="0.08"/>
  <circle cx="800" cy="150" r="100" fill="#ff9ff3" opacity="0.06"/>
  <circle cx="500" cy="30" r="60" fill="#00f2fe" opacity="0.05"/>
  
  <!-- Stars -->
  {''.join(stars)}
  
  <!-- Spaceship -->
  <g transform="translate({ship_x}, {ship_y})" filter="url(#glow)">
    <!-- Engine flame -->
    <path d="M-30,45 Q-10,{55+flame_flicker} 10,45 Q-10,35 -30,45" fill="#feca57" opacity="0.7"/>
    <path d="M-25,45 Q-5,{50+flame_flicker} 5,45 Q-5,40 -25,45" fill="#ff6b6b" opacity="0.5"/>
    
    <!-- Ship hull -->
    <path d="M0,0 L45,0 L45,55 L0,55 Z" fill="url(#shipGrad)"/>
    <path d="M12,12 L33,12 L33,22 L12,22 Z" fill="#2d3436"/>
    <path d="M17,16 L28,16 L28,20 L17,20 Z" fill="#ff7675"/>
    
    <!-- Wings -->
    <path d="M-25,30 L0,30 L0,40 L-25,40 Z" fill="#55efc4" opacity="0.9"/>
    <path d="M45,30 L70,30 L70,40 L45,40 Z" fill="#55efc4" opacity="0.9"/>
    
    <!-- Cockpit -->
    <circle cx="22" cy="28" r="9" fill="#00f2fe" opacity="0.95"/>
    <circle cx="22" cy="28" r="3.5" fill="white" opacity="0.9"/>
    
    <!-- Engine thrusters -->
    <rect x="-15" y="35" width="6" height="12" fill="#ff9ff3" opacity="0.8"/>
    <rect x="34" y="35" width="6" height="12" fill="#ff9ff3" opacity="0.8"/>
  </g>
  
  <!-- Text -->
  <text x="{WIDTH//2}" y="{HEIGHT-25}" font-family="'Courier New', monospace" font-size="20" font-weight="bold" fill="#00f2fe" text-anchor="middle" letter-spacing="1">
    🚀 Infrastructure & Automation & Robotics
  </text>
  <text x="{WIDTH//2}" y="{HEIGHT-5}" font-family="'Courier New', monospace" font-size="12" fill="#a29bfe" text-anchor="middle">
    Generated on {today.strftime("%d.%m.%Y")} • @septimusgorne
  </text>
</svg>
'''

with open("assets/spaceship-animation.svg", "w") as f:
    f.write(svg)

print(f"Generated spaceship SVG for {today}")
print(f"Ship position: x={ship_x}, y={ship_y}")
