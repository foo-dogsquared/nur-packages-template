# {{ cookiecutter.project_name }}

**My personal [NUR](https://github.com/nix-community/NUR) repository**




## Getting started

Follow the instructions at the [NUR project page](https://github.com/nix-community/NUR#installation) for enabling the NUR packages.

In case this repo is not included in the [list of NUR repos](https://github.com/nix-community/NUR/blob/master/repos.json), you can just use this repo directly like the following Nix code in `/etc/nixos/configuration.nix`:

```nix
nixpkgs.config.packageOverrides = pkgs: {
  nur-{{ cookiecutter.author_alias }} = import (
    fetchTarball "https://github.com/{{ cookiecutter.github_username }}/nix-expressions/archive/master.tar.gz") { inherit pkgs; }
  );
};
```

You can then access the packages at `pkgs.nur-{{ cookiecutter.author_alias }}.$PKG`.

{% if cookiecutter.ci == "GitHub Actions" -%}
![Build and populate cache](https://github.com/nix-community/{{ cookiecutter.github_username }}/workflows/Build%20and%20populate%20cache/badge.svg)
{% elif cookiecutter.ci == "Travis CI" -%}
[![Build Status](https://travis-ci.com/{{ cookiecutter.travis_ci_username }}/nur-packages.svg?branch=master)](https://travis-ci.com/{{ cookiecutter.travis_ci_username }}/nur-packages)
{% endif %}

[![Cachix Cache](https://img.shields.io/badge/cachix-{{ cookiecutter.cachix_cache }}-blue.svg)](https://{{ cookiecutter.cachix_cache }}.cachix.org)

