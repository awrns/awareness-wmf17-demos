import awareness as a
import pyaudio

p = pyaudio.PyAudio()

audio_out = p.open(format=p.get_format_from_width(2),
                channels=2,
                rate=44100,
                output=True)


def stream_callback(stream):
	print("Recieved a.Stream containing:")
	print(stream.items)
	list_data = stream.to_bytes()
	data = b''
	for sample in list_data:
		data += sample
	audio_out.write(data)
	return True


mediademo = a.RemoteOperator(b'192.168.2.7')
with mediademo:
	mediademo.process(0, a.Stream.from_blank(1024, 0), progress_callback = stream_callback)
