# IPO-RESULT

Just a simple command line tool to check IPO result from https://iporesult.cdsc.com.np

### Setup
Note: Only if you want to use venv
```
> python -m venv venv
> source venv/bin/activate
```

install all the dependency using this
```
pip install -r requirements.txt
```

Change interval value in `main.py` to increase/decrease the frequency.

### How to run
If you're using venv then activate it
```
source venv/bin/activate
```
and run main command
```
python main.py
```

If you don't want to enter BOID from the prompt, try running like this

```
python main.py 1234567890123456
```

### Alias
You can also create alias in your `.bashrc` or `.zshrc` for shortcut so you don't have to keep entering your BOID.
```
alias ipo="source ~/ipo-result/venv/bin/activate && python ~/ipo-result/main.py 1234567890123456 && deactivate"
```

*The above example assumes that the project is in home folder, change it if you place it else where. Sorry if this does not work on windows* 😂

