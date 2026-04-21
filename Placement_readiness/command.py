import argparse

def main():
    parser = argparse.ArgumentParser(description= "CLI for Job Readiness Analytics Engine")

    parser.add_argument("command" , choices= ["train" , "run" , "report"] , help="Command to execute: train, run, or report")
    args = parser.parse_args()
    if args.command == "train":
        pass
    elif args.command == "run":
        pass
    elif args.command == "report":
        pass
