import csv


def create_csv_file(sentences, prompts, image_links, csv_path):
    with open(csv_path, "w", newline="") as file:
        writer = csv.writer(file)
        # Write the header row
        writer.writerow(["Number", "Sentence", "Prompt", "Image Link"])

        for index, (sentence, prompt, image_link) in enumerate(zip(sentences, prompts, image_links), 1):
            writer.writerow([index, sentence, prompt, image_link])

    return True
