# bf591-test-action



After you have done this, add to the solution repo workflows. The action
has two required inputs:

```
template-repo: <name of repo> # without the organization, i.e. BF591-R
template-repo-key: ${{ secrets.TEMPLATE_REPO_KEY }} # private key from the secret in the solutions repo
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
      - name: Deploy assignment solution
        uses: BF591-R/bf591-deploy-action@v1.0
        with:
          template-repo: test-assignment
          template-repo-key: ${{ secrets.TEMPLATE_REPO_KEY }}
```
