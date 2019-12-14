# Event Judge

To simplify the judging evaluation with automated quick results

### Local Testing

Create virtual environment by:

`python -m venv myvenv`

Then to install this package, do:

`pip install .`

This will install it into your virtual environment and to remove do:

`pip uninstall event-judge`

### Testing

`import event_judge`

`client = event_judge.Client()`

`data = client.repository.fetch('shashank-sharma', 'mythical-feedback')`

Now you'll get the data