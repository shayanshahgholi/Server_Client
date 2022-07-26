from concurrent.futures import ThreadPoolExecutor

values = [x for x in range(10)]


def square(number):
   return number * number


def main():
    with ThreadPoolExecutor(max_workers = 20) as executor:
        results = executor.map(square, values)
        for result in results:
            print(result)

if __name__ == '__main__':
   main()