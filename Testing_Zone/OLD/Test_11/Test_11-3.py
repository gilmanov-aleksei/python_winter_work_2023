#! /usr/bin/python

string = "axR.456 987-456-3456 xdfs.4567 3456-234-2345 R45.d78 23.xuh 987-234-9845 987-234-9sd5 A178BC98 A783BC198"
import re

print(re.findall(r"\b\w\w\w[.]\w\w\w\b", string))
print(re.findall(r"\b\d\d\d-\d\d\d-\d\d\d\d\b", string))
print(re.findall(r"\b\d{3}-\d{3}-\d{4}", string))
print(re.findall(r"\b[A-Z]\d{3}[A-Z]{2}\d{2,3}\b", string))
print(re.findall(r"\b[A-Z]\d{3}[A-Z]{2}1?[7,9]8\b", string))
