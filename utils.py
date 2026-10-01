import json
import math

def calculate_revenue(price: float, quantity: int, discount_pct: float = 0) -> float:
    """
    Returns the final revenue after applying discount.
    Formula: price * quantity * (1 - discount_pct / 100)
    Default discount is 0%.
    """
    return price * quantity * (1 - discount_pct / 100)

def classify_customer(age: float) -> str:
    """
    Returns customer segment as a string:
    - age < 25     → "Youth"
    - 25 <= age < 45 → "Adult"
    - age >= 45    → "Senior"
    - age is None or NaN  → "Unknown"
    """
    # Handle None or pandas/numpy NaN values
    if age is None or (isinstance(age, float) and math.isnan(age)):
        return "Unknown"
    
    if age < 25:
        return "Youth"
    elif 25 <= age < 45:
        return "Adult"
    else:
        return "Senior"

def is_valid_email(email: str) -> bool:
    """
    Returns True if email contains '@' and '.', else False.
    """
    if isinstance(email, str) and '@' in email and '.' in email:
        return True
    return False

def load_config(filepath: str) -> dict:
    """
    Reads a JSON file and returns it as a Python dictionary.
    Uses a context manager (with block).
    """
    with open(filepath, 'r') as f:
        return json.load(f)

def write_summary_report(stats: dict, output_path: str) -> None:
    """
    Writes a plain-text summary report to the given file path.
    Each key-value pair in stats should be on its own line.
    Format: "Key: Value"
    """
    with open(output_path, 'w') as f:
        for key, value in stats.items():
            f.write(f"{key}: {value}\n")

# --- Test Block ---
if __name__ == "__main__":
    # 1. Load the config using load_config()
    config = load_config("config.json")
    
    # 2. Print the project_name and tax_rate
    print(f"Project Name: {config.get('project_name')}")
    print(f"Tax Rate: {config.get('tax_rate')}%")
    
    # 3. Call calculate_revenue(1200, 3, 10) and print the result
    rev = calculate_revenue(1200, 3, 10)
    print(f"Revenue for (1200, 3, 10% discount): ₹{rev}")
    
    # 4. Call classify_customer(None) and print the result
    segment = classify_customer(None)
    print(f"Customer classification for age 'None': {segment}")