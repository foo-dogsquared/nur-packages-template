# {{ cookiecutter.project_name }}

**My personal [NUR](https://github.com/nix-community/NUR) repository**

{% if cookiecutter.ci == "GitHub Actions" %}
![Build and populate cache](https://github.com/nix-community/{{ cookiecutter.github_username }}/workflows/Build%20and%20populate%20cache/badge.svg)

{% elif cookiecutter.ci == "Travis CI" %}
[![Build Status](https://travis-ci.com/{{ cookiecutter.travis_ci_username }}/nur-packages.svg?branch=master)](https://travis-ci.com/{{ cookiecutter.travis_ci_username }}/nur-packages)
{% endif %}

[![Cachix Cache](https://img.shields.io/badge/cachix-{{ cookiecutter.cachix_cache }}-blue.svg)](https://{{ cookiecutter.cachix_cache }}.cachix.org)

