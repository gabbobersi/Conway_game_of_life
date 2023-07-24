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
- **Dynamic Toolbar**
  - Can be set on 'top' or on 'side' of the screen. 
 
## BugFixes
- [x] Label's text position change based on current text's length.
  - Label shoudl be in a fixed position, not based on current text's lenght.
- [ ] Blue team cells can "eat" red team cells.
  - The rule is that if a cell has a different color from "me", counts as a "dead" cell.
- [ ] Area under the toolbar should be considered "dead", like out of screen.

## TODO Features
- [x] Change Team.get_opposite_team into Team.get_opposite_color
- [x] Clarify "is_clicked" method of Button class (the mouse is over the btn here, and not clicked).
- [x] Add a 'Main menu' button in 'play' mode
- [x] Implement 'options' menu
  - [x] Change toolbar position
  - [ ] Change grid resolution
  - [ ] Change player color
  - [ ] Change game's speed
- [x] Create a toolbar with all the buttons
  - [x] Make labels clear
  - [ ] Make the area of the toolbar + area of the labels "dead" as window's borders.
- [ ] Add a little animation for the main menu
- [ ] "Beautify" main menu
- [ ] Online Multiplayer
  - [ ] Server side
  - [ ] Client side
  - [ ] Hidden layer (queue of actions)
  - [ ] Draw mode with limited resources per team 
## Enginering tradeoffs
- **More iterations on the grid:**
  - Positive: code is more organized and maintainable.
  - Negative: in grid.py module, different methods require different iterations on the same matrix (which is the grid, listxlist).
- **Factory patterns:**
  - Positive: More abstraction means less lines of code, since I don't have to use if/else to correct the flow of the instances generation.
  - Negative: More abstraction means more documentation needs and more probability of using the wrong implementation (eg Using directly the class instead of the factory).
