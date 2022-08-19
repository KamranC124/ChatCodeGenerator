# ChatCodeGenerator

I’ve made this Guild Wars 2 chat code generator for fun. If you input the correct values, it’ll be able to produce a chat code for your desired item you can use in-game.

How it works:
Chat codes in Guild Wars 2 use a standard format. They begin with “[&” and end in “]”. Between the two square brackets every chat code has 3 sections, the header, ObjectID, and the footer. These are all hexadecimal values encoded into Base64.  More detail on each section:

The first section is the “header”, this is a byte which identifies what type of item or marker you’re looking for. The menu in the generator covers each category that exists, although categories 1 and 8 are currently disabled by the game developers. The generator will generally take the user input (base 10) and convert it into hexadecimal (base 16).

The “ObjectID” is the ID assigned to each individual item or marker in the game, this can be found using the Guild Wars 2 API, or the Guild Wars 2 Wiki. The format of the chat code requires this to be a 3-byte little-endian integer. The user input is first converted into hexadecimal, then put into the little-endian format subsequently. If the “header” was assigned as “02” (item), it is possible to include a byte for the quantity of the desired item, this will always precede the 3-byte little-endian integer.

The “footer” is a byte of all 0s, the value of this is currently ignored by the game but it is necessary for the chat code to function.

Once you have the value of each section, it will then be encoded into Base64 and placed in between the aforementioned square brackets. You can then use this in-game and be able to view your chat code.

Example:
If you wanted to display “250 obsidian shard”:
Header: 02 (Choose option 2 for “item”)
ObjectID: FAD54D00 (The item id is 19925, provided by the API, this is converted to D54D00. It is then preceded by FA, the base 16 value for 250.)
Footer: 00 (A byte of 0s)

Final hexadecimal value: 02fad54d0000
Base64: AvrVTQAA
Chat code: [&AvrVTQAA]

There is room for improvement on this code, the code could be further optimised and also allow for more complex chat codes. However, this is the first version of the code.
