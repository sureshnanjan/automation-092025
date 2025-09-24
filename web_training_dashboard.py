#!/usr/bin/env python3
"""
Web Training Dashboard using Python Standard Library
Run this script and open http://localhost:8000 in your browser
"""

import http.server
import socketserver
import webbrowser
import threading
import time
from urllib.parse import urlparse, parse_qs

class TrainingDashboardHandler(http.server.BaseHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
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
        super().__init__(*args, **kwargs)
    
    def do_GET(self):
        """Handle GET requests"""
        parsed_path = urlparse(self.path)
        
        if parsed_path.path == '/' or parsed_path.path == '/dashboard':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            html_content = self.generate_dashboard_html()
            self.wfile.write(html_content.encode('utf-8'))
        elif parsed_path.path == '/api/data':
            # API endpoint for data (if needed for future enhancements)
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            import json
            self.wfile.write(json.dumps(self.data).encode('utf-8'))
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<h1>404 - Page Not Found</h1>')
    
    def generate_dashboard_html(self):
        """Generate the complete HTML dashboard"""
        
        # Calculate statistics
        marks_values = list(self.data['marks'].values())
        avg_marks = sum(marks_values) / len(marks_values)
        max_marks = max(marks_values)
        min_marks = min(marks_values)
        
        # Generate topics HTML
        topics_html = ""
        for i, topic in enumerate(self.data['topics']):
            if i % 3 == 0 and i > 0:
                topics_html += "</div><div class='topics-row'>"
            elif i == 0:
                topics_html += "<div class='topics-row'>"
            topics_html += f"<div class='topic-item'>• {topic}</div>"
        topics_html += "</div>"
        
        # Generate student table rows
        student_rows = ""
        for i, student in enumerate(self.data['students']):
            marks = self.data['marks'][student]
            grade = self.get_grade(marks)
            grade_color = self.get_grade_color(marks)
            row_class = "even" if i % 2 == 0 else "odd"
            
            student_rows += f"""
            <tr class="{row_class}">
                <td>{student}</td>
                <td>{marks}</td>
                <td style="color: {grade_color}; font-weight: bold;">{grade}</td>
            </tr>
            """
        
        html_template = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Training Dashboard</title>
            <style>
                * {{
                    margin: 0;
                    padding: 0;
                    box-sizing: border-box;
                }}
                
                body {{
                    font-family: 'Arial', sans-serif;
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    min-height: 100vh;
                    padding: 20px;
                }}
                
                .container {{
                    max-width: 900px;
                    margin: 0 auto;
                    background: white;
                    border-radius: 15px;
                    box-shadow: 0 20px 40px rgba(0,0,0,0.1);
                    overflow: hidden;
                }}
                
                .header {{
                    background: linear-gradient(135deg, #2c3e50 0%, #34495e 100%);
                    color: white;
                    padding: 30px;
                    text-align: center;
                }}
                
                .header h1 {{
                    font-size: 2.5em;
                    margin-bottom: 10px;
                    text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
                }}
                
                .content {{
                    padding: 30px;
                }}
                
                .section {{
                    margin-bottom: 30px;
                    border-radius: 10px;
                    overflow: hidden;
                    box-shadow: 0 5px 15px rgba(0,0,0,0.1);
                }}
                
                .section-header {{
                    background: linear-gradient(135deg, #3498db 0%, #2980b9 100%);
                    color: white;
                    padding: 15px 20px;
                    font-size: 1.2em;
                    font-weight: bold;
                }}
                
                .section-content {{
                    padding: 20px;
                    background: #f8f9fa;
                }}
                
                .course-info {{
                    display: grid;
                    grid-template-columns: 1fr 1fr;
                    gap: 15px;
                }}
                
                .info-item {{
                    padding: 10px;
                    background: white;
                    border-radius: 8px;
                    border-left: 4px solid #3498db;
                }}
                
                .info-label {{
                    font-weight: bold;
                    color: #2c3e50;
                    margin-bottom: 5px;
                }}
                
                .info-value {{
                    color: #34495e;
                    font-size: 1.1em;
                }}
                
                .course-title {{
                    grid-column: 1 / -1;
                    border-left-color: #e74c3c;
                }}
                
                .course-title .info-value {{
                    font-size: 1.3em;
                    font-weight: bold;
                    color: #e74c3c;
                }}
                
                .topics-container {{
                    background: white;
                    border-radius: 8px;
                    padding: 15px;
                }}
                
                .topics-row {{
                    display: flex;
                    justify-content: space-between;
                    margin-bottom: 10px;
                }}
                
                .topic-item {{
                    flex: 1;
                    padding: 10px;
                    margin: 0 5px;
                    background: linear-gradient(135deg, #27ae60 0%, #2ecc71 100%);
                    color: white;
                    border-radius: 20px;
                    text-align: center;
                    font-weight: bold;
                    box-shadow: 0 3px 10px rgba(39, 174, 96, 0.3);
                }}
                
                .students-table {{
                    width: 100%;
                    border-collapse: collapse;
                    background: white;
                    border-radius: 8px;
                    overflow: hidden;
                }}
                
                .students-table th {{
                    background: linear-gradient(135deg, #2c3e50 0%, #34495e 100%);
                    color: white;
                    padding: 15px;
                    text-align: left;
                    font-weight: bold;
                }}
                
                .students-table td {{
                    padding: 12px 15px;
                    border-bottom: 1px solid #ecf0f1;
                }}
                
                .students-table tr.even {{
                    background: #f8f9fa;
                }}
                
                .students-table tr.odd {{
                    background: white;
                }}
                
                .students-table tr:hover {{
                    background: #e8f4fd;
                    transform: scale(1.02);
                    transition: all 0.2s ease;
                }}
                
                .summary-stats {{
                    display: grid;
                    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
                    gap: 15px;
                }}
                
                .stat-card {{
                    background: white;
                    padding: 20px;
                    border-radius: 10px;
                    text-align: center;
                    box-shadow: 0 3px 10px rgba(0,0,0,0.1);
                    border-top: 4px solid #3498db;
                }}
                
                .stat-value {{
                    font-size: 2em;
                    font-weight: bold;
                    color: #2c3e50;
                    margin-bottom: 5px;
                }}
                
                .stat-label {{
                    color: #7f8c8d;
                    font-size: 0.9em;
                    text-transform: uppercase;
                    letter-spacing: 1px;
                }}
                
                .highest {{
                    border-top-color: #27ae60;
                }}
                
                .lowest {{
                    border-top-color: #e74c3c;
                }}
                
                .average {{
                    border-top-color: #f39c12;
                }}
                
                .total {{
                    border-top-color: #9b59b6;
                }}
                
                @media (max-width: 768px) {{
                    .course-info {{
                        grid-template-columns: 1fr;
                    }}
                    
                    .topics-row {{
                        flex-direction: column;
                    }}
                    
                    .topic-item {{
                        margin: 5px 0;
                    }}
                    
                    .summary-stats {{
                        grid-template-columns: repeat(2, 1fr);
                    }}
                }}
                
                .footer {{
                    background: #2c3e50;
                    color: white;
                    text-align: center;
                    padding: 20px;
                    margin-top: 30px;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <h1>🎓 Training Dashboard</h1>
                    <p>Course Management System</p>
                </div>
                
                <div class="content">
                    <!-- Course Information -->
                    <div class="section">
                        <div class="section-header">
                            📚 Course Information
                        </div>
                        <div class="section-content">
                            <div class="course-info">
                                <div class="info-item course-title">
                                    <div class="info-label">Course Title</div>
                                    <div class="info-value">{self.data['title']}</div>
                                </div>
                                <div class="info-item">
                                    <div class="info-label">Start Date</div>
                                    <div class="info-value">{self.data['start_date']}</div>
                                </div>
                                <div class="info-item">
                                    <div class="info-label">End Date</div>
                                    <div class="info-value">{self.data['end_date']}</div>
                                </div>
                                <div class="info-item">
                                    <div class="info-label">Trainer Name</div>
                                    <div class="info-value">{self.data['trainer_name']}</div>
                                </div>
                            </div>
                        </div>
                    </div>
                    
                    <!-- Topics -->
                    <div class="section">
                        <div class="section-header">
                            🛠️ Course Topics
                        </div>
                        <div class="section-content">
                            <div class="topics-container">
                                {topics_html}
                            </div>
                        </div>
                    </div>
                    
                    <!-- Students & Performance -->
                    <div class="section">
                        <div class="section-header">
                            👨‍🎓 Students & Performance
                        </div>
                        <div class="section-content">
                            <table class="students-table">
                                <thead>
                                    <tr>
                                        <th>Student ID</th>
                                        <th>Marks</th>
                                        <th>Grade</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    {student_rows}
                                </tbody>
                            </table>
                        </div>
                    </div>
                    
                    <!-- Summary -->
                    <div class="section">
                        <div class="section-header">
                            📊 Performance Summary
                        </div>
                        <div class="section-content">
                            <div class="summary-stats">
                                <div class="stat-card total">
                                    <div class="stat-value">{len(self.data['students'])}</div>
                                    <div class="stat-label">Total Students</div>
                                </div>
                                <div class="stat-card average">
                                    <div class="stat-value">{avg_marks:.1f}</div>
                                    <div class="stat-label">Average Marks</div>
                                </div>
                                <div class="stat-card highest">
                                    <div class="stat-value">{max_marks}</div>
                                    <div class="stat-label">Highest Score</div>
                                </div>
                                <div class="stat-card lowest">
                                    <div class="stat-value">{min_marks}</div>
                                    <div class="stat-label">Lowest Score</div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                
                <div class="footer">
                    <p>Training Dashboard &copy; 2025 | Built with Python Standard Library</p>
                </div>
            </div>
        </body>
        </html>
        """
        
        return html_template
    
    def get_grade(self, marks):
        """Calculate grade based on marks"""
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
        """Get color for grade display"""
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
    
    def log_message(self, format, *args):
        """Override to customize log messages"""
        print(f"[{self.address_string()}] {format % args}")

def start_server(port=8000):
    """Start the web server"""
    try:
        with socketserver.TCPServer(("", port), TrainingDashboardHandler) as httpd:
            print(f"🚀 Training Dashboard Server started!")
            print(f"📱 Open your browser and go to: http://localhost:{port}")
            print(f"🛑 Press Ctrl+C to stop the server\n")
            
            # Optional: Auto-open browser (you can comment this out if not needed)
            def open_browser():
                time.sleep(1)  # Give server time to start
                try:
                    webbrowser.open(f'http://localhost:{port}')
                    print("🌐 Browser opened automatically")
                except:
                    print("💡 Please manually open your browser and visit the URL above")
            
            browser_thread = threading.Thread(target=open_browser, daemon=True)
            browser_thread.start()
            
            httpd.serve_forever()
            
    except KeyboardInterrupt:
        print("\n🛑 Server stopped by user")
    except OSError as e:
        if "Address already in use" in str(e):
            print(f"❌ Port {port} is already in use. Try a different port:")
            print(f"   python {__file__} --port 8001")
        else:
            print(f"❌ Error starting server: {e}")

def main():
    """Main function with command line argument support"""
    import sys
    
    port = 8000
    
    # Simple command line argument parsing
    if len(sys.argv) > 1:
        for i, arg in enumerate(sys.argv):
            if arg in ['--port', '-p'] and i + 1 < len(sys.argv):
                try:
                    port = int(sys.argv[i + 1])
                except ValueError:
                    print("❌ Invalid port number")
                    return
            elif arg in ['--help', '-h']:
                print("Training Dashboard Web Server")
                print("Usage: python dashboard.py [--port PORT]")
                print("Options:")
                print("  --port, -p PORT    Specify port number (default: 8000)")
                print("  --help, -h         Show this help message")
                return
    
    start_server(port)

if __name__ == "__main__":
    main()