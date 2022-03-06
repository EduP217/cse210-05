## Project
CYCLE - rfk

## Description
Cycle is a game where the players try to cut each other off using cycles that leave a trail behind them.

## Project Structure
---
The project files and folders are organized as follows:
```
root                              (project root folder)
+-- elements                      (specific element classes)
  +-- entity.py                   (class that hold the basic input of the object used in the program)
  +-- collection.py               (class that contains multiple entities)
  +-- snake.py                    (class that inheritance from entity to extend the basic usage, also apply polymorphism to override basic methods)
  +-- score.py                    (class that inheritance from entity to extend the basic usage)
+-- services                      (specific services classes)
  +-- keyboard_service.py         (manage the pyray keyboard events detection)
  +-- video_service.py            (manage the pyray windows events executions)
+-- utils                         (specific utils classes)
  +-- color.py                    (manage the pyray colors)
  +-- point.py                    (manage the pyray pixels positions)
+-- scripting                     (specific scripting classes)
  +-- script.py                   (class that hold all the actions of elements in the window program)
  +-- action.py                   (class that hold basic methods of elements events)
  +-- keyboard_action.py          (manage keyboard service actions, applies polymorphism to action class)
  +-- video_action.py             (manage video service actions, applies polymorphism to action class)
  +-- entity_action.py            (manage entity actions, applies polymorphism to action class)
  +-- game_action.py              (manage game actions, applies polymorphism to action class)
+-- __main__.py                   (class to initialize data for the program)
+-- screen.py                     (class to execute the program)
+-- README.md                     (general info)
```

## Required Technologies
---
* Python 3.8.0
* Raylib Python CFFI 3.7

## Authors
---
* # TODO: Add your name and email here

* Yurinii Fuentes  fue21007@byui.edu 
* Eduardo Prieto  pri21002@byui.edu

## Design
---

* Yurinii Fuentes
  - Implement the basic structure:
    - entity.py
    - collection.py
    - score.py
    - keyboard_service.py
    - action.py
    - keyboard_action.py
    - entity_action.py
    - utils/*
* Eduardo Prieto
  - Implement the configuration structure:
    - __main__.py
    - snake.py
    - video_service.py
    - script.py
    - action.py
    - video_action.py
    - game_action.py
    - screen.py
