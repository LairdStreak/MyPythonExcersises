#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

def main():
    person_dict = {"name": "Bob",
    "languages": ["English", "Fench"],
    "married": True,
    "age": 32
    }

    with open('person.txt', 'w') as json_file:
        json.dump(person_dict, json_file)

    print('Done')

if __name__ == '__main__':
    main()          