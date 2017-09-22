import awareness as a
import wave


class PCMAudioStreamer(a.LocalComponent):
    inputs = 0
    outputs = 4 # 16-bit sample per channel

    def run(self, input, progress_callback=None):
        wf = wave.open("audio.wav", 'rb')
        data = wf.readframes(input.count)
        while data != b'':
            data_spliced = [data[x:x+4] for x in range(0, len(data),4)]
            stream = a.Stream.from_bytes(data_spliced)
            print("Sending a.Stream containing:")
            print(stream.items)
            progress_callback(stream)
            data = wf.readframes(input.count)
        return a.Stream.from_blank(input.count, 4)


machine3 = a.LocalOperator(b'192.168.2.4')
machine3.components = [PCMAudioStreamer()]


machine3.provider.join()