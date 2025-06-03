from ingestion.competitor_messaging import fetch_latest_messaging
from renderers.report_pdf import render_report

data = fetch_latest_messaging("competitor.com")
render_report(data, filename="sample_report.pdf")
