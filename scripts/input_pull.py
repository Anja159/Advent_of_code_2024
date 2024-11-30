import requests
import os

AOC_YEAR = 2024 
AOC_DAY = 1     
OUTPUT_FILE = f"day_{AOC_DAY:02}_input.txt"
SESSION_COOKIE = "<session_cookie>"  # Replace with your session cookie

def fetch_input(year, day, session_cookie):
    """
    Fetches the input for the given day and year from Advent of Code.
    """
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    headers = {
        "Cookie": f"session={session_cookie}"
    }

    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.text
    else:
        raise Exception(f"Failed to fetch input: HTTP {response.status_code} - {response.reason}")

def save_to_file(content, filename):
    """
    Saves the given content to a file.
    """
    with open(filename, "w") as file:
        file.write(content)
    print(f"Input saved to {filename}")

if __name__ == "__main__":
    try:
        input_data = fetch_input(AOC_YEAR, AOC_DAY, SESSION_COOKIE)
        save_to_file(input_data, OUTPUT_FILE)
    except Exception as e:
        print(f"Error: {e}")
