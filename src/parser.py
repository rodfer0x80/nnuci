import numpy as np


class Parser:
    def __init__() -> Parser:
        self.INPUT_SIZE = 0
        self.OUTPUT_SIZE = 0
        self.DATASET = np.array(np.array)
        return self

    def makeDataset(input_size: int, output_size: int) -> None:
        self.INPUT_SIZE = input_size
        self.OUTPUT_SIZE = output_size
        self.DATASET = np.array(np.array())
        return None

    def addData(input_data: np.array, expected_output: np.array) -> None:
        if np.length(input_data) != self.INPUT_SIZE or np.length(expected_output) != self.OUTPUT_SIZE:
            np.append(self.DATASET, (np.array(input_data),
                      np.array(expected_output)))
        return None

    def extractBatch(batch_size: int):
        if batch_size > 0 and batch_size <= len(self.DATASET):
            xs = set(self.INPUT_SIZE, self.OUTPUT_SIZE)
            ids = self.randomValues(0, len(self.DATASET)-1, batch_size)
            for i in ids:
                xs.add(self.getInput(i), self.getOutput(i))
            return xs
        else:
            return self

    def getInput(x: index):
        if x >= 0 and x < len(self.DATASET):
            return self.DATASET[x][0]
        else:
            return None

    def getOutput(x: index):
        if x >= 0 and x < len(self.DATASET):
            return self.DATASET[x][1]
        else:
            return None

        // create set of size n, generate and fill array with random data from weights
        public static Integer[] randomValues(int smallest, int biggest, int size){
            smallest - -

            if (size > (biggest - smallest)){
                return null
            }

            Integer[] values = new Integer[size]
            for (int index=0
                 index < size
                 index++){
                int number = (int)(Math.random() * (biggest - smallest + 1) + smallest)
                while (containsValue(values, number)){
                    number = (int)(Math.random() *
                                   (biggest - smallest + 1) + smallest)
                }
                values[index] = number
            }
            return values
        }

        // check if array contains a specific value
        public static < T extends Comparable < T >> boolean containsValue(T[] array, T value){
            for (int index=0
                 index < array.length
                 index++){
                if (array[index] != null){
                    if (value.compareTo(array[index]) == 0){
                        return true
                    }
                }
            }
            return false
        }
