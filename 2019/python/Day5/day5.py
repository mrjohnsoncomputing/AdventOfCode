import johnson, time


class Computer:
    def __init__(self):
        print("Turning on Computer...")
        time.sleep(1)
        self.input = johnson.readfile("data.txt", ",")
        print("Input Length: {}".format(len(self.input)))

    def process_input(self):
        i = 0
        while i < len(self.input):
            length = 4
            op = self.input[i]
            # print("i: {} || opcode: {}".format(i, op))
            if op[len(op)-1] == "4" or op[len(op)-1] == "3":
                length = 2

            data = self.parse_chunk(i, length)

            if not self.operate_on_data(data):
                print("Halt")
                break
            i += length

    def parse_chunk(self, current_position, l):
        # IMPLEMENT Split Intcode into parameter mode and operation code
        arr = self.input[:]
        int_code = arr[current_position]

        if len(int_code) <= 2:
            p_mode = "0" * (l-1)
        else:
            p_mode = int_code[0:len(int_code) - 2]
            int_code = int(int_code[len(int_code) - 2: len(int_code)])

            while len(p_mode) < l:
                p_mode = "0" + p_mode

        data = [int(int_code)]
        p_mode = p_mode[:]

        if not data[0] == 3:
            for i in range(1, len(p_mode)):
                if p_mode[i-1] == "0":
                    input_position_1 = int(arr[current_position + i])
                    data.append(int(arr[input_position_1]))
                elif p_mode[i-1] == "1":
                    data.append(int(arr[current_position + i]))

            input_position_1 = int(arr[current_position + 3])
            data.append(int(arr[input_position_1]))

        else:
            input_position_1 = int(arr[current_position + 1])
            data.append(int(arr[input_position_1]))

        if data[0] == 3:
            temp = data[1]
            data[1] = 1
            data.append(temp)
        return data

    def operate_on_data(self, data):
        print("Data: {}".format(data))
        if data[0] == 1:
            self.input[data[3]] = data[1] + data[2]
        elif data[0] == 2:
            self.input[data[3]] = data[1] * data[2]
        elif data[0] == 3:
            self.input[data[2]] = data[1]
        elif data[0] == 4:
            print(data[1])
        elif data[0] == 99:
            return False
        else:
            print("{}: Something went wrong... Invalid Intcode".format(data[0]))
        return True


computer = Computer()
computer.process_input()
