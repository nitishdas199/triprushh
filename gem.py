import os
import google.generativeai as genai

# Configure the Google Generative AI SDK (assuming you have it set up)
genai.configure(api_key="AIzaSyBziUj7rge09JxsxjyrdZMdq1dheYT2BJQ")  # Replace with your actual API key

# Create the model
generation_config = {
 "temperature": 0.5,
 "top_p": 0.95,
 "top_k": 64,
 "max_output_tokens": 1000, # Reduced to keep it concise
 "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
 model_name="gemini-1.5-flash",
 generation_config=generation_config
)

# Start a chat session with an empty history
chat_session = model.start_chat(history=[])


# Function to generate itinerary based on user input
def generate_itinerary(departure_location, location, people_count, travel_days, travel_month, audience_choice, budget):
    """
    Generates an itinerary based on the provided user input.

    Args:
        departure_location (str): User's departure location.
        location (str): User's destination location.
        people_count (int): Number of people traveling.
        travel_days (int): Number of travel days.
        travel_month (str): Travel month.
        audience_choice (str): Type of trip (Adventure, Family, Elderly).
        budget (int): Budget in USD.

    Returns:
        str: Generated itinerary.
    """

    prompt = f"""
    You're an expert travel planner. A user has provided the following details for their trip:
    - Departure Location: {departure_location}
    - Travel Month: {travel_month}
    - Number of People: {people_count}
    - Travel Days: {travel_days}
    - Audience: {audience_choice}
    - Location: {location}
    - Budget in USD: {budget}

    Please provide a suitable itinerary based on these inputs.
    Also give recommendations on hotel and transportation.
    """

    response = chat_session.send_message(prompt)
    return response.text


