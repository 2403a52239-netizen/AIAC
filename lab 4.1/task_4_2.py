def analyze_csv_file():
    file_path = input("Enter the CSV file name: ").strip()
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            total_rows = 0
            empty_rows = 0
            total_words = 0
            for line in f:
                total_rows += 1
                stripped_line = line.strip()
                if not stripped_line:
                    empty_rows += 1
                else:
                    cells = stripped_line.split(',')
                    for cell in cells:
                        words = cell.strip().split()
                        total_words += len(words)
            print(f"Total rows: {total_rows}")
            print(f"Empty rows: {empty_rows}")
            print(f"Total words: {total_words}")
    except FileNotFoundError:
        print("File not found. Please check the file name and try again.")

analyze_csv_file()

