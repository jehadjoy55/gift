# Python script to generate random CSS styles for the gift box

import random

def generate_css():
    colors = ['#ff6f61', '#ff4e50', '#f7d84b', '#a29bfe', '#00cec9']
    background_gradient = f"linear-gradient(135deg, {random.choice(colors)}, {random.choice(colors)})"
    box_color = random.choice(colors)
    lid_color = random.choice(colors)
    ribbon_color = random.choice(colors)
    
    css = f"""
    body {{
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        margin: 0;
        background: {background_gradient};
        font-family: Arial, sans-serif;
    }}

    .gift-box {{
        position: relative;
        width: 200px;
        height: 200px;
        background: {box_color};
        box-shadow: 0 8px 15px rgba(0, 0, 0, 0.2);
        border-radius: 10px;
    }}

    .box-lid {{
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 50px;
        background: {lid_color};
        border-top-left-radius: 10px;
        border-top-right-radius: 10px;
        z-index: 2;
    }}

    .box-body {{
        position: absolute;
        bottom: 0;
        left: 0;
        width: 100%;
        height: 150px;
        background: {box_color};
        border-bottom-left-radius: 10px;
        border-bottom-right-radius: 10px;
    }}

    .ribbon-horizontal, .ribbon-vertical {{
        position: absolute;
        background: {ribbon_color};
    }}

    .ribbon-horizontal {{
        width: 100%;
        height: 20px;
        top: 90px;
        left: 0;
        z-index: 3;
    }}

    .ribbon-vertical {{
        width: 20px;
        height: 100%;
        top: 0;
        left: 90px;
        z-index: 3;
    }}
    """
    with open("style.css", "w") as file:
        file.write(css)

generate_css()
