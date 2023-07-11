# Conway's Game Of Life
Implementation of Conway's Game Of Life in Python with PyGame module.

## How to play
Dependencies:
- Python 3.xx
- pygame module (pip install pygame)

Run "main.py", and the game should start.

![Game_Of_Life](https://github.com/gabbobersi/Conway_game_of_life/assets/65022671/6018a1a1-4013-47a6-8d2e-ce1dd4331897)
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
- **Counters** (*WIP*): (they counter per single generation!)
  - RED team live cells counter
  - RED team dead cells counter
  - RED team born cells counter
 
## BugFixes
- [ ] Blue team cells can "eat" red team cells.
  - The rule is that if a cell has a different color from "me", counts as a "dead" cell.

## TODO Features
- [ ] Change Team.get_opposite_team into Team.get_opposite_color
- [ ] Add a 'Main menu' button in 'play' mode
- [ ] Implement 'options' menu
  - [ ] Change grid resolution
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
