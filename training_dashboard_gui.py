import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont

class TrainingDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Training Dashboard")
        self.root.geometry("600x500")
        self.root.configure(bg='#f0f0f0')
        
        # Training data
        self.data = {
            'title': "Appium with Python",
            'start_date': "22/09/2025",
            'end_date': "13/10/2025",
            'trainer_name': "Suresh",
            'topics': ['Python', 'Selenium', 'Git', 'Appium', 'Android', 'IOS'],
            'students': ('st1', 'st2', 'st3'),
            'marks': {'st1': 9, 'st2': 10, 'st3': 8}
        }
        
        self.create_widgets()
    
    def create_widgets(self):
        # Main frame
        main_frame = tk.Frame(self.root, bg='#f0f0f0', padx=20, pady=20)
        main_frame.pack(fill='both', expand=True)
        
        # Title
        title_font = tkFont.Font(family="Arial", size=18, weight="bold")
        title_label = tk.Label(main_frame, text="Training Dashboard", 
                              font=title_font, bg='#f0f0f0', fg='#2c3e50')
        title_label.pack(pady=(0, 20))
        
        # Course Information Frame
        course_frame = tk.LabelFrame(main_frame, text="Course Information", 
                                   font=("Arial", 12, "bold"), 
                                   bg='#f0f0f0', fg='#34495e', padx=15, pady=10)
        course_frame.pack(fill='x', pady=(0, 15))
        
        # Course Title
        tk.Label(course_frame, text=f"Title: {self.data['title']}", 
                font=("Arial", 11, "bold"), bg='#f0f0f0', fg='#2980b9').pack(anchor='w', pady=2)
        
        # Dates and Trainer
        tk.Label(course_frame, text=f"Start Date: {self.data['start_date']}", 
                font=("Arial", 10), bg='#f0f0f0').pack(anchor='w', pady=2)
        tk.Label(course_frame, text=f"End Date: {self.data['end_date']}", 
                font=("Arial", 10), bg='#f0f0f0').pack(anchor='w', pady=2)
        tk.Label(course_frame, text=f"Trainer: {self.data['trainer_name']}", 
                font=("Arial", 10), bg='#f0f0f0').pack(anchor='w', pady=2)
        
        # Topics Frame
        topics_frame = tk.LabelFrame(main_frame, text="Course Topics", 
                                   font=("Arial", 12, "bold"), 
                                   bg='#f0f0f0', fg='#34495e', padx=15, pady=10)
        topics_frame.pack(fill='x', pady=(0, 15))
        
        # Create a grid for topics
        topics_container = tk.Frame(topics_frame, bg='#f0f0f0')
        topics_container.pack(fill='x')
        
        for i, topic in enumerate(self.data['topics']):
            row = i // 3
            col = i % 3
            topic_label = tk.Label(topics_container, text=f"• {topic}", 
                                 font=("Arial", 10), bg='#f0f0f0', fg='#27ae60')
            topic_label.grid(row=row, column=col, sticky='w', padx=(0, 20), pady=2)
        
        # Students and Marks Frame
        students_frame = tk.LabelFrame(main_frame, text="Students & Performance", 
                                     font=("Arial", 12, "bold"), 
                                     bg='#f0f0f0', fg='#34495e', padx=15, pady=10)
        students_frame.pack(fill='x', pady=(0, 15))
        
        # Create table for students and marks
        table_frame = tk.Frame(students_frame, bg='#f0f0f0')
        table_frame.pack(fill='x')
        
        # Table headers
        tk.Label(table_frame, text="Student", font=("Arial", 10, "bold"), 
                bg='#34495e', fg='white', padx=10, pady=5).grid(row=0, column=0, sticky='ew')
        tk.Label(table_frame, text="Marks", font=("Arial", 10, "bold"), 
                bg='#34495e', fg='white', padx=10, pady=5).grid(row=0, column=1, sticky='ew')
        tk.Label(table_frame, text="Grade", font=("Arial", 10, "bold"), 
                bg='#34495e', fg='white', padx=10, pady=5).grid(row=0, column=2, sticky='ew')
        
        # Configure column weights
        table_frame.grid_columnconfigure(0, weight=1)
        table_frame.grid_columnconfigure(1, weight=1)
        table_frame.grid_columnconfigure(2, weight=1)
        
        # Table data
        for i, student in enumerate(self.data['students']):
            marks = self.data['marks'][student]
            grade = self.get_grade(marks)
            row = i + 1
            
            # Alternate row colors
            bg_color = '#ecf0f1' if i % 2 == 0 else '#ffffff'
            
            tk.Label(table_frame, text=student, font=("Arial", 10), 
                    bg=bg_color, padx=10, pady=5).grid(row=row, column=0, sticky='ew')
            tk.Label(table_frame, text=str(marks), font=("Arial", 10), 
                    bg=bg_color, padx=10, pady=5).grid(row=row, column=1, sticky='ew')
            tk.Label(table_frame, text=grade, font=("Arial", 10, "bold"), 
                    bg=bg_color, fg=self.get_grade_color(marks), 
                    padx=10, pady=5).grid(row=row, column=2, sticky='ew')
        
        # Summary Frame
        summary_frame = tk.LabelFrame(main_frame, text="Summary", 
                                    font=("Arial", 12, "bold"), 
                                    bg='#f0f0f0', fg='#34495e', padx=15, pady=10)
        summary_frame.pack(fill='x')
        
        # Calculate statistics
        marks_values = list(self.data['marks'].values())
        avg_marks = sum(marks_values) / len(marks_values)
        max_marks = max(marks_values)
        min_marks = min(marks_values)
        
        summary_info = tk.Frame(summary_frame, bg='#f0f0f0')
        summary_info.pack(fill='x')
        
        tk.Label(summary_info, text=f"Total Students: {len(self.data['students'])}", 
                font=("Arial", 10), bg='#f0f0f0').grid(row=0, column=0, sticky='w', padx=(0, 20))
        tk.Label(summary_info, text=f"Average Marks: {avg_marks:.1f}", 
                font=("Arial", 10), bg='#f0f0f0').grid(row=0, column=1, sticky='w', padx=(0, 20))
        tk.Label(summary_info, text=f"Highest: {max_marks}", 
                font=("Arial", 10), bg='#f0f0f0', fg='#27ae60').grid(row=1, column=0, sticky='w', padx=(0, 20))
        tk.Label(summary_info, text=f"Lowest: {min_marks}", 
                font=("Arial", 10), bg='#f0f0f0', fg='#e74c3c').grid(row=1, column=1, sticky='w', padx=(0, 20))
    
    def get_grade(self, marks):
        if marks >= 9:
            return "A+"
        elif marks >= 8:
            return "A"
        elif marks >= 7:
            return "B+"
        elif marks >= 6:
            return "B"
        else:
            return "C"
    
    def get_grade_color(self, marks):
        if marks >= 9:
            return "#27ae60"  # Green
        elif marks >= 8:
            return "#2980b9"  # Blue
        elif marks >= 7:
            return "#f39c12"  # Orange
        elif marks >= 6:
            return "#e67e22"  # Dark Orange
        else:
            return "#e74c3c"  # Red

def main():
    root = tk.Tk()
    app = TrainingDashboard(root)
    root.mainloop()

if __name__ == "__main__":
    main()