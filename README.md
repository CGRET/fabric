# Fabric examples
Sample code for remote execution using [Fabric](https://docs.fabfile.org).

Create a conda environment and install the Fabric package:
```bash
conda create --name fabric python=2
conda activate fabric
pip install fabric
```

You can use the [Fabric Command-line interface (CLI)](https://docs.fabfile.org/en/latest/cli.html) to run commands remotely:
```bash
fab -H 10.10.0.102 -- uname -a
```
Will run uname on 10.10.0.102.


# References
 * [Fabric](https://docs.fabfile.org) - Pythonic remote execution
