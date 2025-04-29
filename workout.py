
# Imports
from fpdf import FPDF
import os

from fpdf import FPDF

# PDF Class using only system fonts
class PDF(FPDF):
    def __init__(self):
        super().__init__()
        self.set_auto_page_break(auto=True, margin=15)
        self.set_font("Helvetica", "", 11)
        self.line_height = 7

    def title_tile(self, text, color=(30, 144, 255), align="L"):
        self.set_fill_color(*color)
        self.set_text_color(255, 255, 255)
        self.set_font("Helvetica", "B", 14)
        self.cell(0, 8, txt=self.clean(text), ln=True, fill=True, align=align)
        self.ln(3)
        self.set_text_color(0)

    def add_section(self, title, content):
        self.set_font("Helvetica", "B", 12)
        self.set_text_color(0, 0, 128)
        self.cell(0, 6, txt=self.clean(title), ln=True)
        self.set_font("Helvetica", "", 11)
        self.set_text_color(0)
        self.multi_cell(0, 6, txt=self.clean(content))
        self.ln(2)

    def clean(self, text):
        return text.replace("–", "-").replace("—", "-").replace("“", '"').replace("”", '"')


# Create PDF
pdf = PDF()
pdf.add_page()

# Title
pdf.ln(2)
pdf.title_tile("Alhamdulillah Workout Goal", align="C", color=(255, 193, 7))
pdf.ln(4)

# Cardio
pdf.title_tile("Cardio (Daily)", color=(72, 201, 176))
pdf.multi_cell(0, 8, "Walk from Asr to Maghrib for 30 minutes.")
pdf.ln(3)

# Bed Routine
pdf.title_tile("Daily Bed Routine (18 Minutes - Reps Based)", color=(243, 156, 18))
pdf.add_section("Warm-Up (4 Minutes)", "- Supine March: 2 sets x 20 reps (10 per leg)\n- Pelvic Tilt: 2 sets x 15 reps")
pdf.add_section("Main Circuit (12 Minutes)", """- Side-Lying Leg Lifts: 2 sets x 15 reps per side
- Leg Raises: 2 sets x 15 reps
- Core Squeeze Hold: 2 sets x 20 seconds hold (tighten core like bracing)
- Mountain Climbers: 2 sets x 20 reps (10 per leg)
- Leg Raises (Repeat): 1 set x 15 reps""")
pdf.add_section("Cool-Down (2 Minutes)", "- Knee-to-Chest Stretch: Hold each leg for 1 minute")
pdf.ln(3)

# Weekly Routines
days = {
    "Monday - Chest Focus": (231, 76, 60),
    "Tuesday - Back Focus": (46, 204, 113),
    "Wednesday - Chest Focus": (155, 89, 182),
    "Thursday - Back Focus": (52, 152, 219),
    "Friday - Explosive Mixed": (255, 191, 0),
    "Saturday - Box Day (Back Sore)": (230, 126, 34),
    "Sunday - Kick Day (Chest Sore)": (52, 73, 94),
}

routines = {
    "Monday - Chest Focus": """- Push-ups (Standard): 4 sets x 15 reps - 8 minutes  
- Pull-ups (Neutral grip): 3 sets x max reps - 10 minutes  
- Dumbbell Chest Press (Floor): 4 sets x 10 reps - 10 minutes  
- Burpees (Explosive): 3 sets x 12 reps - 6 minutes  
- Mountain Climbers (Fast): 2 sets x 45 sec - 4 minutes  
Total Heavy Routine Time: ~38 minutes""",

    "Tuesday - Back Focus": """- Short-Step Forward Lunges (Bodyweight): 3 sets x 12 reps/leg - 10 minutes  
- Leg Raises: 3 sets x 20 reps - 8 minutes  
- Mountain Climbers: 3 sets x 45 sec - 6 minutes  
- Burpees (Controlled): 2 sets x 10 reps - 6 minutes  
- Shoulder Taps: 1 set - 5 minutes  
Total Heavy Routine Time: 35 minutes""",

    "Wednesday - Chest Focus": """- Push-ups (Incline/Decline): 4 sets x 12 reps - 8 minutes  
- Pull-ups (Wide grip): 3 sets x max reps - 10 minutes  
- Dumbbell Floor Press: 3 sets x 12 reps - 8 minutes  
- Mudgar: 3 sets x 60 sec - 10 minutes  
Total Heavy Routine Time: ~36 minutes""",

    "Thursday - Back Focus": """- Short-Step Forward Lunges (Bodyweight): 3 sets x 15 reps/leg - 10 minutes  
- Leg Raises: 3 sets x 25 reps - 8 minutes  
- Mountain Climbers: 3 sets x 1 min - 6 minutes  
- Burpees (Controlled): 2 sets x 12 reps - 4 minutes  
- Shoulder Taps: 1 set - 7 minutes  
Total Heavy Routine Time: 35 minutes""",

    "Friday - Explosive Mixed": """- Push-ups: 3 sets x 20 reps - 6 minutes  
- Pull-ups: 3 sets x max reps - 10 minutes  
- Leg Raises: 3 sets x 15 reps/leg - 8 minutes  
- Mountain Climbers: 3 sets x 60 sec - 6 minutes  
- Burpees (Controlled): 3 sets x 12 reps - 5 minutes  
Total Heavy Routine Time: 35 minutes""",

    "Saturday - Box Day (Back Sore)": """- Kettlebell: 3 sets x 20 reps - 5 minutes
- Mudgar: 4 sets x 25 reps - 10 minutes
- Boxing: 20 minutes  
Total Heavy Routine Time: 35 minutes""",

    "Sunday - Kick Day (Chest Sore)": """- Kettlebell: 3 sets x 20 reps - 5 minutes
- Mudgar: 4 sets x 25 reps - 10 minutes
- Kicking: 20 minutes  
Total Heavy Routine Time: 35 minutes"""
}

# Add weekly routine sections
for day, color in days.items():
    pdf.title_tile(day, color=color)
    pdf.multi_cell(0, 8, routines[day])
    pdf.ln(2)
    if day=="Tuesday - Back Focus":
        pdf.add_page()

# Save
output_path = "workout.pdf"
pdf.output(output_path)

# Confirm
print(f"✅ PDF generated: {output_path}")
