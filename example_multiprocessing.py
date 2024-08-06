from multiprocessing import Pool

def hello(task):
    print(f"Hello {task}")

def main():
    tasks = range(10)

    with Pool() as pool:
        print(f"Multiprocessing with {pool._processes} workers")

        # Process each task, don't care about ordering
        it = pool.imap_unordered(hello, tasks)

        for result in it:
            # Make sure results are processed
            pass
        

if __name__ == '__main__':
    main()
