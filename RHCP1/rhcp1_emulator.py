class Emulator:

    def __init__(self):
        self.register = [[hex(0), hex(0), hex(0), hex(0)] for x in range(16)]
        self.ram = [[hex(0), hex(0), hex(0), hex(0)] for x in range(64)]

    def execute(self, opcode: str, *args):
        oprands = list(args)
        func = getattr(self, opcode)
        print(func(oprands))

    def instruction(self, oprands=None):  # Instruction method template
        if oprands is None:
            oprands = []
        print(f"Registers : {self.register}")
        print(f"RAM: {self.ram}")
        print(oprands)
        return "bar"


emulator = Emulator()
emulator.execute("instruction", 1, 2, 3)
