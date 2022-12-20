from youtube_transcript_api import YouTubeTranscriptApi

def generate_transcript(id):
	transcript = YouTubeTranscriptApi.get_transcript(id)
	script = ""

	for text in transcript:
		t = text["text"]
		if t != '[Music]':
			script += t + " "
		
	return script, len(script.split())

id = 'DInMru2Eq6E'
transcript, no_of_words = generate_transcript(id)
print(transcript)

text_file = open("Output.txt", "w")
text_file.write(transcript)
text_file.close()