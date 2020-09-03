# NUR packages template

A [Cookiecutter](https://github.com/cookiecutter/cookiecutter/) template for [NUR](https://github.com/nix-community/NUR) repositories.
With this template, you can choose between different CI workflows (GitHub Actions, Travis CI) and automatically set the stuff for you to get started.




## Getting started

1. Install [Cookiecutter](https://github.com/cookiecutter/cookiecutter/) and create the template from this repo (e.g., `cookiecutter https://github.com/foo-dogsquared/nur-packages-template`).
Or don't, use nix-shell, and copy the following command.

```sh
nix-shell -p cookiecutter git --command "cookiecutter https://github.com/foo-dogsquared/nur-packages-template"
```

2. Add your packages to the [`pkgs`](./pkgs) directory and to [`default.nix`](./default.nix).
   * Remember to mark the broken packages as `broken = true;` in the `meta` attribute, or the build process (and consequently caching) will fail!
   * Library functions, modules and overlays go in the respective directories.

3. [Add yourself to NUR.](https://github.com/nix-community/NUR#how-to-add-your-own-repository)

