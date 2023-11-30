# main.py
from extract.main import extract
from transform.main import transform
from load.main import load

def main():
    raw_data = extract()
    transformed_data = transform(raw_data)
    load(transformed_data)

if __name__ == "__main__":
    main()