from datetime import datetime

def count_letters_in_range(file_name, start_date, end_date):
    try:
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
        count = 0

        with open(file_name, 'r') as file:
            for line in file:
                date_str, _ = line.strip().split(',', 1)

                letter_date = datetime.strptime(date_str, "%Y-%m-%d")

                if start_date <= letter_date <= end_date:
                    count += 1

        return count

    except FileNotFoundError:
        return f"Error: The file '{file_name}' does not exist."
    except ValueError as e:
        return f"Error processing the file: {e}"

if __name__ == "__main__":
    sample_file_name = "surat.txt"
    with open(sample_file_name, 'w') as file:
        file.write("2024-01-01,Terima kasih telah menjaga pohon kami.\n")
        file.write("2024-01-02,Bantuanmu membuat ladang subur kembali.\n")
        file.write("2024-01-05,Jangan lupa menjaga akar pohon besar.\n")
        file.write("2024-01-10,Angin musim dingin mulai tiba di hutan kami.\n")

    # Inputs for testing
    test_file_name = "surat.txt"
    test_start_date = "2024-01-01"
    test_end_date = "2024-01-05"

    # Call the function and print the result
    result = count_letters_in_range(test_file_name, test_start_date, test_end_date)
    print(result)
