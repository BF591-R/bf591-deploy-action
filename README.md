# bf591-scrub-main

This action contains a python script that reads in a `main.R` R script from a BF591-R assignment and strips the function definitions for deployment into template repos. The calling workflow must provide the following inputs:

```
input-path: <path to main.R with solutions>
output-path: <path to output main.R that should have solutions scrubbed>
```

Example workflow:

```
name: Test Solutions
run-name: ${{ github.actor }} is testing this assignment solution
on: [push]
jobs:
  Deploy:
    runs-on: ubuntu-latest
    steps:
      - name: check out source repo
        uses: actions/checkout@v4
      - name: scrub main.R of function defs
        uses: BF591-R/bf591-scrub-main@v1.0
        with:
          input-path: main.R
          output-path: scrubbed_main.R
```
