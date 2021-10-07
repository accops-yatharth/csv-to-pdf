import prettytable
import pdfkit
import htmlmin
import os
import datetime
import argparse
import csv
MYSTYLE = ""
real_path = os.path.dirname(os.path.realpath(__file__))
print(real_path)
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("csv_path", help="full path to the csv file.")
    parser.add_argument("output_path", help="full output path to the pdf file.")


    args = parser.parse_args()
    if not args.csv_path.lower().endswith("csv"):
        print("Invalid input file. Ensure the file is csv format.")
        return 1

    if not args.output_path.lower().endswith("pdf"):
        print("Invalid output file. Ensure the file is pdf format.")
        return 1
    with open(os.path.join(real_path, 'mystyle.css'), 'r') as f:
        MYSTYLE = f.read()
    
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
    data = []
    with open(args.csv_path, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            data.append(row)

    header = data[0]
    cols = len(header)
    df = prettytable.PrettyTable(header)
    for i, row in enumerate(data):
        if i == 0: continue
        df.add_row(row)        
 
   
    
    html = htmlmin.minify(f"<style>{MYSTYLE}</style><p>Report generated at : {current_time}</p>\
            {df.get_html_string(attributes={'class':'mystyle'})}<p>Report generated by Accops Reporting Server.</p>")
    pdfkit.from_string(html, args.output_path, options={"quiet": ""})
    return 0


if __name__ == '__main__':
    main()
