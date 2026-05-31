from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self) -> None:
        self.storage: list[tuple[int, str]] = []
        self.rank = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self.storage:
            raise IndexError("No data available")
        return self.storage.pop(0)


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        if (isinstance(data, int | float)):
            return True

        if isinstance(data, list):
            return (all(isinstance(x, int | float) for x in data))

        return False

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise TypeError("Improper numeric data")
        if isinstance(data, list):
            for item in data:
                self.storage.append((self.rank, str(item)))
                self.rank += 1

        else:
            self.storage.append((self.rank, str(data)))
            self.rank += 1


class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        if (isinstance(data, str)):
            return True

        if isinstance(data, list):
            return (all(isinstance(x, str) for x in data))

        return False

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise TypeError("Improper data")
        if isinstance(data, list):
            for item in data:
                self.storage.append((self.rank, item))
                self.rank += 1

        else:
            self.storage.append((self.rank, str(data)))
            self.rank += 1


class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        if (isinstance(data, dict)):
            return (all(
                        isinstance(k, str) and isinstance(v, str)
                        for k, v in data.items()
                        ))

        if isinstance(data, list):
            return all(self.validate(item) for item in data)

        return False

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise TypeError("Improper data")
        if isinstance(data, list):
            for item in data:
                self.storage.append((self.rank, item))
                self.rank += 1

        else:
            self.storage.append((self.rank, data))
            self.rank += 1


if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===\n")

    a = NumericProcessor()
    first = 42
    second = "Hello"
    print("Testing Numeric Processor...")
    print("Trying to validate input '42':", a.validate(first))
    print("Trying to validate input 'Hello':", a.validate(second))
    foo = "M"
    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        a.ingest(foo)
    except TypeError as e:
        print("Got exception:", e)

    third = [1, 2, 3, 4, 5]
    print(f"Processing data: {third}")
    """a.validate(third)"""
    a.ingest(third)
    print("Extracting 3 values...")
    for i in range(3):
        rank, value = a.output()
        print(f"Numeric value {rank}: {value}")

    print("\nTesting Text Processor...")
    b = TextProcessor()
    sec = ['Hello', 'Nexus', 'World']
    print("Trying to validate input '42':", b.validate(first))
    print(f"Processing data: {sec}")
    b.validate(sec)
    b.ingest(sec)
    print("Extracting 1 value...")
    rank, value = b.output()
    print(f"Text value {rank}: {value}")

    print("\nTesting Log Processor...")
    c = LogProcessor()
    print("Trying to validate input 'Hello':", c.validate(second))
    lst = [
            {'log_level': 'NOTICE', 'log_message': 'Connection to server'},
            {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}
            ]
    print("Processing data:", lst)
    print("Extracting 2 values...")
    c.ingest(lst)
    for i in range(2):
        rank, value = c.output()
        print(f"Log entry {i}: {value}")
