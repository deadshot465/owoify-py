# owoify-py
Turning your worst nightmare into a Python package.

- [Python package](https://pypi.org/project/owoify-py/)

This is a Python port of [mohan-cao's owoify-js](https://github.com/mohan-cao/owoify-js), which will help you turn any string into nonsensical babyspeak similar to LeafySweet's infamous Chrome extension.

Just like my other Owoify ports, three levels of owoness are available:
1. **owo (default)**: The most vanilla one.
2. **uwu**: The moderate one.
3. **uvu**: Litewawwy unweadabwal.

Please refer to the original [owoify-js repository](https://github.com/mohan-cao/owoify-js) for more information.

Seriously, if you have seen my other ports, you probably have already known the details.

## Reason for development
PyPI does already have several owoify packages, but just like owoify packages on Crates.io, they don't provide different leves of owoness. And recently I need to make a Discord bot in Python as well, so here is your owoifer in Python.

## Install instructions
Create a virtual environment for your project, and run this following command after activating the virtual environment:
```bash
pip install owoify-py
```

## Usage
owoify.py is implemented as a simple function. That means you only need to import the function and call it inside your code. The difference is that this time the owoness is specified with strings, i.e. **owo**, **uwu**, and **uvu**.
```python
if __name__ == '__main__':
    print(owoify('This is the string to owo! Kinda cute isn\'t it?'))
    print(owoify('This is the string to owo! Kinda cute isn\'t it?', 'uvu'))

# Output:
# This is teh stwing two owo! Kinda cute isn't it?
# fwis is teh stwing twowo owowowo ʕ￫ᴥ￩ʔ Kinda cute isn't it?
```
## Disclaimer
As usual, I'm writing this package for both practicing and bots' needs. **Performance** is NOT guaranteed.

## See also
- [owoify-js](https://github.com/mohan-cao/owoify-js) - The original owoify-js repository.
- [owoify](https://pypi.org/project/owoify/) - The existing owoify package on PyPI.
- [Owoify.Net](https://www.nuget.org/packages/Owoify.Net/1.1.0) - The C# port of Owoify written by me.
- [Owoify++](https://github.com/deadshot465/OwoifyCpp) - The C++ header-only port of Owoify written by me.
- [owoify_rs](https://crates.io/crates/owoify_rs) - The Rust port of Owoify written by me.