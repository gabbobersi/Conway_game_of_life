These are some notes I took while developing this project.
They may not represent the current state of the project.

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