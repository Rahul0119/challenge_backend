import json
from collections import Counter
from typing import List, Tuple

def load_data(filename: str) -> List[int]:
    """Load a list of integers from a JSON file."""
    with open(filename, 'r') as file:
        data = json.load(file)
        return data['numbers']

def calculate_frequency(numbers: List[int]) -> List[Tuple[int, int]]:
    """Calculate the frequency of each unique number and return sorted by frequency descending."""
    # Use Counter to count the occurrences of each number
    counts = Counter(numbers)
    # Sort the counts by frequency in descending order
    sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_counts

def get_third_highest_frequency(frequencies: List[Tuple[int, int]]) -> Tuple[int, int]:
    """Retrieve the third highest frequency from the list of (number, frequency) tuples."""
    # Check if there are at least three distinct frequencies
    if len(frequencies) >= 3:
        # Return the third highest frequency tuple
        return frequencies[2]
    else:
        # If there are fewer than three distinct frequencies, return None
        return None

def save_output(data: dict, filename: str) -> None:
    """Save the given data as JSON in a file."""
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def main():
    numbers = load_data('data.json')
    frequencies = calculate_frequency(numbers)
    third_highest_freq = get_third_highest_frequency(frequencies)
    
    output = {
        "sorted_frequency_distribution": frequencies,
        "third_highest_frequency": third_highest_freq
    }
    
    save_output(output, 'output.json')
    
    print("Output saved to output.json")

if __name__ == "__main__":
    main()
