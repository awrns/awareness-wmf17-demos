import awareness as a
import wave

wf = wave.open("audio.wav", 'rb')


class PCMAudioStreamer(a.LocalComponent):
    inputs = 0
    outputs = 4 # 16-bit sample per channel

    def run(self, input, progress_callback=None):
        data = wf.readframes(1024)
        while data != b'':
            data_spliced = [data[x:x+4] for x in range(0, len(data),4)]
            stream = a.Stream.from_bytes(data_spliced)
            print("Sending a.Stream containing:")
            print(stream.items)
            progress_callback(stream)
            data = wf.readframes(1024)
        return a.Stream.blankFromCountParameters(input.count, 4)


machine3 = a.LocalOperator(b'localhost', port=1603)
machine3.components = [PCMAudioStreamer()]


machine3.provider.join()