# Kutubuku Blog

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
