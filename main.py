"""The Postmortem That Made Us Laugh entry: writes one short account to /output/entry.txt."""
import os

ENTRY = "We traced the outage to a single typo, which HR has now promoted to senior engineer for its impact."

def main():
    out = "/output/entry.txt"
    try:
        os.makedirs("/output", exist_ok=True)
        path = out
    except OSError:
        os.makedirs("./output", exist_ok=True)
        path = "./output/entry.txt"
    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write(ENTRY)
    except OSError:
        os.makedirs("./output", exist_ok=True)
        with open("./output/entry.txt", "w", encoding="utf-8") as f:
            f.write(ENTRY)

if __name__ == "__main__":
    main()
