from datetime import datetime

def generate_html_report(student_name, report):

    # Lists
    strengths_html = "".join(
        f"<li>✅ {s.replace('_', ' ').title()}</li>"
        for s in report["strengths"]
    )

    weaknesses_html = "".join(
        f"<li>⚠️ {w.replace('_', ' ').title()}</li>"
        for w in report["weaknesses"]
    )

    focus_html = "".join(
        f"<li>🎯 {f.replace('_', ' ').title()}</li>"
        for f in report["focus_priorities"]
    )

    trajectory_html = "".join(
        f"<li>📈 {step}</li>"
        for step in report["growth_trajectory"]
    )

    impact_html = "".join(
        f"<li><b>{k.replace('_',' ').title()}</b>: {v}</li>"
        for k, v in report["estimated_impact"].items()
    )

    html = f"""
    <html>
    <head>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f4f6f8;
                padding: 20px;
            }}
            .container {{
                max-width: 800px;
                margin: auto;
                background: #ffffff;
                padding: 25px;
                border-radius: 10px;
            }}
            h1 {{
                text-align: center;
                color: #2c3e50;
            }}
            h2 {{
                color: #34495e;
                border-bottom: 1px solid #eee;
                padding-bottom: 5px;
            }}
            .box {{
                margin-top: 20px;
                padding: 15px;
                background: #f9fafb;
                border-radius: 8px;
            }}
            .badge {{
                display: inline-block;
                padding: 8px 12px;
                border-radius: 20px;
                background: #3498db;
                color: white;
                font-weight: bold;
            }}
            ul {{
                padding-left: 18px;
            }}
        </style>
    </head>

    <body>
        <div class="container">
            <h1>🎓 Placement Readiness Report</h1>

            <p><b>Student:</b> {student_name}</p>
            <p><b>Date:</b> {datetime.now().strftime('%d %b %Y')}</p>

            <div class="box">
                <h2>📊 Scores</h2>
                <p><b>Readiness Score:</b> {round(report["readiness_score"], 2)}</p>
                <p><b>AI-Proof Score:</b> {round(report["ai_proof_score"], 2)}</p>
                <p><b>Estimated Time to Ready:</b> {report["estimated_time_to_ready"]}</p>
            </div>

            <div class="box">
                <h2>🧠 Insights</h2>
                <p><b>Aptitude:</b> {report["aptitude_insight"]}</p>
                <p><b>English:</b> {report["english_insight"]}</p>
                <p><b>Domain Skills:</b> {report["domain_skill_insight"]}</p>
            </div>

            <div class="box">
                <h2>💪 Strengths</h2>
                <ul>{strengths_html}</ul>
            </div>

            <div class="box">
                <h2>⚠️ Weaknesses</h2>
                <ul>{weaknesses_html}</ul>
            </div>

            <div class="box">
                <h2>🎯 Focus Priorities</h2>
                <ul>{focus_html}</ul>
            </div>

            <div class="box">
                <h2>📈 Growth Trajectory</h2>
                <ul>{trajectory_html}</ul>
            </div>

            <div class="box">
                <h2>🚀 Estimated Impact</h2>
                <ul>{impact_html}</ul>
            </div>

            <div class="box">
                <h2>🎯 Career Insights</h2>
                <p><b>Placement Type:</b> {report["placement_type"]}</p>
                <p><b>Domain Switch Feasibility:</b> {report["domain_switch_feasibility"]}</p>
            </div>

            <footer style="margin-top:20px; font-size:12px; text-align:center; color:#888;">
                This report is AI-generated based on skill analysis and peer comparison.
            </footer>

        </div>
    </body>
    </html>
    """

    return html