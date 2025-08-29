from flask import Flask, request, jsonify
import os
import re
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

FULL_NAME = os.getenv("FULL_NAME", "madheshwaran s").strip().lower().replace(" ", "_")
DOB_DDMMYYYY = os.getenv("DOB_DDMMYYYY", "23032005").strip()
EMAIL = os.getenv("EMAIL", "madheshwaran.s2022@vitstudent.ac.in").strip()
ROLL_NUMBER = os.getenv("ROLL_NUMBER", "22BRS1183").strip()
USER_ID = f"{FULL_NAME}_{DOB_DDMMYYYY}"

app = Flask(__name__)

def is_integer_string(s: str) -> bool:
    return bool(re.fullmatch(r"[+-]?\d+", s))

def is_alpha_string(s: str) -> bool:
    return s.isalpha()

def extract_alpha_chars(s: str):
    return [ch for ch in s if ch.isalpha()]

@app.route("/", methods=["GET"])
def root():
    return "BFHL API running", 200

@app.route("/bfhl", methods=["POST"])
def bfhl():
    try:
        body = request.get_json(force=True, silent=True) or {}
        items = body.get("data", []) if isinstance(body, dict) else []

        odd_numbers = []
        even_numbers = []
        alphabets = []
        special_characters = []
        alpha_chars_linear = []
        total_sum = 0

        for item in items:
            s = str(item)
            alpha_chars_linear.extend(extract_alpha_chars(s))

            if is_integer_string(s):
                n = int(s)
                total_sum += n
                if abs(n) % 2 == 0:
                    even_numbers.append(str(n))
                else:
                    odd_numbers.append(str(n))
            elif is_alpha_string(s):
                alphabets.append(s.upper())
            else:
                special_characters.append(s)

        reversed_alpha = list(reversed(alpha_chars_linear))
        alt_cased_chars = [
            (ch.upper() if i % 2 == 0 else ch.lower())
            for i, ch in enumerate(reversed_alpha)
        ]
        concat_string = "".join(alt_cased_chars)

        response = {
            "is_success": True,
            "user_id": USER_ID,
            "email": EMAIL,
            "roll_number": ROLL_NUMBER,
            "odd_numbers": odd_numbers,
            "even_numbers": even_numbers,
            "alphabets": alphabets,
            "special_characters": special_characters,
            "sum": str(total_sum),
            "concat_string": concat_string,
        }
        return jsonify(response), 200

    except Exception as e:
        return jsonify({
            "is_success": False,
            "message": f"Bad Request: {e}",
            "user_id": USER_ID,
            "email": EMAIL,
            "roll_number": ROLL_NUMBER,
        }), 400

if __name__ == "__main__":
    app.run()
