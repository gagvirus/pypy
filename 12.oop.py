class CPU:
    def __init__(self, brand, gen, cores, threads):
        self.brand = brand
        self.gen = gen
        self.cores = cores
        self.threads = threads

    def __str__(self):
        return "{brand} {gen}th gen {cores}x{threads}".format(brand=self.brand, gen=self.gen, cores=self.cores,
                                                        threads=self.threads)


class Computer:
    def __init__(self, cpu, gpu):
        self.cpu = cpu
        self.gpu = gpu

    def __str__(self):
        return """
booting up PC
CPU: {cpu}
GPU: {gpu}
        """.format(cpu=self.cpu, gpu=self.gpu)


i5 = CPU('intel', 9, 6, 1)
myPc = Computer(i5, '1060')

print(myPc)
