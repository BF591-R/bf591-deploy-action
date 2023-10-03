# bf591-deploy-action

This GitHub Action deploys a BF591-R solutions repo to the corresponding
template repo. It should only be used for the assignment solutions repos as it
requires specific files to be in the repo root. Specifically, it does the
following:

1. Clones the current solutions repo
2. Clones the corresponding template repo, passed as an `input` to the action
3. Copies `report.Rmd`, `reference_report.html`, `README.md`, and `test_main.R`
   from the solutions repo to the template repo
4. Parses `main.R` in the solutions repo and strips out the function bodies
   (i.e. the solutions), leaving the rest intact
5. Copies the stripped `main.R` into the template repo
6. Commits changes to the template repo and pushes to GitHub

Additionally, the solutions and template repos must be configured with an
SSH deploy key. Create a public/private key pair somewhere with e.g.:

```
ssh-keygen -t ed25519 -C "bf591-deploy-action key" -N "" -f ./gh-test
```

Copy the contents of `gh-test.pub` as a Deploy Key on the **template** repo.
Copy the contents of the `gh-test` into a new Secret Variable named
`TEMPLATE_REPO_KEY` on the **solutions** repo. You can/should delete the
`gh-test*` files after this is done.

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
        uses: BF591-R/bf591-deploy-action@main
        with:
          template-repo: test-assignment
          template-repo-key: ${{ secrets.TEMPLATE_REPO_KEY }}
```
