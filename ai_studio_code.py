import os
from google import genai
from google.genai import types

# =====================================================================
# 🚨 PASTE YOUR GOOGLE API KEY DIRECTLY BETWEEN THE QUOTES BELOW 🚨
# =====================================================================
api_key = "YOUR_REAL_KEY_HERE"

if not api_key or "YOUR_REAL_KEY" in api_key:
    print("❌ ERROR: Please insert your real Gemini API key!")
    exit()

# Initialize the official Google Gemini client
client = genai.Client(api_key=api_key)

# Configure the advanced AI Studio generation settings
generation_config = {
    'temperature': 1.0,
    'max_output_tokens': 65536,
    'top_p': 0.95,
}

def run_ai_studio_demo(course_material: str):
    """Executes a single processing loop using the exact AI Studio configuration."""
    
    system_instruction = (
        "You are Google Brief, an official autonomous academic AI agent developed by Google. "
        "Your role is to analyze large course materials, extract core knowledge, "
        "and generate a clear executive summary followed by a logical action plan (To-Do list)."
    )
    
    print("🤖 AI Studio Engine is processing the sample data...")
    
    try:
        response = client.models.generate_content(
            model='gemini-3.5-flash',
            contents=f"Analyze the following material and generate a structured summary: {course_material}",
            config=types.GenerateContentConfig(
                system_instruction=system_instruction,
                temperature=generation_config['temperature'],
                max_output_tokens=generation_config['max_output_tokens'],
                top_p=generation_config['top_p']
            )
        )
        print("\n--- GOOGLE AI STUDIO OUTPUT ---")
        print(response.text)
        print("===============================📄")
        
    except Exception as error:
        print(f"\n❌ API CONNECTION ERROR: {error}")

if __name__ == "__main__":
    # Sample data block
    sample_data = (
        "Computer Architecture - Lecture 1. "
        "Today we explore processor core structures, internal registers, and cache memory. "
        "Students must master the fundamental differences between Von Neumann and Harvard architectures."
    )
    run_ai_studio_demo(sample_data)
