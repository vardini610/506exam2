# SI 506 Practice Exam 02

## Background

This practice exam is structured as a problem set. The problem set comprises eight (`8`)
problems that focus on working with nested list of dictionaries.

The exercise involves writing a small program/script that explores player and team shooting
performance during the 2023 FIFA Women's World Cup ⚽ hosted by Australia 🇦🇺 and New Zealand 🇳🇿.
Thirty-two (`32`) teams competed in the tournament with Spain 🇪🇸 emerging as the champion.

Your small program/script will surface a number of insights regarding player and team shooting
performance during the 2023 Women's World Cup. The program features a number of functions including
a `main()` function. You will be reading data into your program from a data file (described below).

:exclamation: Team 506 recommends strongly that you complete each problem in the order
specified in this README document.

## Data

The data was sourced from [FBREF](https://fbref.com/en/). Before commencing the problem set, review
the data file. Note how the data is structured.

:exclamation: Place the data file in the same directory as the README and template `*.py` file.

| File | Source | Description |
| :--- | :----- | :---------- |
| `data-2023-fifa_wwc-players.json` | [FBREF](https://fbref.com/en/comps/106/shooting/Womens-World-Cup-Stats) | Player Shooting 2023 FIFA Women's World Cup. |

## 1.0 Problem 01 (4 bonus points)

__Task__: Access data in a JSON file. Implement the function `thin_player()` to edit down the player
dictionaries to only include the "columns" required for this analysis.

1. In the `main()` function, instantiate an instance of `Path` by passing to it a string that
   represents the name of the data file (e.g., `"< file_name >.< file extension >"`). As you
   instantiate the `Path` object, call its `absolute()` _or_ `resolve()` method to render the path
   absolute. Assign a variable named `filepath` to the `Path` object.

2. Call the function `read_json()` and pass it the required argument `filepath`. Assign a variable
   named `players` to the return value.

3. Implement the function `thin_player()`. Review the function's docstring regarding its expected
   behavior, parameters, and return value.

   __Requirements__

   1. Create an empty dictionary that will become the new player dictionary that you _must_ return.

   2. Next, loop through both the **keys and values** of the `player` dictionary using the appropriate
      dictionary method.

   3. For each key-value pair, check if the key is **in** the `keep_keys` list. If it is, add the
      key and value to the new dictionary.

   4. Outside the loop, return the new dictionary that was created.

4. After implementing `thin_player()`, return to the `main()` function. Iterate over the `players`
   list and thin all the player dictionaries in `players`.

   __Requirements__

   1. Use a `for` loop and the loop variable `i` to iterate over a sequence of integers provided by
      the `range` type. When instantiating (i.e., creating) the `range()` instance pass it the
      `players` list length as the __stop__ argument.

   2. Within the loop block, call `thin_player()` on each player dictionary within `players` and
      assign the return value back to the `players` list in its original place.

      :bulb: When you call `thin_book()`, you _must_ pass `keep_keys` as the second argument.

      :exclamation: The code within the loop block is limited to a __single line of code__.

5. Uncomment the relevant `print()` calls and `assert` statements. Run your code. Confirm that the
   loop operation is mutating the dictionaries within the `players` list correctly.

## 2.0 Problem 02 (4 bonus points)

__Task__: Implement the functions named `format_player_position()` and `clean_squad()`.

1. Implement `format_player_position()`. Review the function's docstring regarding its expected
   behavior, parameters, and return value.

   __Requirements__

   1. Inside the function block call the appropriate `str` method that returns a new version of the
      passed in `position` string in which all commas (",") have been converted to pipes ("|").

   2. Return the new version of the string directly to the caller _without_ first assigning it to a
      local variable.

   3. The function block that you implement is limited to __a single line of code__.

2. After implementing the function return to the `main()` function. Uncomment the relevant
   `assert` statements, run your code, and confirm that the function behaves as expected.

3. Implement `clean_squad()`. Review the function's docstring regarding its expected behavior,
   parameters, and return value.

   __Requirements__

   1. Inside the function block create a two-item tuple literal `(< item_01, item_02 >)` comprising
      the country code and squad/country name derived from the passed in `squad` string as the
      following examples illustrate.

      __Examples__

      | `squad` argument | 2-item tuple to return |
      | :--------------- | :----------- |
      | "es Spain" | `("ES", "Spain")` |
      | "ie Rep. of Ireland" | `("IE", "Rep. of Ireland")` |

   2. Employ slicing to access the two letter country code in the string. As part of the expression
      call the appropriate `str` method to return a version of the slice converted to __upper case__
      (e.g., "ES"). Embed the expression in the tuple literal as the first item.

   3. Also employ slicing to access the squad name (e.g., "Spain"). Embed the expression in the
      tuple literal as the second item.

   4. Return the tuple directly to the caller _without_ first assigning it to a local variable. In
      other words, the function block that you implement is limited to __a single line of code__.

4. After implementing the function return to the `main()` function. Uncomment the relevant
   `assert` statements, run your code, and confirm that the function behaves as expected.

## 3.0 Problem 03 (3 bonus points)

__Task__: Loop over the `players` list, call the functions `format_player_position()` and
`clean_squad()`, and mutate each "player" dictionary with the return values provided by the
functions.

1. Loop over the `players` list, mutate each nested dictionary by assigning new "position",
   "country_code", and "squad" key-value pairs as specified below.

   __Requirements__

   1. Employ a standard `for` loop. Choose a readable loop variable name (e.g., `player`) to represent
      each nested dictionary.

   2. Inside the loop block, call the function `format_player_position()` and pass it the nested
      dictionary's "position" value as the argument. Assign the return value back to the nested
      dictionary's "position" key.

   3. Next, call the function `clean_squad()` and pass it the nested dictionary's "squad" value as the
      argument. __Unpack__ the return value and assign the return values to the nested dictionary's
      new "country_code" and existing "squad" keys.

2. Call the function `write_json()` and pass it the filepath "stu-players.json" along with
   the other arguments it requires __by position__.

3. Run your code and confirm that the file was written to the current working directory. Then
   compare the JSON file to the matching fixture file (`fxt-*.json`). If the files match proceed to
   the next problem.

   :bulb: In VS Code you can compare or "diff" the file you generate against the appropriate test
   fixture file. After calling the `write_json()` function and generating a new file do the following:

   1. Hover over your `stu-*.json` file with your cursor, then right click and choose the "Select for
      Compare" option.

   2. Next, hover over the appropriate `fxt-*.json` test fixture file, then right click and choose
      the "Compare with Selected" option.

   3. Lines highlighted in red indicate row mismatches. If any mismatches are encountered close the
      comparison pane, revise your code, regenerate your file, and compare it again to the test
      fixture file. Repeat as necessary until the files match.

   :exclamation: Your output __must__ match the test fixture file line for line and character for
   character. Review the test fixture file; they are akin to answer keys and should be utilized for
   comparison purposes as you work your way through the assignment.

## 4.0 Problem 04 (4 bonus points)

__Task__: Implement the function named `get_multi_position_players()`. Retrieve players who play
multiple positions and write the data to a JSON file.

1. Implement `get_multi_position_players()`. Review the function's docstring regarding its expected
   behavior, parameters, and return value.

   __Requirements__

   1. In the function block implement the accumulator pattern. Assign a local variable (name your
      choice) to an empty "accumulator" `list`.

   2. Employ a standard `for` loop to iterate over the passed in `players` list. Choose a readable
      loop variable name to represent each nested dictionary.

   3. Inside the loop block, access each nested dictionary's "position" value. As part of the expression,
      call the appropriate `str` method and pass to it the appropriate delimiter/separator value to
      split the string into a list. Assign a local variable to the return value (name your choice).

   4. Add an `if` statement that evaluates whether or not the "position" list includes multiple
      position elements (e.g., `["DF", "FW"]`). Perform an arithmetic comparison. If there are
      multiple elements in the "position" list __append__ the nested list representing the player to
      the accumulator list.

   5. After the loop terminates return the accumulator list to the caller.

2. Return to the `main()` function. Call the function `get_multi_position_players()` and pass it the
   `players` list. Assign a variable named `multi_position_players` to the return value.

3. Call the function `write_json()` and pass it the filepath "stu-players-multi_position.json"
   along with the other arguments it requires __by position__.

4. Run your code and confirm that the file was written to the current working directory. Then
   compare the JSON file to the matching fixture file. If the files match proceed to the next
   problem.

## 5.0 Problem 05 (4 bonus points)

__Task__: Implement the function named `get_team()`. Test the function by retrieving the Chinese
team and then write the team to a JSON file.

1. Implement `get_team()`. Review the function's docstring regarding its expected behavior,
   parameters, and return value.

   __Requirements__

   1. In the function blook, implement the accumulator pattern. Assign a local variable (name your
      choice) to an empty "accumulator" `list`.

   2. Employ a standard `for` loop to iterate over the passed in `players` list. Choose a readable
      loop variable name to represent each nested dictionary.

   3. Inside the loop block, add an `if` statement that evaluates whether or not the nested dictionary's
      "squad" value matches the passed in `squad` string. Perform a _case insensitive_ string
      comparison. If the strings match __append__ the nested dictionary representing the player to the
      accumulator list.

   4. After the loop terminates return the accumulator list to the caller.

2. Return to the `main()` function. Call the function `get_team()` and pass it the arguments
   required to return the Chinese women's national football team 🇨🇳. Assign a variable
   named `team_china` to the return value.

   :exclamation: Use VS Code's search feature to scan the `stu-players.json` file for the Chinese
   team's "Squad" name to pass as an argument. The word "China" comprises only part of the name.

3. Call the function `write_json()` and pass it the filepath "stu-team-china.json" along with
   the other arguments it requires __by position__.

4. Run your code and confirm that the file was written to the current working directory. Then
   compare the JSON file to the matching fixture file. If the files match proceed to the next
   step.

## 6.0 Problem 06 (3 bonus points)

__Task__: Implement the function named `get_top_scorer()`. Retrieve the winner(s) of the ⚽ Golden
Boot award.

1. Implement `get_top_scorer()`. Review the function's docstring regarding its expected behavior,
   parameters, and return value.

   __Requirements__

   1. In the function blook, implement the accumulator pattern. Assign a local variable (name your
      choice) to an empty "accumulator" `list`. This list will hold the top scorer(s).  Also assign
      a local variable (name your choice) to an integer (choose an appropriate value) that will
      serve as the start value for the most goals scored count.

   2. Employ a standard `for` loop to iterate over the passed in `players` list.

   3. Inside the loop block, access the "stats" value of the nested dictionary representing each player.
      Assign a local variable (name your choice) to the expression (which resolves to a dictionary).

   4. Access the "goals" value of the "stats" dictionary. Assign a local variable (name your choice)
      to the expression (which resolves to a value).

      :exclamation: Don't assume that the "goals" value you retrieve is a number. Be prepared to
      convert it to an integer.

   5. After retrieving the player's goals scored value, employ an `if-elif-else` conditional logic
      to locate the top goal scorer(s). By now, the pattern employed to identify either minimum or
      maximum values in a sequence, accounting for ties, should be familiar to you.

   6. Whenever the accumulator list includes player elements that need to be replaced by a new leading
      scorer, adjust the __existing__ accumulator list. __Do not create a new list__.

   7. This problem requires implementing a minor adjustment to the pattern. There are many World Cup
      players who did not score any goals during the tournament. The `if-elif-else` conditional logic
      must account for this possibility and filter out any players with a goal count of zero (`0`).
      Filtering out such players while continuing to evaluate those who scored one or more goals can
      be accomplished by implementing a __compound conditional statement__ that employs the appropriate
      logical operator (e.g., `and`, `or`, `not`).

      :exclamation: Both your `if` and `elif` statements _must_ evaluate __two conditions__ using
      the appropriate logical operator (e.g., `and`, `or`, `not`). In other words, the conditional
      logic _must_ exclude players who did not score as well as identify players who scored the most
      goals during the tournament.

      __`if` statement conditions__

      * Did the player score at least one goal?
      * Is the player's goal count greater than the most goals scored count?

       If `True` update the most goals scored count, remove all players added previously to the
      accumulator list (without creating a new list), and then append the current player's nested
      dictionary to the accumulator list. If `False` then evaluate the next condition.

      __`elif` statement conditions__

      * Did the player score at least one goal?
      * Is the player's goal count equal to the most goals scored count?

      If the equality comparison evaluates to `True` append the player's nested dictionary to the
      accumulator list; otherwise, proceed to the next iteration of the loop.

   8. After the loop terminates, return the top scorer list to the caller.

2. Return to the `main()` function. Call the function `get_top_scorer()` and pass it the `players`
   list. Assign a variable named `top_scorers` to the return value.

3. Uncomment the `print()` call and run your code. If the object streamed to the terminal is a
   list that contains a dictionary representation of the Japanese player Hinata Miyazawa 🇯🇵, winner
   of the 2023 Golden Boot Award (5 goals), then your function is behaving as expected.

## 7.0 Problem 07 (8 points)

__Task__: Implement the function named `get_team_names()`. Retrieve a list of unique team names that
can serve double duty as country names. Then, identify each team's top scorer(s) and write the data
to a JSON file.

1. Implement `get_team_names()`. Review the function's docstring regarding its expected behavior,
   parameters, and return value.

   __Requirements__

   1. In the function block implement the accumulator pattern. Assign a local variable
      (name your choice) to an empty "accumulator" `list`.

   2. Employ a standard `for` loop to iterate over the passed in `players` list.

   3. Inside the loop block, craft an `if` statement that allows you to accumulate a list of team
      names from `players` that contains __no duplicates__. In other words, append a nested dictionary's
      "squad" value to the accumulator list if, and only if, it has not been added previously.

      :bulb: Each dictionary represents a player. Each player is associated with a
      squad/team/country (e.g., Australia). Given that each team can roster up to 23 players,
      duplicate "squad" names exist throughout the `players` list.

   4. After the loop terminates return the list of team names to the caller.

2. Return to the `main()` function. Call the function `get_team_names()` and pass it the `players`
   list to return a list of unique team names. Since the team names correspond to country names
   assign a variable named `countries` to the return value.

3. Sort the `countries` list in ascending order, employing either the appropriate `list` method or
   appropriate built-in function.

   :bulb: The `list` method performs an in-place sort. It does not return a new list.

4. Uncomment the `print()` call and the `assert` statement. Run your code. Confirm that the function
   behaves as expected.

5. Still in the `main()` function, assign a variable named `team_top_scorers` to an empty list.

6. Next, implement a standard `for` loop that iterates over the `countries` list. Choose a readable
   loop variable name to represent each nested list.

7. Inside the loop block, call the function `get_team()` and pass it the arguments it requires to
   return a list of dictionaries of players who competed for the current country. Assign a variable
   named `team` to the return value.

8. Also inside the loop block, call the function `get_top_scorer()` and pass it the argument it
   requires to return a list of dictionaries of the current country's top scorer(s). Assign a variable
   named `top_scorers` to the return value.

9. Once you have the team's top scorers call the appropriate `list` method to add `top_scorers`
   to the `team_top_scorers` list.

   :exclamation: The mutated `team_top_scorers` list _must_
   match the following structure:

   ```python
   [{player_01}, {player_02}, {player_03}, ...]
   ```

10. Call the function `write_json()` and pass it the filepath "stu-team-top_scorers.json" along with
   the other arguments it requires __by position__.

11. Run your code and confirm that the file was written to the current working directory. Then
   compare the JSON file to the matching fixture file. If the files match proceed to the next
   problem.

## 8.0 Problem 08 (2 bonus points)

__Task__: Implement the function named `get_player_shooting_numbers()`.

1. Implement `get_player_shooting_numbers()`. Review the function's docstring regarding its expected
   behavior, parameters, and return value.

   :bulb: The shooting-related key-value pairs ⚽ are "goals", "shots", and "shots_on_target".
   _Shots on target_ is defined as a shot taken that would have resulted in a goal if not blocked by
   the goalkeeper or another player considered the "last defender". Shots that strike the goal post
   or crossbar 🥅 are not considered a shot on target.

   __Requirements__

   1. Access the passed in `player` dictionary's nested "stats" dictionary by using the associated
      key and the subscript operator. Assign a local variable (name your choice) to the expression
      which resolves to a dictionary.

   2. Assign a local variable (name of your choice) to an empty dictionary that will become the new
      "shooting numbers" dictionary that you _must_ return.

   3. Construct a `for` loop that iterates over the keys in `shooting_keys`.

   4. Within the loop block, access the "stats" dictionary's value associated with the current key
      and __convert__ the value from a string to an integer. Assign the integer to the new dictionary
      you created using the current key as the key.

   5. After the loop terminates, prepare to return only the values from your new "shooting numbers"
      dictionary to the caller, rather than the dictionary itself.

      :exclamation: Think about how to extract just the data from a dictionary without needing the
      keys!

2. Return to the `main()` function. Call the function `get_player_shooting_numbers()` and pass it the
   first "player" dictionary in `players` together with the `shooting_keys` list. __Unpack__ the
   return value and assign the variables `goals`, `shots`, and `shots_on_target` to the unpacked
   items.

   :bulb: The Spanish midfielder Teresa Abelleira 🇪🇸 is the first player in the `players` list.

3. Uncomment the `print()` call and the three `assert` statements. Run your code. Confirm that the
   function and item unpacking behaves as expected.

## FINIS :tada:
