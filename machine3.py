import awareness as a
import wave
import numpy


class PCMAudioStreamer(a.LocalComponent):
    inputs = 0
    outputs = 4 # 16-bit sample per channel

    def run(self, input, progress_callback=None):
        wf = wave.open("audio.wav", 'rb')
        data = wf.readframes(input.count)
        while data != b'':
            data_spliced = numpy.fromstring(data, dtype=numpy.uint8)
            data_spliced.shape = (-1, 4)
            stream = a.Stream(data_spliced)
            print("Sending a.Stream containing:")
            print(stream.items)
            progress_callback(stream)
            data = wf.readframes(input.count)
        return a.Stream.from_blank(input.count, 4)



class SetZero(a.LocalComponent):
    inputs = 1
    outputs = 1

    def run(self, input, **kwargs):
        output = []
        for item in input.items:
            output.append([0])
        return a.Stream(output)


machine3 = a.LocalOperator(b'192.168.2.4')
machine3.components = [PCMAudioStreamer(), SetZero()]


machine3.provider.join()