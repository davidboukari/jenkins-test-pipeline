import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="jenkins-test-pipeline",
    version="0.0.1",
    author="David Boukari",
    author_email="davidboukari@gmail.com",
    description="A small example package",
    long_description="long_description ...",
    long_description_content_type="text/markdown",
    url="https://github.com/davidboukari/jenkins-test-pipeline.git",
    package_dir={"app"},
    packages=setuptools.find_packages(where="app"),
    python_requires=">=3.6",
)
