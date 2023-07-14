# Conway's Game Of Life
Implementation of Conway's Game Of Life in Python with PyGame module.

## How to play
If dependencies are met, just run "main.py", and the game should start.
### Controls
- **Left mouse button**: place a cell
- **Right mouse button**: remove a cell
- **Space**: start/stop the game
- **R**: like pressing the "Random" button

![Game_Of_Life](https://github.com/gabbobersi/Conway_game_of_life/assets/65022671/6018a1a1-4013-47a6-8d2e-ce1dd4331897)

## Dependencies
- Python 3.xx
- pygame module (pip install pygame)

## Implemented features
- **Main menu** (*WIP*):
  - play
  - options _WIP_
  - quit _WIP_
- **Activate**
  - start Game Of Life.
- **Stop**:
  - stop the game at any time.
- **Random**:
  - generates a random number of "live" cells in random positions.
- **Clear**:
  - clears the grid.
- **Invasion** (*WIP*):
  - generates in random position, a random number of "live" cells of the opposite teams.
- **Counters** (*WIP*): (they count per single generation!)
  - RED team live cells counter
  - RED team dead cells counter
  - RED team born cells counter
 
## BugFixes
- [ ] Blue team cells can "eat" red team cells.
  - The rule is that if a cell has a different color from "me", counts as a "dead" cell.

## TODO Features
- [X] Change Team.get_opposite_team into Team.get_opposite_color
- [X] Clarify "is_clicked" method of Button class (the mouse is over the btn here, and not clicked).
- [X] Add a 'Main menu' button in 'play' mode
- [ ] Implement 'options' menu
  - [ ] Change grid resolution
    - Micro
    - Standard (default)
    - Huge
  - [ ] Change player color
  - [ ] Change game's speed
- [ ] Create a toolbar with all the buttons
  - [ ] Make labels clear
  - [ ] Make the area of the toolbar + area of the labels "dead" as window's borders.
- [ ] Add a little animation for the main menu
- [ ] "Beautify" main menu
- [ ] Online Multiplayer
  - [ ] Server side
  - [ ] Client side
  - [ ] Hidden layer (queue of actions)
  - [ ] Draw mode with limited resources per team 

## Background
I was searching for a project with fast implementation, quick visual feedback and a lot of room for improvement.  
Here some resources I used:
- [Wikipedia](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)
- [YouTube Numberphile](https://www.youtube.com/watch?v=R9Plq-D1gEk&ab_channel=Numberphile)
- [YouTube Alan Zucconi](https://www.youtube.com/watch?v=Kk2MH9O4pXY&t=284s&ab_channel=AlanZucconi)
