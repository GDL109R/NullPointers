import azure.cognitiveservices.speech as speechsdk

# Set up the subscription info for the Speech Service:
speech_key, service_region = "CdyrFJGcwalz8miGY1EmnhI3Sn1dkQ4f1bvelJE7lUbAoTWx8osaJQQJ99ALACmepeSXJ3w3AAAAACOGAt3k", "uksouth"
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)

# Set the output format to WAV
audio_config = speechsdk.audio.AudioOutputConfig(filename="output.wav")

# Create a synthesizer with the given settings
synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

# Synthesize the text to speech
text = "Hello, this is a test of Azure Text to Speech."
result = synthesizer.speak_text_async(text).get()

if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
    print("Speech synthesized to 'output.wav'")
else:
    print("Speech synthesis canceled: {}".format(result.cancellation_details.reason))
