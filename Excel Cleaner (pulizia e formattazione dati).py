import pandas as pd

def clean_excel(input_file, output_file):
    df = pd.read_excel(input_file)
    df = df.drop_duplicates()
    df = df.dropna(how='all')
    df = df.sort_values(by=df.columns[0])
    df.to_excel(output_file, index=False)
    print(f"File pulito salvato come {output_file}")

if __name__ == "__main__":
    in_file = input("Nome file Excel da pulire: ")
    out_file = "excel_pulito.xlsx"
    clean_excel(in_file, out_file)
