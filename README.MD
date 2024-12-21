Concurrent Wikipedia Article Word Counter

Overview

The Concurrent Wikipedia Article Word Counter is a Python program that processes multiple Wikipedia articles concurrently. It downloads the content of articles, counts the total number of words in each, and writes the results to a file in the format:


<Wikipedia Article URL>, <Word Count>



The program follow multiple ways demostration there.



Features

• Dynamic Input: Accepts a list of Wikipedia article URLs from the user at runtime.

• Concurrency: Processes multiple URLs simultaneously using a configurable number of workers.

• Error Handling: Logs errors for invalid URLs, network issues, or empty article content.

• Logging: Provides detailed logs for the start, success, and failure of URL processing.

• Output: Writes the results to results.txt with each URL and its word count.


How to Run

1. Clone this repository or download the script.

2. Run the script in your terminal:



python main.py



Replace main.py with the name of the Python script file.



3. Enter the Wikipedia URLs when prompted, separated by commas. Example:



Enter Wikipedia URLs (comma-separated):

>> https://en.wikipedia.org/wiki/Python_(programming_language), https://en.wikipedia.org/wiki/Concurrency_(computer_science)





4. Once processing is complete, check the results in the results.txt file.



File Structure

• script_name.py: The main Python script for the program.

• results.txt: The output file containing URLs and word counts.



Configuration



Concurrency Level



The number of concurrent workers (default: 3) can be adjusted by modifying the n_workers parameter in the ConcurrentProcessor class:



processor = ConcurrentProcessor(n_workers=5)  # Change 5 to your desired number



Sample Output



Input



Enter Wikipedia URLs (comma-separated):

>> https://en.wikipedia.org/wiki/Python_(programming_language), https://en.wikipedia.org/wiki/Concurrency_(computer_science), https://en.wikipedia.org/wiki/Artificial_intelligence



Output in results.txt



https://en.wikipedia.org/wiki/Python_(programming_language), 5637

https://en.wikipedia.org/wiki/Concurrency_(computer_science), 4871

https://en.wikipedia.org/wiki/Artificial_intelligence, 7203



Log Output



2024-12-21 14:25:01 - INFO - Starting download: https://en.wikipedia.org/wiki/Python_(programming_language)

2024-12-21 14:25:02 - INFO - Finished https://en.wikipedia.org/wiki/Python_(programming_language) with word count: 5637

2024-12-21 14:25:02 - INFO - Starting download: https://en.wikipedia.org/wiki/Concurrency_(computer_science)

2024-12-21 14:25:03 - INFO - Finished https://en.wikipedia.org/wiki/Concurrency_(computer_science) with word count: 4871

2024-12-21 14:25:03 - INFO - Starting download: https://en.wikipedia.org/wiki/Artificial_intelligence

2024-12-21 14:25:04 - INFO - Finished https://en.wikipedia.org/wiki/Artificial_intelligence with word count: 7203



Error Handling

• Invalid URLs or network errors are logged, and the word count is recorded as 0 in the output file.

• Example of an invalid URL entry in results.txt:



https://invalid-url-example.com, 0



Customization



Input Method



To hardcode URLs instead of taking user input, replace:



user_input = input(">> ")



with a predefined list of URLs:



wikipedia_urls = [

    "https://en.wikipedia.org/wiki/Python_(programming_language)",

    "https://en.wikipedia.org/wiki/Concurrency_(computer_science)"

]



License



This project is released under the MIT License.



Acknowledgments

• Wikipedia articles were used as the data source for testing.

• Developed using Python’s concurrent.futures library for parallel processing.

