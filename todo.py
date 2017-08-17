#!/usr/bin/env python3
import argparse
file_name = "task.txt"
parser=argparse.ArgumentParser(description="To create/modify/delete a Todo List")
parser.add_argument("-a", "--add", help="To add a task to Todo List")
parser.add_argument("-l", "--list", help="Displays the tasks in Todo List", action="store_true")
parser.add_argument("-v", "--version", help="Displays version of Todo App utility", action="store_true")
parser.add_argument("-t", "--tag", help="To add tags to the tasks")

args = parser.parse_args()

with open(file_name, "a") as f:
    if(args.add):
        f.write(args.add+"\n")
if args.list:
    with open(file_name, "r") as f:
        print(f.read())
if args.version:
    print("Todo App: Version 0.0.1") 
