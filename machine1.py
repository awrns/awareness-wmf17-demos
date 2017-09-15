import awareness as a


class Add1(a.LocalComponent):
    inputs = 1
    outputs = 1

    def run(self, input, **kwargs):
        output = []
        for item in input.items:
            output.append([item[0] + 1])
        return a.Stream(output)


class AddTogether(a.LocalComponent):
    inputs = 2
    outputs = 1

    def run(self, input, **kwargs):
        output = []
        for item in input.items:
            output.append([item[0] + item[1]])
        return a.Stream(output)

class Subtract1(a.LocalComponent):
    inputs = 1
    outputs = 1

    def run(self, input, **kwargs):
        output = []
        for item in input.items:
            output.append([item[0] - 1])
        return a.Stream(output)


class SubtractTogether(a.LocalComponent):
    inputs = 2
    outputs = 1

    def run(self, input, **kwargs):
        output = []
        for item in input.items:
            output.append([item[0] - item[1]])
        return a.Stream(output)



machine1 = a.LocalOperator(b'localhost', port=1601)
machine1.components = [Add1(), AddTogether(), Subtract1(), SubtractTogether()]


machine1.provider.join()