import subprocess
import json
from summarise import extract

# Replace these with your Azure details and audio file path
resource_key = "CdyrFJGcwalz8miGY1EmnhI3Sn1dkQ4f1bvelJE7lUbAoTWx8osaJQQJ99ALACmepeSXJ3w3AAAAACOGAt3k"
region = "uksouth"
audio_file_path = r"C:\Users\train\Documents\GitHub\NullPointers\speechrec\sample2.wav"

# Build the curl command
curl_command = [
    "curl",
    "-X", "POST",
    f"https://{region}.stt.speech.microsoft.com/speech/recognition/conversation/cognitiveservices/v1?language=en-US",
    "-H", f"Ocp-Apim-Subscription-Key: {resource_key}",
    "-H", "Content-Type: audio/wav",
    "--data-binary", f"@{audio_file_path}"
]

try:
    # Execute the curl command and capture the output
    result = subprocess.run(curl_command, capture_output=True, text=True, check=True)
    response_json = result.stdout

    # Parse the JSON response to extract the transcription text
    response_data = json.loads(response_json)
    transcribed_text = response_data.get("DisplayText", "Transcription not found")

    # Print the transcribed text
    print("Transcribed Text:", transcribed_text)
    extract(transcribed_text)

except subprocess.CalledProcessError as e:
    print("Error calling Azure Speech-to-Text API:", e.stderr)
except json.JSONDecodeError:
    print("Error parsing the JSON response.")

