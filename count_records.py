try:
    with open("data_files/data.txt", "r") as f:
        records = {}

        for line in f:
            item = line.strip()
            
            print(f"Processing line: '{line}' => Stripped: '{item}'")  
            
            if item:
                if item in records:
                    records[item] += 1  
                else:
                    records[item] = 1 
        
        print(f"Total records: {sum(records.values())}")
        
        print("\nRecord summary:")
        for item, num in records.items():
            print(f"- {item}: {num} time(s)")

except FileNotFoundError:
    print("Error: The file was not found.")
except IOError:
    print("Error: There was a problem with reading the file.")
