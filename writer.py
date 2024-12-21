class ResultWriter:
    def write_to_file(results, filename='result.txt'):
        """
        Write the results to a file.
        """

        with open(filename, "w") as f:
            for url, count in results:
                f.write(f'{url}, {count}\n')
            

