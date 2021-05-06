import json
import hashlib


class CountryIterator:
    def __init__(self, path:str):
        self.file = open(path)
        self.a = json.load(self.file)

    def __iter__(self):
        self.i = 0
        self.country_count = len(self.a)
        return self

    def write_file(self, country_name:str):
        url = f"https://en.wikipedia.org/wiki/{country_name.replace(' ', '_')}"
        with open('result.log', 'a', encoding='utf-8') as f:
            f.write(f"{country_name} {url}")
            f.write('\n')

    def __next__(self):
        if self.i < self.country_count:
            country_name = self.a[self.i]['name']['common']
            self.i += 1
            return country_name
        else:
            raise StopIteration


def md5_for_every_line(path: str):
    with open(path,'rb') as f:
        for line in f:
            hash = hashlib.md5(line)
            yield hash.hexdigest()


if __name__ == '__main__':
    country_iterator = CountryIterator('countries.json')
    for country in country_iterator:
        country_iterator.write_file(country)

    for md5 in md5_for_every_line('result.log'):
        print(md5)
