#!/usr/bin/env bash

set -e

echo Linting...
npm run lint

echo Building...
npm run build

cd dist

git init
git add -A
git commit -m 'Deploy'

git push -f git@github.com:ricky-lim/ricky-lim.github.io.git master:gh-pages

cd -
