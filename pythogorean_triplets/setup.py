import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pythogorean_triplets",
    version="0.0.1",
    author="Akash kumar",
    author_email="hitmanmit1996@gmail.com",
    description="This is my first python project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Akash671/Akash671/pythogorean_triplets",
    project_urls={
        "Bug Tracker": "https://github.com/Akash671/Akash671/pythogorean_triplets",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "Triplets"},
    packages=setuptools.find_packages(where="Triplets"),
    python_requires=">=3.6",
)
