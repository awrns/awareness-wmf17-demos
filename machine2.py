import awareness as a


class Multiply5(a.LocalComponent):
    inputs = 1
    outputs = 1

    def run(self, input, **kwargs):
        output = []
        for item in input.items:
            output.append([item[0] * 5])
        return a.Stream(output)


class MultiplyTogether(a.LocalComponent):
    inputs = 2
    outputs = 1

    def run(self, input, **kwargs):
        output = []
        for item in input.items:
            output.append([item[0] * item[1]])
        return a.Stream(output)

class Divide5(a.LocalComponent):
    inputs = 1
    outputs = 1

    def run(self, input, **kwargs):
        output = []
        for item in input.items:
            output.append([item[0] // 5])
        return a.Stream(output)


class DivideTogether(a.LocalComponent):
    inputs = 2
    outputs = 1

    def run(self, input, **kwargs):
        output = []
        for item in input.items:
            output.append([item[0] // item[1]])
        return a.Stream(output)


a.backend.NativeBackend.setup_logger()
machine2 = a.LocalOperator(b'192.168.2.6')
machine2.components = [Multiply5(), MultiplyTogether(), Divide5(), DivideTogether()]


machine2.provider.join()