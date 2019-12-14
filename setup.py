import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='event-judge',
    version='0.1',
    author="Shashank Sharma",
    author_email="shashank.sharma98@gmail.com",
    description="Simplifying judging for all events",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/isohack/event-judge",
    install_requires=["requests"],
    include_package_data=True,
    packages=['event_judge', 'event_judge.resources', 'event_judge.constants'],
    package_dir={'event_judge': 'event_judge', 'event_judge.resources': 'event_judge/resources'},
    license='MIT',
)