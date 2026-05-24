from abc import ABC, abstractmethod
from typing import Any, Protocol


class DataProcessor(ABC):
    def __init__(self) -> None:
        self.storage: list[tuple[int, str]] = []
        self.rank = 0
        self.total_processed = 0

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
                self.storage.append((self.rank, item))
                self.rank += 1
                self.total_processed += 1

        else:
            self.storage.append((self.rank, str(data)))
            self.rank += 1
            self.total_processed += 1

    def output(self) -> tuple:
        return super().output()


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
        if (isinstance(data, list)):
            for item in data:
                self.storage.append((self.rank, item))
                self.rank += 1
                self.total_processed += 1

        else:
            self.storage.append((self.rank, str(data)))
            self.rank += 1
            self.total_processed += 1

    def output(self) -> tuple:
        return super().output()


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
                self.total_processed += 1

        else:
            self.storage.append((self.rank, data))
            self.rank += 1

    def output(self) -> tuple:
        return super().output()


class ExportPlugin(Protocol):
    def process_output(self, data: list[str]) -> None:
        pass


class CSVExportPlugin:
    def process_output(
        self,
        data: list[str]
    ) -> None:

        print("CSV Output:")
        print(",".join(data))


class JSONExportPlugin:
    def process_output(self, data: list[str]) -> None:
        print("JSON Output:")
        json_str = "{"
        start_index = 3

        for i, value in enumerate(data):
            key = f'"item_{start_index + i}"'
            val = f'"{value}"'
            json_str += f"{key}: {val}"
            if i != len(data) - 1:
                json_str += ", "
        json_str += "}"
        print(json_str)


class DataStream:
    def __init__(self) -> None:
        self.processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for item in stream:
            processed = False

            for proc in self.processors:
                if proc.validate(item):
                    proc.ingest(item)
                    processed = True
                    break

            if not processed:
                print("DataStream error - "
                      f"Can't process element in stream: {item}")

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if len(self.processors) > 0:
            for proc in self.processors:
                name = type(proc).__name__
                count = len(proc.storage)
                print(
                    f"{name}: "
                    f"total {proc.total_processed} items in processor, ",
                    f"remaining {count} on processor")
        else:
            print("No processor found, no data")

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for proc in self.processors:
            exported_data: list[str] = []
            count = 0
            while proc.storage and count < nb:
                rank, value = proc.output()
                if isinstance(value, dict):
                    formatted = (
                        f"{value['log_level']}: "
                        f"{value['log_message']}"
                    )
                    exported_data.append(formatted)

                else:
                    exported_data.append(str(value))
                count += 1

            if exported_data:
                plugin.process_output(exported_data)


if __name__ == "__main__":
    print("=== Code Nexus - Data Pipeline ===\n")

    print("Initialize Data Stream...")
    a = DataStream()
    a.print_processors_stats()
    print("")
    print("Registering Processors")
    a.register_processor(NumericProcessor())
    a.register_processor(TextProcessor())
    a.register_processor(LogProcessor())
    print("")
    first_set = [
        'Hello world',
        [3.14, -1, 2.71],
        [
            {
                'log_level': 'WARNING',
                'log_message': 'Telnet access! Use ssh instead',
            },
            {
                'log_level': 'INFO',
                'log_message': 'User wil is connected',
            },
        ],
        42,
        ['Hi', 'five'],
    ]
    print(f"Send first batch of data on stream: {first_set}")
    a.process_stream(first_set)
    a.print_processors_stats()
    print("")
    print("Send 3 processed data from each processor to a CSV plugin:")
    csv_plugin = CSVExportPlugin()
    a.output_pipeline(3, csv_plugin)

    print()
    a.print_processors_stats()

    second_set = [
        21,
        ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
        [{'log_level': 'ERROR', 'log_message': '500 server crash'},
            {
                'log_level': 'NOTICE',
                'log_message': 'Certificate expires in 10 days'
            }],
        [32, 42, 64, 84, 128, 168], 'World hello']

    a.process_stream(second_set)
    a.print_processors_stats()
    print()
    print("Send 5 processed data from each processor to a JSON plugin:")
    json_plugin = JSONExportPlugin()
    a.output_pipeline(5, json_plugin)
    print()
    a.print_processors_stats()
