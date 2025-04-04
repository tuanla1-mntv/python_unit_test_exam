import csv

from .base_exporter import BaseExporter


class CSVExporter(BaseExporter):

    def export(data, savedir: str, *args, **kwargs) -> None:
        try:
            with open(savedir, "w", newline="") as file_handler:
                writer = csv.writer(file_handler)
                columns = kwargs.get("columns", [])

                if columns:
                    writer.writerow(columns)

                for row in data:
                    writer.writerow(row)

        except IOError as e:
            raise IOError(f"Failed to export order to CSV: {e}")
