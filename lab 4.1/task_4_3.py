import csv
def analyze_csv_file():
    file_path = input("Enter the CSV file name: ").strip()
    try:
        with open(file_path, newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            total_rows = 0
            empty_rows = 0
            total_words = 0
            for row in reader:
                total_rows += 1
                # A row is empty if all cells are empty after stripping
                if all(cell.strip() == '' for cell in row):
                    empty_rows += 1
                total_words += sum(len(cell.strip().split()) for cell in row)
            print(f"Total rows: {total_rows}")
            print(f"Empty rows: {empty_rows}")
            print(f"Total words: {total_words}")
    except FileNotFoundError:
        print("File not found. Please check the file name and try again.")

analyze_csv_file()

