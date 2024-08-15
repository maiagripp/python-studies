def merge_sorted_files(odds_file, evens_file, output_file):
    with open(odds_file, 'r') as f:
        odds = [int(line.strip()) for line in f.readlines()]

    with open(evens_file, 'r') as f:
        evens = [int(line.strip()) for line in f.readlines()]
    
    all_numbers = sorted(odds + evens)
    
    with open(output_file, 'w') as f:
        for number in all_numbers:
            f.write(f"{number}\n")

merge_sorted_files('odds.txt', 'evens.txt', 'numbers.txt')

