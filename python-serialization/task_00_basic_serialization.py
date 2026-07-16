#!/usr/bin/env python3
import json


def serialize_and_save_to_file(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data


if __name__ == "__main__":
    sample_data = {
        "name": "John Doe",
        "age": 30,
        "city": "New York"
    }

    serialize_and_save_to_file(sample_data, 'data.json')
    print("Data serialized and saved to 'data.json'.")

    deserialized = load_and_deserialize('data.json')
    print("Deserialized Data:")
    print(deserialized)
