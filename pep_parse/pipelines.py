import csv
from collections import defaultdict
import datetime as dt
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

class PepParsePipeline:
    def open_spider(self, spider):
        self.peps = defaultdict(int)
        self.results_dir = BASE_DIR / 'results'
        self.results_dir.mkdir(exist_ok=True)
    
    def process_item(self, item, spider):
        self.status = item['status']
        self.peps[self.status] += 1
        return item
    
    def close_spider(self, spider):
        current_time = dt.datetime.now()
        time = current_time.strftime('%Y-%m-%d_%H-%M-%S')
        file_name = f'status_summary_{time}.csv'
        file_path = self.results_dir / file_name
        result = self.peps.items()
        total = sum(self.peps.values())
        with open(file_path, 'w', encoding='utf-8') as f:
            f.writelines([
                'Статус, Количество\n',
                *[f'{status}, {amount}\n' for status, amount in result],
                f'Total, {total}\n'
            ])
