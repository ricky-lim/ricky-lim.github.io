# Kutubuku Blog

![CI](https://github.com/ricky-lim/ricky-lim.github.io/actions/workflows/ci.yml/badge.svg)
![CD](https://github.com/ricky-lim/ricky-lim.github.io/actions/workflows/cd.yml/badge.svg)
[![Changelog](https://img.shields.io/badge/changelog-Common%20Changelog-blue.svg)](CHANGELOG.md)

My blog about tech, life, and everything in between.

## Developmemt Setup

### Getting Started

Clone the repository:

```bash
git clone https://github.com/ricky-lim/ricky-lim.github.io.git

cd ricky-lim.github.io
```

Install dependencies:

```bash
uv venv
source venv/bin/activate

uv pip install -e ".[dev]"
```

Start the development server:

```bash
lektor server
```

Install pre-commit hooks

```bash
pre-commit install
```

Apply branch protection rules

```bash
gh api --method PUT /repos/ricky-lim/ricky-lim.github.io/branches/main/protection \
  --input branch-protection-rules.json
```

## CHANGELOG

All notabel changes to this project are documented in the [CHANGELOG](CHANGELOG.md).
