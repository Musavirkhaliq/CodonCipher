# parse_and_filter_sequences.py

import csv
import re

input_file = "data.txt"
output_file = "tpi_sequences_filtered.csv"

# keywords to eliminate (case-insensitive)
exclude_keywords = ["fragment", "precursor", "chloroplast", "glycosomal"]

# regex to capture structure
pattern = re.compile(
    r"^>(\S+)\s+(\S+)\s+(\S+)\s+[-]+ (.+?)\.\[(.+)\]"
)

rows = []

with open(input_file, "r") as infile:
    for line in infile:
        if line.startswith(">"):
            header = line.strip()
            # skip excluded keywords
            if any(k in header.lower() for k in exclude_keywords):
                continue
            
            match = pattern.match(header)
            if match:
                seq_id, num1, num2, desc, organism = match.groups()
                rows.append({
                    "ID": seq_id,
                    "Number1": num1,
                    "Number2": num2,
                    "Description": desc.strip(),
                    "Organism": organism.strip()
                })

# write to CSV
with open(output_file, "w", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=["ID", "Number1", "Number2", "Description", "Organism"])
    writer.writeheader()
    writer.writerows(rows)

print(f"✅ Done! Filtered and parsed sequences saved to {output_file}")
