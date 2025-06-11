import json
import sys

def scale_json_values(input_path, output_path, factor=1.4):
    with open(input_path, 'r') as f:
        data = json.load(f)

    scaled_data = {}

    for key, value in data.items():

        if isinstance(value, (int, float)):
            scaled_data[key] = round(value * factor, 4)  # Optional: round to 4 decimals
        else:
            scaled_data[key] = value  # Keep unchanged if not numeric
    #if value is dict
        if isinstance(value, dict):
            scaled_data[key] = {k: round(v * factor, 4) if isinstance(v, (int, float)) else v for k, v in value.items()}
        #if value is list
        elif isinstance(value, list):
            scaled_data[key] = [round(v * factor, 4) if isinstance(v, (int, float)) else v for v in value]
    with open(output_path, 'w') as f:
        json.dump(scaled_data, f, indent=4)

    print(f"Scaled values saved to: {output_path}")

if __name__ == "__main__":
    # if len(sys.argv) < 3:
    #     print("Usage: python scale_json_values.py input.json output.json")
    #     sys.exit(1)

    input_file = "/home/dimitris/HoarePrompt-data/Results/Paper/llama3/normal/code_force_pilot_k_0_1/tokens.json"
    output_file = "/home/dimitris/HoarePrompt-data/Results/Paper/llama3/normal/code_force_pilot_k_0_1/tokens2.json"
    scale_json_values(input_file, output_file)
