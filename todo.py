#!/usr/bin/env python3
import argparse
import os
import pdb
file_name = "task.txt"
parser=argparse.ArgumentParser(description="To create/modify/delete a Todo List")
parser.add_argument("-a", "--add", help="To add a task to Todo List")
parser.add_argument("-l", "--list", help="Displays the tasks in Todo List", action="store_true")
parser.add_argument("-v", "--version", help="Displays version of Todo App utility", action="store_true")
parser.add_argument("-t", "--tag", help="To add tags to the tasks")
#parser.add_argument("-u", "update", help="Update existing task")
parser.add_argument("-d", "--delete", help="Delete the task whose number is specified")

args = parser.parse_args()
lines = 0
if(args.add):
    #with open(file_name, "r+") as f:
        #lines = sum(1 for _ in f)
    with open(file_name, "a+") as f:
        #f.write("Task {}: {}".format((lines+1),args.add)+"\n")
        f.write(args.add+"\n")
if args.list:
    with open(file_name, "r") as f:
        print(f.read())
if args.version:
    print("Todo App: Version 0.0.1")
if args.delete:
    #task_num = args.delete
    #with open(file_name, "r") as f:
    #    lines = f.readlines()
    #with open(file_name, "w") as f:
    #    for line in lines:
    #        if(line != args.delete):
    #            f.write(line+"\n")
    f = open(file_name,"r+")
    d = f.readlines()
    f.seek(0)
#    pdb.set_trace()
    for i in d:
        if i != args.delete:
            print(type(i))
            print(type(args.delete))
            f.write(i)
    f.truncate()
    f.close()
