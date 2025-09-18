from statistics import *
import os


def getScores():
    if not os.path.exists("scores.txt"):
        print("File not found")
        exit(1)

    with open("scores.txt", "r") as file:
        scores = file.read().split(",")

        try:
            scores = [float(score.strip()) for score in scores]
            if not scores:
                print("No scores found")
                exit(1)
            return scores  # Added return statement
        except ValueError:
            print("Invalid format")
            exit(1)


def printReport(scores):
    with open("report.txt", "w") as report:
        report.write("---CLASS REPORT---\n")
        report.write(f"Mean: {mean(scores)}\n")
        report.write(f"Median: {median(scores)}\n")
        report.write(f"Mode: {mode(scores)}\n")
        print("Report generated successfully in report.txt")


if __name__ == "__main__":
    scores = getScores()
    printReport(scores)
