import csv


def create_csv_file(sentences, prompts, csv_path):
    with open(csv_path, "w", newline="") as file:
        writer = csv.writer(file)
        # Write the header row
        writer.writerow(["Number", "Sentence", "Prompt", "Image Link"])

        for index, (sentence, prompt) in enumerate(zip(sentences, prompts), 1):
            writer.writerow([index, sentence, prompt])

    return True
