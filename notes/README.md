These are some notes I took while developing this project.
They may not represent the current state of the project.

## Implemented features
- **Home scene**:
  - play
  - options
  - quit
- **Play scene**
  - Activate: start Game Of Life.
  - Stop: stop the game at any time.
  - Random: generates a random number of "live" cells in random positions.
  - Clear: clears the grid.
  - Invasion: generates in random position, a random number of "live" cells of the opposite teams.
  - Informative counters:
    - All teams live cells counter
    - All teams dead cells counter
    - All teams born cells counter
- **Options scene**
  - Change toolbar position
  - Change resolution
  - Change player color
  - Change game speed
- **Quit scene**
  - Correctly quit pygame and system process.  
## BugFixes
- [x] Label's text position change based on current text's length.
  - Label shoudl be in a fixed position, not based on current text's lenght.
- [x] Blue team cells can "eat" red team cells.
  - The rule is that if a cell has a different color from "me", counts as a "dead" cell.
  - **Solution:** Since it is an "invasion", this will be maintained as a feature.
- [ ] Area under the toolbar should be considered "dead", like out of screen.
## TODO Features / QOL improvements
- buttons
  - [x] Clarify "is_clicked" method of Button class (the mouse is over the btn here, and not clicked).
  - [ ] Add a feedback effect to signal "mouse over button".
  - [ ] Add a feedback effect to signal "button clicked". 
- home scene
  - [ ] "Beautify"
    - [ ] Add a little animation
- play scene
  - [x] Add a 'Main menu' button in 'play' mode
  - [ ] Remove Stop button. Make Activate a switch button between playing and drawing modes.
  - [ ] Add a 'Patterns picker' for draw an existent working pattern (so you could potentially use only cool patterns to see their function).
- options scene
  - [x] Change toolbar position
  - [x] Change grid resolution
  - [x] Change player color
  - [x] Change game's speed
- QOL
  - [x] Change Team.get_opposite_team into Team.get_opposite_color.
  - [ ] Improve grid logic to prevent multiple iterations over the same matrix.
  - [ ] Replace matrices and lists creation with Numpy.
- toolbar
  - [x] Make labels clear (choose a visible font)
  - [ ] Make the area of the toolbar + area of the labels "dead" as window's borders.
- [x] Create a UI manager that, based on the current resolution, places the UI elements in the right position.
- [ ] Online Multiplayer
  - [ ] Server side
  - [ ] Client side
  - [ ] Hidden layer (queue of actions)
  - [ ] Draw mode with limited resources per team 
## Engineering tradeoffs
- **More iterations on the grid:**
  - Note: Matrices operations will be ported to Numpy in the future (they represents an obvious bottle-neck).
  - Positive: code is more organized and maintainable.
  - Negative: in grid.py module, different methods require different iterations on the same matrix (which is the grid, listxlist).
- **Factory patterns:**
  - Positive: More abstraction means less lines of code, since I don't have to use if/else to correct the flow of the instances generation.
  - Negative: More abstraction means more need for documentation and more likely to use the wrong implementation (e.g. Using directly the class instead of the factory).
- **Inheritance mixed with composition**:
  - Note: Is clear that UI elements follow the inheritance model pattern well, but is this the best choice?
  To put maintainability and readability as priority, as Gang Of Four also suggests, I decided to implement both. 
  - Positive: maintainability, readability, less lines of code.
  - Negative: different patterns for different UI elements.
- **Oversharing Options object**:
  - Positive: everywhere in the code, I can access the options object and change its values.
  - Negative: Options object will have too many responsibilities.

## Historical screens
(until july 2023)
![Game_Of_Life](https://github.com/gabbobersi/Conway_game_of_life/assets/65022671/6018a1a1-4013-47a6-8d2e-ce1dd4331897)
