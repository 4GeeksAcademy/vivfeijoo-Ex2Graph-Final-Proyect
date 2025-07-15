# vivfeijoo-Ex2Graph-Final-Proyect

## Ex2Graph

**Ex2Graph** is a Python-based automation tool that reads data from Excel spreadsheets and transforms it into charts, which are then inserted into PowerPoint presentations.

## Project Goal

To simplify the process of creating visual reports and slides for meetings by automatically converting Excel data into presentation-ready charts.

##  Features (planned)

- Read data from `.xlsx` Excel files
- Generate bar, line, and pie charts
- Automatically insert charts into PowerPoint slides
- Export final `.pptx` files for presentation use

##  Project Structure

Ex2Graph/
│
├── data/          # Input Excel files
├── output/        # Generated PowerPoint files
├── src/           # Source code
│   ├── excel_reader.py
│   ├── plot_generator.py
│   └── ppt_creator.py
├── requirements.txt
├── README.md
└── .gitignore

##  Requirements

- Python 3.10 or higher
- Packages:
  - `pandas`
  - `openpyxl`
  - `matplotlib`
  - `python-pptx`

Install them using:

```bash
pip install -r requirements.txt


## How it works

	1.	Load the Excel file from the /data folder using excel_reader.py
	2.	Generate visual charts with plot_generator.py
	3.	Create PowerPoint slides and embed the charts using ppt_creator.py

## Next Steps
	•	Upload sample Excel files to data/
	•	Implement Excel reader module
	•	Create chart generator module
	•	Build PowerPoint creator module


Stay tuned — this tool will make visual reporting easier and faster!